# Form

A form allows users to input information.

---

## Default

A form is a group of related fields. You can customize the fields with components such as text field, range field, and checkbox field. You can also pass in default values. Submitting the form calls a callback function. Form is a wrapper that does not render anything itself. Instead, it passes props and information down into the <form> element and its children. This includes information about whether the form is dirty, disabled, reset or submitting. People can submit the form when all fields are valid (see validation). The current state of the fields is the single source of truth for the form. 

## Sign in

Required fields are marked with an asterisk * 

```jsx
import React, { Fragment } from 'react';



import ButtonGroup from '@atlaskit/button/button-group';

import Button from '@atlaskit/button/new';

import { Checkbox } from '@atlaskit/checkbox';

import Form, {

	CheckboxField,

	ErrorMessage,

	Field,

	FormFooter,

	FormHeader,

	FormSection,

	HelperMessage,

	RequiredAsterisk,

	ValidMessage,

} from '@atlaskit/form';

import TextField from '@atlaskit/textfield';



const FormDefaultExample = () => (

	<div

		style={{

			// eslint-disable-next-line @atlaskit/ui-styling-standard/enforce-style-prop -- Ignored via go/DSP-18766

			display: 'flex',

			// eslint-disable-next-line @atlaskit/ui-styling-standard/enforce-style-prop -- Ignored via go/DSP-18766

			width: '400px',

			// eslint-disable-next-line @atlaskit/ui-styling-standard/enforce-style-prop -- Ignored via go/DSP-18766

			maxWidth: '100%',

			// eslint-disable-next-line @atlaskit/ui-styling-standard/enforce-style-prop -- Ignored via go/DSP-18766

			margin: '0 auto',

			// eslint-disable-next-line @atlaskit/ui-styling-standard/enforce-style-prop -- Ignored via go/DSP-18766

			flexDirection: 'column',

		}}

	>

		<Form<{ username: string; password: string; remember: boolean }>

			onSubmit={(data) => {

				console.log('form data', data);

				return new Promise((resolve) => setTimeout(resolve, 2000)).then(() =>

					data.username === 'error' ? { username: 'IN_USE' } : undefined,

				);

			}}

		>

			{({ formProps, submitting }) => (

				<form {...formProps}>

					<FormHeader title="Sign in">

						<p aria-hidden="true">

							Required fields are marked with an asterisk <RequiredAsterisk />

						</p>

					</FormHeader>

					<FormSection>

						<Field

							aria-required={true}

							name="username"

							label="Username"

							isRequired

							defaultValue="dst12"

						>

							{({ fieldProps, error }) => (

								<Fragment>

									<TextField autoComplete="off" {...fieldProps} />

									{!error && (

										<HelperMessage>You can use letters, numbers, and periods</HelperMessage>

									)}

									{error && (

										<ErrorMessage>This username is already in use, try another one</ErrorMessage>

									)}

								</Fragment>

							)}

						</Field>

						<Field

							aria-required={true}

							name="password"

							label="Password"

							defaultValue=""

							isRequired

							validate={(value) => (value && value.length < 8 ? 'TOO_SHORT' : undefined)}

						>

							{({ fieldProps, error, valid, meta }) => {

								return (

									<Fragment>

										<TextField type="password" {...fieldProps} />

										{error && !valid && (

											<HelperMessage>

												Use 8 or more characters with a mix of letters, numbers, and symbols

											</HelperMessage>

										)}

										{error && (

											<ErrorMessage>Password needs to be more than 8 characters</ErrorMessage>

										)}

										{valid && meta.dirty ? <ValidMessage>Awesome password!</ValidMessage> : null}

									</Fragment>

								);

							}}

						</Field>

						<CheckboxField name="remember" defaultIsChecked>

							{({ fieldProps }) => (

								<Checkbox {...fieldProps} label="Always sign in on this device" />

							)}

						</CheckboxField>

					</FormSection>



					<FormFooter>

						<ButtonGroup label="Form submit options">

							<Button appearance="subtle">Cancel</Button>

							<Button type="submit" appearance="primary" isLoading={submitting}>

								Sign up

							</Button>

						</ButtonGroup>

					</FormFooter>

				</form>

			)}

		</Form>

	</div>

);



export default FormDefaultExample;
```

## Custom

You can customize a form field. Any component with a value and onChange handler can be a field. The component renders inside a field and adds an entry to the form state. Selected color: none 

```jsx
/**

 * @jsxRuntime classic

 * @jsx jsx

 */

import React from 'react';



import Button from '@atlaskit/button/new';

import { cssMap, jsx } from '@atlaskit/css';

import Form, { Field, FormFooter } from '@atlaskit/form';

import { Box } from '@atlaskit/primitives/compiled';



interface ColorButtonProps {

	color: string;

	changeHandler: Function;

}



interface ColorButtonsProps {

	colors: Array<string>;

	changeHandler: Function;

}



const colorButtonStyles = cssMap({

	root: {

		color: 'transparent',

		display: 'inline-block',

		height: '40px',

		width: '40px',

		overflow: 'hidden',

	},

});



const ColorButton = ({ color, changeHandler }: ColorButtonProps) => (

	<button

		type="submit"

		style={{

			backgroundColor: color,

			// eslint-disable-next-line @atlaskit/ui-styling-standard/enforce-style-prop

			margin: '0px 5px',

		}}

		css={colorButtonStyles.root}

		onClick={(e) => {

			e.preventDefault();

			/*

			 *

			 * For custom non-form-field fields, this event handler calls the onChange method that is passed to the render prop's fieldProps (i.e. fieldProps.onChange).

			 * It is called with the new value of the field, which will propagate the value up to the Form and back to the Field.

			 */

			changeHandler(color);

		}}

	>

		{color}

	</button>

);



const ColorButtons = ({ colors, changeHandler }: ColorButtonsProps) => (

	<React.Fragment>

		{colors.map((color) => (

			<ColorButton color={color} changeHandler={changeHandler} key={color} />

		))}

	</React.Fragment>

);



const formWrapperStyles = cssMap({

	root: {

		display: 'flex',

		flexDirection: 'column',

		width: '400px',

		margin: '0 auto',

	},

});



const FormCustomFieldExample = () => {

	return (

		<div css={formWrapperStyles.root}>

			<Form onSubmit={(data) => console.log(data)}>

				{({ formProps }) => (

					<form {...formProps}>

						<Field name="favorite-color" defaultValue="" label="Favorite color">

							{({ fieldProps }) => (

								<Box data-name={fieldProps.id} data-value={fieldProps.value}>

									{/* eslint-disable-next-line @atlaskit/ui-styling-standard/enforce-style-prop -- Ignored via go/DSP-18766 */}

									<p style={{ margin: '10px 0' }}>

										Selected color:{' '}

										{fieldProps.value ? (

											<span style={{ color: fieldProps.value }}>{fieldProps.value}</span>

										) : (

											'none'

										)}

									</p>

									<ColorButtons

										colors={['Red', 'Green', 'Orange', 'Blue']}

										changeHandler={fieldProps.onChange}

									/>

								</Box>

							)}

						</Field>

						<FormFooter>

							<Button type="submit" appearance="primary">

								Submit

							</Button>

						</FormFooter>

					</form>

				)}

			</Form>

		</div>

	);

};



export default FormCustomFieldExample;
```

### Select

