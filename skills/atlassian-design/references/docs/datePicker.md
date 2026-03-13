# Date picker

A date picker allows the user to select a particular date.

---

## Default

By default, selecting the date field opens the calendar view. The current date text is bold, underlined, and highlighted blue. Add clearControlLabel to give the clear button an aria-label, and do not place the clear button in the tab order. 

```jsx
import React from 'react';



import { DatePicker } from '@atlaskit/datetime-picker';

import { Label } from '@atlaskit/form';



const DatePickerDefaultExample = () => (

	<>

		<Label id="date" htmlFor="default-date-picker-example">

			Choose date

		</Label>

		<DatePicker

			id="default-date-picker-example"

			clearControlLabel="Clear choose date"

			shouldShowCalendarButton

			inputLabelId="date"

			openCalendarLabel="open calendar"

		/>

	</>

);



export default DatePickerDefaultExample;
```

## Form

When using the date picker with the form component, include a field label and helper text. For more information, see the form component. 

```jsx
import React from 'react';



import Button from '@atlaskit/button/new';

import { DatePicker } from '@atlaskit/datetime-picker';

import Form, { Field, FormFooter, HelperMessage } from '@atlaskit/form';



const DatePickerFormExample = () => (

	<Form onSubmit={(formState: unknown) => console.log('form submitted', formState)}>

		{({ formProps }) => (

			<form {...formProps}>

				<Field name="datepicker-form" label="Start date" isRequired={false} defaultValue="">

					{({ fieldProps }) => (

						<>

							<DatePicker

								{...fieldProps}

								clearControlLabel="Clear start date"

								shouldShowCalendarButton

								inputLabel="Start date"

								openCalendarLabel="open calendar"

							/>

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



export default DatePickerFormExample;
```

### Required

How date picker works when the form is required. 

```jsx
import React from 'react';



import { DatePicker } from '@atlaskit/datetime-picker';

import { Field } from '@atlaskit/form';



const DatePickerRequiredExample = () => (

	<Field name="date" label="Start Date" isRequired>

		{({ fieldProps: { ...rest } }) => (

			<DatePicker shouldShowCalendarButton clearControlLabel="Clear start date" {...rest} />

		)}

	</Field>

);



export default DatePickerRequiredExample;
```

### Validation

This is how date picker behaves within forms. Validation displays an error message related to the restrictions of the date picker. When a user selects the date picker area, the focus color changes to blue. When validating date pickers in real-time, message icons switch based on the message type. For example, helper text becomes an error message when the input content doesn't meet the criteria. Error and warning messages disappear when the criteria is met. Keep helper text as short as possible. For complex information, provide a link to more information in a new browser tab. Use the messaging guidelines for more help. 

```jsx
import React from 'react';



import Button from '@atlaskit/button/new';

import { DatePicker } from '@atlaskit/datetime-picker';

import Form, { ErrorMessage, Field, FormFooter, ValidMessage } from '@atlaskit/form';



const validateField = (value?: string) => {

	if (!value) {

		return 'REQUIRED';

	}

};



const DatePickerValidationExample = () => (

	<Form onSubmit={(formState) => console.log('form submitted', formState)}>

		{({ formProps }) => (

			<form {...formProps}>

				<Field

					name="datepicker-validation"

					label="Start day"

					validate={validateField}

					isRequired

					defaultValue=""

				>

					{({ fieldProps, error, meta: { valid } }) => (

						<>

							<DatePicker

								{...fieldProps}

								clearControlLabel="Clear start day"

								shouldShowCalendarButton

								inputLabel="Start day"

								openCalendarLabel="open calendar"

							/>

							{valid && <ValidMessage>You have entered a valid date</ValidMessage>}

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



export default DatePickerValidationExample;
```

## Disabled dates

If a certain date is not a valid selection, you may disable it in the calendar shown to users. This does not restrict the dates that a user may type, so validation is necessary. 

### Specific dates

Use disabled to restrict selection of individual dates. 

```jsx
import React from 'react';



import { DatePicker } from '@atlaskit/datetime-picker';

import { Label } from '@atlaskit/form';



const disabledDates = [

	'2020-12-07',

	'2020-12-08',

	'2020-12-09',

	'2020-12-16',

	'2020-12-17',

	'2020-12-18',

];



const DatePickerDisabledExample = () => (

	<>

		<Label id="disabled" htmlFor="datepicker-disabled">

			Disabled Dates

		</Label>

		<DatePicker

			defaultValue="2020-12-15"

			disabled={disabledDates}

			id="datepicker-disabled"

			clearControlLabel="Clear disabled dates"

			shouldShowCalendarButton

			inputLabelId="disabled"

			openCalendarLabel="open calendar"

		/>

	</>

);



export default DatePickerDisabledExample;
```

### Date ranges

Use minDate to set a minimum valid date and maxDate to set a maximum valid date. These can be used to define a valid date range. 

