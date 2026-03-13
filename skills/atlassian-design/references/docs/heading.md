# Heading

A heading is a typography component used to display text in different sizes and formats.

---

## Basic

Use a Heading component for all page titles and subheadings to introduce content. Headings are sized to contrast with content, increase visual hierarchy, and help readers easily understand the structure of content. 

## Heading Large

### Heading Medium

```jsx
import React from 'react';



import Heading from '@atlaskit/heading';

import { Stack } from '@atlaskit/primitives/compiled';



export default () => {

	return (

		<Stack testId="headings" space="space.100">

			<Heading size="xxlarge">Heading XXLarge</Heading>

			<Heading size="xlarge">Heading XLarge</Heading>

			<Heading size="large">Heading Large</Heading>

			<Heading size="medium">Heading Medium</Heading>

			<Heading size="small">Heading Small</Heading>

			<Heading size="xsmall">Heading XSmall</Heading>

			<Heading size="xxsmall">Heading XXSmall</Heading>

		</Stack>

	);

};
```

## Mapping to HTML heading elements

The size provided automatically maps to specific HTML heading elements. xxlarge and xlarge both render a <h1>, large renders a <h2>, medium renders a <h3>, and so on. This mapping can be overridden using the as prop, or automatically incremented using the HeadingContextProvider. 

```jsx
import React from 'react';



import Heading from '@atlaskit/heading';

import { Stack } from '@atlaskit/primitives/compiled';



export default () => {

	return (

		<Stack testId="headings" space="space.100">

			<Heading size="medium" as="h1">

				Medium heading that will render as a h1

			</Heading>

		</Stack>

	);

};
```

## Color

Heading uses the color.text token which automatically switches colors to be legible across both light and dark modes. Heading will automatically apply the correct inverse color token if placed within a box component with a bold background color. 

## Heading color is default.

## Heading color is automatically inverted.

## Heading color is automatically inverted.

To invert the heading color manually when not using a box component, use the color prop to apply either color.text.inverse or color.text.warning.inverse depending on the surface. Beyond this, heading color cannot be customised. 

```jsx
import React from 'react';



import Heading from '@atlaskit/heading';

import { Box, Stack } from '@atlaskit/primitives/compiled';



export default () => {

	return (

		<Stack space="space.100">

			<Box backgroundColor="elevation.surface" padding="space.200">

				<Heading size="large">Heading color is default.</Heading>

			</Box>

			<Box backgroundColor="color.background.brand.boldest" padding="space.200">

				<Heading size="large">Heading color is automatically inverted.</Heading>

			</Box>

			<Box backgroundColor="color.background.warning.bold" padding="space.200">

				<Heading size="large">Heading color is automatically inverted.</Heading>

			</Box>

		</Stack>

	);

};
```

## Heading color can be manually inverted.

## Heading color can be manually inverted.

```jsx
/**

 * @jsxRuntime classic

 * @jsx jsx

 */

import { css, jsx } from '@atlaskit/css';

import Heading from '@atlaskit/heading';

import { Stack } from '@atlaskit/primitives/compiled';

import { token } from '@atlaskit/tokens';



const containerStylesBrandBoldest = css({

	backgroundColor: token('color.background.brand.boldest'),

	paddingBlockEnd: token('space.200'),

	paddingBlockStart: token('space.200'),

	paddingInlineEnd: token('space.200'),

	paddingInlineStart: token('space.200'),

});



const containerStylesWarningBold = css({

	backgroundColor: token('color.background.warning.bold'),

	paddingBlockEnd: token('space.200'),

	paddingBlockStart: token('space.200'),

	paddingInlineEnd: token('space.200'),

	paddingInlineStart: token('space.200'),

});



export default () => {

	return (

		<Stack space="space.100">

			{/* Purposefully not using a Box in order to show manually setting Heading color */}

			<div css={containerStylesBrandBoldest}>

				<Heading size="large" color="color.text.inverse">

					Heading color can be manually inverted.

				</Heading>

			</div>

			<div css={containerStylesWarningBold}>

				<Heading size="large" color="color.text.warning.inverse">

					Heading color can be manually inverted.

				</Heading>

			</div>

		</Stack>

	);

};
```

## Arrangement with other text styles

Heading does not apply any vertical margin or spacing. To control space between headings and other content, use a stack component. 

### Update profile image

```jsx
import React from 'react';



import Button from '@atlaskit/button/new';

import { cssMap } from '@atlaskit/css';

import Heading from '@atlaskit/heading';

import { Box, Inline, Stack, Text } from '@atlaskit/primitives/compiled';

import { token } from '@atlaskit/tokens';



const styles = cssMap({

	card: {

		borderRadius: token('border.radius'),

		boxShadow: token('elevation.shadow.overlay'),

		width: '400px',

	},

});



export default () => {

	return (

		<Box backgroundColor="elevation.surface.overlay" padding="space.300" xcss={styles.card}>

			<Stack space="space.200">

				<Heading size="medium">Update profile image</Heading>

				<Text>

					Add a profile image to personalize your account and help others recognize you. Would you

					like to upload a new profile picture now?

				</Text>

				<Inline space="space.100" alignInline="end">

					<Button appearance="subtle">Skip for now</Button>

					<Button appearance="primary">Upload</Button>

				</Inline>

			</Stack>

		</Box>

	);

};
```

## Heading provider

The HeadingContextProvider allows you to configure the default HTML heading level for all headings. By nesting a HeadingContextProvider, you can override the default HTML heading level for a subtree. This is useful when you want to use a different HTML heading level for a section of your page but don't have control over where in the heading hierarchy that section will be placed. 

## Heading xxlarge as h2

### Heading medium as h3

This section's heading is rendered as a h3, despite being medium. This section's heading is rendered as a h4, despite being medium. 

```jsx
import React from 'react';



import Heading, { HeadingContextProvider } from '@atlaskit/heading';

import { Box, Stack, Text } from '@atlaskit/primitives/compiled';



const Section = ({ size, willRenderAs, children }: any) => (

	<HeadingContextProvider>

		<Stack space="space.100">

			<Heading size={size}>

				Heading {size} as {willRenderAs}

			</Heading>

			<Text as="p">

				This section's heading is rendered as a {willRenderAs}, despite being {size}.

			</Text>

			{children}

		</Stack>

	</HeadingContextProvider>

);



export default () => {

	return (

		<HeadingContextProvider value={2}>

			{/* eslint-disable-next-line @atlaskit/ui-styling-standard/enforce-style-prop -- Ignored via go/DSP-18766 */}

			<Box style={{ maxWidth: 850, margin: 'auto' }}>

				<Stack testId="headings" space="space.100">

					<Heading size="xxlarge">Heading xxlarge as h2</Heading>

					<Section size="medium" willRenderAs="h3">

						<Section size="medium" willRenderAs="h4" />

					</Section>

				</Stack>

			</Box>

		</HeadingContextProvider>

	);

};
```

---

[View Original Documentation](https://atlassian.design/components/heading/examples)
