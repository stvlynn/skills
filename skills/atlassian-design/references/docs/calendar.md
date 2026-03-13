# Calendar

An interactive calendar for date selection experiences.

---

## Default

The calendar component provides a way to render dates for selection or presentation purposes. 

## December 2020

```jsx
import React from 'react';



import Calendar from '@atlaskit/calendar';



const defaultPreviouslySelected = ['2020-12-06'];

const defaultSelected = ['2020-12-08'];



export default () => (

	<Calendar

		maxDate={'2020-12-25'}

		defaultPreviouslySelected={defaultPreviouslySelected}

		defaultSelected={defaultSelected}

		defaultMonth={12}

		defaultYear={2020}

		testId={'calendar'}

	/>

);
```

## Disabled

Calendar provides a disabled prop that accepts an array of arbitrary dates to disable. Only disable dates where the reason for disabling dates is clear. For example, a calendar selection for booking appointments, where only the days that have available options are enabled. 

## December 2020

```jsx
import React from 'react';



import Calendar from '@atlaskit/calendar';



// Make sure your filter callback has a stable reference to avoid necessary re-renders,

// either by defining it outside of the render function's scope or using useState

const disabledDates = [

	'2020-12-07',

	'2020-12-08',

	'2020-12-09',

	'2020-12-16',

	'2020-12-17',

	'2020-12-18',

];



export default () => (

	<Calendar defaultMonth={12} defaultYear={2020} defaultDay={15} disabled={disabledDates} />

);
```

## Disabled ranges

To disable all dates before or after a certain date, use minDate or maxDate. These props disable all dates before or after a specific day respectively. Use a minDate and a maxDate together to create a range of days to choose from. The minimum and maximum dates are non inclusive, only the previous and next dates outside of these values will be disabled. 

## December 2020

```jsx
import React from 'react';



import Calendar from '@atlaskit/calendar';



export default () => (

	<Calendar

		defaultMonth={12}

		defaultYear={2020}

		defaultDay={15}

		minDate={'2020-12-10'}

		maxDate={'2020-12-20'}

	/>

);
```

## Disabled filters

For even more control, use the disabledDateFilter prop, which accepts a callback that can be configured to return whether a given date is disabled or not. 

## December 2020

```jsx
import React from 'react';



import { parseISO } from 'date-fns';



import Calendar from '@atlaskit/calendar';



// Make sure your filter callback has a stable reference to avoid necessary re-renders,

// either by defining it outside of the render function's scope or using useCallback

const weekendFilter = (date: string) => {

	const dayOfWeek = parseISO(date).getDay();

	return dayOfWeek === 0 || dayOfWeek === 6;

};



export default () => (

	<Calendar

		defaultMonth={12}

		defaultYear={2020}

		defaultDay={15}

		disabledDateFilter={weekendFilter}

	/>

);
```

## Localization

Use the locale prop to update the calendar language and formatting for different locales. You may also want to pair locale with the weekStartDay prop to change the day of the week the calendar starts with. 

## December 2020

```jsx
/**

 * @jsxRuntime classic

 * @jsx jsx

 */

import { useCallback, useState } from 'react';



import { css } from '@compiled/react';



import Calendar from '@atlaskit/calendar';

import type { WeekDay } from '@atlaskit/calendar/types';

import { cssMap, jsx } from '@atlaskit/css';

import { Label } from '@atlaskit/form';

import LocaleSelect, { type Locale } from '@atlaskit/locale/LocaleSelect';

import { Box } from '@atlaskit/primitives/compiled';

import Select, { type ValueType } from '@atlaskit/select';



const styles = cssMap({

	localeContainer: { maxWidth: '300px' },

});



const localeInputStyles = css({ marginBlockStart: '-0.5em' });



type WeekStartDayOption = {

	value: WeekDay;

	label: string;

};



export default () => {

	const [locale, setLocale] = useState('en-AU');

	const [weekStartDay, setWeekStartDay] = useState<WeekDay>(0);



	const handleLocaleChange = useCallback((locale: Locale) => setLocale(locale.value), []);



	const handleWeekStartDayChange = useCallback(

		(weekStartDayValue: ValueType<WeekStartDayOption>) =>

			setWeekStartDay((weekStartDayValue as WeekStartDayOption).value),

		[],

	);



	return (

		<Box>

			<Calendar

				disabled={['2020-12-04']}

				defaultPreviouslySelected={['2020-12-06']}

				defaultSelected={['2020-12-08']}

				defaultMonth={12}

				defaultYear={2020}

				locale={locale}

				weekStartDay={weekStartDay}

				testId="test"

			/>

			<Box xcss={styles.localeContainer}>

				<Label htmlFor="locale-input">Locale</Label>

				<div css={localeInputStyles}>

					<LocaleSelect id="locale-input" onLocaleChange={handleLocaleChange} />

				</div>

				<Label htmlFor="week-start-day">Start of the week</Label>

				<Select<WeekStartDayOption>

					inputId="week-start-day"

					options={[

						{ label: 'Sunday', value: 0 },

						{ label: 'Monday', value: 1 },

						{ label: 'Tuesday', value: 2 },

						{ label: 'Wednesday', value: 3 },

						{ label: 'Thursday', value: 4 },

						{ label: 'Friday', value: 5 },

						{ label: 'Saturday', value: 6 },

					]}

					placeholder="Choose start day of the week"

					onChange={handleWeekStartDayChange}

				/>

			</Box>

		</Box>

	);

};
```

---

[View Original Documentation](https://atlassian.design/components/calendar/examples)
