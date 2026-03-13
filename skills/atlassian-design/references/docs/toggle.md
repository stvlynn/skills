# Toggle

A toggle is used to view or switch between enabled or disabled states.

---

## Size

### Default

The default form of a toggle. For pages with lots of toggles, use the default size. 

```jsx
import React from 'react';



import Toggle from '@atlaskit/toggle';



import { Label } from './label';



export default function Example() {

	return (

		<>

			<Label htmlFor="toggle-default">Allow pull requests</Label>

			<Toggle id="toggle-default" />

		</>

	);

}
```

### Large

To call attention to a specific action, use a large toggle. 

```jsx
import React from 'react';



import Toggle from '@atlaskit/toggle';



import { Label } from './label';



export default function Example() {

	return (

		<>

			<Label htmlFor="toggle-large">Allow pull requests</Label>

			<Toggle id="toggle-large" size="large" />

		</>

	);

}
```

## Disabled

When a selection has already been made outside of the current context that negates the need for the toggle, you could use the disabled state. 

```jsx
import React from 'react';



import Toggle from '@atlaskit/toggle';



import { Label } from './label';



export default function Example() {

	return (

		<>

			<Label htmlFor="toggle-disabled">Allow pull requests</Label>

			<Toggle id="toggle-disabled" isDisabled defaultChecked />

		</>

	);

}
```

## Tooltips

To add an extra hint about what will happen when people interact with a toggle, use a tooltip. 

```jsx
import React, { useState } from 'react';



import Toggle from '@atlaskit/toggle';

import Tooltip from '@atlaskit/tooltip';



import { Label } from './label';



export default function Example() {

	const [isAllowed, setIsAllowed] = useState(false);



	return (

		<>

			<Label htmlFor="toggle-tooltip">Allow pull requests</Label>



			<Tooltip content={isAllowed ? 'Disable pull requests' : 'Enable pull requests'}>

				<Toggle id="toggle-tooltip" onChange={() => setIsAllowed((prev) => !prev)} />

			</Tooltip>

		</>

	);

}
```

## Checked

Set the initial checked value using defaultChecked (this is optional, by default it will be set as false if not provided). After that point, the checked value is controlled by the component. Provide an onChange handler to be notified of checked value changes. 

```jsx
import React from 'react';



import Toggle from '@atlaskit/toggle';



import { Label } from './label';



export default function Example() {

	return (

		<>

			<Label htmlFor="toggle-default-checked">Allow pull requests</Label>

			<Toggle id="toggle-default-checked" defaultChecked />

		</>

	);

}
```

## Stateless

In a stateless toggle, manage the checked state of the input by providing the isChecked prop. This requires an onChange handler to control the state value that you pass into the isChecked prop. 

```jsx
import React, { useState } from 'react';



import Toggle from '@atlaskit/toggle';



import { Label } from './label';



export default function Example() {

	const [isChecked, setIsChecked] = useState(false);



	return (

		<>

			<Label htmlFor="toggle-controlled">Allow pull requests</Label>



			<Toggle

				id="toggle-controlled"

				onChange={() => setIsChecked((prev) => !prev)}

				isChecked={isChecked}

			/>

		</>

	);

}
```

## Labeled

It's better to include a visible label with the toggle. When there isn't a visible label that you can pair toggle with, use the label prop to tell people who use assistive technology what the toggle is for. 

```jsx
import React from 'react';



import Toggle from '@atlaskit/toggle';



export default function Example() {

	return (

		<>

			<Toggle id="toggle-default" label="Allow pull request" />

		</>

	);

}
```

---

[View Original Documentation](https://atlassian.design/components/toggle/examples)
