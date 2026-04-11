# Vanilla JavaScript

## Class

```js
export class ScrollFadeMask {
  constructor(scrollElement, wrapperElement = scrollElement?.parentElement) {
    if (!scrollElement || !wrapperElement) {
      throw new Error("ScrollFadeMask requires a scroll element and wrapper");
    }

    this.scrollElement = scrollElement;
    this.wrapperElement = wrapperElement;
    this.updateScrollFade = this.updateScrollFade.bind(this);
    this.init();
  }

  updateScrollFade() {
    const { scrollTop, scrollHeight, clientHeight } = this.scrollElement;
    const isAtTop = scrollTop <= 0;
    const isAtBottom = scrollTop + clientHeight >= scrollHeight - 1;

    this.wrapperElement.setAttribute("data-fade-top", String(!isAtTop));
    this.wrapperElement.setAttribute("data-fade-bottom", String(!isAtBottom));
  }

  init() {
    this.updateScrollFade();
    this.scrollElement.addEventListener("scroll", this.updateScrollFade);

    this.resizeObserver = new ResizeObserver(this.updateScrollFade);
    this.resizeObserver.observe(this.scrollElement);
  }

  destroy() {
    this.scrollElement.removeEventListener("scroll", this.updateScrollFade);
    this.resizeObserver?.disconnect();
  }
}
```

## Usage

```html
<div
  class="fc-scroll-fade-wrapper fc-scroll-fade-wrapper-warm"
  data-fade-top="false"
  data-fade-bottom="true"
>
  <div class="chat-messages">
    <!-- messages -->
  </div>
</div>
```

```css
.chat-shell {
  display: flex;
  flex-direction: column;
  min-height: 0;
}

.fc-scroll-fade-wrapper {
  flex: 1;
}

.chat-messages {
  height: 100%;
  overflow-y: auto;
}
```

```js
import { ScrollFadeMask } from "./ScrollFadeMask.js";

const scrollElement = document.querySelector(".chat-messages");
const fadeMask = new ScrollFadeMask(scrollElement);

// Later, if the UI is torn down:
// fadeMask.destroy();
```

## Notes

- `fc-scroll-fade-wrapper-warm` matches `#f5f2ef` style chat surfaces.
- The class supports explicit wrapper injection, but defaulting to the parent wrapper keeps usage terse.
- Mention `min-height: 0` and `flex: 1` whenever the user's container lives inside a flex layout.