```jsx
import React from 'react';



import { DatePicker } from '@atlaskit/datetime-picker';

import { Label } from '@atlaskit/form';



const DatePickerDisableRangeExample = () => (

	<>

		<Label id="disabled" htmlFor="datepicker-disabled-range">

			Disabled Date Range

		</Label>

		<DatePicker

			defaultValue="2020-12-15"

			minDate="2020-12-10"

			maxDate="2020-12-20"

			id="datepicker-disabled-range"

			clearControlLabel="Clear disabled date range"

			shouldShowCalendarButton

			inputLabelId="disabled"

			openCalendarLabel="open calendar"

		/>

	</>

);



export default DatePickerDisableRangeExample;
```

### Complex behavior

Use disabledDateFilter for more complicated date options, like enabling only specific days of the week to be selectable. 

```jsx
import React from 'react';



import { parseISO } from 'date-fns';



import { DatePicker } from '@atlaskit/datetime-picker';

import { Label } from '@atlaskit/form';



const weekendFilter = (date: string) => {

	const dayOfWeek = parseISO(date).getDay();

	return dayOfWeek === 0 || dayOfWeek === 6;

};



const DatePickerDisableComplexExample = () => (

	<>

		<Label id="disabled" htmlFor="datepicker-disable-complex">

			Disabled Dates (Complex)

		</Label>

		<DatePicker

			defaultValue="2020-12-15"

			disabledDateFilter={weekendFilter}

			id="datepicker-disable-complex"

			clearControlLabel="Clear disabled dates (complex)"

			shouldShowCalendarButton

			inputLabelId="disabled"

			openCalendarLabel="open calendar"

		/>

	</>

);



export default DatePickerDisableComplexExample;
```

## Internationalization

DatePicker supports internationalization through two props: 

### Locale

Use locale to tailor UI copy to local audiences. 

```jsx
import React from 'react';



import { DatePicker } from '@atlaskit/datetime-picker';

import { Label } from '@atlaskit/form';



const DatePickerLocaleExample = () => (

	<>

		<Label id="english" htmlFor="datepicker-locale-en">

			English Language Example

		</Label>

		<DatePicker

			locale={'en-US'}

			id="datepicker-locale-en"

			clearControlLabel="Clear English language example"

			shouldShowCalendarButton

			inputLabelId="english"

			openCalendarLabel="open calendar"

		/>

		<br />

		<Label id="japanese" htmlFor="datepicker-locale-jp">

			Japanese Language Example

		</Label>

		<DatePicker

			locale={'ja-JP'}

			id="datepicker-locale-jp"

			clearControlLabel="Clear Japanese language example"

			shouldShowCalendarButton

			inputLabelId="japanese"

			openCalendarLabel="open calendar"

		/>

	</>

);



export default DatePickerLocaleExample;
```

### Week start day

Use weekStartDay to adjust which day of the week is shown first in the calendar. A value of 0 corresponds to Sunday (default), 1 to Monday, and so on. 

```jsx
import React from 'react';



import { DatePicker } from '@atlaskit/datetime-picker';

import { Label } from '@atlaskit/form';



const DatePickerWeekStartDayExample = () => (

	<>

		<Label id="sunday" htmlFor="datepicker-sunday">

			Week Starting on Sunday

		</Label>

		<DatePicker

			weekStartDay={0}

			id="datepicker-sunday"

			clearControlLabel="Clear week starting on Sunday"

			shouldShowCalendarButton

			inputLabelId="sunday"

			openCalendarLabel="open calendar"

		/>

		<br />

		<Label id="monday" htmlFor="datepicker-monday">

			Week Starting on Monday

		</Label>

		<DatePicker

			weekStartDay={1}

			id="datepicker-monday"

			clearControlLabel="Clear week starting on Monday"

			shouldShowCalendarButton

			inputLabelId="monday"

			openCalendarLabel="open calendar"

		/>

	</>

);



export default DatePickerWeekStartDayExample;
```

## Date formats

You can customize the date format using the dateFormat prop. Formats are given as strings and use the syntax specified at Modern JavaScript date utility library. Where possible use locale for date formatting, instead of a custom format. Date formats should be informed by the user’s locale and the use case. 

```jsx
import React from 'react';



import { parseISO } from 'date-fns';



import { DatePicker } from '@atlaskit/datetime-picker';

import { Label } from '@atlaskit/form';



const DatePickerFormattingExample = () => (

	<>

		<Label id="custom" htmlFor="datepicker-format">

			Custom Date Format

		</Label>

		<DatePicker

			dateFormat="YYYY-MM-DD"

			placeholder="2021-06-10"

			parseInputValue={(date: string) => parseISO(date)}

			id="datepicker-format"

			clearControlLabel="Clear Custom Date Format"

			shouldShowCalendarButton

			inputLabelId="custom"

			openCalendarLabel="open calendar"

		/>

	</>

);



export default DatePickerFormattingExample;
```

---

[View Original Documentation](https://atlassian.design/components/datetime-picker/date-picker/examples)
