# Vue 3

## Composable

```ts
import { onMounted, onUnmounted, ref, type Ref } from "vue";

export function useScrollFade() {
  const scrollRef: Ref<HTMLElement | null> = ref(null);
  const fadeTop = ref(false);
  const fadeBottom = ref(false);

  const updateScrollFade = () => {
    const element = scrollRef.value;
    if (!element) return;

    const { scrollTop, scrollHeight, clientHeight } = element;
    const isAtTop = scrollTop <= 0;
    const isAtBottom = scrollTop + clientHeight >= scrollHeight - 1;

    fadeTop.value = !isAtTop;
    fadeBottom.value = !isAtBottom;
  };

  let resizeObserver: ResizeObserver | null = null;

  onMounted(() => {
    const element = scrollRef.value;
    if (!element) return;

    updateScrollFade();
    element.addEventListener("scroll", updateScrollFade);

    resizeObserver = new ResizeObserver(updateScrollFade);
    resizeObserver.observe(element);
  });

  onUnmounted(() => {
    const element = scrollRef.value;
    if (element) {
      element.removeEventListener("scroll", updateScrollFade);
    }

    resizeObserver?.disconnect();
  });

  return { scrollRef, fadeTop, fadeBottom, updateScrollFade };
}
```

## Usage

```vue
<template>
  <div
    class="fc-scroll-fade-wrapper"
    :data-fade-top="fadeTop"
    :data-fade-bottom="fadeBottom"
  >
    <div ref="scrollRef" class="sidebar-list">
      <div v-for="item in items" :key="item.id" class="sidebar-item">
        {{ item.name }}
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import { useScrollFade } from "@/composables/useScrollFade";

const { scrollRef, fadeTop, fadeBottom } = useScrollFade();
</script>
```

## Notes

- The wrapper does not scroll.
- The inner `.sidebar-list` must keep `overflow-y: auto` and a height constraint.
- If the user says "I can't scroll anymore", check `references/troubleshooting.md` before suggesting a rewrite.
