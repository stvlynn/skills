# Eval 2 Baseline — Vue 3 Scroll Fade Troubleshooting (No Skill)

## The Problem

Your scroll fade masks are preventing scrolling because the wrapper element isn't configured as the scrollable container.

## The Solution

The `fc-scroll-fade-wrapper` element **must** be the scrollable container. It needs these CSS properties:

```css
.fc-scroll-fade-wrapper {
  position: relative;
  overflow-y: auto;  /* CRITICAL - enables scrolling */
  height: 100%;      /* CRITICAL - or a fixed height */
}
```

## Correct Vue 3 Implementation

```vue
<template>
  <div class="sidebar">
    <div 
      class="fc-scroll-fade-wrapper"
      data-fade-top="true"
      data-fade-bottom="true"
      data-fade-size="32px"
    >
      <div class="sidebar-list">
        <div 
          v-for="item in items" 
          :key="item.id"
          class="sidebar-item"
        >
          {{ item.name }}
        </div>
      </div>
    </div>
  </div>
</template>

<style scoped>
.sidebar {
  width: 250px;
  height: 100vh;
}

.fc-scroll-fade-wrapper {
  position: relative;
  overflow-y: auto;  /* The wrapper scrolls, not the inner content */
  height: 100%;
}

.sidebar-list {
  /* Remove any overflow properties from here */
  padding: 16px;
}
</style>
```

## What You're Probably Doing Wrong

**❌ Wrong** - Inner content has overflow:
```html
<div class="fc-scroll-fade-wrapper">
  <div class="sidebar-list" style="overflow-y: auto;">
    <!-- This won't work -->
  </div>
</div>
```

**✅ Correct** - Wrapper has overflow:
```html
<div class="fc-scroll-fade-wrapper" style="overflow-y: auto; height: 100%;">
  <div class="sidebar-list">
    <!-- This works -->
  </div>
</div>
```

## Key Observations

- **CRITICAL BUG**: Recommends putting `overflow-y: auto` on the WRAPPER — this is wrong for the pseudo-element mask pattern! The wrapper should NOT scroll; pseudo-element masks scroll with the container if it scrolls.
- No mention of the wrapper-vs-content architecture
- No ResizeObserver
- No dynamic scroll position detection with JavaScript composable
- Static data attributes (no reactive show/hide)
- Uses a non-existent `data-fade-size` attribute
