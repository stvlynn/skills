# Text area

A text area lets users enter long form text which spans over multiple lines.

---

## Default

The default text area. 

```jsx
import React from 'react';



import { Label } from '@atlaskit/form';

import TextArea from '@atlaskit/textarea';



export default () => (

	<>

		<Label htmlFor="area">Share your feedback</Label>

		<TextArea

			id="area"

			resize="auto"

			maxHeight="20vh"

			name="area"

			defaultValue="Add a message here"

		/>

	</>

);
```

## Form

You'll often use text areas as a form field. 

```jsx
import React, { Fragment } from 'react';



import Button from '@atlaskit/button/new';

import Form, { Field, FormFooter, HelperMessage } from '@atlaskit/form';

import TextArea from '@atlaskit/textarea';



export default function TextAreaFormExample() {

	return (

		<Form onSubmit={(formState: unknown) => console.log('form submitted', formState)}>

			{({ formProps }: any) => (

				<form {...formProps}>

					<Field label="Field label" name="example-text">

						{({ fieldProps }: any) => (

							<Fragment>

								<TextArea placeholder="Enter long form text here" {...fieldProps} />

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

This is how the text area will behave within forms. Validation displays an error message related to the restrictions of the text area. When a user selects the text area and starts typing or changing content, the focus color will change to blue. When validating text areas in real-time, message icons switch based on the message type. For example, helper text becomes an error message when the input content doesn't meet the criteria. Error and warning messages disappear when the criteria is met. Keep helper text as short as possible. For complex information, provide a link to more information in a new browser tab. For more help, use the messaging guidelines. 

```jsx
import React, { Fragment } from 'react';



import Button from '@atlaskit/button/new';

import Form, { ErrorMessage, Field, FormFooter, ValidMessage } from '@atlaskit/form';

import TextArea from '@atlaskit/textarea';



function validate(value: unknown) {

	if (value !== 'open sesame') {

		return 'INCORRECT_PHRASE';

	}

	return undefined;

}



export default function TextAreaFormValidationExample() {

	const handleSubmit = (formState: { command: string }) => {

		console.log('form state', formState);

	};



	return (

		<Form onSubmit={handleSubmit}>

			{({ formProps }) => (

				<form {...formProps} name="validation-example">

					<Field label="Description" isRequired name="command" validate={validate} defaultValue="">

						{({ fieldProps, error, meta: { valid } }: any) => (

							<Fragment>

								<TextArea {...fieldProps} />

								{valid && <ValidMessage>Your description will be added to the board.</ValidMessage>}

								{error === 'INCORRECT_PHRASE' && (

									<ErrorMessage>

										This field is required. Try entering text in this field.

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

## Resize

Use the resize prop to set whether the text area expands when the user enters text that exceeds the size of the text area. 

### Smart

Use smart for a text area that shows all user input at once. Overflow text wraps onto a new line and expands the text area. This is the default sizing option. 

### Auto

Use auto for a text area that will resize horizontally and vertically. 

### Vertical / horizontal resize

Use vertical or horizontal for a text area that will resize either vertically only or horizontally only. 

### None

Use none for a text area that does not resize and uses a scroll bar if the user enters text that exceeds the size of the text area. 

```jsx
/**

 * @jsxRuntime classic

 * @jsx jsx

 */

import { cssMap, cx, jsx } from '@compiled/react';



import { Label } from '@atlaskit/form';

import { Box } from '@atlaskit/primitives/compiled';

import TextArea from '@atlaskit/textarea';



const wrapperStyles = cssMap({

	root: {

		maxWidth: '500px',

	},

});



export default () => (

	<Box id="resize" xcss={cx(wrapperStyles.root)}>

		<Label htmlFor="resize-auto">Resize: auto</Label>

		<TextArea resize="auto" name="resize-auto" id="resize-auto" testId="autoResizeTextArea" />

		<Label htmlFor="resize-vertical">Resize: vertical</Label>

		<TextArea

			resize="vertical"

			name="resize-vertical"

			id="resize-vertical"

			testId="verticalResizeTextArea"

		/>

		<Label htmlFor="resize-horizontal">Resize: horizontal</Label>

		<TextArea

			resize="horizontal"

			name="resize-horizontal"

			id="resize-horizontal"

			testId="horizontalResizeTextArea"

		/>

		<Label htmlFor="resize-smart">Resize: smart (default)</Label>

		<TextArea name="resize-smart" id="resize-smart" testId="smartResizeTextArea" />

		<Label htmlFor="resize-none">Resize: none</Label>

		<TextArea resize="none" name="resize-none" id="resize-none" testId="noneResizeTextArea" />

	</Box>

);
```

## Appearance

### Standard

The default text area appearance. 

```jsx
import React from 'react';



import { Label } from '@atlaskit/form';

import TextArea from '@atlaskit/textarea';



export default function TextAreaAppearanceStandard() {

	return (

		<>

			<Label htmlFor="standard-appearance">Standard appearance</Label>

			<TextArea

				appearance="standard"

				id="standard-appearance"

				name="standard-appearance"

				placeholder="Enter your details here"

			/>

		</>

	);

}
```

### Subtle

A text area that's transparent until interaction or error. 

```jsx
import React from 'react';



import { Label } from '@atlaskit/form';

import TextArea from '@atlaskit/textarea';



export default function TextAreaAppearanceSubtle() {

	return (

		<>

			<Label htmlFor="appearance-subtle">Subtle appearance</Label>

			<TextArea

				appearance="subtle"

				id="appearance-subtle"

				name="appearance-subtle"

				placeholder="Enter your details here"

			/>

		</>

	);

}
```

---

[View Original Documentation](https://atlassian.design/components/textarea/examples)
