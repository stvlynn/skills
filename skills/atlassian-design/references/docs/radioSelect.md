# Radio select

Radio select allows users to make a single selection from a list of options.

---

Use the radio select component for dropdown options displayed with radio buttons. Radio buttons can be used for a list of options where only one choice can be selected. If you need to have multiple selectable options, use multi select or checkbox select instead.

```jsx
import React from 'react';



import { Label } from '@atlaskit/form';

import { RadioSelect } from '@atlaskit/select';



import { cities } from '../common/data';



const SelectRadioExample = () => (

	<>

		<Label htmlFor="radio-select-example">What city do you live in?</Label>

		<RadioSelect

			inputId="radio-select-example"

			testId="react-select"

			options={[

				...cities,

				{

					label: "Super long name that no one will ever read because it's way too long",

					value: 'test',

				},

			]}

			placeholder="Choose a city"

		/>

	</>

);



export default SelectRadioExample;
```

---

[View Original Documentation](https://atlassian.design/components/select/radio-select/examples)
