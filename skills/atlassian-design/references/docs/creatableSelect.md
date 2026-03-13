# Creatable select

Creatable select allows users to create new options.

---

Creatable select introduces the onCreateOption prop that you can use to let people create new options that are not yet available.

```jsx
import React, { Component } from 'react';



import { Label } from '@atlaskit/form';

import { CreatableSelect, type OptionType, type ValueType } from '@atlaskit/select';



const defaultOptions = [

	{ label: 'Adelaide', value: 'adelaide' },

	{ label: 'Brisbane', value: 'brisbane' },

	{ label: 'Canberra', value: 'canberra' },

	{ label: 'Darwin', value: 'darwin' },

	{ label: 'Hobart', value: 'hobart' },

	{ label: 'Melbourne', value: 'melbourne' },

	{ label: 'Perth', value: 'perth' },

	{ label: 'Sydney', value: 'sydney' },

];



const createOption = (label: string) => ({

	label,

	value: label.toLowerCase().replace(/\W/g, ''),

});



interface State {

	isLoading: boolean;

	options: Array<{ label: string; value: string }>;

	value?: ValueType<OptionType>;

}



class CreatableAdvanced extends Component<{}, State> {

	state: State = {

		isLoading: false,

		options: defaultOptions,

		value: undefined,

	};



	handleChange = (newValue: any, actionMeta: any) => {

		console.group('Value Changed');

		console.log(newValue);

		console.log(`action: ${actionMeta.action}`);

		console.groupEnd();

		this.setState({ value: newValue });

	};



	handleCreate = (inputValue: any) => {

		// We do not assume how users would like to add newly created options to the existing options list.

		// Instead we pass users through the new value in the onCreate prop

		this.setState({ isLoading: true });

		console.group('Option created');

		console.log('Wait a moment...');

		const { options } = this.state;

		const newOption = createOption(inputValue);

		console.log(newOption);

		console.groupEnd();

		this.setState({

			isLoading: false,

			options: [...options, newOption],

			value: newOption,

		});

	};



	render() {

		const { isLoading, options, value } = this.state;

		return (

			<>

				<Label htmlFor="createable-select-example">What city do you live in?</Label>

				<CreatableSelect

					inputId="createable-select-example"

					isClearable

					clearControlLabel="Clear city"

					isDisabled={isLoading}

					isLoading={isLoading}

					onChange={this.handleChange}

					onCreateOption={this.handleCreate}

					options={options}

					value={value}

				/>

			</>

		);

	}

}



export default () => <CreatableAdvanced />;
```

---

[View Original Documentation](https://atlassian.design/components/select/creatable-select/examples)
