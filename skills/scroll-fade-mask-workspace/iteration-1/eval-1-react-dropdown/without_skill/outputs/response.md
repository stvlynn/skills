# Eval 1 Baseline — React Dropdown Scroll Fade (No Skill)

## ScrollFadeDropdown.tsx

```tsx
import React, { useState, useRef, useEffect } from 'react';
import './ScrollFadeDropdown.css';

interface DropdownOption {
  value: string;
  label: string;
}

interface ScrollFadeDropdownProps {
  options: DropdownOption[];
  value?: string;
  onChange?: (value: string) => void;
  placeholder?: string;
}

export const ScrollFadeDropdown: React.FC<ScrollFadeDropdownProps> = ({
  options,
  value,
  onChange,
  placeholder = 'Select an option...'
}) => {
  const [isOpen, setIsOpen] = useState(false);
  const [showTopFade, setShowTopFade] = useState(false);
  const [showBottomFade, setShowBottomFade] = useState(false);
  const dropdownRef = useRef<HTMLDivElement>(null);
  const listRef = useRef<HTMLDivElement>(null);

  const selectedOption = options.find(opt => opt.value === value);

  const handleScroll = () => {
    if (!listRef.current) return;
    const { scrollTop, scrollHeight, clientHeight } = listRef.current;
    setShowTopFade(scrollTop > 0);
    setShowBottomFade(scrollTop + clientHeight < scrollHeight - 1);
  };

  useEffect(() => {
    if (isOpen && listRef.current) {
      handleScroll();
    }
  }, [isOpen]);

  useEffect(() => {
    const handleClickOutside = (event: MouseEvent) => {
      if (dropdownRef.current && !dropdownRef.current.contains(event.target as Node)) {
        setIsOpen(false);
      }
    };
    document.addEventListener('mousedown', handleClickOutside);
    return () => document.removeEventListener('mousedown', handleClickOutside);
  }, []);

  const handleSelect = (optionValue: string) => {
    onChange?.(optionValue);
    setIsOpen(false);
  };

  return (
    <div className="scroll-fade-dropdown" ref={dropdownRef}>
      <button
        className="dropdown-trigger"
        onClick={() => setIsOpen(!isOpen)}
        type="button"
      >
        <span>{selectedOption?.label || placeholder}</span>
        <span className={`arrow ${isOpen ? 'open' : ''}`}>▼</span>
      </button>

      {isOpen && (
        <div className="dropdown-menu">
          <div
            className="dropdown-list"
            ref={listRef}
            onScroll={handleScroll}
          >
            {options.map((option) => (
              <div
                key={option.value}
                className={`dropdown-item ${option.value === value ? 'selected' : ''}`}
                onClick={() => handleSelect(option.value)}
              >
                {option.label}
              </div>
            ))}
          </div>

          {showTopFade && <div className="fade-mask fade-top" />}
          {showBottomFade && <div className="fade-mask fade-bottom" />}
        </div>
      )}
    </div>
  );
};
```

## ScrollFadeDropdown.css

```css
.scroll-fade-dropdown {
  position: relative;
  width: 300px;
}

.dropdown-trigger {
  width: 100%;
  padding: 12px 16px;
  background: white;
  border: 1px solid #d1d5db;
  border-radius: 8px;
  display: flex;
  justify-content: space-between;
  align-items: center;
  cursor: pointer;
  font-size: 14px;
  transition: border-color 0.2s;
}

.dropdown-trigger:hover { border-color: #9ca3af; }
.dropdown-trigger:focus {
  outline: none;
  border-color: #3b82f6;
  box-shadow: 0 0 0 3px rgba(59, 130, 246, 0.1);
}

.arrow { font-size: 10px; transition: transform 0.2s; color: #6b7280; }
.arrow.open { transform: rotate(180deg); }

.dropdown-menu {
  position: absolute;
  top: calc(100% + 4px);
  left: 0; right: 0;
  background: white;
  border: 1px solid #d1d5db;
  border-radius: 8px;
  box-shadow: 0 10px 25px rgba(0, 0, 0, 0.1);
  z-index: 1000;
  overflow: hidden;
}

.dropdown-list {
  max-height: 320px;
  overflow-y: auto;
}

.dropdown-item {
  padding: 12px 16px;
  cursor: pointer;
  transition: background-color 0.15s;
  font-size: 14px;
}
.dropdown-item:hover { background-color: #f3f4f6; }
.dropdown-item.selected { background-color: #eff6ff; color: #3b82f6; font-weight: 500; }

.fade-mask {
  position: absolute;
  left: 0; right: 0;
  height: 40px;
  pointer-events: none;
  z-index: 1;
}
.fade-top { top: 0; background: linear-gradient(to bottom, white, transparent); }
.fade-bottom { bottom: 0; background: linear-gradient(to top, white, transparent); }
```

## Key Observations

- Uses **conditional rendering** (`{showTopFade && <div>}`) instead of wrapper pattern with pseudo-elements
- Single-step gradient (no multi-stop opacity curve)
- No ResizeObserver for dynamic content changes
- No reusable hook — scroll logic embedded in component
- No wrapper pattern — fade divs are siblings inside `.dropdown-menu`