```jsx
import React, { Fragment } from 'react';



import Button from '@atlaskit/button/new';

import Form, { ErrorMessage, Field, FormFooter } from '@atlaskit/form';

import Select, {

	components,

	type OptionProps,

	type SingleValueProps,

	type ValueType,

} from '@atlaskit/select';

import { token } from '@atlaskit/tokens';



interface Option {

	label: string;

	value: string;

}

interface Category {

	colors?: ValueType<Option>;

	icecream?: ValueType<Option[]>;

	suit?: ValueType<Option[]>;

}



const colors = [

	{ label: 'Blue', value: 'blue' },

	{ label: 'Red', value: 'red' },

	{ label: 'Purple', value: 'purple' },

	{ label: 'Black', value: 'black' },

	{ label: 'White', value: 'white' },

	{ label: 'Gray', value: 'gray' },

	{ label: 'Yellow', value: 'yellow' },

];



const flavors = [

	{ label: 'Vanilla', value: 'vanilla' },

	{ label: 'Strawberry', value: 'strawberry' },

	{ label: 'Chocolate', value: 'chocolate' },

	{ label: 'Mango', value: 'mango' },

	{ label: 'Passionfruit', value: 'passionfruit' },

	{ label: 'Hazelnut', value: 'hazelnut' },

	{ label: 'Durian', value: 'durian' },

];



const validateOnSubmit = (data: Category) => {

	let errors;

	errors = colorsValidation(data, errors);

	errors = flavorValidation(data, errors);

	return errors;

};



const colorsValidation = (data: Category, errors?: Record<string, string>) => {

	if (data.colors && !(data.colors instanceof Array)) {

		return (data.colors as Option).value === 'dog'

			? {

					...errors,

					colors: `${(data.colors as Option).value} is not a color`,

				}

			: errors;

	}

	return errors;

};



const flavorValidation = (data: Category, errors?: Record<string, string>) => {

	if (data.icecream && data.icecream.length >= 3) {

		return {

			...errors,

			icecream: `${data.icecream.length} is too many flavors, please select a maximum of 2 flavors`,

		};

	}



	return errors;

};



const ColorBox = ({ color }: { color: string }) => (

	<span

		style={{

			// eslint-disable-next-line @atlaskit/ui-styling-standard/enforce-style-prop -- Ignored via go/DSP-18766

			width: '10px',

			// eslint-disable-next-line @atlaskit/ui-styling-standard/enforce-style-prop -- Ignored via go/DSP-18766

			height: '10px',

			backgroundColor: color,

			// eslint-disable-next-line @atlaskit/ui-styling-standard/enforce-style-prop -- Ignored via go/DSP-18766

			display: 'inline-block',

			// eslint-disable-next-line @atlaskit/ui-styling-standard/enforce-style-prop -- Ignored via go/DSP-18766

			marginRight: token('space.100'),

			// eslint-disable-next-line @atlaskit/ui-styling-standard/enforce-style-prop -- Ignored via go/DSP-18766

			marginBottom: token('space.050'),

			// eslint-disable-next-line @atlaskit/ui-styling-standard/enforce-style-prop -- Ignored via go/DSP-18766

			verticalAlign: 'middle',

		}}

	/>

);



type ColorOption = (typeof colors)[number];



/**

 * NOTE: this is not declared inline with the Select

 * If you declare inline you'll have issues with refs

 */

const CustomColorOption = ({ children, ...props }: OptionProps<ColorOption>) => (

	// eslint-disable-next-line @repo/internal/react/no-unsafe-spread-props

	<components.Option {...props}>

		<ColorBox color={children as string} /> {children}

	</components.Option>

);



/**

 * NOTE: this is not declared inline with the Select

 * If you declare inline you'll have issues with refs

 */

const CustomValueOption = ({ children, ...props }: SingleValueProps<Option, false>) => (

	// eslint-disable-next-line @repo/internal/react/no-unsafe-spread-props

	<components.SingleValue {...props}>

		<ColorBox color={children as string} /> {children}

	</components.SingleValue>

);



const FormCustomSelectFieldExample = () => {

	return (

		<div

			style={{

				// eslint-disable-next-line @atlaskit/ui-styling-standard/enforce-style-prop -- Ignored via go/DSP-18766

				display: 'flex',

				// eslint-disable-next-line @atlaskit/ui-styling-standard/enforce-style-prop -- Ignored via go/DSP-18766

				width: '400px',

				// eslint-disable-next-line @atlaskit/ui-styling-standard/enforce-style-prop -- Ignored via go/DSP-18766

				margin: '0 auto',

				// eslint-disable-next-line @atlaskit/ui-styling-standard/enforce-style-prop -- Ignored via go/DSP-18766

				flexDirection: 'column',

			}}

		>

			<Form<Category>

				onSubmit={(data) => {

					console.log('form data', data);

					return Promise.resolve(validateOnSubmit(data));

				}}

			>

				{({ formProps }) => (

					<form {...formProps}>

						<Field<ValueType<Option>> name="colors" label="Select a color">

							{({ fieldProps: { id, ...rest }, error }) => (

								<Fragment>

									<Select<Option>

										inputId={id}

										components={{

											Option: CustomColorOption,

											SingleValue: CustomValueOption,

										}}

										{...rest}

										options={colors}

										isClearable

										clearControlLabel="Clear color"

									/>

									{error && <ErrorMessage>{error}</ErrorMessage>}

								</Fragment>

							)}

						</Field>

						<Field<ValueType<Option, true>>

							name="icecream"

							label="Select a flavor"

							defaultValue={[]}

						>

							{({ fieldProps: { id, ...rest }, error }) => (

								<Fragment>

									<Select inputId={id} {...rest} options={flavors} isMulti />

									{error && <ErrorMessage>{error}</ErrorMessage>}

								</Fragment>

							)}

						</Field>

						<FormFooter>

							<Button type="submit" appearance="primary">

								Submit

							</Button>

						</FormFooter>

					</form>

				)}

			</Form>

		</div>

	);

};



export default FormCustomSelectFieldExample;
```

### Other components

You can also use form with other components, such as datetime picker, modal, and select. 

```jsx
import React, { Fragment } from 'react';



import Button from '@atlaskit/button/new';

import { DatePicker, DateTimePicker } from '@atlaskit/datetime-picker';

import Form, { ErrorMessage, Field, FormFooter } from '@atlaskit/form';



interface FormData {

	[key: string]: string;

	DOB: string;

	preference: string;

}



const validateOnSubmit = (data: FormData) => {

	let errors;

	errors = requiredValidator(data, 'DOB', errors);

	errors = requiredValidator(data, 'preference', errors);

	return errors;

};



const requiredValidator = (data: FormData, key: string, errors?: Record<string, string>) => {

	if (!data[key]) {

		return {

			...errors,

			[key]: `Please select a date to continue.`,

		};

	}



	return errors;

};



const FormDateTimePickerExample = () => {

	return (

		<div

			style={{

				// eslint-disable-next-line @atlaskit/ui-styling-standard/enforce-style-prop -- Ignored via go/DSP-18766

				display: 'flex',

				// eslint-disable-next-line @atlaskit/ui-styling-standard/enforce-style-prop -- Ignored via go/DSP-18766

				width: '400px',

				// eslint-disable-next-line @atlaskit/ui-styling-standard/enforce-style-prop -- Ignored via go/DSP-18766

				margin: '0 auto',

				// eslint-disable-next-line @atlaskit/ui-styling-standard/enforce-style-prop -- Ignored via go/DSP-18766

				flexDirection: 'column',

			}}

		>

			<Form<FormData>

				onSubmit={(data) => {

					console.log('form data', data);

					return Promise.resolve(validateOnSubmit(data));

				}}

			>

				{({ formProps }) => (

					<form {...formProps}>

						<Field name="DOB" label="Date of Birth" defaultValue="" isRequired>

							{({ fieldProps: { id, ...rest }, error }) => (

								<Fragment>

									<DatePicker shouldShowCalendarButton {...rest} id={id} />

									{error && <ErrorMessage>Please select a date of birth.</ErrorMessage>}

								</Fragment>

							)}

						</Field>

						<Field

							name="preference"

							label="Preferred appointment date & time"

							defaultValue=""

							isRequired

						>

							{({ fieldProps: { id, ...rest }, error }) => {

								const validationState = error ? 'error' : 'none';

								return (

									<Fragment>

										<DateTimePicker

											{...rest}

											datePickerProps={{

												shouldShowCalendarButton: true,

												selectProps: {

													// @ts-ignore - https://product-fabric.atlassian.net/browse/DSP-21000

													validationState,

												},

												label: 'Date, Preferred appointment date & time',

												id: id,

											}}

											timePickerProps={{

												selectProps: {

													// @ts-ignore - https://product-fabric.atlassian.net/browse/DSP-21000

													validationState,

												},

												label: 'Time, Preferred appointment date & time',

											}}

										/>

										{error && (

											<ErrorMessage>

												{`Please select preferred appointment date & time.`}

											</ErrorMessage>

										)}

									</Fragment>

								);

							}}

						</Field>

						<FormFooter>

							<Button type="submit" appearance="primary">

								Submit

							</Button>

						</FormFooter>

					</form>

				)}

			</Form>

		</div>

	);

};



export default FormDateTimePickerExample;
```

