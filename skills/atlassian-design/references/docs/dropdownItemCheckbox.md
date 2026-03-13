# Dropdown item checkbox

A dropdown item checkbox lets users select items from a list of options.

---

## Default selected

This makes the checkbox item selected when initially opened. Use defaultSelected when not controlling the checkbox item state. 

```jsx
import React from 'react';



import DropdownMenu, {

	DropdownItemCheckbox,

	DropdownItemCheckboxGroup,

} from '@atlaskit/dropdown-menu';



const DropdownItemCheckboxExample = () => {

	return (

		<DropdownMenu trigger="Status" shouldRenderToParent>

			<DropdownItemCheckboxGroup title="Categories" id="actions">

				<DropdownItemCheckbox id="todo" defaultSelected>

					To do

				</DropdownItemCheckbox>

				<DropdownItemCheckbox id="inprogress">In progress</DropdownItemCheckbox>

				<DropdownItemCheckbox id="done">Done</DropdownItemCheckbox>

			</DropdownItemCheckboxGroup>

		</DropdownMenu>

	);

};



export default DropdownItemCheckboxExample;
```

## Selected

This makes the checkbox item selected when true. Use isSelected when controlling the checkbox item state. 

```jsx
import React, { useState } from 'react';



import DropdownMenu, {

	DropdownItemCheckbox,

	DropdownItemCheckboxGroup,

} from '@atlaskit/dropdown-menu';



const DropdownItemCheckboxExample = () => {

	const [checked, setChecked] = useState<Record<string, boolean>>({

		todo: true,

	});

	const toggle = (name: string) => {

		setChecked((prev) => ({

			...prev,

			[name]: !prev[name],

		}));

	};



	return (

		<DropdownMenu trigger="Status" shouldRenderToParent>

			<DropdownItemCheckboxGroup title="Categories" id="actions">

				<DropdownItemCheckbox

					id="todo"

					onClick={(e) => toggle('todo')}

					isSelected={checked['todo']}

				>

					To do

				</DropdownItemCheckbox>

				<DropdownItemCheckbox

					id="inprogress"

					onClick={(e) => toggle('inprogress')}

					isSelected={checked['inprogress']}

				>

					In progress

				</DropdownItemCheckbox>

				<DropdownItemCheckbox

					id="done"

					onClick={(e) => toggle('done')}

					isSelected={checked['done']}

				>

					Done

				</DropdownItemCheckbox>

			</DropdownItemCheckboxGroup>

		</DropdownMenu>

	);

};



export default DropdownItemCheckboxExample;
```

---

[View Original Documentation](https://atlassian.design/components/dropdown-menu/dropdown-item-checkbox/examples)
