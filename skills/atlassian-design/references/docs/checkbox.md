# Checkbox

A checkbox is an input control that allows a user to select one or more options from a number of choices.

---

## Default

The default checkbox input includes a selected and unselected state. 

```jsx
import React from 'react';



import { Checkbox } from '@atlaskit/checkbox';

import __noop from '@atlaskit/ds-lib/noop';



const CheckboxDefaultExample = () => {

	return (

		<Checkbox

			value="default checkbox"

			label="Default checkbox"

			onChange={__noop}

			name="checkbox-default"

			testId="cb-default"

		/>

	);

};



export default CheckboxDefaultExample;
```

## Controlled

In a controlled checkbox, the checked state is managed by the React component. Set isChecked to select the checkbox and use the onChange handler to change the value. 

```jsx
import React, { type ChangeEvent, useCallback, useState } from 'react';



import { Checkbox } from '@atlaskit/checkbox';



const CheckboxControlledExample = () => {

	const [isChecked, setIsChecked] = useState(true);

	const [onChangeResult, setOnChangeResult] = useState('true');



	const onChange = useCallback((event: ChangeEvent<HTMLInputElement>) => {

		setIsChecked((current) => !current);

		setOnChangeResult(`${event.target.checked}`);

	}, []);



	return (

		<Checkbox

			isChecked={isChecked}

			onChange={onChange}

			label={`Controlled checkbox, with props.isChecked: ${onChangeResult}`}

			value="Controlled Checkbox"

			name="controlled-checkbox"

		/>

	);

};



export default CheckboxControlledExample;
```

## Uncontrolled

In an uncontrolled checkbox, the checked state is managed by the DOM. Use defaultChecked to set the initial selected state. 

```jsx
import React from 'react';



import { Checkbox } from '@atlaskit/checkbox';



const CheckboxUncontrolledExample = () => (

	<Checkbox

		defaultChecked

		label="Uncontrolled checkbox"

		value="Uncontrolled checkbox"

		name="uncontrolled-checkbox"

	/>

);



export default CheckboxUncontrolledExample;
```

## Disabled

Use isDisabled to disable a checkbox when another action has to be completed before the checkbox is usable. 

```jsx
import React from 'react';



import { Checkbox } from '@atlaskit/checkbox';



const CheckboxDisabledExample = () => (

	<Checkbox

		isDisabled

		label="Disabled checkbox"

		value="Disabled"

		name="checkbox-disabled"

		testId="cb-disabled"

	/>

);

export default CheckboxDisabledExample;
```

## Invalid

Use isInvalid when a user chooses an incorrect value. 

```jsx
import React, { Fragment } from 'react';



import Button from '@atlaskit/button/new';

import { Checkbox } from '@atlaskit/checkbox';

import Form, { CheckboxField, ErrorMessage, FormFooter } from '@atlaskit/form';



interface FormData {

	[key: string]: string;

	'checkbox-invalid': string;

}



const validateOnSubmit = (data: FormData) => {

	let errors;

	errors = requiredValidator(data, 'checkbox-invalid');

	return errors;

};



const requiredValidator = (data: FormData, key: string) => {

	if (!data[key]) {

		return {

			[key]: `Please read and accept the terms and conditions to continue.`,

		};

	}

};



const CheckboxInvalidExample = () => {

	return (

		<Form<FormData>

			onSubmit={(data) => {

				console.log('form data', data);

				return Promise.resolve(validateOnSubmit(data));

			}}

		>

			{({ formProps }) => (

				<form {...formProps}>

					<CheckboxField name="checkbox-invalid">

						{({ fieldProps, error }) => (

							<Fragment>

								<Checkbox

									{...fieldProps}

									label="By checking this box you agree to the terms and conditions"

									value="By checking this box you agree to the terms and conditions"

									name="checkbox-invalid"

									testId="cb-invalid"

								/>

								{error && <ErrorMessage>{error}</ErrorMessage>}

							</Fragment>

						)}

					</CheckboxField>

					<FormFooter>

						<Button type="submit">Submit</Button>

					</FormFooter>

				</form>

			)}

		</Form>

	);

};



export default CheckboxInvalidExample;
```

## Indeterminate

Use isIndeterminate to show partially checked states. The parent checkbox will be indeterminate if some, but not all child sub-options are checked. Note that the parent checkbox does not have its own state, but simply reflects the state of its children. 

