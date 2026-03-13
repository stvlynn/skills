# Dropdown menu

A dropdown menu displays a list of actions or options to a user.

---

## Appearance

### Default

Use default for the default dropdown menu appearance. The default menu will scroll after its height exceeds the pre-defined amount. 

```jsx
import React from 'react';



import DropdownMenu, { DropdownItem, DropdownItemGroup } from '@atlaskit/dropdown-menu';



const DropdownMenuDefaultExample = () => {

	return (

		<DropdownMenu trigger="Page actions" shouldRenderToParent>

			<DropdownItemGroup>

				<DropdownItem>Edit</DropdownItem>

				<DropdownItem>Share</DropdownItem>

				<DropdownItem>Move</DropdownItem>

				<DropdownItem>Clone</DropdownItem>

				<DropdownItem>Delete</DropdownItem>

				<DropdownItem>Report</DropdownItem>

			</DropdownItemGroup>

		</DropdownMenu>

	);

};



export default DropdownMenuDefaultExample;
```

### Density

Configure the density of the dropdown with the spacing prop. By default the spacing is cozy, but you can also apply compact depending on your use case. 

```jsx
/**

 * @jsxRuntime classic

 * @jsx jsx

 */



// eslint-disable-next-line @atlaskit/ui-styling-standard/use-compiled -- Ignored via go/DSP-18766

import { jsx } from '@emotion/react';



import DropdownMenu, {

	DropdownItem,

	DropdownItemCheckbox,

	DropdownItemGroup,

} from '@atlaskit/dropdown-menu';

import { Inline } from '@atlaskit/primitives';



export default () => (

	<Inline space="space.600">

		<DropdownMenu

			trigger="Compact density"

			testId="dropdown"

			spacing="compact"

			shouldRenderToParent

		>

			<DropdownItemGroup>

				<DropdownItem>Copy issue link</DropdownItem>

				<DropdownItem>Add flag</DropdownItem>

				<DropdownItem>Add label</DropdownItem>

				<DropdownItem>Add parent</DropdownItem>

				<DropdownItem>Print</DropdownItem>

			</DropdownItemGroup>

			<DropdownItemGroup hasSeparator>

				<DropdownItem>Remove from sprint</DropdownItem>

				<DropdownItem>Delete</DropdownItem>

			</DropdownItemGroup>

			<DropdownItemGroup hasSeparator>

				<DropdownItemCheckbox id="action">Action</DropdownItemCheckbox>

				<DropdownItemCheckbox id="filter">Filter</DropdownItemCheckbox>

			</DropdownItemGroup>

		</DropdownMenu>

		<DropdownMenu shouldRenderToParent trigger="Cozy density" testId="dropdown">

			<DropdownItemGroup>

				<DropdownItem>Copy issue link</DropdownItem>

				<DropdownItem>Add flag</DropdownItem>

				<DropdownItem>Add label</DropdownItem>

				<DropdownItem>Add parent</DropdownItem>

				<DropdownItem>Print</DropdownItem>

			</DropdownItemGroup>

			<DropdownItemGroup hasSeparator>

				<DropdownItem>Remove from sprint</DropdownItem>

				<DropdownItem>Delete</DropdownItem>

			</DropdownItemGroup>

			<DropdownItemGroup hasSeparator>

				<DropdownItemCheckbox id="action-2">Action</DropdownItemCheckbox>

				<DropdownItemCheckbox id="filter-2">Filter</DropdownItemCheckbox>

			</DropdownItemGroup>

		</DropdownMenu>

	</Inline>

);
```

### Tall

Use tall to control the height of the menu. The tall menu will not scroll until the height exceeds the height of the viewport. 

