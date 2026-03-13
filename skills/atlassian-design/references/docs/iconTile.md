# Icon tile

An icon with background shape, color, and size options.

---

## Icon tile sizes and appearances

Icon tile places an icon on background tile of a specified size, shape and color. It allows icons to be prominently highlighted in a layout, such as next to a heading. 

### Shape

Icon Tile is available in two shapes: square and circle. 

```jsx
import React from 'react';



import { IconTile } from '@atlaskit/icon';

import AddIcon from '@atlaskit/icon/core/add';

import { Inline } from '@atlaskit/primitives';



const IconSizeExample = () => {

	return (

		<Inline space="space.200">

			<IconTile icon={AddIcon} label="" appearance="blue" shape="square" size="24" />

			<IconTile icon={AddIcon} label="" appearance="blue" shape="circle" size="24" />

		</Inline>

	);

};



export default IconSizeExample;
```

### Size

Unlike standard icons, icons inside Icon Tiles can scale up and down for use in different layouts. There are five options, representing the width and height in pixels: 16, 24, 32, 40 and 48. 

```jsx
import React from 'react';



import { IconTile } from '@atlaskit/icon';

import AddIcon from '@atlaskit/icon/core/add';

import { Inline } from '@atlaskit/primitives';



const sizes = ['16', '24', '32', '40', '48'] as const;



const IconSizeExample = () => {

	return (

		<Inline space="space.200" shouldWrap={true}>

			{sizes.map((size) => (

				<IconTile

					key={size}

					icon={AddIcon}

					label=""

					appearance="purple"

					size={size}

					shape="square"

				/>

			))}

		</Inline>

	);

};



export default IconSizeExample;
```

### Appearance

Appearance options for Icon Tile exist for each hue of available accent token, including bold variants that provide more contrast. 

```jsx
import React from 'react';



import { IconTile } from '@atlaskit/icon';

import AddIcon from '@atlaskit/icon/core/add';

import { Inline, Stack } from '@atlaskit/primitives';



const appearances = [

	'blue',

	'green',

	'lime',

	'magenta',

	'orange',

	'purple',

	'red',

	'teal',

	'yellow',

	'gray',

] as const;



const boldAppearances = [

	'blueBold',

	'greenBold',

	'limeBold',

	'magentaBold',

	'orangeBold',

	'purpleBold',

	'redBold',

	'tealBold',

	'yellowBold',

	'grayBold',

] as const;



const IconSizeExample = () => {

	return (

		<Stack space="space.100">

			{[appearances, boldAppearances].map((appearance) => (

				<Inline space="space.200" shouldWrap={true}>

					{appearance.map((appearance) => (

						<IconTile

							key={appearance}

							icon={AddIcon}

							label=""

							appearance={appearance}

							shape="square"

							size="24"

						/>

					))}

				</Inline>

			))}

		</Stack>

	);

};



export default IconSizeExample;
```

---

[View Original Documentation](https://atlassian.design/components/icon/icon-tile/examples)
