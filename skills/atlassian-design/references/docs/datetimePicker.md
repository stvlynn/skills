# Date time picker

A date time picker allows the user to select an associated date and time.

---

## Default

By default, selecting the date field opens the calendar view. The current date text is bold, underlined, and highlighted blue. Add clearControlLabel to give the clear button an aria-label, and do not place the clear button in the tab order. The time field is used to select a time from the select menu. 

```jsx
import React from 'react';



import { DateTimePicker } from '@atlaskit/datetime-picker';

import { Label } from '@atlaskit/form';



const DateTimePickerDefaultExample = () => (

	<>

		<Label htmlFor="datetime">Appointment date and time</Label>

		<DateTimePicker

			id="datetime"

			clearControlLabel="Clear default example"

			datePickerProps={{ shouldShowCalendarButton: true, label: 'Appointment date' }}

			timePickerProps={{ label: 'Appointment time' }}

		/>

	</>

);



export default DateTimePickerDefaultExample;
```

## Form

Date time picker used with the form component includes a field label and helper text. 

```jsx
import React from 'react';



import Button from '@atlaskit/button/new';

import { DateTimePicker } from '@atlaskit/datetime-picker';

import Form, { Field, FormFooter, HelperMessage } from '@atlaskit/form';



const DateTimePickerFormExample = () => (

	<Form onSubmit={(formState: unknown) => console.log('form submitted', formState)}>

		{({ formProps }) => (

			<form {...formProps}>

				<Field name="datetime-picker" label="Scheduled run time" isRequired={false}>

					{({ fieldProps }) => (

						<>

							<DateTimePicker

								{...fieldProps}

								clearControlLabel="Clear scheduled run time"

								datePickerProps={{

									shouldShowCalendarButton: true,

									label: 'Scheduled run time, date',

								}}

								timePickerProps={{ label: 'Scheduled run time, time' }}

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



export default DateTimePickerFormExample;
```

### Required

How date time picker works when the form is required. 

```jsx
import React from 'react';



import { DateTimePicker } from '@atlaskit/datetime-picker';

import { Field } from '@atlaskit/form';



const DateTimePickerRequiredExample = () => (

	<Field name="datetime" label="Log Entry" isRequired>

		{({ fieldProps: { ...rest } }) => (

			<DateTimePicker

				{...rest}

				clearControlLabel="Clear log entry"

				datePickerProps={{ shouldShowCalendarButton: true, label: 'Log entry, date' }}

				timePickerProps={{ label: 'Log entry, time' }}

			/>

		)}

	</Field>

);



export default DateTimePickerRequiredExample;
```

### Validation

This is how date time picker behaves within forms. Validation displays an error message related to the restrictions of the date time picker. When a user selects the date time picker area, the focus color changes to blue. When validating date time pickers in real-time, message icons switch based on the message type. For example, helper text becomes an error message when the input content doesn't meet the criteria. Error and warning messages disappear when the criteria is met. Keep helper text as short as possible. For complex information, provide a link to more information in a new browser tab. Use the messaging guidelines for more help. 

```jsx
import React from 'react';



import Button from '@atlaskit/button/new';

import { DateTimePicker } from '@atlaskit/datetime-picker';

import Form, { ErrorMessage, Field, FormFooter, ValidMessage } from '@atlaskit/form';



const validateField = (value?: string) => {

	if (!value) {

		return 'REQUIRED';

	} else if (new Date(value) < new Date()) {

		return 'EXPIRED';

	}

};



const DateTimePickerFormExample = () => (

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

							<DateTimePicker

								{...fieldProps}

								clearControlLabel="Clear scheduled run time"

								datePickerProps={{

									shouldShowCalendarButton: true,

									label: 'Scheduled run time, date',

								}}

								timePickerProps={{ label: 'Scheduled run time, time' }}

							/>

							{valid && <ValidMessage>You have entered a valid datetime</ValidMessage>}

							{error === 'REQUIRED' && <ErrorMessage>This field is required</ErrorMessage>}

							{error === 'EXPIRED' && (

								<ErrorMessage>You may not enter a datetime that is in the past</ErrorMessage>

							)}

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



export default DateTimePickerFormExample;
```