```jsx
import React from 'react';



import DropdownMenu, { DropdownItem, DropdownItemGroup } from '@atlaskit/dropdown-menu';



const DropdownMenuTallExample = () => {

	return (

		<DropdownMenu trigger="Page actions" appearance="tall" shouldRenderToParent>

			<DropdownItemGroup>

				<DropdownItem>One of many items</DropdownItem>

				<DropdownItem>One of many items</DropdownItem>

				<DropdownItem>One of many items</DropdownItem>

				<DropdownItem>One of many items</DropdownItem>

				<DropdownItem>One of many items</DropdownItem>

				<DropdownItem>One of many items</DropdownItem>

				<DropdownItem>One of many items</DropdownItem>

				<DropdownItem>One of many items</DropdownItem>

				<DropdownItem>One of many items</DropdownItem>

				<DropdownItem>One of many items</DropdownItem>

				<DropdownItem>One of many items</DropdownItem>

				<DropdownItem>One of many items</DropdownItem>

				<DropdownItem>One of many items</DropdownItem>

				<DropdownItem>One of many items</DropdownItem>

				<DropdownItem>One of many items</DropdownItem>

				<DropdownItem>One of many items</DropdownItem>

				<DropdownItem>One of many items</DropdownItem>

				<DropdownItem>One of many items</DropdownItem>

				<DropdownItem>One of many items</DropdownItem>

				<DropdownItem>One of many items</DropdownItem>

				<DropdownItem>One of many items</DropdownItem>

				<DropdownItem>One of many items</DropdownItem>

				<DropdownItem>One of many items</DropdownItem>

				<DropdownItem>One of many items</DropdownItem>

				<DropdownItem>One of many items</DropdownItem>

				<DropdownItem>One of many items</DropdownItem>

				<DropdownItem>One of many items</DropdownItem>

				<DropdownItem>One of many items</DropdownItem>

				<DropdownItem>One of many items</DropdownItem>

				<DropdownItem>One of many items</DropdownItem>

				<DropdownItem>One of many items</DropdownItem>

				<DropdownItem>One of many items</DropdownItem>

				<DropdownItem>One of many items</DropdownItem>

				<DropdownItem>One of many items</DropdownItem>

				<DropdownItem>One of many items</DropdownItem>

				<DropdownItem>One of many items</DropdownItem>

				<DropdownItem>One of many items</DropdownItem>

				<DropdownItem>One of many items</DropdownItem>

				<DropdownItem>One of many items</DropdownItem>

				<DropdownItem>One of many items</DropdownItem>

				<DropdownItem>One of many items</DropdownItem>

				<DropdownItem>One of many items</DropdownItem>

				<DropdownItem>One of many items</DropdownItem>

				<DropdownItem>One of many items</DropdownItem>

				<DropdownItem>One of many items</DropdownItem>

				<DropdownItem>One of many items</DropdownItem>

				<DropdownItem>One of many items</DropdownItem>

				<DropdownItem>One of many items</DropdownItem>

				<DropdownItem>One of many items</DropdownItem>

				<DropdownItem>One of many items</DropdownItem>

			</DropdownItemGroup>

		</DropdownMenu>

	);

};



export default DropdownMenuTallExample;
```

## Custom triggers

There are three recommended ways to customize a trigger. 

### Using trigger

Set trigger to a custom react component which accepts the provided props. Use the trigger prop and pass in an html element. Use the trigger prop and pass in a string. 

```jsx
import React from 'react';



import { IconButton } from '@atlaskit/button/new';

import DropdownMenu, { DropdownItem, DropdownItemGroup } from '@atlaskit/dropdown-menu';

import ShowMoreIcon from '@atlaskit/icon/glyph/more';



const DropdownMenuCustomTriggerButtonExample = () => {

	return (

		<DropdownMenu<HTMLButtonElement>

			trigger={({ triggerRef, ...props }) => (

				<IconButton {...props} icon={ShowMoreIcon} label="more" ref={triggerRef} />

			)}

			shouldRenderToParent

		>

			<DropdownItemGroup>

				<DropdownItem>Edit</DropdownItem>

				<DropdownItem>Share</DropdownItem>

				<DropdownItem>Move</DropdownItem>

				<DropdownItem>Clone</DropdownItem>

				<DropdownItem>Delete</DropdownItem>

				<DropdownItem>Report</DropdownItem>

			</DropdownItemGroup>

		</DropdownMenu>

	);

};



export default DropdownMenuCustomTriggerButtonExample;
```

