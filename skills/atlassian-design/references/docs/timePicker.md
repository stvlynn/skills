# Time picker

A time picker allows the user to select a specific time.

---

## Default

By default, the time field is used to select a time from the select menu. The current time text is bold, underlined, and highlighted blue. Add clearControlLabel to give the clear button an aria-label, and do not place the clear button in the tab order. 

```jsx
import React from 'react';



import { TimePicker } from '@atlaskit/datetime-picker';

import { Label } from '@atlaskit/form';



const TimePickerDefaultExample = () => (

	<>

		<Label htmlFor="default-time-picker-example">Choose time</Label>

		<TimePicker clearControlLabel="Clear choose time" id="default-time-picker-example" />

	</>

);



export default TimePickerDefaultExample;
```

## Form

When using the time picker with the form component, include a field label and helper text. For more information, see the form component. 

```jsx
import React from 'react';



import Button from '@atlaskit/button/new';

import { TimePicker } from '@atlaskit/datetime-picker';

import Form, { Field, FormFooter, HelperMessage } from '@atlaskit/form';



const TimePickerFormExample = () => (

	<Form onSubmit={(formState: unknown) => console.log('form submitted', formState)}>

		{({ formProps }) => (

			<form {...formProps}>

				<Field name="time-picker" label="Scheduled run time" isRequired={false}>

					{({ fieldProps }) => (

						<>

							<TimePicker clearControlLabel="Clear scheduled run time" {...fieldProps} />

							<HelperMessage>Help or instruction text goes here</HelperMessage>

						</>

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



export default TimePickerFormExample;
```

### Required

How time picker works when the form is required. 

```jsx
import React from 'react';



import { TimePicker } from '@atlaskit/datetime-picker';

import { Field } from '@atlaskit/form';



const TimePickerRequiredExample = () => (

	<Field name="time" label="Start Time" isRequired>

		{({ fieldProps: { ...rest } }) => <TimePicker clearControlLabel="Clear start time" {...rest} />}

	</Field>

);



export default TimePickerRequiredExample;
```

### Validation

This is how time picker behaves within forms. Validation displays an error message related to the restrictions of the time picker. When a user selects the time picker area, the focus color changes to blue. When validating time pickers in real-time, message icons switch based on the message type. For example, helper text becomes an error message when the input content doesn't meet the criteria. Error and warning messages disappear when the criteria is met. Keep helper text as short as possible. For complex information, provide a link to more information in a new browser tab. Use the messaging guidelines for more help. 

```jsx
import React from 'react';



import Button from '@atlaskit/button/new';

import { TimePicker } from '@atlaskit/datetime-picker';

import Form, { ErrorMessage, Field, FormFooter, ValidMessage } from '@atlaskit/form';



const validateField = (value?: string) => {

	if (!value) {

		return 'REQUIRED';

	}

};



const TimePickerValidationExample = () => (

	<Form onSubmit={(formState) => console.log('form submitted', formState)}>

		{({ formProps }) => (

			<form {...formProps}>

				<Field

					name="datetime-picker"

					label="Scheduled run time"

					validate={validateField}

					isRequired

				>

					{({ fieldProps, error, meta: { valid } }) => (

						<>

							<TimePicker clearControlLabel="Clear scheduled run time" {...fieldProps} />

							{valid && <ValidMessage>You have entered a valid datetime</ValidMessage>}

							{error === 'REQUIRED' && <ErrorMessage>This field is required</ErrorMessage>}

						</>

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



export default TimePickerValidationExample;
```

## Internationalization

### Locale

Use locale to display times in a format which is appropriate to users. 

```jsx
import React from 'react';



import { TimePicker } from '@atlaskit/datetime-picker';

import { Label } from '@atlaskit/form';



const TimePickerLocaleExample = () => (

	<>

		<Label htmlFor="timepicker-locale-en">English locale</Label>

		<TimePicker clearControlLabel="Clear English locale" locale="en-US" id="timepicker-locale-en" />

		<br />

		<Label htmlFor="timepicker-locale-ko">Korean locale</Label>

		<TimePicker clearControlLabel="Clear Korean locale" locale="ko-KR" id="timepicker-locale-ko" />

	</>

);



export default TimePickerLocaleExample;
```

## Time formats

TimePicker supports customizing the format of times. Formats are given as strings and use the syntax specified at Modern JavaScript Date Utility Library. Where possible use locale for time formatting, instead of a custom format. Time formats should be informed by the user’s locale and the use case. 

```jsx
import React from 'react';



import { TimePicker } from '@atlaskit/datetime-picker';

import { Label } from '@atlaskit/form';



const TimePickerFormattingExample = () => (

	<>

		<Label htmlFor="timepicker-custom-format">Custom Time Format</Label>

		<TimePicker

			clearControlLabel="Clear custom time format"

			timeFormat="HH:mm"

			placeholder="13:30"

			id="timepicker-custom-format"

		/>

	</>

);



export default TimePickerFormattingExample;
```

## Time editable

This allows the time field to be edited via keyboard prompts. 

```jsx
import React from 'react';



import { TimePicker } from '@atlaskit/datetime-picker';

import { Label } from '@atlaskit/form';



export default function App() {

	return (

		<>

			<Label htmlFor="timepicker-editable-time">Editable time example</Label>

			<TimePicker

				clearControlLabel="Clear editable time example"

				timeIsEditable

				id="timepicker-editable-time"

			/>

		</>

	);

}
```

---

[View Original Documentation](https://atlassian.design/components/datetime-picker/time-picker/examples)