```jsx
/**

 * @jsxRuntime classic

 * @jsx jsx

 */

import { type ChangeEvent, useState } from 'react';



import { Checkbox } from '@atlaskit/checkbox';

import { jsx } from '@atlaskit/css';

import { Box, xcss } from '@atlaskit/primitives';



type Checkboxes = Record<string, boolean>;



const childCheckBoxesStyle = xcss({ paddingInlineStart: 'space.300' });



const parentCheckbox = { id: 'ALL_PROJECTS', label: 'All projects' };



const childrenCheckboxes = [

	{ id: 'DESIGN_SYSTEM', label: 'Design System' },

	{ id: 'JIRA_SOFTWARE', label: 'Jira Software' },

	{ id: 'CONFLUENCE', label: 'Confluence' },

];



const getInitialCheckedItems = (): Checkboxes => {

	const initialChildCheckboxes: Checkboxes = {};

	childrenCheckboxes.forEach((child) => (initialChildCheckboxes[child.id] = false));

	return initialChildCheckboxes;

};



const IndeterminateCheckboxExample = () => {

	const [childCheckboxes, setChildCheckboxes] = useState(getInitialCheckedItems());



	const getAllChildren = () => Object.keys(childCheckboxes);



	const getCheckedChildrenCount = () => getAllChildren().filter(isChildChecked).length;



	const isParentChecked = () => getCheckedChildrenCount() > 0;

	const isChildChecked = (childCheckboxId: string) => childCheckboxes[childCheckboxId];



	const isIndeterminate = () => {

		const checkedChildrenCount = getCheckedChildrenCount();

		const notAllChildrenAreChecked = checkedChildrenCount < getAllChildren().length;

		const atLeastOneChildIsChecked = checkedChildrenCount > 0;



		return atLeastOneChildIsChecked && notAllChildrenAreChecked;

	};



	const handleParentCheckboxChange = (_event: ChangeEvent<HTMLInputElement>) => {

		const newCheckedState: boolean = !isParentChecked();

		const newChildCheckboxesState: Checkboxes = {};

		getAllChildren().forEach((childCheckboxId) => {

			newChildCheckboxesState[childCheckboxId] = newCheckedState;

		});

		setChildCheckboxes(newChildCheckboxesState);

	};



	const handleChildCheckboxChange = (event: ChangeEvent<HTMLInputElement>) => {

		const { value } = event.target;

		const newCheckboxState = !isChildChecked(value);

		setChildCheckboxes({

			...childCheckboxes,

			[value]: newCheckboxState,

		});

	};



	return (

		<Box>

			<Checkbox

				isChecked={isParentChecked()}

				isIndeterminate={isIndeterminate()}

				onChange={handleParentCheckboxChange}

				label={parentCheckbox.label}

				value={parentCheckbox.id}

				testId="parent"

			/>

			<Box xcss={childCheckBoxesStyle}>

				{childrenCheckboxes.map((childCheckbox, i) => (

					<Checkbox

						isChecked={isChildChecked(childCheckbox.id)}

						onChange={handleChildCheckboxChange}

						label={childCheckbox.label}

						value={childCheckbox.id}

						testId={`child-${i + 1}`}

						key={childCheckbox.id}

					/>

				))}

			</Box>

		</Box>

	);

};



export default IndeterminateCheckboxExample;
```

## Required

Use isRequired to make the checkbox required and change the label style. 

```jsx
import React, { type ChangeEvent, Fragment, useCallback, useState } from 'react';



import Button from '@atlaskit/button/new';

import { Checkbox } from '@atlaskit/checkbox';

import Form, { CheckboxField, FormFooter } from '@atlaskit/form';



const CheckboxRequiredExample = () => {

	const [isChecked, setIsChecked] = useState(false);



	const onChange = useCallback((event: ChangeEvent<HTMLInputElement>) => {

		setIsChecked((current) => !current);

	}, []);



	return (

		<Form onSubmit={(formData) => console.log('form data', formData)}>

			{({ formProps }) => (

				<form {...formProps}>

					<CheckboxField name="checkbox-required" isRequired>

						{({ fieldProps }) => (

							<Fragment>

								<Checkbox

									{...fieldProps}

									isChecked={isChecked}

									onChange={onChange}

									label="By checking this box you agree to the terms and conditions"

									value="By checking this box you agree to the terms and conditions"

									name="checkbox-required"

								/>

							</Fragment>

						)}

					</CheckboxField>

					<FormFooter>

						<Button type="submit" isDisabled={!isChecked}>

							Submit

						</Button>

					</FormFooter>

				</form>

			)}

		</Form>

	);

};



export default CheckboxRequiredExample;
```

---

[View Original Documentation](https://atlassian.design/components/checkbox/examples)
