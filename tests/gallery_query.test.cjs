const { test } = require('node:test');
const assert = require('node:assert/strict');
const { readFileSync } = require('node:fs');
const { runInNewContext } = require('node:vm');
const source = readFileSync(`${__dirname}/../site/assets/gallery.js`, 'utf8');

function gallery(query = '') {
  const element = (values = []) => ({
    value: '', options: values.map(value => ({ value })), hidden: false,
    listeners: {}, addEventListener(type, fn) { this.listeners[type] = fn; },
    replaceChildren() {}, append() {},
  });
  const controls = {
    '#title-search': element(), '#modality': element(['', '画像', '言語']),
    '#task': element(['', '画像分類', '質問応答']), '#year': element(['', '2009', '2024', '2025']),
    '#sort-order': element(['year-desc', 'year-asc', 'created-desc', 'created-asc', 'updated-desc', 'updated-asc']),
    '#reset': element(), '#result-count': element(), '#empty': element(), '.filters': element(),
    '#gallery': { children: [], append(...cards) { this.children = cards; } },
  };
  const cards = [
    ['Vision', '画像', '質問応答', '2025', '2020-01-01', '2024-05-01'],
    ['ImageNet', '画像', '画像分類', '2009', '2021-01-01', '2024-04-01'],
    ['Language', '言語', '質問応答', '2024', '2022-01-01', '2024-06-01'],
  ].map(([title, modality, tasks, year, createdAt, updatedAt]) => ({
    title, dataset: { modality, tasks, year, createdAt, updatedAt },
    querySelector: () => ({ textContent: title }),
  }));
  const urls = [`https://example.com/gallery/${query}`];
  let index = 0;
  const window = { location: new URL(urls[0]), listeners: {}, addEventListener(type, fn) { this.listeners[type] = fn; } };
  window.history = {
    state: null,
    pushState(state, _, url) { urls.splice(++index); urls[index] = String(url); window.location = new URL(url); },
    replaceState(state, _, url) { urls[index] = String(url); window.location = new URL(url); },
  };
  const document = { querySelector: key => controls[key], querySelectorAll: () => cards, createElement: () => element() };
  runInNewContext(source, { document, window, URL, URLSearchParams });
  return {
    controls, cards,
    params: () => new URLSearchParams(window.location.search),
    url: () => window.location,
    set(selector, value, event = 'change') { controls[selector].value = value; controls[selector].listeners[event](); },
    reset: () => controls['#reset'].listeners.click(),
    back() { window.location = new URL(urls[--index]); window.listeners.popstate(); },
    forward() { window.location = new URL(urls[++index]); window.listeners.popstate(); },
    order: () => controls['#gallery'].children.map(card => card.title),
  };
}

test('restores deep-link filters and creation/update ordering', () => {
  const app = gallery('?q=ｖｉｓｉｏｎ&modality=画像&task=質問応答&year=2025&sort=created-desc');
  assert.deepEqual(app.cards.filter(card => !card.hidden).map(card => card.title), ['Vision']);
  assert.deepEqual(app.order(), ['Language', 'ImageNet', 'Vision']);
  const updated = gallery('?sort=updated-asc');
  assert.deepEqual(updated.order(), ['ImageNet', 'Vision', 'Language']);
});

test('selection changes support back/forward; typing replaces the current entry', () => {
  const app = gallery('?utm_source=example#gallery');
  app.set('#modality', '画像');
  app.set('#sort-order', 'updated-desc');
  app.back();
  assert.equal(app.controls['#sort-order'].value, 'year-desc');
  assert.equal(app.controls['#modality'].value, '画像');
  app.forward();
  assert.equal(app.controls['#sort-order'].value, 'updated-desc');
  app.set('#title-search', 'Image Net & 日本語', 'input');
  assert.equal(app.params().get('q'), 'Image Net & 日本語');
  app.back();
  assert.equal(app.controls['#title-search'].value, '');
  assert.equal(app.params().get('utm_source'), 'example');
  assert.equal(app.url().hash, '#gallery');
});

test('reset removes only gallery conditions and can be undone', () => {
  const app = gallery('?q=Vision&modality=画像&task=質問応答&year=2025&sort=created-asc&keep=1#gallery');
  app.reset();
  assert.equal(app.url().search, '?keep=1');
  assert.equal(app.url().hash, '#gallery');
  assert.equal(app.cards.filter(card => !card.hidden).length, 3);
  app.back();
  assert.equal(app.controls['#title-search'].value, 'Vision');
  assert.equal(app.controls['#sort-order'].value, 'created-asc');
});

test('invalid and duplicate selections normalize without losing unrelated parameters', () => {
  const app = gallery('?modality=invalid&year=9999&sort=invalid&task=質問応答&task=画像分類&keep=1');
  assert.equal(app.controls['#modality'].value, '');
  assert.equal(app.controls['#year'].value, '');
  assert.equal(app.controls['#sort-order'].value, 'year-desc');
  assert.deepEqual(app.params().getAll('task'), ['質問応答']);
  assert.equal(app.params().get('keep'), '1');
  assert.equal(app.params().has('sort'), false);
});
