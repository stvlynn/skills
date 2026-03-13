# Avatar skeleton

A skeleton is the loading state for the avatar component.

---

## Appearance

### Circle

The default appearance. Use appearance="circle" for a circular skeleton. 

```jsx
import React from 'react';



import { Skeleton } from '@atlaskit/avatar';



const AvatarSkeletonCircleExample = () => {

	return <Skeleton appearance="circle" />;

};



export default AvatarSkeletonCircleExample;
```

### Square

Use appearance="square" for a square skeleton. 

```jsx
import React from 'react';



import { Skeleton } from '@atlaskit/avatar';



const AvatarSkeletonSquareExample = () => {

	return <Skeleton appearance="square" />;

};



export default AvatarSkeletonSquareExample;
```

## Size

Use size to define the size of the skeleton. 

```jsx
import React from 'react';



import { Skeleton } from '@atlaskit/avatar';



const AvatarSkeletonSizeExample = () => {

	return (

		<div>

			<Skeleton size="xsmall" />

			<Skeleton size="small" />

			<Skeleton size="medium" />

			<Skeleton size="large" />

			<Skeleton size="xlarge" />

			<Skeleton size="xxlarge" />

		</div>

	);

};



export default AvatarSkeletonSizeExample;
```

## Color

### Default

By default, a skeleton inherits the color of its parent container. 

```jsx
import React from 'react';



import { Skeleton } from '@atlaskit/avatar';

import { token } from '@atlaskit/tokens';



const AvatarSkeletonColorDefaultExample = () => {

	return (

		// eslint-disable-next-line @atlaskit/ui-styling-standard/enforce-style-prop -- Ignored via go/DSP-18766

		<div style={{ color: token('color.background.accent.purple.subtler') }}>

			<Skeleton />

		</div>

	);

};



export default AvatarSkeletonColorDefaultExample;
```

### Specific color

Set the color of a skeleton by defining the color property. 

```jsx
import React from 'react';



import { Skeleton } from '@atlaskit/avatar';

import { token } from '@atlaskit/tokens';



const AvatarSkeletonColorExample = () => {

	return <Skeleton color={token('color.background.accent.blue.subtler')} />;

};



export default AvatarSkeletonColorExample;
```

## Weight

### Default opacity

Use weight="normal" for the default opacity for the skeleton. 

```jsx
import React from 'react';



import { Skeleton } from '@atlaskit/avatar';

import { token } from '@atlaskit/tokens';



const AvatarSkeletonWeightNormalExample = () => {

	return <Skeleton color={token('color.background.accent.yellow.subtler')} weight="normal" />;

};



export default AvatarSkeletonWeightNormalExample;
```

### Strong opacity

Use weight="strong" for a stronger opacity for the skeleton. 

```jsx
import React from 'react';



import { Skeleton } from '@atlaskit/avatar';

import { Y500 } from '@atlaskit/theme/colors';



const AvatarSkeletonWeightStrongExample = () => {

	return <Skeleton color={Y500} weight="strong" />;

};



export default AvatarSkeletonWeightStrongExample;
```

---

[View Original Documentation](https://atlassian.design/components/avatar/avatar-skeleton/examples)
