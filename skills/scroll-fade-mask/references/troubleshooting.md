# Troubleshooting

## Can't scroll

Most likely causes:

1. The wrapper has `overflow: hidden` or `overflow-y: auto`
2. The inner scroll container lost `overflow-y: auto`
3. The inner scroll container has no real height constraint

Correct architecture:

```html
<div class="fc-scroll-fade-wrapper" data-fade-top="true" data-fade-bottom="true">
  <div class="your-scroll-container">
    <!-- content -->
  </div>
</div>
```

```css
.fc-scroll-fade-wrapper {
  position: relative;
  display: flex;
  flex-direction: column;
  min-height: 0;
}

.your-scroll-container {
  flex: 1;
  min-height: 0;
  overflow-y: auto;
}
```

State this explicitly when troubleshooting:

- The wrapper should not own overflow.
- The inner container should own scrolling.

## Masks do not show

Check these in order:

1. `data-fade-top` and `data-fade-bottom` are changing
2. The behavior ref or binding is attached to the inner scroll container
3. The gradient color matches the actual background
4. `::before` and `::after` are not hidden by a stacking-context issue

Useful debug commands:

```js
const wrapper = document.querySelector(".fc-scroll-fade-wrapper");
const content = wrapper?.querySelector(".your-scroll-container");

console.log("wrapper overflow", getComputedStyle(wrapper).overflow);
console.log("content overflowY", getComputedStyle(content).overflowY);
console.log("scrollHeight", content?.scrollHeight);
console.log("clientHeight", content?.clientHeight);
console.log("data-fade-top", wrapper?.getAttribute("data-fade-top"));
console.log("data-fade-bottom", wrapper?.getAttribute("data-fade-bottom"));
```

## Wrong edge state

Use an off-by-one guard:

```js
const isAtBottom = scrollTop + clientHeight >= scrollHeight - 1;
```

This avoids sub-pixel rounding errors near the bottom edge.

## Content appears under the mask

- Keep `pointer-events: none` on the pseudo-elements
- Add content padding if text or buttons feel too tight to the fade region
- Only change mask height after checking that the visual obstruction is not just missing inner padding
