# Box

A box is a generic container that provides managed access to design tokens.

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

## Basic

Box is a general-purpose container that allows for controlled use of design tokens. Use the given props to configure display behavior and styling that aligns with the Atlassian Design System. Use XCSS to style primitive components safely with tokens.

```jsx
import React from 'react';



import { Box, xcss } from '@atlaskit/primitives';



const boxStyles = xcss({

	borderColor: 'color.border.discovery',

	borderStyle: 'solid',

	borderRadius: '3px',

	borderWidth: 'border.width',

});



export default function Example() {

	return (

		<Box padding="space.400" backgroundColor="color.background.discovery" xcss={boxStyles}></Box>

	);

}
```

## Padding

Use padding props to access spacing design tokens and control internal layout. The following example demonstrates how each prop works with space tokens.

### padding

### paddingInline

### paddingBlock

### paddingInlineStart

### paddingInlineEnd

### paddingBlockStart

### paddingBlockEnd

The nomenclature used by these props follows logical properties. This naming is used to support different writing modes in Atlassian products.

```jsx
import React, { useState } from 'react';



import Heading from '@atlaskit/heading';

import { Box, Flex, Inline, type Space, Stack, xcss } from '@atlaskit/primitives';

import Range from '@atlaskit/range';



const boxStyles = xcss({

	display: 'block',

	justifyContent: 'start',

	color: 'color.text',

	borderColor: 'color.border.discovery',

	borderStyle: 'solid',

	borderRadius: '3px',

	borderWidth: 'border.width',

});



const spacingValues: Space[] = [

	'space.0',

	'space.025',

	'space.050',

	'space.075',

	'space.100',

	'space.150',

	'space.200',

	'space.250',

	'space.300',

	'space.400',

	'space.500',

	'space.600',

	'space.800',

	'space.1000',

];



export default function Example() {

	const [padding, setPadding] = useState(6);

	const [paddingInline, setPaddingInline] = useState(6);

	const [paddingInlineStart, setPaddingInlineStart] = useState(6);

	const [paddingInlineEnd, setPaddingInlineEnd] = useState(6);

	const [paddingBlock, setPaddingBlock] = useState(6);

	const [paddingBlockStart, setPaddingBlockStart] = useState(6);

	const [paddingBlockEnd, setPaddingBlockEnd] = useState(6);



	return (

		<Inline space="space.200">

			<Stack grow="fill">

				<Heading size="medium" id="box-padding">

					padding

				</Heading>

				<Box>{spacingValues[padding]}</Box>

				<Range

					max={spacingValues.length - 1}

					step={1}

					value={padding}

					onChange={(padding) => setPadding(padding)}

					aria-labelledby="box-padding"

				/>



				<Flex>

					<Box

						backgroundColor="color.background.discovery"

						xcss={boxStyles}

						padding={spacingValues[padding]}

					>

						Content

					</Box>

				</Flex>

			</Stack>



			<Stack grow="fill">

				<Heading size="medium" id="box-padding-inline">

					paddingInline

				</Heading>

				<Box>{spacingValues[paddingInline]}</Box>

				<Range

					max={spacingValues.length - 1}

					step={1}

					value={paddingInline}

					onChange={(paddingInline) => setPaddingInline(paddingInline)}

					aria-labelledby="box-padding-inline"

				/>



				<Heading size="medium" id="box-padding-block">

					paddingBlock

				</Heading>

				<Box>{spacingValues[paddingBlock]}</Box>

				<Range

					max={spacingValues.length - 1}

					step={1}

					value={paddingBlock}

					onChange={(paddingBlock) => setPaddingBlock(paddingBlock)}

					aria-labelledby="box-padding-block"

				/>



				<Flex>

					<Box

						backgroundColor="color.background.discovery"

						xcss={boxStyles}

						paddingInline={spacingValues[paddingInline]}

						paddingBlock={spacingValues[paddingBlock]}

					>

						Content

					</Box>

				</Flex>

			</Stack>



			<Stack grow="fill">

				<Heading size="medium" id="box-padding-inline-start">

					paddingInlineStart

				</Heading>

				<Box>{spacingValues[paddingInlineStart]}</Box>

				<Range

					max={spacingValues.length - 1}

					step={1}

					value={paddingInlineStart}

					onChange={(paddingInlineStart) => setPaddingInlineStart(paddingInlineStart)}

					aria-labelledby="box-padding-inline-start"

				/>



				<Heading size="medium" id="box-padding-inline-end">

					paddingInlineEnd

				</Heading>

				<Box>{spacingValues[paddingInlineEnd]}</Box>

				<Range

					max={spacingValues.length - 1}

					step={1}

					value={paddingInlineEnd}

					onChange={(paddingInlineEnd) => setPaddingInlineEnd(paddingInlineEnd)}

					aria-labelledby="box-padding-inline-end"

				/>



				<Heading size="medium" id="box-padding-block-start">

					paddingBlockStart

				</Heading>

				<Box>{spacingValues[paddingBlockStart]}</Box>

				<Range

					max={spacingValues.length - 1}

					step={1}

					value={paddingBlockStart}

					onChange={(paddingBlockStart) => setPaddingBlockStart(paddingBlockStart)}

					aria-labelledby="box-padding-block-start"

				/>



				<Heading size="medium" id="box-padding-block-end">

					paddingBlockEnd

				</Heading>

				<Box>{spacingValues[paddingBlockEnd]}</Box>

				<Range

					max={spacingValues.length - 1}

					step={1}

					value={paddingBlockEnd}

					onChange={(paddingBlockEnd) => setPaddingBlockEnd(paddingBlockEnd)}

					aria-labelledby="box-padding-block-end"

				/>



				<Flex>

					<Box

						backgroundColor="color.background.discovery"

						xcss={boxStyles}

						paddingBlockStart={spacingValues[paddingBlockStart]}

						paddingBlockEnd={spacingValues[paddingBlockEnd]}

						paddingInlineStart={spacingValues[paddingInlineStart]}

						paddingInlineEnd={spacingValues[paddingInlineEnd]}

					>

						Content

					</Box>

				</Flex>

			</Stack>

		</Inline>

	);

}
```