```jsx
import React, { useState } from 'react';



import Button from '@atlaskit/button/new';

import { Checkbox } from '@atlaskit/checkbox';

import Form, { CheckboxField, Field } from '@atlaskit/form';

import ModalDialog, {

	ModalBody,

	ModalFooter,

	ModalHeader,

	ModalTitle,

	ModalTransition,

} from '@atlaskit/modal-dialog';

import { RadioGroup } from '@atlaskit/radio';

import Textfield from '@atlaskit/textfield';



const FormModalDialogExample = () => {

	const [isOpen, setIsOpen] = useState(false);



	const open = () => setIsOpen(true);

	const close = () => setIsOpen(false);



	return (

		<>

			<Button onClick={open}>Open Modal</Button>



			<ModalTransition>

				{isOpen && (

					<ModalDialog onClose={close}>

						<Form

							onSubmit={(value) =>

								window.alert(`You submitted:\n${JSON.stringify(value, undefined, 2)}`)

							}

						>

							{({ formProps }) => (

								<form id="form-with-id" {...formProps}>

									<ModalHeader hasCloseButton>

										<ModalTitle>Modal dialog with form</ModalTitle>

									</ModalHeader>



									<ModalBody>

										<p>Enter some text then submit the form to see the response.</p>



										<Field label="Name" name="my-name" defaultValue="">

											{({ fieldProps }) => <Textfield {...fieldProps} />}

										</Field>



										<Field label="Email" name="my-email" defaultValue="">

											{({ fieldProps }) => (

												<Textfield

													autoComplete="off"

													placeholder="charlie@atlassian.com"

													{...fieldProps}

												/>

											)}

										</Field>



										<CheckboxField name="remember" defaultIsChecked>

											{({ fieldProps }) => (

												<Checkbox {...fieldProps} label="Always sign in on this device" />

											)}

										</CheckboxField>



										<Field name="radiogroup" label="Colors" defaultValue="">

											{({ fieldProps: { value, ...others } }) => (

												<RadioGroup

													options={[

														{ name: 'color', value: 'red', label: 'Red' },

														{ name: 'color', value: 'blue', label: 'Blue' },

														{ name: 'color', value: 'yellow', label: 'Yellow' },

													]}

													{...others}

												/>

											)}

										</Field>

									</ModalBody>

									<ModalFooter>

										<Button onClick={close} appearance="subtle">

											Cancel

										</Button>

										<Button type="submit" form="form-with-id" appearance="primary">

											Submit

										</Button>

									</ModalFooter>

								</form>

							)}

						</Form>

					</ModalDialog>

				)}

			</ModalTransition>

		</>

	);

};



export default FormModalDialogExample;
```

```jsx
import React, { Fragment } from 'react';



import Button from '@atlaskit/button/new';

import Form, { ErrorMessage, Field, FormFooter } from '@atlaskit/form';

import Select, { type ValueType as Value } from '@atlaskit/select';



interface Option {

	label: string;

	value: string;

}

interface Category {

	colors?: Value<Option>;

	icecream?: Value<Option[]>;

	suit?: Value<Option[]>;

}



const colors = [

	{ label: 'Blue', value: 'blue' },

	{ label: 'Red', value: 'red' },

	{ label: 'Purple', value: 'purple' },

	{ label: 'Black', value: 'black' },

	{ label: 'White', value: 'white' },

	{ label: 'Gray', value: 'gray' },

	{ label: 'Yellow', value: 'yellow' },

];



const flavors = [

	{ label: 'Vanilla', value: 'vanilla' },

	{ label: 'Strawberry', value: 'strawberry' },

	{ label: 'Chocolate', value: 'chocolate' },

	{ label: 'Mango', value: 'mango' },

	{ label: 'Passionfruit', value: 'passionfruit' },

	{ label: 'Hazelnut', value: 'hazelnut' },

	{ label: 'Durian', value: 'durian' },

];



const suits = [

	{ label: 'Diamonds', value: 'diamonds' },

	{ label: 'Clubs', value: 'clubs' },

	{ label: 'Hearts', value: 'hearts' },

	{ label: 'Spades', value: 'spades' },

];



const validateOnSubmit = (data: Category) => {

	let errors;

	errors = colorsValidation(data, errors);

	errors = flavorValidation(data, errors);

	return errors;

};



const colorsValidation = (data: Category, errors?: Record<string, string>) => {

	if (data.colors && !(data.colors instanceof Array)) {

		return (data.colors as Option).value === 'dog'

			? {

					...errors,

					colors: `${(data.colors as Option).value} is not a color`,

				}

			: errors;

	}

	return errors;

};



const flavorValidation = (data: Category, errors?: Record<string, string>) => {

	if (data.icecream && data.icecream.length >= 3) {

		return {

			...errors,

			icecream: `${data.icecream.length} is too many flavors, please select a maximum of 2 flavors`,

		};

	}



	return errors;

};



const FormSelectExample = () => {

	return (

		<div

			style={{

				// eslint-disable-next-line @atlaskit/ui-styling-standard/enforce-style-prop -- Ignored via go/DSP-18766

				display: 'flex',

				// eslint-disable-next-line @atlaskit/ui-styling-standard/enforce-style-prop -- Ignored via go/DSP-18766

				width: '400px',

				// eslint-disable-next-line @atlaskit/ui-styling-standard/enforce-style-prop -- Ignored via go/DSP-18766

				margin: '0 auto',

				// eslint-disable-next-line @atlaskit/ui-styling-standard/enforce-style-prop -- Ignored via go/DSP-18766

				flexDirection: 'column',

			}}

		>

			<Form<Category>

				onSubmit={(data) => {

					console.log('form data', data);

					return Promise.resolve(validateOnSubmit(data));

				}}

			>

				{({ formProps }) => (

					<form {...formProps}>

						<Field<Value<Option>> name="colors" label="Select a color" defaultValue={null}>

							{({ fieldProps: { id, ...rest }, error }) => (

								<Fragment>

									<Select<Option>

										inputId={id}

										{...rest}

										options={colors}

										isClearable

										clearControlLabel="Clear color"

									/>

									{error && <ErrorMessage>{error}</ErrorMessage>}

								</Fragment>

							)}

						</Field>

						<Field<Value<Option, true>> name="icecream" label="Select a flavor" defaultValue={[]}>

							{({ fieldProps: { id, ...rest }, error }) => (

								<Fragment>

									<Select inputId={id} {...rest} options={flavors} isMulti />

									{error && <ErrorMessage>{error}</ErrorMessage>}

								</Fragment>

							)}

						</Field>

						<Field<Value<Option, true>>

							name="suits"

							label="Select suits"

							defaultValue={suits.slice(2)}

						>

							{({ fieldProps: { id, ...rest }, error }) => (

								<Fragment>

									<Select inputId={id} {...rest} options={suits} isMulti />

									{error && <ErrorMessage>{error}</ErrorMessage>}

								</Fragment>

							)}

						</Field>

						<FormFooter>

							<Button type="submit" appearance="primary">

								Submit

							</Button>

						</FormFooter>

					</form>

				)}

			</Form>

		</div>

	);

};



export default FormSelectExample;
```

