# Text

Text is a token-backed typography component to display body text.

---

## Basic

Use a Text component for main content. Text typically appears after headings or subheadings as detailed descriptions and messages, but also as standalone text in components. The size prop expresses the visual appearance of the text element: 

```jsx
import React from 'react';



import { Stack, Text } from '@atlaskit/primitives';



export default () => {

	return (

		<Stack space="space.100">

			<Text size="large">Text size: large</Text>

			<Text>Text size: medium (default)</Text>

			<Text size="small">Text size: small</Text>

		</Stack>

	);

};
```

## Color

Text uses the color.text token which automatically switches colors to be legible across both light and dark modes. Text will automatically apply the correct inverse color token if placed within a box component with a bold background color. The color prop can be used with any text color token. If Text is nested inside another Text component, color will automatically inherit from its parent. 

```jsx
import React from 'react';



import { Box, Stack, Text } from '@atlaskit/primitives';



export default () => {

	return (

		<Stack space="space.100">

			<Box backgroundColor="color.background.information" padding="space.200">

				<Text weight="bold">Text color is default.</Text>

			</Box>

			<Box backgroundColor="color.background.brand.bold" padding="space.200">

				<Text weight="bold">Text color is automatically inverted.</Text>

			</Box>

			<Box backgroundColor="color.background.warning.bold" padding="space.200">

				<Text weight="bold">Text color is automatically inverted.</Text>

			</Box>

		</Stack>

	);

};
```

```jsx
import React from 'react';



import { Stack, Text } from '@atlaskit/primitives';



export default () => {

	return (

		<Stack space="space.100">

			<Text weight="medium" color="color.text.discovery">

				Text color <Text weight="bold">is inherited</Text> from its parent.

			</Text>

			<Text weight="medium" color="color.text.accent.purple">

				Text color{' '}

				<Text weight="bold" color="color.text.accent.purple.bolder">

					can also be overriden.

				</Text>

			</Text>

		</Stack>

	);

};
```

## Font weight

Font weight defaults to regular (400) and can be set using the weight prop. More information about the available weights can be found on the typography foundations page. Note: Text supports the semibold weight, however due to differences between font stacks across different operating systems, semibold text may render as bold. We recommend using regular, medium, and bold for the best results. 

```jsx
import React from 'react';



import { Stack, Text } from '@atlaskit/primitives';



export default () => {

	return (

		<Stack space="space.100">

			<Text>Text weight: regular (default)</Text>

			<Text weight="medium">Text weight: medium</Text>

			<Text weight="semibold">Text weight: semibold</Text>

			<Text weight="bold">Text weight: bold</Text>

		</Stack>

	);

};
```

## Alignment

Text can be aligned using the align prop. Text alignment: Start Text alignment: Center Text alignment: End 

```jsx
import React from 'react';



import { Stack, Text } from '@atlaskit/primitives';



export default () => {

	return (

		<Stack space="space.100">

			<Stack space="space.0">

				<Text align="start" as="p">

					Text alignment:

				</Text>

				<Text align="start" as="p">

					Start

				</Text>

			</Stack>

			<Stack space="space.0">

				<Text align="center" as="p">

					Text alignment:

				</Text>

				<Text align="center" as="p">

					Center

				</Text>

			</Stack>

			<Stack space="space.0">

				<Text align="end" as="p">

					Text alignment:

				</Text>

				<Text align="end" as="p">

					End

				</Text>

			</Stack>

		</Stack>

	);

};
```

## Rendered HTML element

Text renders a HTML <span> element by default. Use the as prop to change the rendered HTML element. Text as <p> 

```jsx
import React from 'react';



import { Stack, Text } from '@atlaskit/primitives';



export default () => {

	return (

		<Stack space="space.100">

			<Text>Text as {'<span>'} (default)</Text>

			<Text as="p">Text as {'<p>'}</Text>

			<Text as="strong">Text as {'<strong>'}</Text>

			<Text as="em">Text as {'<em>'}</Text>

		</Stack>

	);

};
```

## Arrangement with other text styles

Text does not apply any vertical margin or spacing. To control space between text and other content, use a stack component. The available values for paragraph spacing are outlined in the Typography foundations page. 

### Update profile image

```jsx
import React from 'react';



import Button from '@atlaskit/button/new';

import Heading from '@atlaskit/heading';

import { Box, Inline, Stack, Text, xcss } from '@atlaskit/primitives';



export default () => {

	return (

		<Box backgroundColor="elevation.surface.overlay" padding="space.300" xcss={cardStyles}>

			<Stack space="space.200">

				<Heading size="medium">Update profile image</Heading>

				<Stack space="space.200">

					<Text>

						Add a profile image to personalize your account and help others recognize you.

					</Text>

					<Text>Would you like to upload a new profile picture now?</Text>

				</Stack>

				<Inline space="space.100" alignInline="end">

					<Button appearance="subtle">Skip for now</Button>

					<Button appearance="primary">Upload</Button>

				</Inline>

			</Stack>

		</Box>

	);

};



const cardStyles = xcss({

	borderRadius: '3px',

	boxShadow: 'elevation.shadow.overlay',

	width: '400px',

});
```

## Truncation

Truncation in product experiences should be avoided. However if truncation cannot be avoided, for example when displaying user-generated content, use the maxLines prop to indicate how text should be truncated. 

```jsx
import React from 'react';



import { Box, Stack, Text, xcss } from '@atlaskit/primitives';



export default () => {

	return (

		<Box xcss={boxStyles}>

			<Stack space="space.300">

				<Text maxLines={1}>

					This text truncates within one line and displays an ellipsis at the end of the content to

					indicate truncation has occurred.

				</Text>

				<Text maxLines={2}>

					This text truncates within two lines and displays an ellipsis at the end of the content to

					indicate truncation has occurred.

				</Text>

				<Text maxLines={3}>

					This text truncates within three lines and displays an ellipsis at the end of the content

					to indicate truncation has occurred.

				</Text>

			</Stack>

		</Box>

	);

};



const boxStyles = xcss({

	width: '220px',

});
```

## Customization

A restricted set of styles can be customized using the xcss prop. This is only available in the Compiled version of Text. 

```jsx
import React from 'react';



import { cssMap } from '@atlaskit/css';

import { Box, Inline, Stack, Text } from '@atlaskit/primitives/compiled';

import { token } from '@atlaskit/tokens';



const styles = cssMap({

	customStylesContainer: {

		width: '200px',

		borderWidth: token('border.width.indicator'),

		borderColor: token('color.border.accent.magenta'),

		borderStyle: 'solid',

	},

	customTextDecorationLine: { textDecorationLine: 'line-through' },

	customOverflowWrap: { overflowWrap: 'normal' },

});



export default () => {

	return (

		<Stack space="space.100">

			<Text xcss={styles.customTextDecorationLine}>Striked through text</Text>

			<Inline space="space.100">

				<Box xcss={styles.customStylesContainer}>

					<Text>

						Default overflow wrap with a really long word

						Vierhundertvierundvierzigtausendvierhundertvierundvierzig that can break to avoid

						overflowing its container.

					</Text>

				</Box>

				<Box xcss={styles.customStylesContainer}>

					<Text xcss={styles.customOverflowWrap}>

						Custom overflow wrap with a really long word

						Vierhundertvierundvierzigtausendvierhundertvierundvierzig that overflows its container.

					</Text>

				</Box>

			</Inline>

		</Stack>

	);

};
```

---

[View Original Documentation](https://atlassian.design/components/primitives/text/examples)
