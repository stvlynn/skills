# Empty state

An empty state appears when there is no data to display and describes what the user can do next.

---

## Default

The only required part of an empty state is the header. 

```jsx
import React from 'react';



import EmptyState from '@atlaskit/empty-state';



const EmptyStateDefaultExample = () => {

	return <EmptyState header="You don't have access to this issue" />;

};



export default EmptyStateDefaultExample;
```

## Custom heading level

The heading level rendered by default is heading level 4. To make sure that the empty state is accessible, headings must follow a logical order. If the empty state does not follow an h3 or h4 in the reading order, then you will need to modify the heading order to the next logical heading level. Use the headingLevel prop to set the heading level of the header element. 

## You don't have access to this issue

Make sure the issue exists in this project. If it does, ask a project admin for permission to see the project's issues. 

```jsx
import React from 'react';



import Button from '@atlaskit/button/new';

import EmptyState from '@atlaskit/empty-state';



import LockClosedImage from '../images/LockClosed.png';



const EmptyStateWithHeadingProps = () => {

	return (

		<EmptyState

			header="You don't have access to this issue"

			description="Make sure the issue exists in this project. If it does, ask a project admin for permission to see the project's issues."

			headingLevel={2}

			primaryAction={<Button appearance="primary">Request access</Button>}

			imageUrl={LockClosedImage}

		/>

	);

};



export default EmptyStateWithHeadingProps;
```

## Description

Descriptions should add useful and relevant additional information. Make sure the issue exists in this project. If it does, ask a project admin for permission to see the project's issues. 

```jsx
import React from 'react';



import EmptyState from '@atlaskit/empty-state';



const EmptyStateDescriptionExample = () => {

	return (

		<EmptyState

			header="You don't have access to this issue"

			description="Make sure the issue exists in this project. If it does, ask a project admin for permission to see the project's issues."

		/>

	);

};



export default EmptyStateDescriptionExample;
```

## Actions

### Primary

Use a primary action button to recommend the best next step that people can take. Make sure the issue exists in this project. If it does, ask a project admin for permission to see the project's issues. 

```jsx
import React from 'react';



import Button from '@atlaskit/button/new';

import EmptyState from '@atlaskit/empty-state';



const EmptyStatePrimaryActionExample = () => {

	return (

		<EmptyState

			header="You don't have access to this issue"

			description="Make sure the issue exists in this project. If it does, ask a project admin for permission to see the project's issues."

			primaryAction={<Button appearance="primary">Request access</Button>}

		/>

	);

};



export default EmptyStatePrimaryActionExample;
```

### Secondary

Use a secondary action button to recommend an alternate step that people could take. Make sure the issue exists in this project. If it does, ask a project admin for permission to see the project's issues. 

```jsx
import React from 'react';



import Button from '@atlaskit/button/new';

import EmptyState from '@atlaskit/empty-state';



const EmptyStateSecondaryActionExample = () => {

	return (

		<EmptyState

			header="You don't have access to this issue"

			description="Make sure the issue exists in this project. If it does, ask a project admin for permission to see the project's issues."

			primaryAction={<Button appearance="primary">Request access</Button>}

			secondaryAction={<Button>View permissions</Button>}

		/>

	);

};



export default EmptyStateSecondaryActionExample;
```

### Tertiary

Use tertiary action buttons to link to external resources or documentation to further explain how to resolve the empty state. Make sure the issue exists in this project. If it does, ask a project admin for permission to see the project's issues. 

```jsx
import React from 'react';



import Button, { LinkButton } from '@atlaskit/button/new';

import EmptyState from '@atlaskit/empty-state';



const EmptyStateTertiaryActionExample = () => {

	return (

		<EmptyState

			header="You don't have access to this issue"

			description="Make sure the issue exists in this project. If it does, ask a project admin for permission to see the project's issues."

			primaryAction={<Button appearance="primary">Request access</Button>}

			secondaryAction={<Button>View permissions</Button>}

			tertiaryAction={

				<LinkButton appearance="subtle" href="http://www.atlassian.com" target="_blank">

					About permissions

				</LinkButton>

			}

		/>

	);

};



export default EmptyStateTertiaryActionExample;
```

## Loading state

Use the isLoading prop to indicate a loading state. This will show a spinner next to the action buttons when true. Make sure the issue exists in this project. If it does, ask a project admin for permission to see the project's issues. 

```jsx
import React from 'react';



import Button from '@atlaskit/button/new';

import EmptyState from '@atlaskit/empty-state';



const EmptyStateLoadingExample = () => {

	return (

		<EmptyState

			header="You don't have access to this issue"

			description="Make sure the issue exists in this project. If it does, ask a project admin for permission to see the project's issues."

			primaryAction={<Button appearance="primary">Request access</Button>}

			secondaryAction={<Button>View permissions</Button>}

			isLoading={true}

		/>

	);

};



export default EmptyStateLoadingExample;
```

## Illustrations

### Image URL

