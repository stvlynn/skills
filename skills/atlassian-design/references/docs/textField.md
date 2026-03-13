# Text field

A text field is an input that allows a user to write or edit text.

---

## Basic

A basic text field. If you use a text field outside of a form component, always use a label and associate the label to the field properly. 

```jsx
import React from 'react';



import { Label } from '@atlaskit/form';

import Textfield from '@atlaskit/textfield';



export default function TextFieldBasicExample() {

	return (

		<>

			<Label htmlFor="basic-textfield">Field label</Label>

			<Textfield name="basic" id="basic-textfield" />

		</>

	);

}
```

## Text field in a form component

You'll often use text fields as a form field, which must include a visible label. 

```jsx
import React, { Fragment } from 'react';



import Button from '@atlaskit/button/new';

import Form, { Field, FormFooter, HelperMessage } from '@atlaskit/form';

import Textfield from '@atlaskit/textfield';



export default function TextFieldFormExample() {

	return (

		<Form onSubmit={(formState: unknown) => console.log('form submitted', formState)}>

			{({ formProps }: any) => (

				<form {...formProps}>

					<Field label="Field label" name="example-text">

						{({ fieldProps }: any) => (

							<Fragment>

								<Textfield placeholder="Enter your details here" {...fieldProps} />

								<HelperMessage>Help or instruction text goes here</HelperMessage>

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

	);

}
```

## Validation

### Native

Validation can display a native error message related to the restrictions of the pattern attribute. Keep this text as short as possible. Use the writing guidelines for more help. For complicated information, provide a link to more information in a new browser tab. 

```jsx
import React, { Fragment } from 'react';



import Button from '@atlaskit/button/new';

import Form, { Field, FormFooter } from '@atlaskit/form';

import Textfield from '@atlaskit/textfield';



export default function TextFieldFormNativeValidationExample() {

	return (

		<Form onSubmit={(formData) => console.log('form data', formData)}>

			{({ formProps }) => (

				<form {...formProps} name="native-validation-example">

					<Field

						label="Input must contain less than 20 characters"

						name="command"

						isRequired

						defaultValue=""

					>

						{({ fieldProps }: any) => (

							<Fragment>

								<Textfield

									{...fieldProps}

									pattern=".{0,20}"

									data-testid="nativeFormValidationTest"

								/>

							</Fragment>

						)}

					</Field>

					<Field label="Input must be numeric" name="number" isRequired defaultValue="">

						{({ fieldProps }: any) => (

							<Fragment>

								<Textfield

									{...fieldProps}

									type="number"

									data-testid="nativeFormValidationTestNumber"

								/>

							</Fragment>

						)}

					</Field>

					<Field label="Input must be an email" name="email" isRequired defaultValue="">

						{({ fieldProps }: any) => (

							<Fragment>

								<Textfield

									{...fieldProps}

									type="email"

									data-testid="nativeFormValidationTestEmail"

								/>

							</Fragment>

						)}

					</Field>

					<Field label="Password must not be empty" name="password" isRequired defaultValue="">

						{({ fieldProps }: any) => (

							<Fragment>

								<Textfield

									{...fieldProps}

									type="password"

									data-testid="nativeFormValidationTestPassword"

								/>

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

	);

}
```

### Custom

```jsx
import React, { Fragment, useState } from 'react';



import Button from '@atlaskit/button/new';

import Form, { ErrorMessage, Field, FormFooter, ValidMessage } from '@atlaskit/form';

import { Box } from '@atlaskit/primitives/compiled';

import Textfield from '@atlaskit/textfield';



export default function FormValidationExample() {

	const [fieldValue, setFieldValue] = useState<string | undefined>('');

	const [fieldHasError, setFieldHasError] = useState(false);

	const [isFieldNotFocused, setIsFieldNotFocused] = useState(false);



	function validate(value: string | undefined) {

		setFieldValue(value);

		if (value === 'regular user') {

			setFieldHasError(false);

		} else {

			return 'INCORRECT_PHRASE';

		}

		return undefined;

	}



	const handleSubmit = (formState: { command: string }) => {

		console.log('form state', formState);

	};



	const handleBlurEvent = () => {

		setIsFieldNotFocused(true);

		if (fieldValue !== 'regular user') {

			setFieldHasError(true);

		}

	};



	const handleFocusEvent = () => {

		setIsFieldNotFocused(false);

	};



	type Obj = { [key: string]: string };

	const errorAttributes: Obj = {};



	if (isFieldNotFocused) {

		errorAttributes['aria-relevant'] = 'all';

		errorAttributes['aria-atomic'] = 'false';

	}



	const generateErrorMessage = () => {

		if (isFieldNotFocused) {

			return <Box as="span">Incorrect, try &lsquo;regular user&rsquo;</Box>;

		} else if (!isFieldNotFocused) {

			return <p>Incorrect, try &lsquo;regular user&rsquo;</p>;

		}

	};



	return (

		<Form onSubmit={handleSubmit}>

			{({ formProps }) => (

				<form {...formProps} name="validation-example">

					<Field

						label="Validates entering existing role"

						isRequired

						name="command"

						validate={validate}

						defaultValue=""

					>

						{({ fieldProps, meta: { valid } }: any) => (

							<Fragment>

								<Textfield

									testId="formValidationTest"

									{...fieldProps}

									onBlur={handleBlurEvent}

									onFocus={handleFocusEvent}

								/>

								{valid && <ValidMessage>Your role is valid</ValidMessage>}

								{fieldHasError && (

									<ErrorMessage>

										<Box aria-live="polite" {...errorAttributes}>

											{generateErrorMessage()}

										</Box>

									</ErrorMessage>

								)}

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

	);

}
```

