# React

## Reusable hook

```ts
import { useCallback, useEffect, useRef, useState } from "react";

export function useScrollFade<T extends HTMLElement = HTMLDivElement>() {
  const ref = useRef<T>(null);
  const [fadeTop, setFadeTop] = useState(false);
  const [fadeBottom, setFadeBottom] = useState(false);

  const updateScrollFade = useCallback(() => {
    const element = ref.current;
    if (!element) return;

    const { scrollTop, scrollHeight, clientHeight } = element;
    const isAtTop = scrollTop <= 0;
    const isAtBottom = scrollTop + clientHeight >= scrollHeight - 1;

    setFadeTop(!isAtTop);
    setFadeBottom(!isAtBottom);
  }, []);

  useEffect(() => {
    const element = ref.current;
    if (!element) return;

    updateScrollFade();
    element.addEventListener("scroll", updateScrollFade);

    const resizeObserver = new ResizeObserver(updateScrollFade);
    resizeObserver.observe(element);

    return () => {
      element.removeEventListener("scroll", updateScrollFade);
      resizeObserver.disconnect();
    };
  }, [updateScrollFade]);

  return { ref, fadeTop, fadeBottom, updateScrollFade };
}
```

## Usage

```tsx
import { useScrollFade } from "./hooks/useScrollFade";

export function ScrollFadeDropdown({ options }: { options: string[] }) {
  const { ref, fadeTop, fadeBottom } = useScrollFade<HTMLDivElement>();

  return (
    <div
      className="fc-scroll-fade-wrapper fc-scroll-fade-wrapper-white"
      data-fade-top={fadeTop}
      data-fade-bottom={fadeBottom}
    >
      <div ref={ref} className="dropdown-list">
        {options.map((option) => (
          <button key={option} className="dropdown-item" type="button">
            {option}
          </button>
        ))}
      </div>
    </div>
  );
}
```

## Notes

- Keep the hook reusable. Avoid burying the scroll logic directly in one component unless the user asked for a one-off patch.
- For white dropdowns, use `fc-scroll-fade-wrapper-white`.
- If the container content changes after async fetches, the `ResizeObserver` handles it.
