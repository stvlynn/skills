# Checkbox select

Checkbox select allows users to make multiple selections from a list of options.

---

Use the checkbox select component for dropdown options displayed as checkboxes. People can use the checkbox select to choose multiple options at once.

```jsx
import React from 'react';



import { Label } from '@atlaskit/form';

import { CheckboxSelect } from '@atlaskit/select';



import { cities } from '../common/data';



const SelectCheckboxExample = () => (

	<>

		<Label htmlFor="checkbox-select-example">What cities have you lived in?</Label>

		<CheckboxSelect

			inputId="checkbox-select-example"

			testId="select"

			options={[

				...cities,

				{

					label:

						"Super long name that no one will ever read because it's way too long to be a realistic option but it will highlight the flexbox grow and shrink styles",

					value: 'test',

				},

			]}

			placeholder="Choose a city"

		/>

	</>

);



export default SelectCheckboxExample;
```

---

[View Original Documentation](https://atlassian.design/components/select/checkbox-select/examples)
