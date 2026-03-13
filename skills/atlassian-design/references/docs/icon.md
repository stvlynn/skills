# Icon

An icon is a symbol representing a command, device, directory, or common action.

---

## Default (16px)

Icons default to a medium size of 16px. 

```jsx
import React from 'react';



import AttachmentIcon from '@atlaskit/icon/core/attachment';

import ImageIcon from '@atlaskit/icon/core/image';

import OfficeBuildingIcon from '@atlaskit/icon/core/office-building';

import StopwatchIcon from '@atlaskit/icon/core/stopwatch';

import { Inline } from '@atlaskit/primitives';



const IconDefaultNewExample = () => {

	return (

		<Inline space="space.100">

			<ImageIcon label="" />

			<AttachmentIcon label="" />

			<OfficeBuildingIcon label="" />

			<StopwatchIcon label="" />

		</Inline>

	);

};



export default IconDefaultNewExample;
```

## Small (12px)

## New

Small icons are 12px, for use next to small size text, such as in bylines, and inside small components such as lozenges. 

```jsx
import React from 'react';



import ArrowRightIcon from '@atlaskit/icon/core/arrow-right';

import ChevronIcon from '@atlaskit/icon/core/chevron-down';

import DragHandleVerticalIcon from '@atlaskit/icon/core/drag-handle-vertical';

import ErrorIcon from '@atlaskit/icon/core/error';

import { Inline } from '@atlaskit/primitives';



const IconSmallNewExample = () => {

	return (

		<Inline space="space.100">

			<ChevronIcon label="" size="small" />

			<ArrowRightIcon label="" size="small" />

			<ErrorIcon label="" size="small" />

			<DragHandleVerticalIcon label="" size="small" />

		</Inline>

	);

};



export default IconSmallNewExample;
```

## Utility (12px)

## Soon to be deprecated

Utility icons are 12px for special cases and component parts that require a smaller size. Some glyphs aren't legible at this size, so only certain icons are offered at 12px. 

```jsx
import React from 'react';



import ArrowRightIcon from '@atlaskit/icon/utility/arrow-right';

import ChevronIcon from '@atlaskit/icon/utility/chevron-down';

import DragHandleVerticalIcon from '@atlaskit/icon/utility/drag-handle-vertical';

import ErrorIcon from '@atlaskit/icon/utility/error';

import { Inline } from '@atlaskit/primitives';



const IconUtilityExample = () => {

	return (

		<Inline space="space.100">

			<ChevronIcon label="" />

			<ArrowRightIcon label="" />

			<ErrorIcon label="" />

			<DragHandleVerticalIcon label="" />

		</Inline>

	);

};



export default IconUtilityExample;
```

## Label

If an icon doesn’t have an existing text label or accessible text, provide a clear label with the label prop. If an icon is associated with a button or element that also has a text label, you don’t need to provide alternative text for the icon, because the label clarifies the meaning of the icon. You can do this by setting the label prop to an empty string (""). 

```jsx
import React from 'react';



import Button, { IconButton } from '@atlaskit/button/new';

import Heading from '@atlaskit/heading';

import AddIcon from '@atlaskit/icon/core/add';

import EditIcon from '@atlaskit/icon/core/edit';

import EpicIcon from '@atlaskit/icon/core/epic';

import FiltersIcon from '@atlaskit/icon/core/filter';

import MergeSuccessIcon from '@atlaskit/icon/core/merge-success';

import WarningIcon from '@atlaskit/icon/core/warning';

import { Inline, Stack, Text } from '@atlaskit/primitives';

import { token } from '@atlaskit/tokens';



const IconLabelExample = () => {

	return (

		<Inline space="space.1000">

			<Stack space="space.200" alignBlock="center">

				<Heading size="small">Icons with labels:</Heading>

				<Inline space="space.100" alignBlock="center">

					<EpicIcon color={token('color.icon.accent.purple')} label="Issue type: Epic" />

					<Text weight="bold">Beta release</Text>

				</Inline>

				<Inline space="space.100" alignBlock="center">

					<WarningIcon color={token('color.icon.warning')} label="warning" />

					<Text weight="bold" color="color.text.warning">

						Saving was interrupted

					</Text>

				</Inline>

				<IconButton label="Add" icon={AddIcon} />

			</Stack>

			<Stack space="space.200" alignBlock="center">

				<Heading size="small">Icons without labels:</Heading>

				<Inline space="space.100" alignBlock="center">

					<EditIcon color={token('color.text')} label="" />

					<Text color="color.text">Last edited: yesterday</Text>

				</Inline>

				<Inline space="space.100" alignBlock="center">

					<MergeSuccessIcon color={token('color.text.success')} label="" />

					<Text color="color.text.success">Merged</Text>

				</Inline>

				<Button iconBefore={FiltersIcon}>Filters</Button>

			</Stack>

		</Inline>

	);

};



export default IconLabelExample;
```

