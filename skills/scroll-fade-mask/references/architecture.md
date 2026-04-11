# Architecture

## Table of contents

- Core pattern
- CSS system
- Integration rules
- Common layout shapes
- Customization

## Core pattern

Use a two-layer structure:

```html
<div
  class="fc-scroll-fade-wrapper fc-scroll-fade-wrapper-white"
  data-fade-top="false"
  data-fade-bottom="true"
>
  <div class="your-scroll-container">
    <!-- scrollable content -->
  </div>
</div>
```

- Wrapper:
  - owns `::before` and `::after`
  - owns `data-fade-top` and `data-fade-bottom`
  - stays `position: relative`
  - does not scroll
- Inner container:
  - owns `overflow-y: auto`
  - owns the height constraint
  - receives the framework ref, action, or class binding

This avoids the two most common failures:

- the masks scroll away with the content
- `overflow` on the wrapper breaks the pseudo-element pattern or blocks scrolling

## CSS system

Start from this global CSS:

```css
.fc-scroll-fade-wrapper {
  --fc-scroll-fade-rgb: 248 249 251;
  --fc-scroll-fade-height: 48px;
  --fc-scroll-fade-z: 100;
  position: relative;
  display: flex;
  flex-direction: column;
  min-height: 0;
}

.fc-scroll-fade-wrapper::before,
.fc-scroll-fade-wrapper::after {
  content: "";
  position: absolute;
  left: 0;
  right: 0;
  height: var(--fc-scroll-fade-height);
  opacity: 0;
  pointer-events: none;
  transition: opacity 200ms ease;
  z-index: var(--fc-scroll-fade-z);
}

.fc-scroll-fade-wrapper::before {
  top: 0;
  background: linear-gradient(
    to bottom,
    rgb(var(--fc-scroll-fade-rgb) / 1) 0%,
    rgb(var(--fc-scroll-fade-rgb) / 0.95) 15%,
    rgb(var(--fc-scroll-fade-rgb) / 0.85) 30%,
    rgb(var(--fc-scroll-fade-rgb) / 0.6) 50%,
    rgb(var(--fc-scroll-fade-rgb) / 0.3) 70%,
    rgb(var(--fc-scroll-fade-rgb) / 0.1) 85%,
    transparent 100%
  );
}

.fc-scroll-fade-wrapper::after {
  bottom: 0;
  background: linear-gradient(
    to top,
    rgb(var(--fc-scroll-fade-rgb) / 1) 0%,
    rgb(var(--fc-scroll-fade-rgb) / 0.95) 15%,
    rgb(var(--fc-scroll-fade-rgb) / 0.85) 30%,
    rgb(var(--fc-scroll-fade-rgb) / 0.6) 50%,
    rgb(var(--fc-scroll-fade-rgb) / 0.3) 70%,
    rgb(var(--fc-scroll-fade-rgb) / 0.1) 85%,
    transparent 100%
  );
}

.fc-scroll-fade-wrapper[data-fade-top="true"]::before {
  opacity: 1;
}

.fc-scroll-fade-wrapper[data-fade-bottom="true"]::after {
  opacity: 1;
}

.fc-scroll-fade-wrapper-white {
  --fc-scroll-fade-rgb: 255 255 255;
}

.fc-scroll-fade-wrapper-warm {
  --fc-scroll-fade-rgb: 245 242 239;
}
```

## Integration rules

- Put the CSS in a global stylesheet such as `globals.css`, `app.css`, or `styles.css`.
- Keep `pointer-events: none` on the masks.
- Attach behavior to the inner scroll container, not the wrapper.
- In flex layouts, keep `min-height: 0` on the wrapper and ensure the inner container has a real height path via `flex: 1`, `height: 100%`, or `max-height`.

## Common layout shapes

### Existing scroll class

```css
.fc-scroll-fade-wrapper > .your-scroll-container {
  min-height: 0;
  overflow-y: auto;
}
```

### Sidebar or panel

```css
.sidebar {
  display: flex;
  flex-direction: column;
  height: 100vh;
}

.sidebar .fc-scroll-fade-wrapper {
  flex: 1;
}

.sidebar .sidebar-content {
  height: 100%;
  overflow-y: auto;
}
```

### Dropdown or popover

- Put the wrapper on the floating panel
- Put the scroll container inside it
- Use `max-height` on the scroll container or panel as appropriate

## Customization

- White surface: add `fc-scroll-fade-wrapper-white`
- Beige or cream surface: add `fc-scroll-fade-wrapper-warm`
- Custom surface: override `--fc-scroll-fade-rgb`
- Taller masks: override `--fc-scroll-fade-height`
- Higher stacking context: override `--fc-scroll-fade-z`
