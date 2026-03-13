# Custom SVG

A custom SVG component provides a similar API to the Icon component without requiring a wrapping positional span.

---

## Default

This is a way that you can provide a similar API to the Icon component, without needing to use one of the icons in our library and without bringing along the wrapping positional span that comes with the Icon component. Some constraints to be aware of: 

```jsx
import React from 'react';



import SVG from '@atlaskit/icon/svg';

import type { SVGProps } from '@atlaskit/icon/types';

import { Box } from '@atlaskit/primitives';

import { B300, G300 } from '@atlaskit/theme/colors';



const CustomSVGExample = (props: SVGProps) => {

	const { primaryColor, size, label } = props;

	return (

		<SVG primaryColor={primaryColor} size={size} label={label}>

			<path

				fill="currentColor"

				d="M24 12c0 6.627-5.373 12-12 12-6.628 0-12-5.373-12-12C0 5.372 5.372 0 12 0c6.627 0 12 5.372 12 12zM12 2.92A9.08 9.08 0 002.92 12 9.08 9.08 0 0012 21.08 9.08 9.08 0 0021.081 12 9.08 9.08 0 0012 2.92zm0 16.722A7.64 7.64 0 014.36 12 7.64 7.64 0 0112 4.36 7.64 7.64 0 0119.641 12a7.64 7.64 0 01-7.64 7.641z"

			/>

		</SVG>

	);

};



const ExampleContainer = () => (

	<Box>

		<CustomSVGExample primaryColor={B300} size="small" label="spinner" />

		<CustomSVGExample primaryColor={B300} size="medium" label="spinner" />

		<CustomSVGExample primaryColor={B300} size="large" label="spinner" />

		<CustomSVGExample primaryColor={G300} size="small" label="spinner" />

		<CustomSVGExample primaryColor={G300} size="medium" label="spinner" />

		<CustomSVGExample primaryColor={G300} size="large" label="spinner" />

	</Box>

);



export default ExampleContainer;
```

---

[View Original Documentation](https://atlassian.design/components/icon/custom-svg/examples)
