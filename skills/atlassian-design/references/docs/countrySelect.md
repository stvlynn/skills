# Country select

Country select allows users to make a single selection from a list of countries.

---

Use country select to let people select a single country from a list of countries.

```jsx
import React from 'react';



import { Label } from '@atlaskit/form';

import { CountrySelect } from '@atlaskit/select';



const CountrySelectExample = () => (

	<>

		<Label htmlFor="country-select-example">What country do you live in?</Label>

		<CountrySelect inputId="country-select-example" placeholder="Country" />

	</>

);



export default CountrySelectExample;
```

---

[View Original Documentation](https://atlassian.design/components/select/country-select/examples)
