# Select

Select allows users to make a single selection or multiple selections from a list of options.

---

## Async select

Select now supports to handle loading data from remote sources by default, please use loadOptions prop that can be given a promise or callback that will eventually resolve to its list of options instead of options. 

```jsx
import React from 'react';



import { Label } from '@atlaskit/form';

import Select, { type OptionsType } from '@atlaskit/select';



import { cities } from '../common/data';



const filterCities = (inputValue: string) =>

	cities.filter((i) => i.label.toLowerCase().includes(inputValue.toLowerCase()));



const promiseOptions = (inputValue: string) =>

	new Promise<OptionsType>((resolve) => {

		setTimeout(() => {

			resolve(filterCities(inputValue));

		}, 1000);

	});



const WithPromises = () => {

	return (

		<>

			<Label htmlFor="async-select-example">What city do you live in?</Label>

			<Select

				inputId="async-select-example"

				cacheOptions

				defaultOptions

				loadOptions={promiseOptions}

			/>

		</>

	);

};



export default () => <WithPromises />;
```

## Single select

Allows the user to select a single item from a dropdown list of options. 

```jsx
import React from 'react';



import { Label } from '@atlaskit/form';

import Select from '@atlaskit/select';



const SelectSingleExample = () => (

	<>

		<Label htmlFor="single-select-example">What city do you live in?</Label>

		<Select

			inputId="single-select-example"

			testId="react-select"

			options={[

				{ label: 'Adelaide', value: 'adelaide' },

				{ label: 'Brisbane', value: 'brisbane' },

				{ label: 'Canberra', value: 'canberra' },

				{ label: 'Darwin', value: 'darwin' },

				{ label: 'Hobart', value: 'hobart' },

				{ label: 'Melbourne', value: 'melbourne' },

				{ label: 'Perth', value: 'perth' },

				{ label: 'Sydney', value: 'sydney' },

			]}

			placeholder="Choose a city"

		/>

	</>

);



export default SelectSingleExample;
```

## Single select clearable

Setting isClearable to true lets users clear their selection using the Backspace or Delete key. 

```jsx
import React from 'react';



import { Label } from '@atlaskit/form';

import Select from '@atlaskit/select';



const SelectSingleClearable = () => (

	<>

		<Label htmlFor="single-select-example-clearable">What city do you live in?</Label>

		<Select

			inputId="single-select-example-clearable"

			testId="react-select"

			isClearable={true}

			clearControlLabel="Clear city"

			options={[

				{ label: 'Adelaide', value: 'adelaide' },

				{ label: 'Brisbane', value: 'brisbane' },

				{ label: 'Canberra', value: 'canberra' },

				{ label: 'Darwin', value: 'darwin' },

				{ label: 'Hobart', value: 'hobart' },

				{ label: 'Melbourne', value: 'melbourne' },

				{ label: 'Perth', value: 'perth' },

				{ label: 'Sydney', value: 'sydney' },

			]}

			placeholder="Choose a city"

		/>

	</>

);



export default SelectSingleClearable;
```

## Multi select

Allows the user to select multiple items from a dropdown list of options. 

```jsx
import React from 'react';



import { Label } from '@atlaskit/form';

import Select from '@atlaskit/select';



import { cities } from '../common/data';



const SelectMultiExample = () => (

	<>

		<Label htmlFor="multi-select-example">What cities have you lived in?</Label>

		<Select

			inputId="multi-select-example"

			testId="react-select"

			options={cities}

			isMulti

			isSearchable={false}

			placeholder="Choose a city"

		/>

	</>

);



export default SelectMultiExample;
```

## Grouped options

Related options can be grouped together in both a single and multi select. 

```jsx
import React from 'react';



import { Label } from '@atlaskit/form';

import Select from '@atlaskit/select';



const SelectGroupedOptionsExample = () => (

	<>

		<Label htmlFor="grouped-options-example">What city do you live in?</Label>

		<Select

			inputId="grouped-options-example"

			testId="react-select"

			options={[

				{

					label: 'NSW',

					options: [

						{ label: 'Sydney', value: 's' },

						{ label: 'Newcastle', value: 'n' },

					],

				},

				{

					label: 'QLD',

					options: [

						{ label: 'Brisbane', value: 'b' },



						{ label: 'Gold coast', value: 'g' },

					],

				},

				{

					label: 'Other',

					options: [

						{ label: 'Canberra', value: 'c' },

						{ label: 'Williamsdale', value: 'w' },

						{ label: 'Darwin', value: 'd' },

						{ label: 'Perth', value: 'p' },

					],

				},

			]}

			placeholder="Choose a city"

		/>

	</>

);



export default SelectGroupedOptionsExample;
```

## Appearance

### Default

The default select appearance. 

