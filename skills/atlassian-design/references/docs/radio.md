# Radio

A radio input allows users to select only one option from a number of choices. Radio is generally displayed in a radio group.

---

## Default

The default way to present a single option from a list. In most situations where you want to present a list of mutually exclusive options, you will want to use a radio group. 

```jsx
import React from 'react';



import noop from '@atlaskit/ds-lib/noop';

import { Box } from '@atlaskit/primitives/compiled';

import { Radio } from '@atlaskit/radio';



export default function RadioDefaultExample() {

	return (

		<Box>

			<Radio

				value="default radio"

				label="Default radio"

				name="radio-default"

				testId="radio-default"

				isChecked={true}

				onChange={noop}

			/>

			<Radio

				value="disabled radio"

				label="Disabled radio"

				name="radio-disabled"

				testId="radio-disabled"

				isChecked={false}

				isDisabled={true}

				onChange={noop}

			/>

		</Box>

	);

}
```

## Complex radio usage

There may be some situations where you are unable to directly stack the radio inputs vertically (for example, within a table). In those situations, you can use individual Radio components rather than a RadioGroup. 

```jsx
/**

 * @jsxRuntime classic

 * @jsx jsx

 */

import { type SyntheticEvent, useCallback, useState } from 'react';



import { cssMap, jsx } from '@atlaskit/css';

import { Box } from '@atlaskit/primitives/compiled';

import { Radio } from '@atlaskit/radio';

import { token } from '@atlaskit/tokens';



const styles = cssMap({

	selectedValue: {

		marginBlock: token('space.200'),

		paddingTop: token('space.100'),

		paddingRight: token('space.100'),

		paddingBottom: token('space.100'),

		paddingLeft: token('space.100'),

		borderColor: token('color.border'),

		borderStyle: 'dashed',

		borderWidth: token('border.width'),

		color: token('color.text'),

	},

});



interface RadioOptions {

	id: number;

	value: string;

	name: string;

	description: string;

	commit: string;

	updated: string;

}



const items: Array<RadioOptions> = [

	{

		id: 1,

		value: '1',

		name: 'branch',

		description: 'master',

		commit: 'dcc0f15',

		updated: '14 minutes ago',

	},

	{

		id: 2,

		value: '2',

		name: 'branch',

		description: 'feature/dark-mode',

		commit: 'cbc0fa3',

		updated: '56 minutes ago',

	},

	{

		id: 3,

		value: '3',

		name: 'branch',

		description: 'feature/right-to-left',

		commit: '69568ea',

		updated: '16 hours ago',

	},

	{

		id: 4,

		value: '4',

		name: 'branch',

		description: 'bug/type-incorrect-for-checked-prop',

		commit: '1159c76',

		updated: 'yesterday',

	},

];



export default function RadioInputExample() {

	const [value, setValue] = useState<string>('1');



	const onChange = useCallback(

		({ currentTarget: { value } }: SyntheticEvent<any>) => {

			setValue(value);

		},

		[setValue],

	);



	return (

		<Box>

			<table>

				<thead>

					<tr>

						{/* eslint-disable-next-line @atlaskit/ui-styling-standard/enforce-style-prop -- Ignored via go/DSP-18766 */}

						<td style={{ width: 0 }} />

						<th id="head-description">Branch</th>

						<th id="head-commit">Last commit</th>

						<th id="head-updated">Updated</th>

					</tr>

				</thead>

				<tbody>

					{items.map((item) => (

						<tr

							onClick={() => setValue(item.value)}

							key={`${item.value}${item.name}${item.id}`}

							style={{

								backgroundColor:

									item.value === value ? token('color.background.selected') : 'transparent',

								// eslint-disable-next-line @atlaskit/ui-styling-standard/enforce-style-prop -- Ignored via go/DSP-18766

								transition: 'background-color 200ms ease-in-out',

							}}

						>

							{/* eslint-disable-next-line @atlaskit/ui-styling-standard/enforce-style-prop -- Ignored via go/DSP-18766 */}

							<th scope="row" style={{ width: 24, paddingRight: 0 }}>

								<Radio

									isChecked={item.value === value}

									onChange={onChange}

									name={item.name}

									value={item.value}

									aria-labelledby={`head-description row-${item.id}-description head-commit row-${item.id}-commit head-updated row-${item.id}-updated`}

								/>

							</th>

							<td id={`row-${item.id}-description`}>{item.description}</td>

							<td id={`row-${item.id}-commit`}>{item.commit}</td>

							<td id={`row-${item.id}-updated`}>{item.updated}</td>

						</tr>

					))}

				</tbody>

			</table>

			<Box xcss={styles.selectedValue}>currently selected value: {value}</Box>

		</Box>

	);

}
```