## Background color

Box accepts a wide variety of background colors, referenced as semantic design tokens. For the full list of color tokens, visit the token list.

```jsx
import React, { useState } from 'react';



import DropdownMenu, { DropdownItem } from '@atlaskit/dropdown-menu';

import { type BackgroundColor, Box, Inline, Stack, xcss } from '@atlaskit/primitives';



const boxStyles = xcss({

	borderStyle: 'solid',

	borderRadius: '3px',

	borderWidth: 'border.width',

});



const borderColorStylesMap = {

	neutral: xcss({ borderColor: 'color.border' }),

	warning: xcss({ borderColor: 'color.border.warning' }),

	selected: xcss({ borderColor: 'color.border.selected' }),

	danger: xcss({ borderColor: 'color.border.danger' }),

	success: xcss({ borderColor: 'color.border.success' }),

	discovery: xcss({ borderColor: 'color.border.discovery' }),

	information: xcss({ borderColor: 'color.border.information' }),

};



const colorMap = {

	neutral: {

		background: 'color.background.neutral',

		border: 'neutral',

	},

	warning: {

		background: 'color.background.warning',

		border: 'warning',

	},

	selected: {

		background: 'color.background.selected',

		border: 'selected',

	},

	danger: {

		background: 'color.background.danger',

		border: 'danger',

	},

	success: {

		background: 'color.background.success',

		border: 'success',

	},

	discovery: {

		background: 'color.background.discovery',

		border: 'discovery',

	},

	information: {

		background: 'color.background.information',

		border: 'information',

	},

};



export default function Example() {

	const [color, setColor]: [keyof typeof colorMap, Function] = useState('discovery');



	return (

		<Stack space="space.200" alignInline="start">

			<Inline alignBlock="center" space="space.100">

				<Box

					padding="space.400"

					backgroundColor={colorMap[color].background as BackgroundColor}

					xcss={[boxStyles, borderColorStylesMap[color]]}

				/>

				{color}

			</Inline>

			<DropdownMenu shouldRenderToParent trigger="Choose a color">

				{Object.keys(colorMap).map((el) => (

					<DropdownItem key={el} isSelected={el === color} onClick={() => setColor(el)}>

						{el}

					</DropdownItem>

				))}

			</DropdownMenu>

		</Stack>

	);

}
```

