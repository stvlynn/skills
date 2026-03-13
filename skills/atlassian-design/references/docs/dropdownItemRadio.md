# Dropdown item radio

A dropdown item radio lets users select one option from a list of options.

---

## Default selected

This makes the radio item selected when initially opened. Use defaultSelected when not controlling the radio item state. 

```jsx
import React from 'react';



import DropdownMenu, { DropdownItemRadio, DropdownItemRadioGroup } from '@atlaskit/dropdown-menu';



const DropdownItemRadioExample = () => {

	return (

		<DropdownMenu trigger="Views" shouldRenderToParent>

			<DropdownItemRadioGroup title="Views" id="actions">

				<DropdownItemRadio id="detail" defaultSelected>

					Detail view

				</DropdownItemRadio>

				<DropdownItemRadio id="list">List view</DropdownItemRadio>

			</DropdownItemRadioGroup>

		</DropdownMenu>

	);

};



export default DropdownItemRadioExample;
```

## Selected

This makes the radio item selected when true. Use isSelected when controlling the radio item state. 

```jsx
import React, { useState } from 'react';



import DropdownMenu, { DropdownItemRadio, DropdownItemRadioGroup } from '@atlaskit/dropdown-menu';



const DropdownItemRadioExample = () => {

	const [selected, setSelected] = useState<string>('detail');



	return (

		<DropdownMenu trigger="Views" shouldRenderToParent>

			<DropdownItemRadioGroup title="Views" id="actions">

				<DropdownItemRadio

					id="detail"

					onClick={() => setSelected('detail')}

					isSelected={selected === 'detail'}

				>

					Detail view

				</DropdownItemRadio>

				<DropdownItemRadio

					id="list"

					onClick={() => setSelected('list')}

					isSelected={selected === 'list'}

				>

					List view

				</DropdownItemRadio>

			</DropdownItemRadioGroup>

		</DropdownMenu>

	);

};



export default DropdownItemRadioExample;
```

---

[View Original Documentation](https://atlassian.design/components/dropdown-menu/dropdown-item-radio/examples)
