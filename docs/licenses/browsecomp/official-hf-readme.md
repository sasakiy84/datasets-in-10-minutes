---
license: mit
task_categories:
- question-answering
---

# BrowseComp Long Context

BrowseComp Long Context is a dataset based on [BrowseComp](https://openai.com/index/browsecomp/) to benchmark LLM’s capability to retrieve relevant information from noisy data in its context. It converts the agentic question answering tasks from Browsecomp into long context tasks.

For each of the questions in a subset of BrowseComp, a list of urls are attached. Each url will be paired with an indicator indicating whether the content of the web page is required to answer the question or is additional content served as supplement information or noise. The required urls are collected and reviewed by a human to ensure they are sufficient and necessary to answer the original question. The additional urls are obtained by searching relevant questions that can help answer the original question.

The data is extensible to different context windows, with the provided list of urls, it’s feasible to construct model prompts beyond 1m context window.

This eval is challenging because:
- The constructed prompt is based on real data where most of the context is somewhat relevant, as opposed to a broad web corpus where very little data is relevant
- The model must combine multiple pieces of information in order to answer the question
- The order of the information appearing in the context might not align with the order of when they needed in reasoning flow
- The model needs to be able to not be confused by additional information that is relevant
- The longer the context, the harder the task

## Data Schema
For each row the data will contain:
- Problem
- Answer
- List of urls each paired with a "required" or "additional" to indicate if the url is required to answer the question.

Data can be loaded with the following method.
```python
def derive_key(password: str, length: int) -> bytes:
    """Derive a fixed-length key from the password using SHA256."""
    hasher = hashlib.sha256()
    hasher.update(password.encode())
    key = hasher.digest()
    return key * (length // len(key)) + key[: length % len(key)]


def decrypt(ciphertext_b64: str, password: str) -> str:
    """Decrypt base64-encoded ciphertext with XOR."""
    encrypted = base64.b64decode(ciphertext_b64)
    key = derive_key(password, len(encrypted))
    decrypted = bytes(a ^ b for a, b in zip(encrypted, key))
    return decrypted.decode()


data = [
    {
        "problem": decrypt(row["problem"], row["canary"]),
        "answer": decrypt(row["answer"], row["canary"]),
        "urls": decrypt(row['urls'],row["canary"]),
    }
    for row in encrypted_data
]
```

## Reference prompt construction implementation


```python
def _fit_pages(self, pages:list[str], token_budget:int):
    """
    Fit pages into a token budget.

    Args:
        pages: list of pages to fit into the token budget.
        token_budget: the token budget.

    Returns:
        tuple:
            - int: number of pages fitted into the token budget.
            - int: token budget remaining.
    """
    fitted_pages = 0
    for page in pages:
        page_tokens = self._count_token(page)
        if page_tokens<=token_budget:
            token_budget-=page_tokens
            fitted_pages+=1
        else:
            break
    return fitted_pages,token_budget


def render_prompt(self, problem: str, urls: list[tuple[str,bool]], token_budget: int) -> tuple[str, bool]:
    """
    Render a prompt for a given problem and a list of URLs.

    Args:
        problem: The problem to answer.
        urls: List of URLs to use to answer the problem.
        token_budget: The token budget.

    Returns:
        tuple:
            - str: constructed model prompt.
            - bool: whether the prompt was constructed successfully.
    """

    initial_msg = f"""Given a list of websites, answer the following question: {problem}\n
Your final answer should be a concise sentence, in the following format:
Final Answer: put your answer here.

It's critical your answer is concise and following the format strictly.\n"""
final_msg = f"""\nNow answer the original question, recall the question is: {problem}

VERY IMPORTANT: Do not use any web search tools or browser tools to answer the question, you may only use the provided documents to answer the question."""

    token_budget -= self._count_token(initial_msg)+self._count_token(final_msg)
    required_pages = [self._fetch_url(url) for url,is_required in urls if is_required]
    additional_pages = [self._fetch_url(url) for url,is_required in urls if not is_required]

    num_required_fitted, token_budget = self._fit_pages(required_pages, token_budget)
    if num_required_fitted < len(required_pages):
        return "", False
    num_additional_fitted, token_budget = self._fit_pages(additional_pages, token_budget)

    page_msgs = [*required_pages[:num_required_fitted], *additional_pages[:num_additional_fitted]]
    self._rng.shuffle(page_msgs)
    return "\n".join([initial_msg, *page_msgs, final_msg]), True

```
\* Note the implementation and quality of _fetch_url method can affect the benchmark results. It’s recommended to use a consistent implementation of this method across different runs.


## Grading 
Grading is performed following the same method of [BrowseComp](https://openai.com/index/browsecomp/). More specifically, it can be done by prompting a model with a grading template providing question, model response and reference answer.
