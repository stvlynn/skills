# Range

A range lets users choose an approximate value on a slider.

---

## Default

The default form of a range. 

```jsx
import React from 'react';



import { Label } from '@atlaskit/form';

import Range from '@atlaskit/range';



const RangeDefaultExample = () => (

	<>

		<Label htmlFor="range-input">Adjust volume</Label>

		<Range id="range-input" step={1} min={1} max={100} />

	</>

);



export default RangeDefaultExample;
```

## Form

Range used with the form component. 

```jsx
import React from 'react';



import Button from '@atlaskit/button/new';

import Form, { FormFooter, HelperMessage, RangeField } from '@atlaskit/form';

import Range from '@atlaskit/range';



export default function TextFieldFormExample() {

	return (

		<Form onSubmit={(formState: unknown) => console.log('form submitted', formState)}>

			{({ formProps }: any) => (

				<form {...formProps}>

					<RangeField label="Adjust brightness" name="example-text" defaultValue={50}>

						{({ fieldProps }) => (

							<>

								<Range {...fieldProps} />

								<HelperMessage>

									Move the slider to set your preferred brightness level, then press submit.

								</HelperMessage>

							</>

						)}

					</RangeField>

					<FormFooter>

						<Button type="submit" appearance="primary">

							Submit

						</Button>

					</FormFooter>

				</form>

			)}

		</Form>

	);

}
```

## Controlled

In a controlled range, the state is managed by the React component. Use the onChange handler to set the value. The current value is: 50 

```jsx
import React, { useState } from 'react';



import Range from '@atlaskit/range';



const RangeControlledExample = () => {

	const [value, setValue] = useState(50);



	return (

		<>

			<Range

				aria-label="controlled range"

				step={1}

				value={value}

				onChange={(value) => setValue(value)}

			/>

			<p>The current value is: {value}</p>

		</>

	);

};



export default RangeControlledExample;
```

## Uncontrolled

In an uncontrolled range, the state is managed by the DOM. 

```jsx
import React from 'react';



import Range from '@atlaskit/range';



const RangeUncontrolledExample = () => {

	return (

		<Range

			aria-label="uncontrolled range"

			step={1}

			onChange={(value) => console.log('new value', value)}

		/>

	);

};



export default RangeUncontrolledExample;
```

## Disabled

Set isDisabled to disable a range when another action has to be completed before the range is usable. Avoid using disabled UI where possible. This can cause accessibility problems, because disabled UI does not give enough information about what went wrong and how to proceed. 

```jsx
import React from 'react';



import Range from '@atlaskit/range';



const RangeDisabledExample = () => {

	return <Range aria-label="disabled range" isDisabled step={1} min={1} max={100} />;

};



export default RangeDisabledExample;
```

---

[View Original Documentation](https://atlassian.design/components/range/examples)
