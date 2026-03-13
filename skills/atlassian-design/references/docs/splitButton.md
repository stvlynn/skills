# Split button

A split button lets people perform an action or choose from a small group of similar actions.

---

## Default

The default form of a split button, used for most cases. For most split buttons the secondary action should be a dropdown menu. 

```jsx
import React from 'react';



import Button, { IconButton, SplitButton } from '@atlaskit/button/new';

import DropdownMenu, { DropdownItem, DropdownItemGroup } from '@atlaskit/dropdown-menu';

import ChevronDownIcon from '@atlaskit/icon/glyph/chevron-down';



const SplitButtonDefaultExample = () => {

	return (

		<SplitButton>

			<Button>Link issue</Button>

			<DropdownMenu<HTMLButtonElement>

				shouldRenderToParent

				trigger={({ triggerRef, ...triggerProps }) => (

					<IconButton

						ref={triggerRef}

						{...triggerProps}

						icon={ChevronDownIcon}

						label="More link issue options"

					/>

				)}

			>

				<DropdownItemGroup>

					<DropdownItem>Option one</DropdownItem>

					<DropdownItem>Option two</DropdownItem>

				</DropdownItemGroup>

			</DropdownMenu>

		</SplitButton>

	);

};



export default SplitButtonDefaultExample;
```

## Appearance

### Primary

Use a primary split button to call attention to highlight the strongest call to action on a page. Primary split buttons should only appear once per container (not including the application header or in a modal dialog). 

```jsx
import React from 'react';



import Button, { IconButton, SplitButton } from '@atlaskit/button/new';

import DropdownMenu, { DropdownItem, DropdownItemGroup } from '@atlaskit/dropdown-menu';

import ChevronDownIcon from '@atlaskit/icon/glyph/chevron-down';



const SplitButtonPrimaryExample = () => {

	return (

		<SplitButton appearance="primary">

			<Button>Update</Button>

			<DropdownMenu<HTMLButtonElement>

				shouldRenderToParent

				trigger={({ triggerRef, ...triggerProps }) => (

					<IconButton

						ref={triggerRef}

						{...triggerProps}

						icon={ChevronDownIcon}

						label="More update options"

					/>

				)}

			>

				<DropdownItemGroup>

					<DropdownItem>Option one</DropdownItem>

					<DropdownItem>Option two</DropdownItem>

				</DropdownItemGroup>

			</DropdownMenu>

		</SplitButton>

	);

};



export default SplitButtonPrimaryExample;
```

## Spacing

### Compact

```jsx
import React from 'react';



import Button, { IconButton, SplitButton } from '@atlaskit/button/new';

import DropdownMenu, { DropdownItem, DropdownItemGroup } from '@atlaskit/dropdown-menu';

import ChevronDownIcon from '@atlaskit/icon/glyph/chevron-down';



const SplitButtonPrimaryExample = () => {

	return (

		<SplitButton spacing="compact">

			<Button>Link issue</Button>

			<DropdownMenu<HTMLButtonElement>

				shouldRenderToParent

				trigger={({ triggerRef, ...triggerProps }) => (

					<IconButton

						ref={triggerRef}

						{...triggerProps}

						icon={ChevronDownIcon}

						label="More link issue options"

					/>

				)}

			>

				<DropdownItemGroup>

					<DropdownItem>Option one</DropdownItem>

					<DropdownItem>Option two</DropdownItem>

				</DropdownItemGroup>

			</DropdownMenu>

		</SplitButton>

	);

};



export default SplitButtonPrimaryExample;
```

---

[View Original Documentation](https://atlassian.design/components/button/split-button/examples)
