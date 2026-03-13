# Bleed

A bleed controls negative whitespace in layouts.

---

## Installation

### Package installation information

### Install

`yarn add @atlaskit/primitives`

### Source

[Bitbucket.org﻿, (opens new window)](https://bitbucket.org/atlassian/atlassian-frontend-mirror/src/master/design-system/primitives)

npm

[@atlaskit/primitives﻿, (opens new window)](https://www.npmjs.com/package/@atlaskit/primitives)

Bundle

[unpkg.com﻿, (opens new window)](https://unpkg.com/@atlaskit/primitives/dist/)

## Using Bleed

Bleed is a component that allows its children to break the boundaries of its container. This is useful for content that wants to negate the padding or whitespace applied by its parent in a controlled manner. For example in the below grid layout, the middle item bleeds across the inline and block axes to overlap the gap set by the grid.

```jsx
import React from 'react';



import { Bleed, Box, Grid } from '@atlaskit/primitives';



import ExampleBox from '../shared/example-box';



export default function Basic() {

	return (

		<Box padding="space.200" backgroundColor="color.background.neutral">

			<Grid templateColumns="1fr 1fr 1fr" gap="space.100">

				<ExampleBox />

				<ExampleBox />

				<ExampleBox />

				<ExampleBox />

				<Bleed all="space.150">

					<ExampleBox

						// eslint-disable-next-line @atlaskit/ui-styling-standard/enforce-style-prop -- Ignored via go/DSP-18766

						style={{ height: '100%', position: 'relative' }}

						backgroundColor="color.background.discovery.pressed"

					/>

				</Bleed>

				<ExampleBox />

				<ExampleBox />

				<ExampleBox />

				<ExampleBox />

			</Grid>

		</Box>

	);

}
```

## Bleed and no bleed

Bleed might be utilised to create a stacking effect with a group of avatars. Here each avatar is laid out with the Inline parent container. Without a bleed, each avatar would sit directly adjacent to its sibling. With Bleed we can negate the whitespace and force each avatar to overlap its direct sibling and create our desired stack.

```jsx
import React from 'react';



import PersonIcon from '@atlaskit/icon/glyph/person';

import { Bleed, Inline, Pressable, Stack, xcss } from '@atlaskit/primitives';



const buttonStyles = xcss({

	padding: 'space.0',

	color: 'color.text.inverse',

	borderRadius: '9999px',

	borderWidth: 'border.width.outline',

	borderColor: 'color.border.bold',

	borderStyle: 'solid',

	fontSize: '1.5rem',

	lineHeight: '1.5rem',

	':hover': {

		position: 'relative',

		backgroundColor: 'color.background.neutral.bold.hovered',

	},

});



const nudgeStyles = xcss({

	paddingInlineStart: 'space.050',

});



export default function Basic() {

	return (

		<Stack space="space.100">

			<Inline>

				{['first', 'second', 'third', 'fourth'].map((key) => (

					<Pressable key={key} xcss={buttonStyles} backgroundColor="color.background.neutral.bold">

						<PersonIcon label="An avatar" size="medium" />

					</Pressable>

				))}

			</Inline>

			<Inline xcss={nudgeStyles}>

				{['first', 'second', 'third', 'fourth'].map((key) => (

					<Bleed inline="space.050" key={key}>

						<Pressable xcss={buttonStyles} backgroundColor="color.background.neutral.bold">

							<PersonIcon label="An avatar" size="medium" />

						</Pressable>

					</Bleed>

				))}

			</Inline>

		</Stack>

	);

}
```

## Block whitespace

Bleed can be controlled on the block axis (vertical) with the block property. The values of this property are tied to our spacing scale. Note, in the context of a flex container bleed will collapse the whitespace around its child element.

```jsx
import React from 'react';



import { Bleed, Box, Stack } from '@atlaskit/primitives';



import ExampleBox from '../shared/example-box';



export default function Basic() {

	return (

		<Box padding="space.200" backgroundColor="color.background.neutral">

			<Stack space="space.100">

				<ExampleBox />

				<ExampleBox />

				<Bleed block="space.150">

					<ExampleBox

						// eslint-disable-next-line @atlaskit/ui-styling-standard/enforce-style-prop -- Ignored via go/DSP-18766

						style={{ position: 'relative' }}

						backgroundColor="color.background.discovery.pressed"

					/>

				</Bleed>

				<ExampleBox />

				<ExampleBox />

			</Stack>

		</Box>

	);

}
```

## Inline whitespace

Bleed can also be controlled on the inline axis (horizontal) with the inline property. The values of this property are tied to our spacing scale. Note, in the context of a flex container bleed will collapse the whitespace around its child element.

```jsx
import React from 'react';



import { Bleed, Box, Inline } from '@atlaskit/primitives';



import ExampleBox from '../shared/example-box';



export default function Basic() {

	return (

		<Box padding="space.200" backgroundColor="color.background.neutral">

			<Inline space="space.100">

				<ExampleBox />

				<ExampleBox />

				<Bleed inline="space.150">

					<ExampleBox

						// eslint-disable-next-line @atlaskit/ui-styling-standard/enforce-style-prop -- Ignored via go/DSP-18766

						style={{ position: 'relative' }}

						backgroundColor="color.background.discovery.pressed"

					/>

				</Bleed>

				<ExampleBox />

				<ExampleBox />

			</Inline>

		</Box>

	);

}
```

---

[View Original Documentation](https://atlassian.design/components/primitives/bleed/examples)