## XCSS

Box exposes an xcss prop. This prop accepts xcss function calls that contain a subset of permitted styles. When used with Box, xcss accepts most CSS properties, and when a token exists, the rule accepts that token as a value. For more information on XCSS, see the dedicated XCSS documentation.

```jsx
import React from 'react';



import { Box, Stack, xcss } from '@atlaskit/primitives';



const listStyles = xcss({

	paddingInlineStart: 'space.0',

});



const boxStyles = xcss({

	color: 'color.text',

	backgroundColor: 'color.background.discovery',

	borderWidth: 'border.width',

	borderStyle: 'solid',

	borderColor: 'color.border.discovery',

	padding: 'space.100',

	borderRadius: 'border.radius.100',

	transitionDuration: '200ms',

	listStyle: 'none',

	'::before': {

		content: '"✨"',

		paddingInlineEnd: 'space.050',

	},

	'::after': {

		content: '"✨"',

		paddingInlineStart: 'space.050',

	},

	':hover': {

		backgroundColor: 'color.background.discovery.bold.hovered',

		color: 'color.text.inverse',

		transform: 'scale(1.02)',

	},

});



export default function Example() {

	return (

		<Stack as="ul" xcss={listStyles}>

			<Box xcss={boxStyles} as="li">

				Hover over me

			</Box>

			<Box xcss={boxStyles} as="li">

				Hover over me

			</Box>

			<Box xcss={boxStyles} as="li">

				Hover over me

			</Box>

			<Box xcss={boxStyles} as="li">

				Hover over me

			</Box>

		</Stack>

	);

}
```

## Conditional styles

To achieve conditional styles, we suggest composing conditional styles via the props.xcss API rather than applying conditional behaviour to individual props. Toggle background color:

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

## Practical card example

Box is designed to be composed with inline, stack, and other components to create layouts. Atlassian uses dozens of distinct card-like components across products. Therefore, rather than providing a strict component, the Atlassian Design System empowers and supports you to build your own card components in ways that are consistent and will scale over time.

```jsx
import React from 'react';



import Avatar from '@atlaskit/avatar';

import Heading from '@atlaskit/heading';

import PullRequestIcon from '@atlaskit/icon/glyph/bitbucket/pullrequests';

import ShowMoreHorizontalIcon from '@atlaskit/icon/glyph/more';

import { AtlassianIcon } from '@atlaskit/logo';

import Lozenge from '@atlaskit/lozenge';

import { Box, Inline, Stack, Text, xcss } from '@atlaskit/primitives';



const containerStyles = xcss({

	display: 'flex',

	flexDirection: 'column',

	backgroundColor: 'elevation.surface.raised',

	padding: 'space.150',

	transition: '200ms',

	borderRadius: 'border.radius.100',

	boxShadow: 'elevation.shadow.raised',

	':hover': {

		backgroundColor: 'elevation.surface.hovered',

	},

});



const inlineStyles = xcss({

	display: 'flex',

	alignItems: 'center',

});



const extraInfoStyles = xcss({

	display: 'flex',

	justifyContent: 'space-between',

	paddingBlock: 'space.050',

});



export default function Example() {

	return (

		<Stack xcss={containerStyles} space="space.100">

			<Text as="span">

				Dropdown menu items in Modal are not accessible to keyboard/screen readers in Safari

			</Text>

			<Box as="span">

				<Lozenge appearance="new">Accelerate Cloud Accessibility</Lozenge>

			</Box>

			<Box xcss={extraInfoStyles}>

				<Box xcss={inlineStyles}>

					<AtlassianIcon appearance="brand" size="small" label="" />

					<Heading size="xxsmall">DSP-9786</Heading>

				</Box>

				<Inline space="space.100" alignBlock="center">

					<PullRequestIcon size="small" label="" />

					<ShowMoreHorizontalIcon size="small" label="" />

					<Avatar size="small" />

				</Inline>

			</Box>

		</Stack>

	);

}
```

---

[View Original Documentation](https://atlassian.design/components/primitives/box/examples)
