# Icon (legacy)

An icon is a visual representation of a command, device, directory, or common action.

---

## New icons are available for Atlassian's visual refresh

Legacy icons will be deprecated after the new icons are fully released in products. 

## Default

By default, icons are displayed in the medium size. 

```jsx
import React from 'react';



import LikeIcon from '@atlaskit/icon/glyph/like';

import { Box } from '@atlaskit/primitives';



const IconDefaultExample = () => {

	return (

		<Box>

			<LikeIcon label="" />

		</Box>

	);

};



export default IconDefaultExample;
```

## Migration

Atlassian products can feature flag between the old and new icon components via the migration entrypoint for the new icons, or manually via the LEGACY_fallbackIcon prop. To learn more about feature flagging and LEGACY_ prefixed props, see the icon migration guide. 

```jsx
import React from 'react';



import LikeIconMigration from '@atlaskit/icon/core/migration/thumbs-up--like';

import LikeIcon from '@atlaskit/icon/core/thumbs-up';

import LegacyLikeIcon from '@atlaskit/icon/glyph/like';

import { Box, Inline, Stack, Text, xcss } from '@atlaskit/primitives';



const TextBoxStyles = xcss({ width: '150px' });



const IconDefaultExample = () => {

	return (

		<Stack space="space.100">

			<Inline space="space.100">

				<Box xcss={TextBoxStyles}>

					<Text weight="bold">Legacy icon</Text>

				</Box>

				<LegacyLikeIcon label="" />

			</Inline>

			<Inline space="space.100">

				<Box xcss={TextBoxStyles}>

					<Text weight="bold">Feature flagged</Text>

				</Box>

				<LikeIconMigration LEGACY_size="medium" spacing="spacious" label="" />

				<LikeIcon

					LEGACY_fallbackIcon={LegacyLikeIcon}

					LEGACY_size="medium"

					spacing="spacious"

					label=""

				/>

			</Inline>

			<Inline space="space.100">

				<Box xcss={TextBoxStyles}>

					<Text weight="bold">New icon</Text>

				</Box>

				<LikeIcon spacing="spacious" label="" />

			</Inline>

		</Stack>

	);

};



export default IconDefaultExample;
```

## Sizing

### Small

The small icon size (16px) is used when space is at a premium, such as search results or inline content. 

```jsx
import React from 'react';



import LikeIcon from '@atlaskit/icon/glyph/like';

import { Box } from '@atlaskit/primitives';



const IconSmallExample = () => {

	return (

		<Box>

			<LikeIcon size="small" label="" />

		</Box>

	);

};



export default IconSmallExample;
```

### Medium

The medium icon size (24px) is used in common interfaces. 

```jsx
import React from 'react';



import LikeIcon from '@atlaskit/icon/glyph/like';

import { Box } from '@atlaskit/primitives';



const IconMediumExample = () => {

	return (

		<Box>

			<LikeIcon size="medium" label="" />

		</Box>

	);

};



export default IconMediumExample;
```

### Large

The large icon size (32px) is used in common interfaces. 

```jsx
import React from 'react';



import LikeIcon from '@atlaskit/icon/glyph/like';

import { Box } from '@atlaskit/primitives';



const IconLargeExample = () => {

	return (

		<Box>

			<LikeIcon size="large" label="" />

		</Box>

	);

};



export default IconLargeExample;
```

## Color

### Primary color

This refers to the main color of the icon. The icon’s primary color inherits the current font color by default. 

```jsx
/**

 * @jsxRuntime classic

 * @jsx jsx

 */

// eslint-disable-next-line @atlaskit/ui-styling-standard/use-compiled -- Ignored via go/DSP-18766

import { css, jsx } from '@compiled/react';



import LikeIcon from '@atlaskit/icon/glyph/like';

import WarningIcon from '@atlaskit/icon/glyph/warning';

import { token } from '@atlaskit/tokens';



const stylesStyles = css({

	color: token('color.icon.warning'),

});



const IconPrimaryColorExample = () => {

	return (

		<div css={stylesStyles}>

			{/* primaryColor is explicitly set */}

			<LikeIcon primaryColor={token('color.icon.brand')} label="" />

			{/* inherited from the color prop of the parent element */}

			<WarningIcon label="" />

		</div>

	);

};



export default IconPrimaryColorExample;
```

---

[View Original Documentation](https://atlassian.design/components/icon/icon-legacy/examples)