You can display an image by supplying the imageUrl prop. This url will be passed directly into the src attribute of an img component. Make sure the issue exists in this project. If it does, ask a project admin for permission to see the project's issues. 

```jsx
import React from 'react';



import Button from '@atlaskit/button/new';

import EmptyState from '@atlaskit/empty-state';



import LockClosedImage from '../images/LockClosed.png';



const EmptyStateImageUrlExample = () => {

	return (

		<EmptyState

			header="You don't have access to this issue"

			description="Make sure the issue exists in this project. If it does, ask a project admin for permission to see the project's issues."

			primaryAction={<Button appearance="primary">Request access</Button>}

			imageUrl={LockClosedImage}

		/>

	);

};



export default EmptyStateImageUrlExample;
```

### Render image

An alternate approach to displaying an image is to use the renderImage prop. This render prop approach will only be used if there is no imageUrl prop supplied. Make sure the issue exists in this project. If it does, ask a project admin for permission to see the project's issues. 

```jsx
import React from 'react';



import Button from '@atlaskit/button/new';

import EmptyState from '@atlaskit/empty-state';



import ExampleImageComponent from './example-image-component';



const EmptyStateRenderImageExample = () => {

	return (

		<EmptyState

			header="You don't have access to this issue"

			description="Make sure the issue exists in this project. If it does, ask a project admin for permission to see the project's issues."

			primaryAction={<Button appearance="primary">Request access</Button>}

			renderImage={() => <ExampleImageComponent />}

		/>

	);

};



export default EmptyStateRenderImageExample;
```

### Image dimensions

Setting the imageWidth and imageHeight props can be useful to prevent your layout from reflowing when images load in. If you have used the imageUrl approach, the imageWidth and imageHeight props set the width and height attributes on the underlying img element. If you have used the renderImage prop, they will be passed in as props to the render function. If you are resizing a spot illustration to try and squeeze it into a layout, it's a good time to ask whether you should include the image at all. Make sure the issue exists in this project. If it does, ask a project admin for permission to see the project's issues. 

```jsx
import React from 'react';



import Button from '@atlaskit/button/new';

import EmptyState from '@atlaskit/empty-state';



import LockClosedImage from '../images/LockClosed.png';



const EmptyStateImageDimensionsExample = () => {

	return (

		<EmptyState

			header="You don't have access to this issue"

			description="Make sure the issue exists in this project. If it does, ask a project admin for permission to see the project's issues."

			primaryAction={<Button appearance="primary">Request access</Button>}

			imageUrl={LockClosedImage}

			imageWidth={100}

		/>

	);

};



export default EmptyStateImageDimensionsExample;
```

### Maximum image dimensions

Applying maxImageHeight and maxImageWidth works in the same way. Make sure the issue exists in this project. If it does, ask a project admin for permission to see the project's issues. 

```jsx
import React from 'react';



import Button from '@atlaskit/button/new';

import EmptyState from '@atlaskit/empty-state';



import LockClosedImage from '../images/LockClosed.png';



const EmptyStateImageMaxDimensionsExample = () => {

	return (

		<EmptyState

			header="You don't have access to this issue"

			description="Make sure the issue exists in this project. If it does, ask a project admin for permission to see the project's issues."

			primaryAction={<Button appearance="primary">Request access</Button>}

			imageUrl={LockClosedImage}

			maxImageHeight={160}

			maxImageWidth={160}

		/>

	);

};



export default EmptyStateImageMaxDimensionsExample;
```

## Width

The horizontal space that an empty state takes up can be controlled with the width prop. It can be set to either narrow or wide. 

### Narrow

Make sure the issue exists in this project. If it does, ask a project admin for permission to see the project's issues. 

```jsx
import React from 'react';



import Button from '@atlaskit/button/new';

import EmptyState from '@atlaskit/empty-state';



import LockClosedImage from '../images/LockClosed.png';



const EmptyStateNarrow = () => {

	return (

		<EmptyState

			header="You don't have access to this issue"

			description="Make sure the issue exists in this project. If it does, ask a project admin for permission to see the project's issues."

			primaryAction={<Button appearance="primary">Request access</Button>}

			imageUrl={LockClosedImage}

			width="narrow"

		/>

	);

};



export default EmptyStateNarrow;
```

### Wide

Make sure the issue exists in this project. If it does, ask a project admin for permission to see the project's issues. 

```jsx
import React from 'react';



import Button from '@atlaskit/button/new';

import EmptyState from '@atlaskit/empty-state';



import LockClosedImage from '../images/LockClosed.png';



const EmptyStateWide = () => {

	return (

		<EmptyState

			header="You don't have access to this issue"

			description="Make sure the issue exists in this project. If it does, ask a project admin for permission to see the project's issues."

			primaryAction={<Button appearance="primary">Request access</Button>}

			imageUrl={LockClosedImage}

			width="wide"

		/>

	);

};



export default EmptyStateWide;
```

---

[View Original Documentation](https://atlassian.design/components/empty-state/examples)