## Disabled dates

If a certain date is not a valid selection, you may disable it in the calendar shown to users. This does not restrict the dates that a user may type, so validation is necessary. 

### Specific dates

Use disabled to restrict selection of individual dates. 

```jsx
import React from 'react';



import { DateTimePicker } from '@atlaskit/datetime-picker';

import { Label } from '@atlaskit/form';



const disabledDates = [

	'2020-12-07',

	'2020-12-08',

	'2020-12-09',

	'2020-12-16',

	'2020-12-17',

	'2020-12-18',

];



const DateTimePickerDisabledExample = () => (

	<>

		<Label htmlFor="datetime">Appointment date and time</Label>

		<DateTimePicker

			id="datetime"

			clearControlLabel="Clear disabled dates"

			datePickerProps={{

				disabled: disabledDates,

				shouldShowCalendarButton: true,

				label: 'Appointment date',

			}}

			defaultValue="2020-12-15"

			timePickerProps={{ label: 'Appointment time' }}

		/>

	</>

);



export default DateTimePickerDisabledExample;
```

### Date ranges

Use minDate to set a minimum valid date and maxDate to set a maximum valid date. These can be used to define a valid date range. 

```jsx
import React from 'react';



import { DateTimePicker } from '@atlaskit/datetime-picker';

import { Label } from '@atlaskit/form';



const DateTimePickerDisableRangeExample = () => (

	<>

		<Label htmlFor="datetime">Appointment date and time</Label>

		<DateTimePicker

			id="datetime"

			clearControlLabel="Clear range"

			datePickerProps={{

				minDate: '2020-12-10',

				maxDate: '2020-12-20',

				shouldShowCalendarButton: true,

				label: 'Appointment date',

			}}

			defaultValue="2020-12-15"

			timePickerProps={{

				label: 'Appointment time',

			}}

		/>

	</>

);



export default DateTimePickerDisableRangeExample;
```

### Complex behavior

Use disabledDateFilter for more complicated date options, like enabling only specific days of the week to be selectable. 

```jsx
import React from 'react';



import { parseISO } from 'date-fns';



import { DateTimePicker } from '@atlaskit/datetime-picker';

import { Label } from '@atlaskit/form';



const weekendFilter = (date: string) => {

	const dayOfWeek = parseISO(date).getDay();

	return dayOfWeek === 0 || dayOfWeek === 6;

};



const DateTimePickerDisableComplexExample = () => (

	<>

		<Label htmlFor="datetime">Appointment date and time</Label>

		<DateTimePicker

			id="datetime"

			clearControlLabel="Clear complex dates"

			defaultValue="2020-12-15"

			datePickerProps={{

				disabledDateFilter: weekendFilter,

				shouldShowCalendarButton: true,

				label: 'Appointment date',

			}}

			timePickerProps={{ label: 'Appointment time' }}

		/>

	</>

);



export default DateTimePickerDisableComplexExample;
```

## Internationalization

Date time picker supports internationalization through two props: 

### Locale

Use locale to tailor UI copy to local audiences. 

```jsx
import React from 'react';



import { DateTimePicker } from '@atlaskit/datetime-picker';

import { Label } from '@atlaskit/form';

import { Box } from '@atlaskit/primitives/compiled';



const DateTimePickerLocaleExample = () => (

	<>

		<Label htmlFor="locale-1">Date and time in US</Label>

		<DateTimePicker

			id="locale-1"

			clearControlLabel="Clear Date and time in US"

			datePickerProps={{ shouldShowCalendarButton: true, label: 'Date in US' }}

			locale={'en-US'}

			timePickerProps={{ label: 'Time in US' }}

		/>



		<Box>

			<Label htmlFor="locale-2">Date and time in Japan</Label>

			<DateTimePicker

				id="locale-2"

				clearControlLabel="Clear Date and time in Japan"

				datePickerProps={{ shouldShowCalendarButton: true, label: 'Date in Japan' }}

				locale={'ja-JP'}

				timePickerProps={{ label: 'Time in Japan' }}

			/>

		</Box>

	</>

);



export default DateTimePickerLocaleExample;
```

