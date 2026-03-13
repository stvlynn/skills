# Progress tracker

A progress tracker displays the steps and progress through a journey.

---

## Default

The default version of a progress tracker that shows all the steps and states in a journey. 

```jsx
import React from 'react';



import { ProgressTracker, type Stages } from '@atlaskit/progress-tracker';



const items: Stages = [

	{

		id: 'disabled-1',

		label: 'Disabled step',

		percentageComplete: 100,

		status: 'disabled',

		href: '#',

	},

	{

		id: 'visited-1',

		label: 'Visited step',

		percentageComplete: 100,

		status: 'visited',

		href: '#',

	},

	{

		id: 'current-1',

		label: 'Current step',

		percentageComplete: 0,

		status: 'current',

		href: '#',

	},

	{

		id: 'unvisited-1',

		label: 'Unvisited step 1',

		percentageComplete: 0,

		status: 'unvisited',

		href: '#',

	},

	{

		id: 'unvisited-2',

		label: 'Unvisited step 2',

		percentageComplete: 0,

		status: 'unvisited',

		href: '#',

	},

	{

		id: 'unvisited-3',

		label: 'Unvisited step 3',

		percentageComplete: 0,

		status: 'unvisited',

		href: '#',

	},

];



export default () => <ProgressTracker items={items} />;
```

## Spacing

The margin spacing in between the steps of a progress tracker. 

### Comfortable

Progress tracker with comfortable spacing. 

```jsx
import React from 'react';



import { ProgressTracker, type Stages } from '@atlaskit/progress-tracker';



const items: Stages = [

	{

		id: 'move-issues',

		label: 'Move issues',

		percentageComplete: 100,

		status: 'disabled',

		href: '#',

	},

	{

		id: 'select-destination',

		label: 'Select destination',

		percentageComplete: 100,

		status: 'visited',

		href: '#',

	},

	{

		id: 'map-statuses',

		label: 'Map statuses',

		percentageComplete: 0,

		status: 'current',

		href: '#',

	},

	{

		id: 'data-classification',

		label: 'Data classification',

		percentageComplete: 0,

		status: 'unvisited',

		href: '#',

	},

	{

		id: 'update-fields',

		label: 'Update fields',

		percentageComplete: 0,

		status: 'unvisited',

		href: '#',

	},

	{

		id: 'confirmation',

		label: 'Confirm changes',

		percentageComplete: 0,

		status: 'unvisited',

		href: '#',

	},

];



export default () => <ProgressTracker items={items} spacing="comfortable" />;
```

### Cosy (default)

Progress tracker with default cosy spacing. 

```jsx
/**

 * @jsxRuntime classic

 * @jsx jsx

 */

import { cssMap, jsx } from '@atlaskit/css';

import { Box } from '@atlaskit/primitives/compiled';

import { ProgressTracker, type Stages } from '@atlaskit/progress-tracker';



const styles = cssMap({

	container: {

		maxWidth: '400px',

		margin: 'auto',

	},

});



const items: Stages = [

	{

		id: 'welcome',

		label: 'Welcome',

		percentageComplete: 100,

		status: 'disabled',

		href: '#',

	},

	{

		id: 'create-space',

		label: 'Create a space',

		percentageComplete: 100,

		status: 'visited',

		href: '#',

	},

	{

		id: 'upload-photo',

		label: 'Upload a photo',

		percentageComplete: 0,

		status: 'current',

		href: '#',

	},

	{

		id: 'your-details',

		label: 'Your details',

		percentageComplete: 0,

		status: 'unvisited',

		href: '#',

	},

	{

		id: 'invite-users',

		label: 'Invite users',

		percentageComplete: 0,

		status: 'unvisited',

		href: '#',

	},

	{

		id: 'confirmation',

		label: 'Confirmation',

		percentageComplete: 0,

		status: 'unvisited',

		href: '#',

	},

];



export default () => (

	<Box xcss={styles.container}>

		<ProgressTracker items={items} spacing="cosy" />

	</Box>

);
```

### Compact

Progress tracker with compact spacing. 

```jsx
/**

 * @jsxRuntime classic

 * @jsx jsx

 */

import { cssMap, jsx } from '@atlaskit/css';

import { Box } from '@atlaskit/primitives/compiled';

import { ProgressTracker, type Stages } from '@atlaskit/progress-tracker';



const styles = cssMap({

	container: {

		maxWidth: '400px',

		margin: 'auto',

	},

});



const items: Stages = [

	{

		id: 'welcome',

		label: 'Welcome',

		percentageComplete: 100,

		status: 'disabled',

		href: '#',

	},

	{

		id: 'create-account',

		label: 'Create account',

		percentageComplete: 100,

		status: 'visited',

		href: '#',

	},

	{

		id: 'details',

		label: 'Your details',

		percentageComplete: 0,

		status: 'current',

		href: '#',

	},

	{

		id: 'select-plan',

		label: 'Select a plan',

		percentageComplete: 0,

		status: 'unvisited',

		href: '#',

	},

	{

		id: 'payment-methods',

		label: 'Add payment method',

		percentageComplete: 0,

		status: 'unvisited',

		href: '#',

	},

	{

		id: 'confirmation',

		label: 'Complete purchase',

		percentageComplete: 0,

		status: 'unvisited',

		href: '#',

	},

];



export default () => (

	<Box xcss={styles.container}>

		<ProgressTracker items={items} spacing="compact" />

	</Box>

);
```

## Completed

A progress tracker that shows all steps have been completed. 

```jsx
import React from 'react';



import { ProgressTracker, type Stages } from '@atlaskit/progress-tracker';



const items: Stages = [

	{

		id: 'get-started',

		label: 'Get started',

		percentageComplete: 100,

		status: 'visited',

		href: '#',

	},

	{

		id: 'create-team',

		label: 'Create a team',

		percentageComplete: 100,

		status: 'visited',

		href: '#',

	},

	{

		id: 'invite-people',

		label: 'Invite people',

		percentageComplete: 100,

		status: 'visited',

		href: '#',

	},

	{

		id: 'permissions',

		label: 'Set permissions',

		percentageComplete: 100,

		status: 'visited',

		href: '#',

	},

	{

		id: 'email-settings',

		label: 'Email settings',

		percentageComplete: 100,

		status: 'visited',

		href: '#',

	},

	{

		id: 'confirmation',

		label: 'Confirm changes',

		percentageComplete: 0,

		status: 'current',

		href: '#',

	},

];



export default () => <ProgressTracker items={items} />;
```

---

[View Original Documentation](https://atlassian.design/components/progress-tracker/examples)
