# Popup select

Popup select lets people filter through a list of options.

---

## Default

Use popup select to let people filter through a list of actions where limited space is a concern for the trigger. 

```jsx
import React from 'react';



import Button from '@atlaskit/button/new';

import ChevronDownIcon from '@atlaskit/icon/glyph/chevron-down';

import { PopupSelect } from '@atlaskit/select';



const options = [

	{ label: 'accessibility', value: 'accessibility' },

	{ label: 'analytics', value: 'analytics' },

	{ label: 'ktlo', value: 'ktlo' },

	{ label: 'testing', value: 'testing' },

	{ label: 'regression', value: 'regression' },

	{ label: 'layering', value: 'layering' },

	{ label: 'innovation', value: 'innovation' },

	{ label: 'new-feature', value: 'new' },

	{ label: 'existing', value: 'existing' },

	{ label: 'wont-do', value: 'wont-do' },

];



const PopupSelectExample = () => {

	return (

		<PopupSelect

			placeholder="Search labels..."

			options={options}

			target={({ isOpen, ...triggerProps }) => (

				<Button {...triggerProps} iconAfter={ChevronDownIcon}>

					Label

				</Button>

			)}

		/>

	);

};



export default PopupSelectExample;
```

## Hidden search input

Use the searchThreshold prop to hide the search input. 

```jsx
import React from 'react';



import Button from '@atlaskit/button/new';

import ChevronDownIcon from '@atlaskit/icon/glyph/chevron-down';

import { PopupSelect } from '@atlaskit/select';



const options = [

	{ label: 'Blocked', value: 'blocked' },

	{ label: 'Gathering interest', value: 'gathering' },

	{ label: 'To do', value: 'todo' },

	{ label: 'Ready for sprint', value: 'ready' },

	{ label: 'In progress', value: 'progress' },

	{ label: 'Cancelled', value: 'cancelled' },

];



const PopupSelectExample = () => {

	return (

		<PopupSelect

			searchThreshold={10}

			value={options[2]}

			options={options}

			target={({ isOpen, ...triggerProps }) => (

				<Button {...triggerProps} iconAfter={ChevronDownIcon}>

					To do

				</Button>

			)}

		/>

	);

};



export default PopupSelectExample;
```

## Checkbox options

Enable checkbox options and multi select using the checkbox option component and isMulti prop. 

```jsx
import React from 'react';



import Button from '@atlaskit/button/new';

import ChevronDownIcon from '@atlaskit/icon/glyph/chevron-down';

import { CheckboxOption, PopupSelect } from '@atlaskit/select';

const options = [

	{

		label: 'Standard issue types',

		options: [

			{ label: 'Epic', value: 'epic' },

			{ label: 'Initiative', value: 'initiative' },

			{ label: 'Task', value: 'task' },

		],

	},

	{

		label: 'Sub-task issue types',

		options: [

			{ label: 'Feature', value: 'feature' },

			{ label: 'Bug', value: 'bug' },

		],

	},

];



const PopupSelectExample = () => {

	return (

		<PopupSelect

			components={{ Option: CheckboxOption }}

			options={options}

			closeMenuOnSelect={false}

			hideSelectedOptions={false}

			isMulti

			label="Filter issue types"

			placeholder="Filter issue types..."

			target={({ isOpen, ...triggerProps }) => (

				<Button {...triggerProps} isSelected={isOpen} iconAfter={ChevronDownIcon}>

					Type

				</Button>

			)}

		/>

	);

};



export default PopupSelectExample;
```

## Placement

Use placement to position the popup relative to the trigger. 

```jsx
import React from 'react';



import Button from '@atlaskit/button/new';

import ChevronDownIcon from '@atlaskit/icon/glyph/chevron-down';

import { PopupSelect } from '@atlaskit/select';



const options = [

	{

		label: 'States',

		options: [

			{ label: 'Adelaide', value: 'adelaide' },

			{ label: 'Brisbane', value: 'brisbane' },

			{ label: 'Melbourne', value: 'melbourne' },

			{ label: 'Perth', value: 'perth' },

			{ label: 'Sydney', value: 'sydney' },

			{ label: 'Hobart', value: 'hobart' },

		],

	},

	{

		label: 'Territories',

		options: [

			{ label: 'Canberra', value: 'canberra' },

			{ label: 'Darwin', value: 'darwin' },

		],

	},

];



const PopupSelectExample = () => {

	return (

		<PopupSelect

			searchThreshold={10}

			placeholder="Choose a city"

			options={options}

			popperProps={{ placement: 'right-start' }}

			target={({ isOpen, ...triggerProps }) => (

				<Button {...triggerProps} isSelected={isOpen} iconAfter={ChevronDownIcon}>

					Open

				</Button>

			)}

		/>

	);

};



export default PopupSelectExample;
```

