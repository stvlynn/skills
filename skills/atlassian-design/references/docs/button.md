# Button

A button triggers an event or action. They let users know what will happen next.

---

## Default

Use default buttons for most actions that aren't the main call to action for a page or area. Default buttons are less prominent than primary buttons. 

```jsx
import React from 'react';



import Button from '@atlaskit/button/new';



const ButtonDefaultExample = () => {

	return <Button>Default button</Button>;

};



export default ButtonDefaultExample;
```

## Appearance

### Primary

Use a primary button to call attention to a form submission or to highlight the most important call to action on a page. Primary buttons should only appear once per area, but not every screen needs a primary button. The placement of the primary button typically matches the alignment of the button(s) in the layout. Review usage details for alignment examples. 

```jsx
import React from 'react';



import Button from '@atlaskit/button/new';



const ButtonPrimaryExample = () => {

	return <Button appearance="primary">Primary button</Button>;

};



export default ButtonPrimaryExample;
```

### Subtle

Use a subtle button with a primary button for secondary actions. Subtle buttons are best used in spaces where it's already clear items can be interacted with, like toolbars or groups of buttons next to each other. Avoid using them in other situations, as they aren't as obviously clickable as other button styles. 

```jsx
import React from 'react';



import Button from '@atlaskit/button/new';



const ButtonSubtleExample = () => {

	return <Button appearance="subtle">Subtle button</Button>;

};



export default ButtonSubtleExample;
```

### Warning

Warning buttons confirm actions that may cause a significant change or a loss of data. Warnings alert people of a problem that might happen if they proceed. These appearances are often used in confirmation modals. 

```jsx
import React from 'react';



import Button from '@atlaskit/button/new';



const ButtonWarningExample = () => {

	return <Button appearance="warning">Warning button</Button>;

};



export default ButtonWarningExample;
```

### Danger

A danger button appears as a final confirmation for a destructive and irreversible action, such as deleting. 

```jsx
import React from 'react';



import Button from '@atlaskit/button/new';



const ButtonDangerExample = () => {

	return <Button appearance="danger">Danger button</Button>;

};



export default ButtonDangerExample;
```

### Discovery

A discovery button can be used as the call to action for new experiences. 

```jsx
import React from 'react';



import Button from '@atlaskit/button/new';



const ButtonDiscoveryExample = () => {

	return <Button appearance="discovery">Discovery button</Button>;

};



export default ButtonDiscoveryExample;
```

## States

### Disabled

Set isDisabled to disable a button that shouldn't be actionable. The button will appear faded and won't respond to user interaction. Disabled buttons can cause accessibility issues (disabled elements are not in the tab order) so wherever possible, avoid using isDisabled. Instead, use validation or other techniques to show users how to proceed. 

```jsx
import React from 'react';



import Button from '@atlaskit/button/new';



const ButtonDisabledExample = () => {

	return (

		<Button appearance="primary" isDisabled>

			Disabled button

		</Button>

	);

};



export default ButtonDisabledExample;
```

### Selected

Set isSelected to indicate the button is selected. When a button is still loading and not actionable, a loading spinner can be displayed in place of the button label. This also disables the button and blocks user interaction. 

```jsx
import React from 'react';



import Button from '@atlaskit/button/new';



const ButtonSelectedExample = () => {

	return <Button isSelected>Selected button</Button>;

};



export default ButtonSelectedExample;
```

```jsx
import React, { useCallback, useState } from 'react';



import Button from '@atlaskit/button/new';

import { Inline, Stack } from '@atlaskit/primitives';

import Toggle from '@atlaskit/toggle';



const ButtonLoadingExample = () => {

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

			<Button isLoading={isLoading}>Button</Button>

		</Stack>

	);

};



export default ButtonLoadingExample;
```

## Spacing

Button spacing depends on the surrounding UI. Default spacing is used for most use cases, compact for tables. 

```jsx
import React from 'react';



import { ButtonGroup } from '@atlaskit/button';

import Button from '@atlaskit/button/new';



const ButtonSpacingExample = () => {

	return (

		<ButtonGroup>

			<Button appearance="primary">Default</Button>

			<Button appearance="primary" spacing="compact">

				Compact

			</Button>

		</ButtonGroup>

	);

};



export default ButtonSpacingExample;
```

## Full width

Buttons can expand to full width to fill the parent container. This is sometimes done in login forms. Follow the alignment guidance for more options. 

```jsx
import React from 'react';



import Button from '@atlaskit/button/new';



const ButtonFullWidthExample = () => {

	return (

		<Button shouldFitContainer appearance="primary">

			Full width button

		</Button>

	);

};



export default ButtonFullWidthExample;
```

## Button with icon

Buttons may include an icon before or after the text label. For an icon-only button, see icon button. 

### Icon before

Display an icon before the text. 

```jsx
import React from 'react';



import Button from '@atlaskit/button/new';

import StarStarredIcon from '@atlaskit/icon/glyph/star-filled';



const ButtonIconBeforeExample = () => {

	return (

		<Button iconBefore={StarStarredIcon} appearance="primary">

			Icon before

		</Button>

	);

};



export default ButtonIconBeforeExample;
```

### Icon after

Display an icon after the text. 

```jsx
import React from 'react';



import Button from '@atlaskit/button/new';

import StarStarredIcon from '@atlaskit/icon/glyph/star-filled';



const ButtonIconAfterExample = () => {

	return (

		<Button iconAfter={StarStarredIcon} appearance="primary">

			Icon after

		</Button>

	);

};



export default ButtonIconAfterExample;
```

### Overriding icon props

Use the iconBefore or iconAfter render prop to override the default icon props. 

```jsx
import React from 'react';



import Button from '@atlaskit/button/new';

import WarningIcon from '@atlaskit/icon/glyph/warning';

import { token } from '@atlaskit/tokens';



const ButtonIconOverrideExample = () => {

	return (

		<Button

			iconBefore={(iconProps) => (

				<WarningIcon

					{...iconProps}

					size="small"

					primaryColor={token('color.icon.warning')}

					secondaryColor={token('color.icon.inverse')}

				/>

			)}

			appearance="warning"

		>

			Icon with overrides

		</Button>

	);

};



export default ButtonIconOverrideExample;
```

## Truncation

Avoid truncation whenever possible. Make sure there's always a way to access the full content for all users. Text will truncate when buttons are in a narrow container to prevent wrapping onto a new line and breaking layouts. An ellipsis will be added to the end to indicate that the text has been truncated. The truncation is implemented with styles, so screen readers will still read the full text. For more information see truncation. 

```jsx
import React from 'react';



import Button from '@atlaskit/button/new';

import { Box, xcss } from '@atlaskit/primitives';



const containerStyles = xcss({

	maxWidth: 'size.1000',

});



const ButtonTruncationExample = () => {

	return (

		<Box xcss={containerStyles}>

			<Button>This text is truncated to fit within the container</Button>

		</Box>

	);

};



export default ButtonTruncationExample;
```

## Custom buttons

## Coming soon

The legacy CustomThemeButton will soon be deprecated. We're working on a replacement for this with safe style overrides using XCSS. 

---

[View Original Documentation](https://atlassian.design/components/button/examples)
