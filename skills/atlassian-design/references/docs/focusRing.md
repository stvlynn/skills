# Focus ring

A focus ring clearly indicates which item has keyboard focus.

---

## Default

A focus ring indicates the currently focused item. The default focus ring shows a line around the outside of the focused item. 

```jsx
/**

 * @jsxRuntime classic

 * @jsx jsx

 */

import { useEffect, useRef } from 'react';



// eslint-disable-next-line @atlaskit/ui-styling-standard/use-compiled -- Ignored via go/DSP-18766

import { css, jsx } from '@emotion/react';



import FocusRing from '@atlaskit/focus-ring';

import { Box, xcss } from '@atlaskit/primitives';

import { token } from '@atlaskit/tokens';



const buttonStyles = css({

	display: 'block',

	margin: `${token('space.150')} 0`,

	padding: token('space.100'),

	border: 'none',

	borderRadius: '3px',

});



const spacerStyles = xcss({

	padding: 'space.100',

});



export default () => {

	const buttonRef = useRef<HTMLButtonElement | null>(null);

	useEffect(() => {

		if (buttonRef.current) {

			buttonRef.current.focus();

		}

	}, []);



	return (

		<Box xcss={spacerStyles}>

			<FocusRing>

				<button type="button" ref={buttonRef} css={buttonStyles}>

					Keyboard focus to show ring

				</button>

			</FocusRing>

		</Box>

	);

};
```

## Inset line

You can toggle the focus ring to show inside the focused item. This is for cases when an inset line is more visible than the default line or to avoid overlapping other UI. 

```jsx
/**

 * @jsxRuntime classic

 * @jsx jsx

 */

import { useEffect, useRef } from 'react';



// eslint-disable-next-line @atlaskit/ui-styling-standard/use-compiled -- Ignored via go/DSP-18766

import { css, jsx } from '@emotion/react';



import FocusRing from '@atlaskit/focus-ring';

import { Box, xcss } from '@atlaskit/primitives';

import { token } from '@atlaskit/tokens';



const buttonStyles = css({

	display: 'block',

	margin: `${token('space.150')} 0`,

	padding: token('space.100'),

	border: 'none',

	borderRadius: '3px',

});



const spacerStyles = xcss({

	padding: 'space.100',

});



export default () => {

	const buttonRef = useRef<HTMLButtonElement | null>(null);

	useEffect(() => {

		if (buttonRef.current) {

			buttonRef.current.focus();

		}

	}, []);



	return (

		<Box xcss={spacerStyles}>

			<FocusRing isInset>

				<button type="button" ref={buttonRef} css={buttonStyles}>

					Keyboard focus to show ring

				</button>

			</FocusRing>

		</Box>

	);

};
```

---

[View Original Documentation](https://atlassian.design/components/focus-ring/examples)