```jsx
import React from 'react';



import { Label } from '@atlaskit/form';

import Select from '@atlaskit/select';



export default function SelectAppearanceDefault() {

	return (

		<>

			<Label htmlFor="default-appearance-example">Favorite fruit</Label>

			<Select

				inputId="default-appearance-example"

				appearance="default"

				options={[

					{ label: 'Apple', value: 'a' },

					{ label: 'Banana', value: 'b' },

				]}

			/>

		</>

	);

}
```

### Subtle

A select that's transparent until interaction or error. 

```jsx
import React from 'react';



import { Label } from '@atlaskit/form';

import Select from '@atlaskit/select';



export default function SelectAppearanceSubtle() {

	return (

		<>

			<Label htmlFor="subtle-appearance-example">Favorite fruit</Label>

			<Select

				inputId="subtle-appearance-example"

				appearance="subtle"

				options={[

					{ label: 'Apple', value: 'a' },

					{ label: 'Banana', value: 'b' },

				]}

			/>

		</>

	);

}
```

## Customization

The following components are customizable and switchable: 

### Clear indicator

The indicator is presented to clear the values from a multi-select. The default component is a cross. The indicator will not render when: 

```jsx
/**

 * @jsxRuntime classic

 * @jsx jsx

 */

import { type CSSProperties, Fragment, type FunctionComponent } from 'react';



import { cssMap, cx, jsx } from '@compiled/react';



import { Label } from '@atlaskit/form';

import { Box } from '@atlaskit/primitives/compiled';

import Select, { type ClearIndicatorProps, type OptionType } from '@atlaskit/select';

import { token } from '@atlaskit/tokens';



import { cities } from '../common/data';



const clearIndicatorStyles = cssMap({

	default: {

		paddingInline: token('space.050'),

		color: token('color.text'),

	},

	focus: {

		color: token('color.text.brand'),

	},

});



const CustomClearText: FunctionComponent = () => <Fragment>clear all</Fragment>;



const ClearIndicator = (props: ClearIndicatorProps<OptionType, true>) => {

	const {

		children = <CustomClearText />,

		getStyles,

		innerProps: { ref, ...restInnerProps },

		isFocused,

	} = props;



	return (

		<div

			{...restInnerProps}

			ref={ref}

			// eslint-disable-next-line @atlaskit/ui-styling-standard/enforce-style-prop -- Ignored via go/DSP-18766

			style={getStyles('clearIndicator', props) as CSSProperties}

		>

			<Box xcss={cx(clearIndicatorStyles.default, isFocused && clearIndicatorStyles.focus)}>

				{children}

			</Box>

		</div>

	);

};



export default () => (

	<Fragment>

		<Label htmlFor="indicators-clear">What city do you live in?</Label>

		<Select

			inputId="indicators-clear"

			closeMenuOnSelect={false}

			components={{ ClearIndicator }}

			defaultValue={[cities[4], cities[5]]}

			isMulti

			options={cities}

		/>

	</Fragment>

);
```

### Dropdown indicator

The indicator for opening the Select is designed to indicate to users that this is a Select component. By default, it is a chevron pointed down, but in this example we have replaced it with an emoji. 

```jsx
import React from 'react';



import { Label } from '@atlaskit/form';

import EmojiIcon from '@atlaskit/icon/glyph/emoji';

import Select, { components, type DropdownIndicatorProps, type OptionType } from '@atlaskit/select';



import { cities } from '../common/data';



const DropdownIndicator = (props: DropdownIndicatorProps<OptionType, true>) => {

	return (

		<components.DropdownIndicator {...props}>

			<EmojiIcon label="Emoji" />

		</components.DropdownIndicator>

	);

};



export default () => (

	<>

		<Label htmlFor="indicators-dropdown">What city do you live in?</Label>

		<Select

			inputId="indicators-dropdown"

			closeMenuOnSelect={false}

			components={{ DropdownIndicator }}

			defaultValue={[cities[4], cities[5]]}

			isMulti

			options={cities}

		/>

	</>

);
```

### Loading indicator

Loading indicator to be displayed in the Indicators Container when isLoading is true. 

```jsx
import React from 'react';



import { Label } from '@atlaskit/form';

import Select, { type OptionType } from '@atlaskit/select';



import { cities } from '../common/data';



const filterCities = (inputValue: string) =>

	cities.filter((i) => i.label.toLowerCase().includes(inputValue.toLowerCase()));



const promiseOptions = (inputValue: string) =>

	new Promise<OptionType[]>((resolve) => {

		setTimeout(() => {

			resolve(filterCities(inputValue));

		}, 1000);

	});



export default () => {

	return (

		<>

			<Label htmlFor="indicators-loading">What city do you live in?</Label>

			<Select

				inputId="indicators-loading"

				cacheOptions

				defaultOptions

				loadOptions={promiseOptions}

			/>

		</>

	);

};
```

---

[View Original Documentation](https://atlassian.design/components/select/examples)
