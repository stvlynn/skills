# Responsive

Responsive helpers and primitives to build responsive UIs.

---

## Installation

### Package installation information

#### Install

`yarn add @atlaskit/primitives`

#### Source

[Bitbucket.org﻿, (opens new window)](https://bitbucket.org/atlassian/atlassian-frontend-mirror/src/master/design-system/primitives)

npm

[@atlaskit/primitives﻿, (opens new window)](https://www.npmjs.com/package/@atlaskit/primitives)

Bundle

[unpkg.com﻿, (opens new window)](https://unpkg.com/@atlaskit/primitives/dist/)

## Responsive css or xcss

Utilize our media queries exposed in css, styled, or xcss as computed keys to build responsive UIs. Learn more about these media query exports in usage.

### Using with xcss

Please use xcss whenever possible to ensure consistency and safety with style overrides. Read more at xcss

```jsx
import React from 'react';



import { Box, xcss } from '@atlaskit/primitives';

import { media } from '@atlaskit/primitives/responsive';



const cardStyles = xcss({

	borderColor: 'color.border.discovery',

	borderStyle: 'solid',

	borderWidth: 'border.width.0',

	padding: 'space.050',

	[media.above.xs]: {

		padding: 'space.100',

	},

	[media.above.sm]: {

		borderWidth: 'border.width',

		padding: 'space.150',

	},

	[media.above.md]: {

		borderWidth: 'border.width.outline',

		padding: 'space.200',

	},

});



export default () => (

	<Box xcss={cardStyles}>

		Border becomes narrower at smaller breakpoints. Try it out by resizing the browser window.

	</Box>

);
```

### Using with css

```jsx
/**

 * @jsxRuntime classic

 * @jsx jsx

 */

// eslint-disable-next-line @atlaskit/ui-styling-standard/use-compiled -- Ignored via go/DSP-18766

import { css, jsx } from '@emotion/react';



import { media } from '@atlaskit/primitives/responsive';

import { token } from '@atlaskit/tokens';



const cardStyles = css({

	padding: token('space.050'),

	borderColor: token('color.border.discovery'),

	borderStyle: 'solid',

	borderWidth: token('border.width.0'),

	[media.above.xs]: {

		padding: token('space.100'),

	},

	[media.above.sm]: {

		padding: token('space.150'),

		borderWidth: token('border.width'),

	},

	[media.above.md]: {

		padding: token('space.200'),

		borderWidth: token('border.width.outline'),

	},

});



export default () => (

	<div css={cardStyles}>

		Border becomes narrower at smaller breakpoints. Try it out by resizing the browser window.

	</div>

);
```

## Responsive primitives

Consider these shortcuts to writing your own custom media queries. Composing with our primitives will be far quicker and consistent to implement, but may result in excess DOM nodes.

---

[View Original Documentation](https://atlassian.design/components/primitives/responsive/examples)