```jsx
import React from 'react';



import DropdownMenu, { DropdownItem, DropdownItemGroup } from '@atlaskit/dropdown-menu';



const DropdownMenuCustomTriggerExample = () => {

	return (

		<DropdownMenu<HTMLButtonElement>

			trigger={({ triggerRef, isSelected, testId, ...providedProps }) => (

				<button type="button" {...providedProps} ref={triggerRef}>

					&lt;button/&gt; trigger{' '}

				</button>

			)}

			shouldRenderToParent

		>

			<DropdownItemGroup>

				<DropdownItem>Edit</DropdownItem>

				<DropdownItem>Share</DropdownItem>

				<DropdownItem>Move</DropdownItem>

				<DropdownItem>Clone</DropdownItem>

				<DropdownItem>Delete</DropdownItem>

				<DropdownItem>Report</DropdownItem>

			</DropdownItemGroup>

		</DropdownMenu>

	);

};



export default DropdownMenuCustomTriggerExample;
```

```jsx
import React from 'react';



import DropdownMenu, { DropdownItem, DropdownItemGroup } from '@atlaskit/dropdown-menu';



const DropdownMenuDefaultExample = () => {

	return (

		<DropdownMenu trigger="Page actions" shouldRenderToParent>

			<DropdownItemGroup>

				<DropdownItem>Edit</DropdownItem>

				<DropdownItem>Share</DropdownItem>

				<DropdownItem>Move</DropdownItem>

				<DropdownItem>Clone</DropdownItem>

				<DropdownItem>Delete</DropdownItem>

				<DropdownItem>Report</DropdownItem>

			</DropdownItemGroup>

		</DropdownMenu>

	);

};



export default DropdownMenuDefaultExample;
```

## Nested dropdown menu

You can nest dropdown menus inside other dropdown menus. However, be mindful that nested menus quickly become confusing, inaccessible, and difficult to navigate. We recommend limiting nesting to two layers only. 

```jsx
import React from 'react';



import DropdownMenu, { DropdownItem, DropdownItemGroup } from '@atlaskit/dropdown-menu';

import ChevronRightIcon from '@atlaskit/icon/glyph/chevron-right';

import { token } from '@atlaskit/tokens';



const NestedDropdown = () => {

	return (

		<DropdownMenu

			placement="right-start"

			shouldRenderToParent

			trigger={({ triggerRef, ...triggerProps }) => (

				<DropdownItem

					{...triggerProps}

					ref={triggerRef}

					elemAfter={

						<ChevronRightIcon

							primaryColor={token('color.icon.subtle')}

							label=""

						/>

					}

				>

					<span>Nested Menu</span>

				</DropdownItem>

			)}

		>

			<DropdownItemGroup>

				<NestedDropdown />

				<DropdownItem>One of many items</DropdownItem>

				<DropdownItem>One of many items</DropdownItem>

			</DropdownItemGroup>

		</DropdownMenu>

	);

};

const NestedDropdownMenuExample = () => {

	return (

		<DropdownMenu trigger="Nested" shouldRenderToParent>

			<DropdownItemGroup>

				<NestedDropdown />

				<DropdownItem>One of many items</DropdownItem>

				<DropdownItem>One of many items</DropdownItem>

			</DropdownItemGroup>

		</DropdownMenu>

	);

};



export default NestedDropdownMenuExample;
```

## States

If isLoading is true, a spinner is rendered instead of the dropdown items. 

```jsx
import React from 'react';



import DropdownMenu, { DropdownItem, DropdownItemGroup } from '@atlaskit/dropdown-menu';



const DropdownMenuLoadingExample = () => {

	return (

		<DropdownMenu isLoading trigger="Page actions" shouldRenderToParent>

			<DropdownItemGroup>

				<DropdownItem>Loaded action</DropdownItem>

			</DropdownItemGroup>

		</DropdownMenu>

	);

};



export default DropdownMenuLoadingExample;
```

### Open

