# Eval 2 With Skill — Vue 3 Scroll Fade Troubleshooting

## The Problem

You can't scroll after adding the scroll fade mask wrapper to your Vue 3 sidebar. The content is there but won't move when you try to scroll.

## Root Cause

The wrapper has `overflow: hidden` or the scroll container lost its `overflow-y: auto` property. The wrapper pattern requires:

1. **Wrapper** — holds the gradient masks, NO overflow property
2. **Scroll container** — has `overflow-y: auto` and constrained height

## The Fix

### Correct Implementation

```vue
<template>
  <!-- Wrapper: NO overflow property -->
  <div class="fc-scroll-fade-wrapper" 
       :data-fade-top="showTopMask" 
       :data-fade-bottom="showBottomMask">
    
    <!-- Scroll container: HAS overflow-y and height -->
    <div ref="scrollContainer" class="sidebar-list">
      <div v-for="item in items" :key="item.id" class="sidebar-item">
        {{ item.name }}
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted, onUnmounted } from 'vue'

const scrollContainer = ref(null)
const showTopMask = ref(false)
const showBottomMask = ref(false)

const updateMasks = () => {
  const el = scrollContainer.value
  if (!el) return

  const { scrollTop, scrollHeight, clientHeight } = el
  showTopMask.value = scrollTop > 10
  showBottomMask.value = scrollTop + clientHeight < scrollHeight - 10
}

let resizeObserver = null

onMounted(() => {
  const el = scrollContainer.value
  if (!el) return

  el.addEventListener('scroll', updateMasks)
  resizeObserver = new ResizeObserver(updateMasks)
  resizeObserver.observe(el)
  updateMasks()
})

onUnmounted(() => {
  const el = scrollContainer.value
  if (el) el.removeEventListener('scroll', updateMasks)
  if (resizeObserver) resizeObserver.disconnect()
})
</script>

<style scoped>
.sidebar-list {
  overflow-y: auto;  /* Required for scrolling */
  height: 100%;      /* Or max-height, or flex: 1 */
  padding: 16px;
}
</style>
```

## Quick Fixes

1. **Remove `overflow: hidden` from wrapper** — The wrapper should have NO overflow property
2. **Add `overflow-y: auto` to scroll container** — Your `.sidebar-list` needs this
3. **Add height constraint** — Use `height: 100%`, `max-height`, or `flex: 1`
4. **Put ref on scroll container** — `ref="scrollContainer"` goes on the inner div, not wrapper

## CSS Check

Ensure your global CSS has:

```css
.fc-scroll-fade-wrapper {
  position: relative;
  display: flex;
  flex-direction: column;
  min-height: 0;
  /* NO overflow property here */
}
```

The wrapper holds the masks (::before and ::after pseudo-elements) but doesn't scroll. The inner container does the scrolling.

## Key Observations

- Correctly identifies wrapper pattern architecture (wrapper holds masks, inner scrolls)
- Identifies overflow: hidden as root cause
- Provides Vue 3 Composition API code with ResizeObserver
- Includes debug checklist items
- References fc-scroll-fade-wrapper class from the skill