## Field

Each field is an entry in the form. Fields come with props that give more information about the field state. The state can be passed onto the inner component. When a user focuses on a field and starts changing content, the focus color becomes blue. 

```jsx
import React from 'react';



import ButtonGroup from '@atlaskit/button/button-group';

import Button from '@atlaskit/button/new';

import Form, { Field, FormFooter } from '@atlaskit/form';

import TextField from '@atlaskit/textfield';



const UsernameField = () => (

	<Field aria-required={true} name="username" defaultValue="" label="Username" isRequired>

		{({ fieldProps, error, valid }) => <TextField {...fieldProps} />}

	</Field>

);



const FormFieldExample = () => (

	<div

		style={{

			// eslint-disable-next-line @atlaskit/ui-styling-standard/enforce-style-prop -- Ignored via go/DSP-18766

			display: 'flex',

			// eslint-disable-next-line @atlaskit/ui-styling-standard/enforce-style-prop -- Ignored via go/DSP-18766

			width: '400px',

			// eslint-disable-next-line @atlaskit/ui-styling-standard/enforce-style-prop -- Ignored via go/DSP-18766

			maxWidth: '100%',

			// eslint-disable-next-line @atlaskit/ui-styling-standard/enforce-style-prop -- Ignored via go/DSP-18766

			margin: '0 auto',

			// eslint-disable-next-line @atlaskit/ui-styling-standard/enforce-style-prop -- Ignored via go/DSP-18766

			flexDirection: 'column',

		}}

	>

		<Form<{ username: string }>

			onSubmit={(data) => {

				console.log('form data', data);

				return new Promise((resolve) => setTimeout(resolve, 2000)).then(() =>

					data.username === 'error' ? { username: 'IN_USE' } : undefined,

				);

			}}

		>

			{({ formProps, submitting }) => (

				<form {...formProps}>

					<UsernameField />

					<FormFooter>

						<ButtonGroup label="Form submit options">

							<Button appearance="subtle">Cancel</Button>

							<Button type="submit" appearance="primary" isLoading={submitting}>

								Submit

							</Button>

						</ButtonGroup>

					</FormFooter>

				</form>

			)}

		</Form>

	</div>

);



export default FormFieldExample;
```

### Checkbox field

Use a checkbox or radio component when you want to let people choose from a small number of predefined options. By default, the value of a checkbox field is true or false. Use the value prop to pass a value when the field is checked. This will return an array that contains value. 

```jsx
import React from 'react';



import Button from '@atlaskit/button/new';

import { Checkbox } from '@atlaskit/checkbox';

import Form, { CheckboxField, Field, Fieldset, FormFooter } from '@atlaskit/form';

import { RadioGroup } from '@atlaskit/radio';



const FormCheckboxExample = () => {

	return (

		<div

			style={{

				// eslint-disable-next-line @atlaskit/ui-styling-standard/enforce-style-prop -- Ignored via go/DSP-18766

				display: 'flex',

				// eslint-disable-next-line @atlaskit/ui-styling-standard/enforce-style-prop -- Ignored via go/DSP-18766

				width: '400px',

				// eslint-disable-next-line @atlaskit/ui-styling-standard/enforce-style-prop -- Ignored via go/DSP-18766

				margin: '0 auto',

				// eslint-disable-next-line @atlaskit/ui-styling-standard/enforce-style-prop -- Ignored via go/DSP-18766

				flexDirection: 'column',

			}}

		>

			<Form onSubmit={(data) => console.log(data)}>

				{({ formProps }) => (

					<form {...formProps}>

						<Fieldset legend="Products">

							<CheckboxField name="product" value="jira">

								{({ fieldProps }) => <Checkbox {...fieldProps} label="Jira" />}

							</CheckboxField>

							<CheckboxField name="product" value="confluence">

								{({ fieldProps }) => <Checkbox {...fieldProps} label="Confluence" />}

							</CheckboxField>

							<CheckboxField name="product" value="bitbucket">

								{({ fieldProps }) => <Checkbox {...fieldProps} label="Bitbucket" />}

							</CheckboxField>

						</Fieldset>



						<Field name="permission" defaultValue="" label="Permissions">

							{({ fieldProps }) => (

								<RadioGroup

									options={[

										{ name: 'permission', value: 'user', label: 'End user' },

										{

											name: 'permission',

											value: 'project-admin',

											label: 'Project admin',

										},

										{

											name: 'permission',

											value: 'admin',

											label: 'Admin',

										},

									]}

									{...fieldProps}

								/>

							)}

						</Field>



						<CheckboxField name="remember" defaultIsChecked>

							{({ fieldProps }) => <Checkbox {...fieldProps} label="Remember me" />}

						</CheckboxField>



						<FormFooter>

							<Button type="submit" appearance="primary">

								Submit

							</Button>

						</FormFooter>

					</form>

				)}

			</Form>

		</div>

	);

};



export default FormCheckboxExample;
```

### Fieldset

Fieldset groups related fields under the same name or heading. Use legend to assign a caption to the fieldset – this improves accessibility for when the fieldset is rendered non-visually for screen readers. 

```jsx
import React from 'react';



import { Checkbox } from '@atlaskit/checkbox';

import Form, { CheckboxField, Fieldset } from '@atlaskit/form';

import { Box } from '@atlaskit/primitives/compiled';



const FormFieldsetExample = () => (

	<Box>

		<Form onSubmit={(data) => console.log(data)}>

			{({ formProps }) => (

				<form {...formProps}>

					<Fieldset legend="Products">

						<CheckboxField name="product" value="jira">

							{({ fieldProps }) => <Checkbox {...fieldProps} label="Jira" />}

						</CheckboxField>

						<CheckboxField name="product" value="confluence">

							{({ fieldProps }) => <Checkbox {...fieldProps} label="Confluence" />}

						</CheckboxField>

						<CheckboxField name="product" value="bitbucket">

							{({ fieldProps }) => <Checkbox {...fieldProps} label="Bitbucket" />}

						</CheckboxField>

					</Fieldset>

					<Fieldset legend="Teams">

						<CheckboxField name="teams" value="jwm">

							{({ fieldProps }) => <Checkbox {...fieldProps} label="Jira" />}

						</CheckboxField>

						<CheckboxField name="teams" value="design-system">

							{({ fieldProps }) => <Checkbox {...fieldProps} label="Design System" />}

						</CheckboxField>

						<CheckboxField name="teams" value="forge">

							{({ fieldProps }) => <Checkbox {...fieldProps} label="Forge" />}

						</CheckboxField>

					</Fieldset>

				</form>

			)}

		</Form>

	</Box>

);



export default FormFieldsetExample;
```

### Range field

Use a range slider when you want people to select from a predefined numeric range. This component supports validation and required fields through the isInvalid and isRequired props respectively. 

```jsx
import React from 'react';



import Button from '@atlaskit/button/new';

import Form, { FormFooter, RangeField } from '@atlaskit/form';

import { Box } from '@atlaskit/primitives/compiled';

import Range from '@atlaskit/range';



const FormRangeFieldExample = () => {

	return (

		<Box>

			<Form onSubmit={(data) => console.log(data)}>

				{({ formProps }) => (

					<form {...formProps}>

						<RangeField name="threshold" defaultValue={50} label="Threshold">

							{({ fieldProps }) => <Range {...fieldProps} min={0} max={70} />}

						</RangeField>



						<FormFooter>

							<Button type="submit" appearance="primary">

								Submit

							</Button>

						</FormFooter>

					</form>

				)}

			</Form>

		</Box>

	);

};



export default FormRangeFieldExample;
```

## Layout

### Form header

