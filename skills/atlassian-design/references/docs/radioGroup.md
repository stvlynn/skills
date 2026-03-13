# Radio group

A radio group presents a list of options where only one choice can be selected.

---

## Default

The default way to select a single option from a list. 

```jsx
/**

 * @jsxRuntime classic

 * @jsx jsx

 */

import { Fragment, type SyntheticEvent, useCallback, useState } from 'react';



import { css, jsx } from '@compiled/react';



import { Checkbox } from '@atlaskit/checkbox';

import { RadioGroup } from '@atlaskit/radio';

import { type OptionsPropType } from '@atlaskit/radio/types';



const options: OptionsPropType = [

	{ name: 'color', value: 'red', label: 'Red' },

	{ name: 'color', value: 'blue', label: 'Blue' },

	{ name: 'color', value: 'yellow', label: 'Yellow' },

	{ name: 'color', value: 'green', label: 'Green' },

	{ name: 'color', value: 'black', label: 'Black' },

];



const radioGroupStyles = css({

	margin: '0.5em',

	padding: '0.5em',

	borderColor: '#ccc',

	borderStyle: 'dashed',

	borderWidth: '1px',

	color: '#ccc',

});



export default function BasicExample() {

	const [isDisabled, setIsDisabled] = useState<boolean>();

	const [onChangeResult, setOnChangeResult] = useState<string>(

		'Click on a radio field to trigger onChange',

	);



	const onChange = useCallback((event: SyntheticEvent<HTMLInputElement>) => {

		setOnChangeResult(`onChange called with value: ${event.currentTarget.value}`);

	}, []);



	const toggleCheckbox = useCallback((event: SyntheticEvent<HTMLInputElement>) => {

		setIsDisabled(event.currentTarget.checked);

	}, []);



	return (

		<Fragment>

			<h4 id="radiogroup-label">Choose a color:</h4>

			<RadioGroup

				isDisabled={isDisabled}

				options={options}

				onChange={onChange}

				aria-labelledby="radiogroup-label"

			/>

			<div css={radioGroupStyles}>{onChangeResult}</div>

			<Checkbox

				value="isDisabled"

				label="Make this radio group disabled"

				onChange={toggleCheckbox}

			/>

		</Fragment>

	);

}
```

## Form

Radio groups can be used within a form. 

### Simple

```jsx
import React from 'react';



import Button from '@atlaskit/button/new';

import Form, { Field, type FieldProps, FormFooter } from '@atlaskit/form';

import { RadioGroup } from '@atlaskit/radio';

import { type OptionsPropType } from '@atlaskit/radio/types';



const options: OptionsPropType = [

	{ name: 'color', value: 'red', label: 'Red' },

	{ name: 'color', value: 'blue', label: 'Blue' },

	{ name: 'color', value: 'yellow', label: 'Yellow' },

	{ name: 'color', value: 'green', label: 'Green' },

	{ name: 'color', value: 'black', label: 'Black' },

];



export default function FormExampleSimple() {

	return (

		<Form onSubmit={(data: object) => console.log('form data', data)}>

			{({ formProps }: { formProps: object }) => {

				return (

					<form {...formProps} name="form-example">

						<Field label="Regular radio group" name="fruit" defaultValue="peach">

							{({ fieldProps }: { fieldProps: FieldProps<string> }) => (

								<RadioGroup {...fieldProps} options={options} />

							)}

						</Field>

						<FormFooter>

							<Button type="submit" appearance="primary">

								Submit

							</Button>

						</FormFooter>

					</form>

				);

			}}

		</Form>

	);

}
```

### Complex disabled behavior

The isDisabled attribute of RadioGroup will override the isDisabled value of its children. This means that by default, individual radio items cannot be disabled while setting the disabled state of the entire Field. The following code example shows how to have RadioGroup override its children to disable the entire group. 

```jsx
import React, { type SyntheticEvent, useCallback, useState } from 'react';



import Button from '@atlaskit/button/new';

import { Checkbox } from '@atlaskit/checkbox';

import Form, { Field, type FieldProps, FormFooter } from '@atlaskit/form';

import { Box } from '@atlaskit/primitives/compiled';

import { RadioGroup } from '@atlaskit/radio';

import { type OptionsPropType } from '@atlaskit/radio/types';



const options: OptionsPropType = [

	{ name: 'color', value: 'red', label: 'Red' },

	{ name: 'color', value: 'blue', label: 'Blue' },

	{ name: 'color', value: 'yellow', label: 'Yellow' },

	{ name: 'color', value: 'green', label: 'Green', isDisabled: true },

];



export default function FormExample() {

	const [isDisabledChecked, setIsDisabled] = useState<boolean>(false);

	const toggleCheckbox = useCallback((event: SyntheticEvent<HTMLInputElement>) => {

		setIsDisabled(event.currentTarget.checked);

	}, []);

	return (

		<Box>

			<Form onSubmit={(data: object) => console.log('form data', data)}>

				{({ formProps }: { formProps: object }) => {

					return (

						<form {...formProps} name="form-example">

							<Field

								label="Radio group which can be dynamically disabled, with a single radio item disabled"

								name="weather"

								defaultValue="windy"

								isDisabled={isDisabledChecked}

							>

								{({

									fieldProps: { isDisabled, ...fieldProps },

								}: {

									fieldProps: FieldProps<string>;

								}) => (

									<RadioGroup

										{...fieldProps}

										isDisabled={isDisabled || undefined}

										options={options}

									/>

								)}

							</Field>

							<Checkbox

								value="isDisabledChecked"

								label="Make this radio group disabled"

								onChange={toggleCheckbox}

							/>

							<FormFooter>

								<Button type="submit" appearance="primary">

									Submit

								</Button>

							</FormFooter>

						</form>

					);

				}}

			</Form>

		</Box>

	);

}
```

---

[View Original Documentation](https://atlassian.design/components/radio/radio-group/examples)