Use isOpen to control the open state of the dropdown menu. 

```jsx
import React, { useState } from 'react';



import DropdownMenu, { DropdownItemRadio, DropdownItemRadioGroup } from '@atlaskit/dropdown-menu';

import { type OnOpenChangeArgs } from '@atlaskit/dropdown-menu/types';



const DropdownOpenExample = () => {

	const [isOpen, setIsOpen] = useState(false);



	return (

		<DropdownMenu

			isOpen={isOpen}

			onOpenChange={(attrs: OnOpenChangeArgs) => {

				setIsOpen(attrs.isOpen);

			}}

			trigger="Page actions"

			shouldRenderToParent

		>

			<DropdownItemRadioGroup id="actions">

				<DropdownItemRadio id="edit">Edit</DropdownItemRadio>

				<DropdownItemRadio id="move">Move</DropdownItemRadio>

			</DropdownItemRadioGroup>

		</DropdownMenu>

	);

};



export default DropdownOpenExample;
```

## Positioning

### Default placement

By default, the dropdown menu will be placed next to your trigger. 

```jsx
import React from 'react';



import DropdownMenu, { DropdownItem, DropdownItemGroup } from '@atlaskit/dropdown-menu';



const DropdownMenuPositionDefaultExample = () => {

	return (

		<DropdownMenu trigger="Page actions" shouldRenderToParent>

			<DropdownItemGroup>

				<DropdownItem>Edit</DropdownItem>

				<DropdownItem>Move</DropdownItem>

				<DropdownItem>Clone</DropdownItem>

			</DropdownItemGroup>

		</DropdownMenu>

	);

};



export default DropdownMenuPositionDefaultExample;
```

### Placement

Use placement to set the menu placement to the bottom end, for example. 

```jsx
import React from 'react';



import DropdownMenu, { DropdownItem, DropdownItemGroup } from '@atlaskit/dropdown-menu';



const DropdownMenuPositionExample = () => {

	return (

		<DropdownMenu trigger="Page actions" placement="bottom-end" shouldRenderToParent>

			<DropdownItemGroup>

				<DropdownItem>Edit</DropdownItem>

				<DropdownItem>Move</DropdownItem>

				<DropdownItem>Clone</DropdownItem>

			</DropdownItemGroup>

		</DropdownMenu>

	);

};



export default DropdownMenuPositionExample;
```

### Should flip

If it doesn't fit in the viewport, use shouldFlip to place to the dropdown menu on the opposite side of its trigger. 

```jsx
import React from 'react';



import DropdownMenu, { DropdownItem, DropdownItemGroup } from '@atlaskit/dropdown-menu';



const DropdownMenuShouldFlipExample = () => {

	return (

		<DropdownMenu trigger="Page actions" shouldFlip shouldRenderToParent>

			<DropdownItemGroup>

				<DropdownItem>Edit</DropdownItem>

				<DropdownItem>Move</DropdownItem>

				<DropdownItem>Clone</DropdownItem>

			</DropdownItemGroup>

		</DropdownMenu>

	);

};



export default DropdownMenuShouldFlipExample;
```

### Z-index

Use zIndex to resolve clashes with other layered components with competing z-index values, such as popup. 

```jsx
import React, { useState } from 'react';



import { IconButton } from '@atlaskit/button/new';

import DropdownMenu, { DropdownItem, DropdownItemGroup } from '@atlaskit/dropdown-menu';

import CommentAddIcon from '@atlaskit/icon/glyph/media-services/add-comment';

import Popup from '@atlaskit/popup';

import { Box, xcss } from '@atlaskit/primitives';



const containerStyles = xcss({

	width: 'size.300',

	height: 'size.300',

});



const DropdownMenuZIndex = () => {

	const [isOpen, setIsOpen] = useState(false);



	return (

		<Popup

			shouldRenderToParent

			isOpen={isOpen}

			onClose={() => setIsOpen(false)}

			placement="bottom-start"

			zIndex={600}

			content={() => (

				<Box padding="space.100" xcss={containerStyles}>

					<DropdownMenu trigger="Page actions" zIndex={610} testId="dropdown" shouldRenderToParent>

						<DropdownItemGroup>

							<DropdownItem>Move</DropdownItem>

							<DropdownItem>Clone</DropdownItem>

							<DropdownItem>Delete</DropdownItem>

						</DropdownItemGroup>

					</DropdownMenu>

				</Box>

			)}

			trigger={(triggerProps) => (

				<IconButton

					{...triggerProps}

					isSelected={isOpen}

					onClick={() => setIsOpen(!isOpen)}

					value="Add"

					icon={CommentAddIcon}

					label="Add"

					testId="popup--trigger"

				/>

			)}

		/>

	);

};



export default DropdownMenuZIndex;
```

