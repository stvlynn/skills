# Async creatable select

Async creatable select handles loading data from remote sources and allows users to create new options.

---

Async creatable select introduces a loadOptions prop that can be given a promise or callback that will eventually resolve to its list of options. It also introduces the onCreateOption prop that you can use to let people create new options that are not yet available.

```jsx
import React, { Component } from 'react';



import { Checkbox } from '@atlaskit/checkbox';

import { Label } from '@atlaskit/form';

import { AsyncCreatableSelect as AsyncCreatable, type OptionsType } from '@atlaskit/select';



import { cities } from '../common/data';



interface State {

	allowCreateWhileLoading: boolean;

	options: OptionsType;

}



const createOption = (inputValue: string) => ({

	label: inputValue,

	value: inputValue.toLowerCase().replace(/\W/g, ''),

});



class AsyncCreatableExample extends Component<{}, State> {

	state = {

		allowCreateWhileLoading: false,

		options: cities,

	};



	loadTimeoutId?: number = undefined;



	componentWillUnmount() {

		clearTimeout(this.loadTimeoutId);

	}



	handleCreateOption = (inputValue: string) => {

		console.log('handleCreateOption here');

		this.setState({

			options: [createOption(inputValue), ...this.state.options],

		});

	};



	// you control how the options are filtered

	filterOptions = (inputValue: string) => {

		return this.state.options.filter((option) =>

			option.label.toLowerCase().includes(inputValue.toLowerCase()),

		);

	};



	// async load function using callback (promises also supported)

	loadOptions = (inputValue: string, callback: (options: OptionsType) => void) => {

		this.loadTimeoutId = window.setTimeout(() => {

			callback(this.filterOptions(inputValue));

		}, 1000);

	};



	toggleValue = ({ value }: Record<string, any>) => {

		this.setState((state) => ({ ...state, value }));

	};



	render() {

		const { allowCreateWhileLoading } = this.state;

		return (

			<>

				<Label htmlFor="async-createable-select-example">What city do you live in?</Label>

				<AsyncCreatable

					inputId="async-createable-select-example"

					loadOptions={this.loadOptions}

					allowCreateWhileLoading={allowCreateWhileLoading}

					onCreateOption={this.handleCreateOption}

					placeholder="Choose a city"

				/>

				<Checkbox

					value="allowCreateWhileLoading"

					label="Allow create while loading"

					name="allowCreateWhileLoading"

					onChange={this.toggleValue}

				/>

			</>

		);

	}

}



export default () => <AsyncCreatableExample />;
```

---

[View Original Documentation](https://atlassian.design/components/select/async-creatable-select/examples)
