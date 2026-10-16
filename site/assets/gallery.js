const cards = [...document.querySelectorAll('.card')];
const modality = document.querySelector('#modality');
const task = document.querySelector('#task');
const year = document.querySelector('#year');
const sortOrder = document.querySelector('#sort-order');
const gallery = document.querySelector('#gallery');
const titleSearch = document.querySelector('#title-search');
const normalize = value => value.normalize('NFKC').toLocaleLowerCase('ja').trim();
const titles = new Map(cards.map(card => [card, normalize(card.querySelector('h2').textContent)]));
const count = document.querySelector('#result-count');
const empty = document.querySelector('#empty');
function sortCards() {
  const direction = sortOrder.value === 'year-asc' ? 1 : -1;
  const ordered = [...cards].sort((a, b) => direction * (Number(a.dataset.year) - Number(b.dataset.year)));
  gallery.append(...ordered);
}
function filter() {
  let visible = 0;
  const query = normalize(titleSearch.value);
  for (const card of cards) {
    const matches = (!modality.value || card.dataset.modality === modality.value)
      && (!task.value || card.dataset.tasks.split('|').includes(task.value))
      && (!year.value || card.dataset.year === year.value)
      && (!query || titles.get(card).includes(query));
    card.hidden = !matches;
    if (matches) visible++;
  }
  count.replaceChildren();
  const number = document.createElement('strong');
  number.textContent = visible;
  count.append(number, ` / ${cards.length} datasets`);
  empty.hidden = visible > 0;
}
for (const select of [modality, task, year]) select.addEventListener('change', filter);
titleSearch.addEventListener('input', filter);
sortOrder.addEventListener('change', sortCards);
document.querySelector('#reset').addEventListener('click', () => {
  titleSearch.value = '';
  for (const select of [modality, task, year]) select.value = '';
  sortOrder.value = 'year-desc';
  sortCards();
  filter();
});
sortCards();
document.querySelector('.filters').hidden = false;
