# Async select

Async select handles loading data from remote sources.

---

Async select introduces a loadOptions prop that can be given a promise or callback that will eventually resolve to its list of options.

```jsx
import React from 'react';



import { Label } from '@atlaskit/form';

import Select, { type OptionsType } from '@atlaskit/select';



import { cities } from '../common/data';



const filterCities = (inputValue: string) =>

	cities.filter((i) => i.label.toLowerCase().includes(inputValue.toLowerCase()));



const promiseOptions = (inputValue: string) =>

	new Promise<OptionsType>((resolve) => {

		setTimeout(() => {

			resolve(filterCities(inputValue));

		}, 1000);

	});



const WithPromises = () => {

	return (

		<>

			<Label htmlFor="async-select-example">What city do you live in?</Label>

			<Select

				inputId="async-select-example"

				cacheOptions

				defaultOptions

				loadOptions={promiseOptions}

			/>

		</>

	);

};



export default () => <WithPromises />;
```

---

[View Original Documentation](https://atlassian.design/components/select/async-select/examples)
