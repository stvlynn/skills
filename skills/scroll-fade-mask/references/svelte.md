# Svelte

## Action

```ts
import { writable } from "svelte/store";

export function scrollFade(node: HTMLElement) {
  const fadeTop = writable(false);
  const fadeBottom = writable(false);

  const updateScrollFade = () => {
    const { scrollTop, scrollHeight, clientHeight } = node;
    const isAtTop = scrollTop <= 0;
    const isAtBottom = scrollTop + clientHeight >= scrollHeight - 1;

    fadeTop.set(!isAtTop);
    fadeBottom.set(!isAtBottom);
  };

  updateScrollFade();
  node.addEventListener("scroll", updateScrollFade);

  const resizeObserver = new ResizeObserver(updateScrollFade);
  resizeObserver.observe(node);

  return {
    destroy() {
      node.removeEventListener("scroll", updateScrollFade);
      resizeObserver.disconnect();
    },
    stores: { fadeTop, fadeBottom },
  };
}
```

## Usage

```svelte
<script lang="ts">
  import { scrollFade } from "./actions/scrollFade";

  let fadeTop = false;
  let fadeBottom = false;

  function bindScrollFade(node: HTMLElement) {
    const action = scrollFade(node);
    action.stores.fadeTop.subscribe((value) => (fadeTop = value));
    action.stores.fadeBottom.subscribe((value) => (fadeBottom = value));
    return action;
  }
</script>

<div
  class="fc-scroll-fade-wrapper"
  data-fade-top={fadeTop}
  data-fade-bottom={fadeBottom}
>
  <div use:bindScrollFade class="list-content">
    <!-- content -->
  </div>
</div>
```

## Notes

- Bind the action to the scroll container, not the wrapper.
- Keep the wrapper classes and data attributes in normal markup so the CSS system stays reusable.