Use a form header to describe the contents of the form. This is the title and description of the form. If your form contains required fields, the form header is also where you should include a legend for sighted users to know that * indicates a required field. 

### Form section

Use a form section to group related information together, so that longer forms are easier to understand. There can be multiple form sections in one form. 

### Form footer

Use a form footer to set the content at the end of the form. This is used for a button that submits the form. Content should be left-aligned in single-page forms, flags, cards, and section messages with the primary button on the left. See the button positioning for more details. This is positioned after the last field in the form. It can also be fixed to the bottom of viewport for longer forms. 

## Create a new repository

Required fields are marked with an asterisk * 

```jsx
import React from 'react';



import ButtonGroup from '@atlaskit/button/button-group';

import Button from '@atlaskit/button/new';

import { Checkbox } from '@atlaskit/checkbox';

import Form, { Field, FormFooter, FormHeader, FormSection, RequiredAsterisk } from '@atlaskit/form';

import { RadioGroup } from '@atlaskit/radio';

import Select, {

	components,

	type InputProps,

	type OptionType,

	type ValueType,

} from '@atlaskit/select';

import Textfield from '@atlaskit/textfield';



const RequiredInput = (props: InputProps<OptionType, false>) => {

	const newProps = {

		...props,

		'aria-required': true,

	};

	return <components.Input {...newProps} />;

};



const FormLayoutExample = () => {

	return (

		<div

			style={{

				// eslint-disable-next-line @atlaskit/ui-styling-standard/enforce-style-prop -- Ignored via go/DSP-18766

				display: 'flex',

				// eslint-disable-next-line @atlaskit/ui-styling-standard/enforce-style-prop -- Ignored via go/DSP-18766

				width: '400px',

				// eslint-disable-next-line @atlaskit/ui-styling-standard/enforce-style-prop -- Ignored via go/DSP-18766

				margin: '0 auto',

				// eslint-disable-next-line @atlaskit/ui-styling-standard/enforce-style-prop -- Ignored via go/DSP-18766

				minHeight: '60vh',

				// eslint-disable-next-line @atlaskit/ui-styling-standard/enforce-style-prop -- Ignored via go/DSP-18766

				flexDirection: 'column',

			}}

		>

			<Form onSubmit={console.log}>

				{({ formProps }) => (

					<form

						{...formProps}

						action="//httpbin.org/get"

						method="GET"

						target="submitFrame"

						name="create-repo"

					>

						<FormHeader title="Create a new repository">

							<p aria-hidden="true">

								Required fields are marked with an asterisk <RequiredAsterisk />

							</p>

						</FormHeader>



						<FormSection>

							<Field<ValueType<OptionType>>

								label="Owner"

								name="owner"

								id="owner"

								defaultValue={{

									label: 'Atlassian',

									value: 'atlassian',

								}}

							>

								{({ fieldProps: { id, ...rest } }) => (

									<Select

										id={`${id}-select`}

										isSearchable={false}

										options={[

											{ label: 'Atlassian', value: 'atlassian' },

											{ label: 'Sean Curtis', value: 'scurtis' },

											{ label: 'Mike Gardiner', value: 'mg' },

											{ label: 'Charles Lee', value: 'clee' },

										]}

										{...rest}

									/>

								)}

							</Field>



							<Field<ValueType<OptionType>>

								aria-required={true}

								name="project"

								id="project"

								label="Project"

								isRequired

							>

								{({ fieldProps: { id, ...rest } }) => (

									<Select

										components={{ Input: RequiredInput }} // Needed to explicitly set required on the Select

										id={`${id}-select`}

										options={[

											{ label: 'Atlaskit', value: 'atlaskit' },

											{ label: 'Bitbucket', value: 'bitbucket' },

											{ label: 'Confluence', value: 'confluence' },

											{ label: 'Jira', value: 'jira' },

										]}

										placeholder="Choose a project&hellip;"

										{...rest}

									/>

								)}

							</Field>



							<Field name="repo-name" label="Repository name" defaultValue="">

								{({ fieldProps }) => <Textfield {...fieldProps} />}

							</Field>



							<Field name="access-level" label="Access level">

								{({ fieldProps: { value, ...others } }) => (

									<Checkbox label="This is a private repository" isChecked={!!value} {...others} />

								)}

							</Field>

							<Field name="color" label="Pick a color">

								{({ fieldProps: { value, ...others } }) => (

									<RadioGroup

										options={[

											{ name: 'color', value: 'red', label: 'Red' },

											{

												name: 'color',

												value: 'blue',

												label: 'Blue',

											},

											{ name: 'color', value: 'yellow', label: 'Yellow' },

											{ name: 'color', value: 'green', label: 'Green' },

										]}

										value={value}

										{...others}

									/>

								)}

							</Field>

							<Field<ValueType<OptionType>>

								name="include-readme"

								id="include-readme"

								label="Include a README?"

								defaultValue={{ label: 'No', value: 'no' }}

							>

								{({ fieldProps: { id, ...rest } }) => (

									<Select

										id={`${id}-select`}

										isSearchable={false}

										options={[

											{ label: 'No', value: 'no' },

											{

												label: 'Yes, with a template',

												value: 'yes-with-template',

											},

											{

												label: 'Yes, with a tutorial (for beginners)',

												value: 'yes-with-tutorial',

											},

										]}

										{...rest}

									/>

								)}

							</Field>

						</FormSection>

						<FormFooter>

							<ButtonGroup label="Form submit options">

								<Button appearance="subtle" id="create-repo-cancel">

									Cancel

								</Button>

								<Button appearance="primary" id="create-repo-button" type="submit">

									Create repository

								</Button>

							</ButtonGroup>

						</FormFooter>

					</form>

				)}

			</Form>

		</div>

	);

};



export default FormLayoutExample;
```

## Validation

Use validation and error messages to indicate when a form submission fails or requires more information. Keep helper text as short as possible. For complex information, provide a link to more information in a new browser tab. Use the messaging guidelines for more help. When validating text fields in real-time, the message icons will switch depending on the message type. For example, the helper text turns into an error message when the user input doesn't fit the criteria. These error and warning messages disappear when the criteria is met. To ensure error messages are rendered through assistive technologies, like a screen reader, use MessageWrapper to wrap error messages. This must be in the DOM at the time the form is rendered. 

### Field-level validation

Validate a field’s value using the validate prop. This accepts a function that receives the current field value and is called whenever a field value changes. Return an error when it is invalid. Otherwise, return undefined. 

## Log In

Required fields are marked with an asterisk * 

