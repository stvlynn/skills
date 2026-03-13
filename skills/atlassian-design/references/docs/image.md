# Image

An image that changes in light or dark themes.

---

## Appearance

### Default

The image component works exactly like a native img element. It recognizes and accepts all img props, but future versions will have limitations to exclude unsafe props like className and css. 

```jsx
import React from 'react';



import Image from '@atlaskit/image';

import { Inline, xcss } from '@atlaskit/primitives';



import ExampleImage from '../images/Celebration.png';



const containerStyles = xcss({

	height: '100%',

});



const ImageDefaultExample = () => {

	return (

		<Inline alignBlock="center" alignInline="center" xcss={containerStyles}>

			<Image src={ExampleImage} alt="Simple example" testId="image" />

		</Inline>

	);

};



export default ImageDefaultExample;
```

### Dark mode

Use the image component to provide a dark mode image source with srcDark. When provided, srcDark will automatically display when in dark mode and src in all other cases. If a theme hasn't been explicitly selected in the product, the Image component will check for operating system preferences. 

```jsx
/**

 * @jsxRuntime classic

 * @jsx jsx

 */

import { jsx } from '@compiled/react';



import Image from '@atlaskit/image';

import { Inline, xcss } from '@atlaskit/primitives';



import Dark from '../images/SpotDark.png';

import Light from '../images/SpotLight.png';



const containerStyles = xcss({

	height: '100%',

});



const ImageThemedExample = () => {

	return (

		<Inline alignBlock="center" alignInline="center" xcss={containerStyles}>

			<Image src={Light} srcDark={Dark} alt="Theming in action" testId="image" />

		</Inline>

	);

};



export default ImageThemedExample;
```

---

[View Original Documentation](https://atlassian.design/components/image/examples)