### Week start day

Use weekStartDay to adjust which day of the week is shown first in the calendar. A value of 0 corresponds to Sunday (default), 1 to Monday, and so on. 

```jsx
import React from 'react';



import { DateTimePicker } from '@atlaskit/datetime-picker';

import { Label } from '@atlaskit/form';

import { Box } from '@atlaskit/primitives/compiled';



const DateTimePickerWeekStartDayExample = () => (

	<>

		<Label htmlFor="datetime-1">Sunday example</Label>

		<DateTimePicker

			id="datetime-1"

			clearControlLabel="Clear Sunday example"

			datePickerProps={{

				weekStartDay: 0,

				shouldShowCalendarButton: true,

				label: 'Sunday example, date',

			}}

			timePickerProps={{ label: 'Sunday example, time' }}

		/>

		<Box>

			<Label htmlFor="datetime-2">Monday example</Label>

			<DateTimePicker

				id="datetime-2"

				clearControlLabel="Clear Monday Example"

				datePickerProps={{

					weekStartDay: 1,

					shouldShowCalendarButton: true,

					label: 'Monday example, date',

				}}

				timePickerProps={{ label: 'Monday example, time' }}

			/>

		</Box>

	</>

);



export default DateTimePickerWeekStartDayExample;
```

## Date and time formats

Date time picker supports customizing the format of dates and times. Formats are given as strings and use the syntax specified at Modern JavaScript Date Utility Library. Where possible use locale for date and time formatting, instead of a custom format. Date and time formats should be informed by the user’s locale and the use case. 

```jsx
import React from 'react';



import { parseISO } from 'date-fns';



import { DateTimePicker } from '@atlaskit/datetime-picker';

import { Label } from '@atlaskit/form';



const DateTimePickerFormattingExample = () => (

	<>

		<Label htmlFor="datetime">Appointment date and time</Label>

		<DateTimePicker

			id="datetime"

			clearControlLabel="Clear Appointment date and time"

			datePickerProps={{

				dateFormat: 'YYYY-MM-DD',

				placeholder: '2021-06-10',

				parseInputValue: (date: string) => parseISO(date),

				shouldShowCalendarButton: true,

				label: 'Appointment date',

			}}

			timePickerProps={{

				timeFormat: 'HH:mm',

				placeholder: '13:30',

				label: 'Appointment time',

			}}

		/>

	</>

);



export default DateTimePickerFormattingExample;
```

## Accessibility

If using fields with labels other than "Date" and "Time" for the date picker and time picker respectively, use datePickerProps and timePickerProps to pass the label prop. 

```jsx
import React from 'react';



import Button from '@atlaskit/button/new';

import { DateTimePicker } from '@atlaskit/datetime-picker';

import Form, { Field, FormFooter } from '@atlaskit/form';



const DateTimePickerFormAccessibleExample = () => (

	<Form onSubmit={(formState: unknown) => console.log('form submitted', formState)}>

		{({ formProps }) => (

			<form {...formProps}>

				<Field name="datetime-picker-accessible" label="Scheduled run time" isRequired>

					{({ fieldProps }) => (

						<DateTimePicker

							{...fieldProps}

							datePickerProps={{

								label: 'Scheduled run time, date',

								shouldShowCalendarButton: true,

							}}

							timePickerProps={{ label: 'Scheduled run time, time' }}

							clearControlLabel="Clear scheduled run time"

						/>

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



export default DateTimePickerFormAccessibleExample;
```

---

[View Original Documentation](https://atlassian.design/components/datetime-picker/examples)