```jsx
import React, { Fragment, useEffect, useState } from 'react';



import Button from '@atlaskit/button/new';

import { cssMap } from '@atlaskit/css';

import Form, {

	ErrorMessage,

	Field,

	FormFooter,

	FormHeader,

	MessageWrapper,

	RequiredAsterisk,

	ValidMessage,

} from '@atlaskit/form';

import { Box, Text } from '@atlaskit/primitives/compiled';

import Select, { type ValueType } from '@atlaskit/select';

import TextField from '@atlaskit/textfield';



interface Option {

	label: string;

	value: string;

}



const colors = [

	{ label: 'blue', value: 'blue' },

	{ label: 'red', value: 'red' },

	{ label: 'purple', value: 'purple' },

	{ label: 'black', value: 'black' },

	{ label: 'white', value: 'white' },

	{ label: 'gray', value: 'gray' },

	{ label: 'yellow', value: 'yellow' },

	{ label: 'orange', value: 'orange' },

	{ label: 'teal', value: 'teal' },

];



const userNameData = ['jsmith', 'mchan'];



const errorMessages = {

	shortUsername: 'Please enter a username longer than 4 characters',

	validUsername: 'Nice one, this username is available',

	usernameInUse: 'This username is already taken, try entering another one',

	selectError: 'Please select a color',

};



const formContainerStyle = cssMap({

	root: {

		display: 'flex',

		width: '400px',

		maxWidth: '100%',

		margin: '0 auto',

		flexDirection: 'column',

	},

});



const { shortUsername, validUsername, usernameInUse, selectError } = errorMessages;



const checkUserName = (value: string) => {

	return userNameData.includes(value);

};



let isUsernameUsed: boolean = false;



export default function FieldLevelValidationExample() {

	const [fieldValue, setFieldValue] = useState('');

	const [fieldHasError, setFieldHasError] = useState(false);

	const [selectHasError, setSelectHasError] = useState(false);

	const [selectValue, setSelectValue] = useState<ValueType<Option>>();

	const [errorMessageText, setErrorMessageText] = useState('');

	const [messageId, setMessageId] = useState('');



	const handleSubmit = (formState: { command: string }) => {

		console.log('form state', formState);

	};



	const handleBlurEvent = () => {

		isUsernameUsed = checkUserName(fieldValue);

		if (fieldValue.length >= 5 && !isUsernameUsed) {

			setFieldHasError(false);

			setErrorMessageText('IS_VALID');

		} else {

			setFieldHasError(true);

			if (fieldValue.length <= 5) {

				setErrorMessageText('TOO_SHORT');

			} else if (isUsernameUsed) {

				setErrorMessageText('IN_USE');

			}

		}

	};



	const handleSelectBlurEvent = () => {

		selectValue ? setSelectHasError(false) : setSelectHasError(true);

	};



	useEffect(() => {

		switch (errorMessageText) {

			case 'IS_VALID':

				setMessageId('-valid');

				break;

			case 'TOO_SHORT':

			case 'IN_USE':

				setMessageId('-error');

				break;

			default:

				setMessageId('-error');

		}

	}, [errorMessageText]);



	return (

		<Box xcss={formContainerStyle.root}>

			<Form onSubmit={handleSubmit}>

				{({ formProps }) => (

					<form {...formProps}>

						<FormHeader title="Log In">

							<Text as="p" aria-hidden={true}>

								Required fields are marked with an asterisk <RequiredAsterisk />

							</Text>

						</FormHeader>

						<Field

							name="username"

							label="Username"

							defaultValue=""

							isRequired

							validate={(value) => {

								if (value) {

									setFieldValue(value);

								}

							}}

						>

							{({ fieldProps: { id, ...rest } }) => {

								return (

									<Fragment>

										<TextField

											{...rest}

											aria-describedby={fieldHasError ? `${id}${messageId}` : undefined}

											isInvalid={fieldHasError}

											onBlur={handleBlurEvent}

										/>

										<MessageWrapper>

											{!fieldHasError && errorMessageText === 'IS_VALID' && (

												<ValidMessage>{validUsername}</ValidMessage>

											)}

											{fieldHasError && errorMessageText === 'TOO_SHORT' && (

												<ErrorMessage>{shortUsername}</ErrorMessage>

											)}

											{fieldHasError && errorMessageText === 'IN_USE' && (

												<ErrorMessage>{usernameInUse}</ErrorMessage>

											)}

										</MessageWrapper>

									</Fragment>

								);

							}}

						</Field>

						<Field<ValueType<Option>>

							name="colors"

							label="Select a color"

							defaultValue={null}

							isRequired

							validate={(value) => {

								setSelectValue(value);

							}}

						>

							{({ fieldProps: { id, ...rest } }) => {

								return (

									<Fragment>

										<Select<Option>

											inputId={id}

											{...rest}

											options={colors}

											isClearable

											clearControlLabel="Clear color"

											isInvalid={selectHasError}

											descriptionId={selectHasError ? `${id}-error` : undefined}

											onBlur={handleSelectBlurEvent}

										/>

										<MessageWrapper>

											{selectHasError && <ErrorMessage>{selectError}</ErrorMessage>}

										</MessageWrapper>

									</Fragment>

								);

							}}

						</Field>

						<FormFooter>

							<Button type="submit">Next</Button>

						</FormFooter>

					</form>

				)}

			</Form>

		</Box>

	);

}
```

### Asynchronous validation

If the validation requires an async check, the validation function can return a promise. Note that the promise should resolve with the error, rather than reject with the error. Use the validating status in the meta prop to help with asynchronous validation. This provides a better user experience. For example, a spinner tells the user that something is happening under the hood when validating. 

## Sign in

Required fields are marked with an asterisk * 

```jsx
import React, { Fragment } from 'react';



import ButtonGroup from '@atlaskit/button/button-group';

import Button from '@atlaskit/button/new';

import { Checkbox } from '@atlaskit/checkbox';

import Form, {

	CheckboxField,

	ErrorMessage,

	Field,

	FormFooter,

	FormHeader,

	HelperMessage,

	RequiredAsterisk,

	ValidMessage,

} from '@atlaskit/form';

import TextField from '@atlaskit/textfield';



export default () => {

	const simpleMemoize = <T, U>(fn: (arg: T) => U): ((arg: T) => U) => {

		let lastArg: T;

		let lastResult: U;

		return (arg: T): U => {

			if (arg !== lastArg) {

				lastArg = arg;

				lastResult = fn(arg);

			}

			return lastResult;

		};

	};



	const validateUsername = (value: string = '') => {

		if (value.length < 5) {

			return 'TOO_SHORT';

		}

		return undefined;

	};



	const validatePassword = simpleMemoize((value: string = '') => {

		if (value.length < 8) {

			return new Promise((resolve) => setTimeout(resolve, 300)).then(() => 'TOO_SHORT');

		}

		return undefined;

	});



	return (

		<div

			style={{

				// eslint-disable-next-line @atlaskit/ui-styling-standard/enforce-style-prop -- Ignored via go/DSP-18766

				display: 'flex',

				// eslint-disable-next-line @atlaskit/ui-styling-standard/enforce-style-prop -- Ignored via go/DSP-18766

				width: '400px',

				// eslint-disable-next-line @atlaskit/ui-styling-standard/enforce-style-prop -- Ignored via go/DSP-18766

				maxWidth: '100%',

				// eslint-disable-next-line @atlaskit/ui-styling-standard/enforce-style-prop -- Ignored via go/DSP-18766

				margin: '0 auto',

				// eslint-disable-next-line @atlaskit/ui-styling-standard/enforce-style-prop -- Ignored via go/DSP-18766

				flexDirection: 'column',

			}}

		>

			<Form<{ username: string; password: string; remember: boolean }>

				onSubmit={(data) => {

					console.log('form data', data);

					return new Promise((resolve) => setTimeout(resolve, 2000)).then(() =>

						data.username === 'error' ? { username: 'IN_USE' } : undefined,

					);

				}}

			>

				{({ formProps, submitting }) => (

					<form {...formProps}>

						<FormHeader title="Sign in">

							<p aria-hidden="true">

								Required fields are marked with an asterisk <RequiredAsterisk />

							</p>

						</FormHeader>

						<Field

							name="username"

							label="Username"

							isRequired

							defaultValue="hello"

							validate={validateUsername}

						>

							{({ fieldProps, error }) => (

								<Fragment>

									<TextField autoComplete="username" {...fieldProps} />

									{!error && (

										<HelperMessage>You can use letters, numbers, and periods.</HelperMessage>

									)}

									{error === 'TOO_SHORT' && (

										<ErrorMessage>

											Please enter a username that's longer than 4 characters.

										</ErrorMessage>

									)}

									{error === 'IN_USE' && (

										<ErrorMessage>This username is already in use, try another one.</ErrorMessage>

									)}

								</Fragment>

							)}

						</Field>

						<Field

							name="password"

							label="Password"

							defaultValue=""

							isRequired

							validate={validatePassword}

						>

							{({ fieldProps, error, valid, meta }) => (

								<Fragment>

									<TextField type="password" {...fieldProps} />

									{error === 'TOO_SHORT' && (

										<ErrorMessage>

											Please enter a password that's longer than 8 characters.

										</ErrorMessage>

									)}

									{meta.validating && meta.dirty ? (

										<HelperMessage>Checking......</HelperMessage>

									) : null}

									{!meta.validating && valid && meta.dirty ? (

										<ValidMessage>Awesome password!</ValidMessage>

									) : null}

								</Fragment>

							)}

						</Field>

						<CheckboxField name="remember" defaultIsChecked>

							{({ fieldProps }) => (

								<Checkbox {...fieldProps} label="Always sign in on this device" />

							)}

						</CheckboxField>

						<FormFooter>

							<ButtonGroup label="Form submit options">

								<Button appearance="subtle">Cancel</Button>

								<Button type="submit" appearance="primary" isLoading={submitting}>

									Sign in

								</Button>

							</ButtonGroup>

						</FormFooter>

					</form>

				)}

			</Form>

		</div>

	);

};
```