## Max characters

Text fields can be set with a maximum character limit for constraining the amount of content that can be entered. Inline validation can also be set to alert the user and clarify the request. 

```jsx
import React, { Fragment } from 'react';



import Button from '@atlaskit/button/new';

import Form, { Field, FormFooter, HelperMessage } from '@atlaskit/form';

import Textfield from '@atlaskit/textfield';



export default function TextFieldMaxValueExample() {

	return (

		<Form onSubmit={(formData) => console.log('form data', formData)}>

			{({ formProps }) => (

				<form {...formProps} name="max-length-example">

					<Field label="Example for using maxLength" name="max-length" defaultValue="">

						{({ fieldProps }: any) => (

							<Fragment>

								<Textfield {...fieldProps} maxLength={5} />

								<HelperMessage>Max length of 5</HelperMessage>

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

	);

}
```

## Appearance

### Standard

The default text field appearance. 

```jsx
import React from 'react';



import Textfield from '@atlaskit/textfield';



export default function TextFieldAppearanceStandard() {

	return <Textfield appearance="standard" label="Standard" placeholder="Enter your details here" />;

}
```

### Subtle

A text field that's transparent until interaction or error. 

```jsx
import React from 'react';



import Textfield from '@atlaskit/textfield';



export default function TextFieldAppearanceSubtle() {

	return <Textfield appearance="subtle" label="Subtle" placeholder="Enter your details here" />;

}
```

## Elements before and after input

Text fields can include non-interactive elements before and after the input. This is useful for adding elements like icons into the text field. Don’t nest interactive elements in the text field, as it will cause accessibility and focus issues. 

```jsx
import React, { Fragment } from 'react';



import Avatar from '@atlaskit/avatar';

import Form, { Field } from '@atlaskit/form';

import ErrorIcon from '@atlaskit/icon/glyph/error';

import Textfield from '@atlaskit/textfield';



export default function TextFieldElementsBeforeAndAfterExample() {

	return (

		<Form onSubmit={(formData) => console.log('form data', formData)}>

			{({ formProps }) => (

				<form {...formProps} name="elements-before-and-after-example">

					<Field label="After input" name="after-input" defaultValue="">

						{({ fieldProps }: any) => (

							<Fragment>

								<Textfield {...fieldProps} elemAfterInput={<ErrorIcon label="error" />} />

							</Fragment>

						)}

					</Field>

					<Field label="Before input" name="before-input" defaultValue="">

						{({ fieldProps }: any) => (

							<Fragment>

								<Textfield

									{...fieldProps}

									elemBeforeInput={<Avatar size="small" borderColor="transparent" />}

								/>

							</Fragment>

						)}

					</Field>

				</form>

			)}

		</Form>

	);

}
```

## Customization

Use the data attributes data-ds--text-field--container and data-ds--text-field--input to customize the style of the text field container and input element. 

```jsx
/**

 * @jsxRuntime classic

 * @jsx jsx

 */

import { css, jsx } from '@compiled/react';



import Textfield from '@atlaskit/textfield';

import { token } from '@atlaskit/tokens';



const bigFontStyles = css({

	// container style

	paddingBlockEnd: token('space.075'),

	paddingBlockStart: token('space.075'),

	paddingInlineEnd: token('space.075'),

	paddingInlineStart: token('space.075'),

	// eslint-disable-next-line @atlaskit/design-system/no-nested-styles, @atlaskit/ui-styling-standard/no-nested-selectors -- Ignored via go/DSP-18766

	'& > [data-ds--text-field--input]': {

		// input style

		fontSize: 20,

	},

});



export default function TextFieldCustomizationExample() {

	return (

		<Textfield

			aria-label="customized text field"

			// eslint-disable-next-line @atlaskit/design-system/no-unsafe-style-overrides

			css={bigFontStyles}

		/>

	);

}
```

---

[View Original Documentation](https://atlassian.design/components/textfield/examples)
