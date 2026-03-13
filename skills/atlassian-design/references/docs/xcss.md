# XCSS

XCSS is a safer, tokens-first approach to CSS-in-JS.

---

## Installation

<### Package installation information

#### Install

`yarn add @atlaskit/primitives`

#### Source

[Bitbucket.org﻿, (opens new window)](https://bitbucket.org/atlassian/atlassian-frontend-mirror/src/master/design-system/primitives)

npm

[@atlaskit/primitives﻿, (opens new window)](https://www.npmjs.com/package/@atlaskit/primitives)

Bundle

[unpkg.com﻿, (opens new window)](https://unpkg.com/@atlaskit/primitives/dist/)

## Basic

XCSS can pull together different types of interactions and UI in a safer, more composable way.

### A Card

```jsx
import React from 'react';



import Heading from '@atlaskit/heading';

import { Box, Stack, xcss } from '@atlaskit/primitives';



const textStyles = xcss({

	color: 'color.text',

});



const cardStyles = xcss({

	backgroundColor: 'elevation.surface',

	padding: 'space.200',

	borderColor: 'color.border',

	borderWidth: 'border.width',

	borderStyle: 'solid',

	borderRadius: 'border.radius.100',

});



const MyCard = () => (

	<Box xcss={cardStyles}>

		<Stack space="space.100">

			<Heading size="medium">A Card</Heading>

			<Box xcss={textStyles}>With a description.</Box>

		</Stack>

	</Box>

);



export default MyCard;
```

## Interactivity

To enable interactivity, use familiar selectors like :hover and :focus-visible.

### A Card

```jsx
import React from 'react';



import Heading from '@atlaskit/heading';

import { Box, Stack, xcss } from '@atlaskit/primitives';



const textStyles = xcss({

	color: 'color.text',

});



const cardStyles = xcss({

	backgroundColor: 'elevation.surface',

	padding: 'space.200',

	borderColor: 'color.border',

	borderWidth: 'border.width',

	borderStyle: 'solid',

	borderRadius: '3px',

	':hover': {

		backgroundColor: 'elevation.surface.hovered',

	},

	':focus-visible': {

		outline: '2px solid',

		outlineOffset: 'space.025',

		outlineColor: 'color.border.focused',

	},

});



const InteractiveCard = () => (

	<Box xcss={cardStyles} tabIndex={0}>

		<Stack space="space.100">

			<Heading size="medium">A Card</Heading>

			<Box xcss={textStyles}>With a description.</Box>

		</Stack>

	</Box>

);



export default InteractiveCard;
```

## Responsiveness

XCSS also accepts a subset of media queries at predefined breakpoints.

### A Responsive Card

```jsx
import React from 'react';



import Heading from '@atlaskit/heading';

import { Box, Stack, xcss } from '@atlaskit/primitives';

import { media } from '@atlaskit/primitives/responsive';



const textStyles = xcss({

	color: 'color.text',

});



const cardStyles = xcss({

	backgroundColor: 'color.background.neutral',

	padding: 'space.200',

	borderColor: 'color.border',

	borderWidth: 'border.width.outline',

	borderStyle: 'solid',

	borderRadius: '2px',

	[media.above.xxs]: {

		backgroundColor: 'color.background.accent.red.subtler',

	},

	[media.above.xs]: {

		backgroundColor: 'color.background.accent.yellow.subtler',

	},

	[media.above.sm]: {

		backgroundColor: 'color.background.accent.green.subtler',

	},

	[media.above.md]: {

		backgroundColor: 'color.background.accent.orange.subtler',

	},

	[media.above.lg]: {

		backgroundColor: 'color.background.accent.magenta.subtler',

	},

});



const ResponsiveCard = () => (

	<Box xcss={cardStyles} tabIndex={0}>

		<Stack space="space.100">

			<Heading size="medium">A Responsive Card</Heading>

			<Box xcss={textStyles}>Change your screen width to see me change color.</Box>

		</Stack>

	</Box>

);



export default ResponsiveCard;
```

## Conditional styles

For conditional styles, try composing styles together via the array with ternary or boolean operators. Toggle background color:

```jsx
import React, { useState } from 'react';



import { Box, Inline, xcss } from '@atlaskit/primitives';

import Toggle from '@atlaskit/toggle';



const baseStyles = xcss({

	paddingBlock: 'space.500',

	width: '100%',

	borderRadius: '3px',

});



const enabledStyles = xcss({

	backgroundColor: 'color.background.accent.green.bolder',

});



const disabledStyles = xcss({

	backgroundColor: 'color.background.accent.gray.bolder',

});



export default function ConditionalStyles() {

	const [isEnabled, setEnabled] = useState(false);



	return (

		<Box testId="example" padding="space.200">

			<Inline alignBlock="center">

				<p>Toggle background color:</p>

				<Toggle onChange={() => setEnabled((current) => !current)} />

			</Inline>

			<Box xcss={[baseStyles, isEnabled ? enabledStyles : disabledStyles]} />

		</Box>

	);

}
```

---

[View Original Documentation](https://atlassian.design/components/primitives/xcss/examples)