### Submission validation

On submission, the current state gets passed onto the onSubmit handler. For submission errors, the onSubmit handler should return an object. For example, if there's a problem with the password field, the object should contain the key and the error as the value. If the submission succeeds, the onSubmit handler should return undefined. The onSubmit handler can return synchronously or return a promise that resolves to the result. Note that the promise should resolve with the error, rather than reject with the error. 

## Log In

Required fields are marked with an asterisk * 

```jsx
import React, { Component, Fragment } from 'react';



import Button from '@atlaskit/button/new';

import Form, {

	ErrorMessage,

	Field,

	FormFooter,

	FormHeader,

	HelperMessage,

	RequiredAsterisk,

} from '@atlaskit/form';

import TextField from '@atlaskit/textfield';



const sleep = (ms: number) => new Promise((resolve) => setTimeout(resolve, ms));



const createUser = async (data: { username: string; email: string }) => {

	await sleep(500);

	const errors = {

		username: ['jsmith', 'mchan'].includes(data.username)

			? 'This username is already taken, try entering a different username'

			: undefined,

		email: !data.email.includes('@')

			? 'Enter your email in a valid format, like: name@example.com'

			: undefined,

	};

	if (!errors.username && !errors.email) {

		console.log(data);

	}

	return errors;

};



// eslint-disable-next-line import/no-anonymous-default-export

export default class extends Component<{}> {

	handleSubmit = (data: { username: string; email: string }) => {

		return createUser(data);

	};



	render() {

		return (

			<div

				style={{

					// eslint-disable-next-line @atlaskit/ui-styling-standard/enforce-style-prop -- Ignored via go/DSP-18766

					display: 'flex',

					// eslint-disable-next-line @atlaskit/ui-styling-standard/enforce-style-prop -- Ignored via go/DSP-18766

					width: '400px',

					// eslint-disable-next-line @atlaskit/ui-styling-standard/enforce-style-prop -- Ignored via go/DSP-18766

					maxWidth: '100%',

					// eslint-disable-next-line @atlaskit/ui-styling-standard/enforce-style-prop -- Ignored via go/DSP-18766

					margin: '0 auto',

					// eslint-disable-next-line @atlaskit/ui-styling-standard/enforce-style-prop -- Ignored via go/DSP-18766

					flexDirection: 'column',

				}}

			>

				<Form onSubmit={this.handleSubmit}>

					{({ formProps, submitting }) => (

						<form noValidate {...formProps}>

							<FormHeader title="Log In">

								<p aria-hidden="true">

									Required fields are marked with an asterisk <RequiredAsterisk />

								</p>

							</FormHeader>

							<Field

								aria-required={true}

								name="username"

								label="Username"

								defaultValue=""

								isRequired

							>

								{({ fieldProps, error }) => (

									<Fragment>

										<TextField {...fieldProps} />

										{!error && <HelperMessage>Try 'jsmith' or 'mchan'</HelperMessage>}

										{error && <ErrorMessage testId="userSubmissionError">{error}</ErrorMessage>}

									</Fragment>

								)}

							</Field>

							<Field name="email" label="Email" defaultValue="" isRequired>

								{({ fieldProps, error }) => (

									<Fragment>

										<TextField {...fieldProps} />

										{!error && <HelperMessage>Must contain @ symbol</HelperMessage>}

										{error && <ErrorMessage>{error}</ErrorMessage>}

									</Fragment>

								)}

							</Field>

							<FormFooter>

								<Button appearance="primary" type="submit" isLoading={submitting}>

									Create account

								</Button>

							</FormFooter>

						</form>

					)}

				</Form>

			</div>

		);

	}

}
```

## Form with all fields and labels

This form has every possible input, and all required field labels. 

## Form header

Required fields are marked with an asterisk * 

```jsx
import React, { Fragment } from 'react';



import ButtonGroup from '@atlaskit/button/button-group';

import Button from '@atlaskit/button/new';

import { Checkbox } from '@atlaskit/checkbox';

import { DateTimePicker } from '@atlaskit/datetime-picker';

import Form, {

	CheckboxField,

	Field,

	Fieldset,

	FormFooter,

	FormHeader,

	FormSection,

	HelperMessage,

	Label,

	RangeField,

	RequiredAsterisk,

} from '@atlaskit/form';

import { RadioGroup } from '@atlaskit/radio';

import Range from '@atlaskit/range';

import Select, { type OptionType, type ValueType } from '@atlaskit/select';

import TextArea from '@atlaskit/textarea';

import TextField from '@atlaskit/textfield';

import Toggle from '@atlaskit/toggle';



const FormAllOptionsExample = () => (

	<div

		style={{

			// eslint-disable-next-line @atlaskit/ui-styling-standard/enforce-style-prop -- Ignored via go/DSP-18766

			display: 'flex',

			// eslint-disable-next-line @atlaskit/ui-styling-standard/enforce-style-prop -- Ignored via go/DSP-18766

			width: '800px',

			// eslint-disable-next-line @atlaskit/ui-styling-standard/enforce-style-prop -- Ignored via go/DSP-18766

			maxWidth: '100%',

			// eslint-disable-next-line @atlaskit/ui-styling-standard/enforce-style-prop -- Ignored via go/DSP-18766

			margin: '0 auto',

			// eslint-disable-next-line @atlaskit/ui-styling-standard/enforce-style-prop -- Ignored via go/DSP-18766

			flexDirection: 'column',

		}}

	>

		<Form<{ username: string; password: string; remember: boolean }>

			onSubmit={(data) => {

				console.log('form data', data);

				return new Promise((resolve) => setTimeout(resolve, 2000)).then(() =>

					data.username === 'error' ? { username: 'IN_USE' } : undefined,

				);

			}}

		>

			{({ formProps, submitting }) => (

				<form {...formProps}>

					<FormHeader title="Form header">

						<p aria-hidden="true">

							Required fields are marked with an asterisk <RequiredAsterisk />

						</p>

					</FormHeader>



					<FormSection>

						<Field

							aria-required={true}

							name="textfield-name"

							label="Textfield label"

							isRequired

							defaultValue="default value"

						>

							{({ fieldProps }) => (

								<Fragment>

									<TextField autoComplete="off" {...fieldProps} />

									<HelperMessage>This is a helper message</HelperMessage>

								</Fragment>

							)}

						</Field>



						<Field label="Textarea field label" isRequired name="textarea-field-name">

							{({ fieldProps }: any) => (

								<Fragment>

									<TextArea {...fieldProps} />

								</Fragment>

							)}

						</Field>



						<Fieldset legend="Checkbox fieldset legend">

							<CheckboxField name="product" value="jira">

								{({ fieldProps }) => <Checkbox {...fieldProps} label="Jira" />}

							</CheckboxField>

							<CheckboxField name="product" value="confluence">

								{({ fieldProps }) => <Checkbox {...fieldProps} label="Confluence" />}

							</CheckboxField>

							<CheckboxField name="product" value="bitbucket">

								{({ fieldProps }) => <Checkbox {...fieldProps} label="Bitbucket" />}

							</CheckboxField>

						</Fieldset>



						<Fieldset legend="Datetime picker legend">

							{/* This label uses a legend because datetime picker has two fields in it. */}

							<Field name="datetime-picker-accessible" isRequired>

								{({ fieldProps: { id, ...rest } }) => (

									<DateTimePicker

										{...rest}

										datePickerProps={{

											shouldShowCalendarButton: true,

											label: 'Select date',

											id: id,

										}}

										timePickerProps={{

											label: 'Select time',

										}}

									/>

								)}

							</Field>

						</Fieldset>



						<RangeField name="rangefield-name" defaultValue={50} label="Range field label">

							{({ fieldProps }) => <Range {...fieldProps} min={0} max={100} />}

						</RangeField>



						<Field<ValueType<OptionType>>

							label="Select field label"

							name="select-field-name"

							id="owner"

							defaultValue={{

								label: 'Atlassian',

								value: 'atlassian',

							}}

						>

							{({ fieldProps }) => (

								<Select

									isSearchable={false}

									inputId={fieldProps.id}

									options={[

										{ label: 'Atlassian', value: 'atlassian' },

										{ label: 'Sean Curtis', value: 'scurtis' },

										{ label: 'Mike Gardiner', value: 'mg' },

										{ label: 'Charles Lee', value: 'clee' },

									]}

									{...fieldProps}

								/>

							)}

						</Field>



						<Fieldset legend="Radio group legend">

							<Field name="color-selection">

								{({ fieldProps: { value, ...rest } }) => (

									<RadioGroup

										options={[

											{ name: 'color', value: 'red', label: 'Red' },

											{

												name: 'color',

												value: 'blue',

												label: 'Blue',

											},

											{ name: 'color', value: 'yellow', label: 'Yellow' },

											{ name: 'color', value: 'green', label: 'Green' },

										]}

										value={value}

										{...rest}

									/>

								)}

							</Field>

						</Fieldset>



						<Label htmlFor="toggle-default">Toggle label</Label>

						<Toggle id="toggle-default" />

					</FormSection>



					<FormFooter>

						<ButtonGroup label="Form submit options">

							<Button appearance="subtle">Cancel</Button>

							<Button type="submit" appearance="primary" isLoading={submitting}>

								Submit

							</Button>

						</ButtonGroup>

					</FormFooter>

				</form>

			)}

		</Form>

	</div>

);



export default FormAllOptionsExample;
```

