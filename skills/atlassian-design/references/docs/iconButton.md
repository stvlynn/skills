# Icon button

An icon-only button lets people take a common and recognizable action where space is limited.

---

## Default

The default icon button, used for most cases. They aren't impactful enough to represent a primary action. 

```jsx
import React from 'react';



import { IconButton } from '@atlaskit/button/new';

import EditIcon from '@atlaskit/icon/glyph/edit';



const IconButtonDefaultExample = () => {

	return <IconButton icon={EditIcon} label="Edit" />;

};



export default IconButtonDefaultExample;
```

## Tooltips

Set isTooltipDisabled to false to enable the tooltip. The value of label will be used for the tooltip content. 

```jsx
import React from 'react';



import { IconButton } from '@atlaskit/button/new';

import AddIcon from '@atlaskit/icon/glyph/add';



const IconButtonPrimaryExample = () => {

	return <IconButton icon={AddIcon} label="Create page" isTooltipDisabled={false} />;

};



export default IconButtonPrimaryExample;
```

### Overriding tooltip props

Use the tooltip prop to override the default tooltip props. It accepts all tooptip props, excluding children. 

```jsx
import React from 'react';



import { IconButton, type IconButtonProps } from '@atlaskit/button/new';

import AddIcon from '@atlaskit/icon/glyph/add';



const tooltipOptions: IconButtonProps['tooltip'] = {

	position: 'right',

	hideTooltipOnClick: true,

};



const IconButtonPrimaryExample = () => {

	return (

		<IconButton

			icon={AddIcon}

			label="Create page"

			isTooltipDisabled={false}

			tooltip={tooltipOptions}

		/>

	);

};



export default IconButtonPrimaryExample;
```

## Appearance

### Primary

A primary button calls attention to the most important action on a page or in an area. Primary icon buttons aren't common because critical actions should typically use a button with a label for clarity. 

```jsx
import React from 'react';



import { IconButton } from '@atlaskit/button/new';

import AddIcon from '@atlaskit/icon/glyph/add';



const IconButtonPrimaryExample = () => {

	return <IconButton appearance="primary" icon={AddIcon} label="Create page" />;

};



export default IconButtonPrimaryExample;
```

### Subtle

Use a subtle icon button for secondary actions. 

```jsx
import React from 'react';



import { IconButton } from '@atlaskit/button/new';

import LinkIcon from '@atlaskit/icon/glyph/link';



const IconButtonSubtleExample = () => {

	return <IconButton appearance="subtle" icon={LinkIcon} label="Copy link" />;

};



export default IconButtonSubtleExample;
```

## Spacing

Icon button spacing depends on the surrounding UI. Default spacing is used for most use cases and compact for tables or smaller spaces. 

```jsx
import React from 'react';



import { IconButton } from '@atlaskit/button/new';

import MoreIcon from '@atlaskit/icon/glyph/more';

import { Inline } from '@atlaskit/primitives';



const IconButtonSpacingExample = () => {

	return (

		<Inline space="space.200">

			<IconButton icon={MoreIcon} appearance="primary" label="More actions" />

			<IconButton icon={MoreIcon} appearance="primary" spacing="compact" label="More actions" />

		</Inline>

	);

};



export default IconButtonSpacingExample;
```

## Shape

### Circle

Only use circle icon buttons in the top navigation or other areas that already have circular buttons. 

```jsx
import React from 'react';



import { IconButton } from '@atlaskit/button/new';

import ShowMoreHorizontalIcon from '@atlaskit/icon/glyph/more';



const IconButtonCircleExample = () => {

	return <IconButton shape="circle" icon={ShowMoreHorizontalIcon} label="More actions" />;

};



export default IconButtonCircleExample;
```

## Overriding icon props

Use the icon render prop to override the default icon props. 

```jsx
import React from 'react';



import { IconButton } from '@atlaskit/button/new';

import StarStarredIcon from '@atlaskit/icon/glyph/star-filled';

import { token } from '@atlaskit/tokens';



const IconButtonIconOverridesExample = () => {

	return (

		<IconButton

			icon={(iconProps) => (

				<StarStarredIcon

					{...iconProps}

					primaryColor={token('color.icon.accent.orange')}

				/>

			)}

			label="Add to favorites"

		/>

	);

};



export default IconButtonIconOverridesExample;
```

## States

### Disabled

Set isDisabled to disable an icon button that shouldn't be actionable. The icon button will appear faded and won't respond to user interaction. Avoid disabling buttons because this can cause accessibility problems, and never put a tooltip on a disabled button. 

```jsx
import React from 'react';



import { IconButton } from '@atlaskit/button/new';

import EditIcon from '@atlaskit/icon/glyph/edit';



const IconButtonDisabledExample = () => {

	return <IconButton isDisabled icon={EditIcon} label="Edit" />;

};



export default IconButtonDisabledExample;
```

### Selected

Set isSelected to indicate the button is selected. When a button is still loading and not actionable, a loading spinner can be displayed in place of the icon. This also disables the button and blocks user interaction. 

```jsx
import React from 'react';



import { IconButton } from '@atlaskit/button/new';

import ShowMoreHorizontalIcon from '@atlaskit/icon/glyph/more';



const IconButtonSelectedExample = () => {

	return <IconButton isSelected icon={ShowMoreHorizontalIcon} label="More actions" />;

};



export default IconButtonSelectedExample;
```

```jsx
import React, { useCallback, useState } from 'react';



import { IconButton } from '@atlaskit/button/new';

import EditIcon from '@atlaskit/icon/glyph/edit';

import { Inline, Stack } from '@atlaskit/primitives';

import Toggle from '@atlaskit/toggle';



const IconButtonLoadingExample = () => {

	const [isLoading, setIsLoading] = useState(true);



	const toggleLoading = useCallback((event: React.ChangeEvent<HTMLInputElement>) => {

		setIsLoading(event.currentTarget.checked);

	}, []);



	return (

		<Stack space="space.200" alignInline="start">

			<Inline alignBlock="center">

				<Toggle isChecked={isLoading} id="enable-loading" onChange={toggleLoading} />

				<label htmlFor="show-overlay">Enable loading state</label>

			</Inline>

			<IconButton isLoading={isLoading} icon={EditIcon} label="Edit" />

		</Stack>

	);

};



export default IconButtonLoadingExample;
```

---

[View Original Documentation](https://atlassian.design/components/button/icon-button/examples)
