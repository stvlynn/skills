# Visually hidden

A utility that hides content from the screen while retaining readability by screen readers for accessibility.

---

## Default

The content will be hidden from the screen. 

```jsx
import React, { Fragment } from 'react';



import VisuallyHidden from '@atlaskit/visually-hidden';



import ToggleVisuallyHidden from './utils/toggle-visually-hidden';



const VisuallyHiddenDefaultExample = () => {

	const hiddenContent = "Can't see me!";



	return (

		<ToggleVisuallyHidden id="default-example">

			{(isVisible) => (

				<Fragment>

					There is text hidden between these brackets: [

					{isVisible ? hiddenContent : <VisuallyHidden>{hiddenContent}</VisuallyHidden>}]

				</Fragment>

			)}

		</ToggleVisuallyHidden>

	);

};



export default VisuallyHiddenDefaultExample;
```

## Similiar controls

Multiple controls with the same label such as "Read more" make it difficult for a screen reader to differentiate them. Using Visually Hidden, more descriptive labels can be added without interfering with the design for screen users. 

```jsx
import React from 'react';



import ButtonGroup from '@atlaskit/button/button-group';

import Button from '@atlaskit/button/new';

import VisuallyHidden from '@atlaskit/visually-hidden';



import ToggleVisuallyHidden from './utils/toggle-visually-hidden';



const VisuallyHiddenButtonsExample = () => {

	return (

		<ToggleVisuallyHidden id="buttons-example">

			{(isVisible) => (

				<ButtonGroup label="Buttons with hidden content">

					<Button>

						Read more

						{isVisible ? ' about horses' : <VisuallyHidden> about horses</VisuallyHidden>}

					</Button>

					<Button>

						Read more

						{isVisible ? ' about dogs' : <VisuallyHidden> about dogs</VisuallyHidden>}

					</Button>

					<Button>

						Read more

						{isVisible ? ' about cats' : <VisuallyHidden> about cats</VisuallyHidden>}

					</Button>

				</ButtonGroup>

			)}

		</ToggleVisuallyHidden>

	);

};



export default VisuallyHiddenButtonsExample;
```

---

[View Original Documentation](https://atlassian.design/components/visually-hidden/examples)