## Listening to form state with useFormState

### Form previews

A somewhat common need is to utilize the current form state to generate a preview while the user is filling their form in. This can be achieved with the useFormState hook. Do not use these values for any permanent storage or state. You should rely on form submission for the final values. 

```jsx
/**

 * @jsxRuntime classic

 * @jsx jsx

 */



import Banner from '@atlaskit/banner';

import { css, jsx } from '@atlaskit/css';

import Form, { Field, useFormState } from '@atlaskit/form';

import Select, { type ValueType as Value } from '@atlaskit/select';

import TextArea from '@atlaskit/textarea';

import { token } from '@atlaskit/tokens';



interface Option {

	label: string;

	value: 'warning' | 'error' | 'announcement';

}



const formContainerStyles = css({

	maxWidth: '400px',

	margin: '0 auto',

});



const previewStyles = css({ marginBlockStart: token('space.200') });



type BannerForm = {

	appearance: Option;

	content: string;

};



const FormPreview = () => {

	const formState = useFormState<BannerForm>({

		values: true,

		pristine: true,

		dirty: true,

	});



	return (

		// eslint-disable-next-line @atlaskit/design-system/use-primitives

		<div css={previewStyles}>

			<Banner appearance={formState?.values.appearance.value}>{formState?.values.content}</Banner>

			<pre>{JSON.stringify(formState, null, 2)}</pre>;

		</div>

	);

};



export default function StateSubscriptionExample() {

	return (

		<Form

			onSubmit={(data) => {

				console.log('form data', data);

			}}

		>

			{({ formProps }) => (

				<form {...formProps}>

					<div css={formContainerStyles}>

						<Field<string, HTMLTextAreaElement>

							name="content"

							defaultValue=" "

							label="Banner content"

						>

							{({ fieldProps }) => <TextArea {...fieldProps} />}

						</Field>



						<Field<Value<Option>>

							name="appearance"

							label="Select banner appearance"

							defaultValue={{ label: 'Announcement', value: 'announcement' }}

						>

							{({ fieldProps: { id, ...rest }, error }) => (

								<Select<Option>

									inputId={id}

									{...rest}

									options={[

										{ label: 'Announcement', value: 'announcement' },

										{ label: 'Warning', value: 'warning' },

										{ label: 'Error', value: 'error' },

									]}

									isClearable

									clearControlLabel="Clear appearance"

								/>

							)}

						</Field>

					</div>

					<FormPreview />

				</form>

			)}

		</Form>

	);

}
```

### Conditional fields

You can include conditional fields in your form by checking the form state with useFormState. 

```jsx
import React from 'react';



import { cssMap } from '@atlaskit/css';

import Form, { Field, useFormState } from '@atlaskit/form';

import { Box } from '@atlaskit/primitives/compiled';

import { RadioGroup } from '@atlaskit/radio';

import { type OptionsPropType } from '@atlaskit/radio/types';

import TextField from '@atlaskit/textfield';



const formContainerStyles = cssMap({

	root: {

		maxWidth: '400px',

		margin: '0 auto',

	},

});



const radioItems: OptionsPropType = [

	{ name: 'existingAccount', value: 'yes', label: 'Yes' },

	{ name: 'existingAccount', value: 'no', label: 'No' },

];



type LoginOrSignUpForm = {

	existingAccount?: 'yes' | 'no';

	name?: string;

	email?: string;

	password?: string;

	confirmPassword?: string;

};



const LoginForm = () => {

	return (

		<>

			<Field name="email" label="Email" defaultValue="" isRequired>

				{({ fieldProps }) => <TextField {...fieldProps} />}

			</Field>

			<Field name="password" label="Password" defaultValue="" isRequired>

				{({ fieldProps }) => <TextField {...fieldProps} />}

			</Field>

		</>

	);

};



const SignUpForm = () => {

	return (

		<>

			<Field name="name" label="Name" defaultValue="" isRequired>

				{({ fieldProps }) => <TextField {...fieldProps} />}

			</Field>

			<Field name="email" label="Email" defaultValue="" isRequired>

				{({ fieldProps }) => <TextField {...fieldProps} />}

			</Field>

			<Field name="password" label="Password" defaultValue="" isRequired>

				{({ fieldProps }) => <TextField {...fieldProps} />}

			</Field>

			<Field name="confirmPassword" label="Confirm password" defaultValue="" isRequired>

				{({ fieldProps }) => <TextField {...fieldProps} />}

			</Field>

		</>

	);

};



const AccountLoginOrSignUpConditionalFields = () => {

	const formState = useFormState<LoginOrSignUpForm>({ values: true });

	return (

		<>

			{formState?.values.existingAccount === 'yes' && <LoginForm />}

			{formState?.values.existingAccount === 'no' && <SignUpForm />}

		</>

	);

};



export default function ConditionalFieldsExample() {

	return (

		<Box xcss={formContainerStyles.root}>

			<Form

				onSubmit={(data) => {

					console.log('form data', data);

				}}

			>

				{({ formProps }) => (

					<form {...formProps}>

						<Field

							label="Do you have an existing account?"

							name="existingAccount"

							defaultValue=""

							isRequired

						>

							{({ fieldProps }) => <RadioGroup {...fieldProps} options={radioItems} />}

						</Field>

						<AccountLoginOrSignUpConditionalFields />

					</form>

				)}

			</Form>

		</Box>

	);

}
```

---

[View Original Documentation](https://atlassian.design/components/form/examples)