| Branch | Last commit | Updated |
| --- | --- | --- |
| master | dcc0f15 | 14 minutes ago |
| feature/dark-mode | cbc0fa3 | 56 minutes ago |
| feature/right-to-left | 69568ea | 16 hours ago |
| bug/type-incorrect-for-checked-prop | 1159c76 | yesterday |

## Invalid radio

Use isInvalid for situations where the selected field is invalid or incorrect. Remember to provide useful validation messages to help people understand how to proceed. 

```jsx
import React, { Fragment } from 'react';



import Button from '@atlaskit/button/new';

import Form, { ErrorMessage, Field, FormFooter } from '@atlaskit/form';

import { RadioGroup } from '@atlaskit/radio';

import { type OptionsPropType } from '@atlaskit/radio/types';



interface FormData {

	[key: string]: string;

	'radio-group-invalid': string;

}



const validateOnSubmit = (data: FormData) => {

	let errors;

	errors = requiredValidator(data, 'radio-group-invalid');

	return errors;

};



const requiredValidator = (data: FormData, key: string) => {

	if (data[key] === 'invalid') {

		return {

			[key]: `This field is invalid.`,

		};

	}

};



const options: OptionsPropType = [

	{ name: 'radio-group-invalid', value: 'valid', label: 'Valid' },

	{ name: 'radio-group-invalid', value: 'invalid', label: 'Invalid' },

];



export default function RadioInvalid() {

	return (

		<Form<FormData>

			onSubmit={(data) => {

				console.log('form data', data);

				return Promise.resolve(validateOnSubmit(data));

			}}

		>

			{({ formProps }) => (

				<form {...formProps}>

					<Field

						label="Radio group with validation"

						name="radio-group-invalid"

						defaultValue="valid"

					>

						{({ fieldProps, error }) => (

							<Fragment>

								<RadioGroup {...fieldProps} options={options} />

								{error && <ErrorMessage>{error}</ErrorMessage>}

							</Fragment>

						)}

					</Field>

					<FormFooter>

						<Button type="submit">Submit</Button>

					</FormFooter>

				</form>

			)}

		</Form>

	);

}
```

## Required radio

Use isRequired to require users to fill out the input field before submitting the form. 

```jsx
import React from 'react';



import Button from '@atlaskit/button/new';

import Form, { Field, FormFooter } from '@atlaskit/form';

import { RadioGroup } from '@atlaskit/radio';

import { type OptionsPropType } from '@atlaskit/radio/types';



const colorItems: OptionsPropType = [

	{ name: 'color', value: 'red', label: 'Red' },

	{ name: 'color', value: 'blue', label: 'Blue' },

	{ name: 'color', value: 'yellow', label: 'Yellow' },

	{ name: 'color', value: 'green', label: 'Green' },

];



export default function RadioRequired() {

	return (

		<Form<FormData> onSubmit={(formData) => console.log('form data', formData)}>

			{({ formProps }) => (

				<form {...formProps}>

					<Field label="Required radio group" name="color" defaultValue="" isRequired>

						{({ fieldProps }) => <RadioGroup {...fieldProps} options={colorItems} />}

					</Field>

					<FormFooter>

						<Button type="submit">Submit</Button>

					</FormFooter>

				</form>

			)}

		</Form>

	);

}
```

---

[View Original Documentation](https://atlassian.design/components/radio/examples)