## Layering

Currently there is no foundational platform solution that enables layered components to be composed together without extra effort. Use the offset and preventOverflow props from popper to keep them in view as a stop-gap. 

```jsx
import React, { useState } from 'react';



import ButtonGroup from '@atlaskit/button/button-group';

import Button from '@atlaskit/button/new';

import { Drawer, DrawerCloseButton, DrawerContent, DrawerSidebar } from '@atlaskit/drawer/compiled';

import ChevronDownIcon from '@atlaskit/icon/glyph/chevron-down';

import ModalDialog, {

	ModalBody,

	ModalHeader,

	ModalTitle,

	ModalTransition,

} from '@atlaskit/modal-dialog';

import { PopupSelect } from '@atlaskit/select';



const options = [

	{ label: 'Adelaide', value: 'adelaide' },

	{ label: 'Brisbane', value: 'brisbane' },

	{ label: 'Canberra', value: 'canberra' },

	{ label: 'Darwin', value: 'darwin' },

	{ label: 'Hobart', value: 'hobart' },

	{ label: 'Melbourne', value: 'melbourne' },

	{ label: 'Perth', value: 'perth' },

	{ label: 'Sydney', value: 'sydney' },

];



const SelectPopupModalExample = () => {

	const [type, setType] = useState<'modal' | 'drawer'>();



	const popupSelectElement = (

		<PopupSelect

			isSearchable={false}

			options={options}

			menuPlacement="bottom"

			popperProps={{

				modifiers: [

					{ name: 'offset', options: { offset: [0, 8] } },

					{

						name: 'preventOverflow',

						enabled: false,

					},

				],

			}}

			target={({ isOpen, ...triggerProps }) => (

				<Button {...triggerProps} isSelected={isOpen} iconAfter={ChevronDownIcon}>

					Open

				</Button>

			)}

		/>

	);



	return (

		<>

			<ButtonGroup label="Choose an option">

				<Button onClick={() => setType('modal')}>Open modal</Button>

				<Button onClick={() => setType('drawer')}>Open drawer</Button>

			</ButtonGroup>



			<Drawer

				label="Popup select inside Drawer"

				onClose={() => setType(undefined)}

				isOpen={type === 'drawer'}

			>

				<DrawerSidebar>

					<DrawerCloseButton />

				</DrawerSidebar>

				<DrawerContent>{popupSelectElement}</DrawerContent>

			</Drawer>



			<ModalTransition>

				{type === 'modal' && (

					<ModalDialog onClose={() => setType(undefined)}>

						<ModalHeader hasCloseButton>

							<ModalTitle>Popup select modal</ModalTitle>

						</ModalHeader>

						<ModalBody>{popupSelectElement}</ModalBody>

					</ModalDialog>

				)}

			</ModalTransition>

		</>

	);

};



export default SelectPopupModalExample;
```

## Content without portal

By default, the PopupSelect content is rendered inside React.Portal. Use popperProps={{ strategy: 'fixed' }} prop to render the content directly after the trigger element. 

```jsx
import React from 'react';



import Button from '@atlaskit/button/new';

import ChevronDownIcon from '@atlaskit/icon/glyph/chevron-down';

import { PopupSelect } from '@atlaskit/select';



const options = [

	{ label: 'accessibility', value: 'accessibility' },

	{ label: 'analytics', value: 'analytics' },

	{ label: 'ktlo', value: 'ktlo' },

	{ label: 'testing', value: 'testing' },

	{ label: 'regression', value: 'regression' },

	{ label: 'layering', value: 'layering' },

	{ label: 'innovation', value: 'innovation' },

	{ label: 'new-feature', value: 'new' },

	{ label: 'existing', value: 'existing' },

	{ label: 'wont-do', value: 'wont-do' },

];



const PopupSelectWithoutPortalExample = () => {

	return (

		<PopupSelect

			placeholder="Search labels..."

			searchThreshold={10}

			options={options}

			popperProps={{ strategy: 'fixed' }}

			target={({ isOpen, ...triggerProps }) => (

				<Button {...triggerProps} iconAfter={ChevronDownIcon}>

					Label

				</Button>

			)}

		/>

	);

};



export default PopupSelectWithoutPortalExample;
```

---

[View Original Documentation](https://atlassian.design/components/select/popup-select/examples)