## Content without portal

By default, the dropdown menu content is rendered inside React.Portal. Use shouldRenderToParent prop to render the content directly after the trigger element. 

```jsx
import React from 'react';



import DropdownMenu, { DropdownItem, DropdownItemGroup } from '@atlaskit/dropdown-menu';



const DropdownMenuWithoutPortalExample = () => {

	return (

		<DropdownMenu trigger="Page actions" shouldRenderToParent>

			<DropdownItemGroup>

				<DropdownItem>Edit</DropdownItem>

				<DropdownItem>Share</DropdownItem>

				<DropdownItem>Move</DropdownItem>

				<DropdownItem>Clone</DropdownItem>

				<DropdownItem>Delete</DropdownItem>

				<DropdownItem>Report</DropdownItem>

			</DropdownItemGroup>

		</DropdownMenu>

	);

};



export default DropdownMenuWithoutPortalExample;
```

## Full width dropdown menu

Use shouldFitContainer to fit the dropdown menu width to its parent's width. When set to true, the trigger and dropdown menu elements will be wrapped in a div with position: relative. The dropdown menu will be rendered as a sibling to the trigger element, and will be full width. 

```jsx
import React from 'react';



import Button from '@atlaskit/button/new';

import DropdownMenu, { DropdownItem, DropdownItemGroup } from '@atlaskit/dropdown-menu';



const DropdownMenuFullWidth = () => {

	return (

		<DropdownMenu<HTMLButtonElement>

			shouldFitContainer

			shouldRenderToParent

			trigger={({ triggerRef, ...triggerProps }) => (

				<Button ref={triggerRef} {...triggerProps} shouldFitContainer>

					Page actions

				</Button>

			)}

		>

			<DropdownItemGroup>

				<DropdownItem>Edit</DropdownItem>

				<DropdownItem>Share</DropdownItem>

				<DropdownItem>Move</DropdownItem>

				<DropdownItem>Clone</DropdownItem>

				<DropdownItem>Delete</DropdownItem>

				<DropdownItem>Report</DropdownItem>

			</DropdownItemGroup>

		</DropdownMenu>

	);

};



export default DropdownMenuFullWidth;
```

## Accessible labels

Sometimes multiple instances of a dropdown menu with the same visible label are required. In order to provide more context to assistive technologies, you can specify a unique aria-label for each unique menu. When providing the aria-label along with a visible label, make sure that the first few words of the aria-label match the visible label. This is to support Voice Input users that use the visible label to interact with controls. 

```jsx
import React from 'react';



import DropdownMenu, { DropdownItem, DropdownItemGroup } from '@atlaskit/dropdown-menu';



const DropdownMenuLabelExample = () => {

	return (

		<DropdownMenu trigger="More" label="More actions" shouldRenderToParent>

			<DropdownItemGroup>

				<DropdownItem>Edit</DropdownItem>

				<DropdownItem>Share</DropdownItem>

				<DropdownItem>Move</DropdownItem>

				<DropdownItem>Clone</DropdownItem>

				<DropdownItem>Delete</DropdownItem>

				<DropdownItem>Report</DropdownItem>

			</DropdownItemGroup>

		</DropdownMenu>

	);

};



export default DropdownMenuLabelExample;
```

---

[View Original Documentation](https://atlassian.design/components/dropdown-menu/examples)
