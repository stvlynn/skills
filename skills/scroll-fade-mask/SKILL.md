---
name: scroll-fade-mask
description: Use this skill whenever the user wants iOS-style scroll fades, gradient masks, scroll-edge overlays, or top/bottom indicators on a scrollable list, dropdown, sidebar, modal, chat log, or panel. It implements a reusable wrapper-based scroll fade mask pattern across React, Vue, Svelte, and vanilla JavaScript, and it is also the right skill when the user says the fade masks broke scrolling, do not show, or do not match the background.
---

# Scroll Fade Mask

Use this skill to implement or troubleshoot gradient fade masks on scrollable containers without breaking scrolling behavior.

## What is bundled

- Architecture and CSS system: `references/architecture.md`
- Framework implementations:
  - React: `references/react.md`
  - Vue 3: `references/vue.md`
  - Svelte: `references/svelte.md`
  - Vanilla JS: `references/vanilla-js.md`
- Troubleshooting and debugging checklist: `references/troubleshooting.md`
- Eval prompts for regression testing: `evals/evals.json`

## Task mapping

- New implementation: open `references/architecture.md` plus the framework file for the user's stack.
- Existing component integration: open `references/architecture.md` and adapt the wrapper around the user's current scroll container.
- Bug report or broken behavior: open `references/troubleshooting.md` first, then the framework file if behavior code is involved.

## Working rules

1. Start from the wrapper pattern in `references/architecture.md`. Do not improvise with conditional fade divs unless the user explicitly asks for that tradeoff.
2. Keep responsibilities split:
   - Wrapper owns pseudo-element masks and `data-fade-*` state.
   - Inner element owns `overflow-y: auto` and the actual scrolling.
3. The wrapper must not become the scroll container by accident. Avoid recommending `overflow: hidden` or `overflow-y: auto` on the wrapper.
4. Match the gradient color to the real background. Use the provided white or warm variants when they fit, otherwise customize the CSS variable.
5. For framework implementations, prefer a reusable primitive:
   - React hook
   - Vue composable
   - Svelte action
   - Vanilla JS class
6. Include `ResizeObserver` when you provide behavior code so the masks react to dynamic content changes.
7. For troubleshooting, diagnose layout and overflow first, then refs/listeners, then z-index/background issues.
8. Respond in the user's language unless the surrounding codebase clearly suggests otherwise.

## Default workflow

1. Identify the task type: implementation, integration into existing markup, or troubleshooting.
2. Open `references/architecture.md` first.
3. Open the smallest relevant framework file for the user's stack.
4. If the user reports a bug, also open `references/troubleshooting.md`.
5. Return adapted code, not a generic dump:
   - CSS system
   - behavior primitive for their stack
   - integration example using their container shape
   - brief notes on why the wrapper pattern matters

## Routing shortcuts

- Global CSS and class variants: `references/architecture.md`
- React hook + JSX usage: `references/react.md`
- Vue 3 composable + template usage: `references/vue.md`
- Svelte action + state wiring: `references/svelte.md`
- Framework-free implementation: `references/vanilla-js.md`
- "Can't scroll", masks not showing, wrong edge state: `references/troubleshooting.md`

## Output expectations

- Implementation requests should include the wrapper markup, the scroll container contract, and the behavior code for the user's stack.
- Troubleshooting requests should clearly identify the likely root cause before presenting the fix.
- When the user gives a background color, incorporate it into the recommended gradient setup.
- Keep code production-oriented: reusable helpers, no brittle inline scroll logic unless the user asks for the fastest possible one-off patch.