## Color

Icons can use color tokens for icons, text, links, or the current text color. 

```jsx
import React from 'react';



import ErrorIcon from '@atlaskit/icon/core/error';

import LinkIcon from '@atlaskit/icon/core/link';

import SettingsIcon from '@atlaskit/icon/core/settings';

import WhiteboardIcon from '@atlaskit/icon/core/whiteboard';

import { ButtonItem } from '@atlaskit/menu';

import { Box, Inline, Stack } from '@atlaskit/primitives';

import { token } from '@atlaskit/tokens';



const IconColorExample = () => {

	const [isMenuSelected, setIsMenuSelected] = React.useState(true);

	return (

		<Stack space="space.200" alignBlock="center">

			<Inline space="space.100">

				<WhiteboardIcon color={token('color.icon.accent.teal')} label="" />

				<ErrorIcon color={token('color.icon.danger')} label="" />

				<LinkIcon color={token('color.link')} label="" />

			</Inline>

			<Box testId="button-items">

				<ButtonItem

					isSelected={isMenuSelected}

					iconBefore={<SettingsIcon spacing="spacious" label="" />}

					onClick={() => setIsMenuSelected(!isMenuSelected)}

				>

					Settings

				</ButtonItem>

			</Box>

		</Stack>

	);

};



export default IconColorExample;
```

## Spacing props

Icons support a spacing prop to add padding around the icon. spacious spacing sets the bounding box to 24px. Both small and utility icons support an additional option, compact, that sets the bounding box to 16px. 

```jsx
import React from 'react';



import Heading from '@atlaskit/heading';

import AddIcon from '@atlaskit/icon/core/add';

import ChevronIcon from '@atlaskit/icon/core/chevron-down';

import ChevronIconUtility from '@atlaskit/icon/utility/chevron-down';

import Lozenge from '@atlaskit/lozenge';

import { Box, Inline, Stack, xcss } from '@atlaskit/primitives';



const IconSpacingExample = () => {

	return (

		<Stack space="space.100">

			<Heading size="small">Core icons (medium):</Heading>

			<Inline space="space.100">

				<IconContainer>

					<AddIcon label="" />

				</IconContainer>

				<IconContainer>

					<AddIcon label="" spacing="spacious" />

				</IconContainer>

			</Inline>

			<Heading size="small">Core icons (small):</Heading>

			<Inline space="space.100">

				<IconContainer>

					<ChevronIcon label="" size="small" />

				</IconContainer>

				<IconContainer>

					<ChevronIcon label="" size="small" spacing="compact" />

				</IconContainer>

				<IconContainer>

					<ChevronIcon label="" size="small" spacing="spacious" />

				</IconContainer>

			</Inline>

			<Heading size="small">

				Utility icons:{' '}

				<Lozenge appearance="moved" isBold>

					Soon to be deprecated

				</Lozenge>

			</Heading>

			<Inline space="space.100">

				<IconContainer>

					<ChevronIconUtility label="" />

				</IconContainer>

				<IconContainer>

					<ChevronIconUtility label="" spacing="compact" />

				</IconContainer>

				<IconContainer>

					<ChevronIconUtility label="" spacing="spacious" />

				</IconContainer>

			</Inline>

		</Stack>

	);

};



const iconContainerStyles = xcss({

	border: '1px dashed',

	borderRadius: 'border.radius.100',

	lineHeight: '0',

	borderColor: 'color.border.accent.magenta',

});

const IconContainer = ({ children }: { children: React.ReactChild }) => (

	// renders children with a surrounding box to show the icon size

	<Box xcss={iconContainerStyles}>{children}</Box>

);



export default IconSpacingExample;
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

---

[View Original Documentation](https://atlassian.design/components/icon/examples)
