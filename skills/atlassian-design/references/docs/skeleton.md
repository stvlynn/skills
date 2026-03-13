# Skeleton

A skeleton acts as a placeholder for content, usually while the content loads.

---

## Basic

```jsx
import React from 'react';



import Skeleton from '@atlaskit/skeleton';



export default () => <Skeleton width="200px" height="16px" testId="skeleton" />;
```

## Shimmering effect

The shimmering animation can be controlled via the isShimmering prop. 

```jsx
import React from 'react';



import Skeleton from '@atlaskit/skeleton';



export default () => <Skeleton width="200px" height="16px" isShimmering testId="skeleton" />;
```

## Customized color

The default skeleton color can be overrided via the color prop. 

```jsx
import React from 'react';



import Skeleton from '@atlaskit/skeleton';

import { token } from '@atlaskit/tokens';



export default () => (

	<Skeleton

		width="200px"

		height="16px"

		color={token('color.background.accent.gray.subtle')}

		testId="skeleton"

	/>

);
```

## Customized shimmering animation color

The default shimmering animation from and to colors can be overrided via the color and ShimmeringEndColor prop. 

```jsx
import React from 'react';



import Skeleton from '@atlaskit/skeleton';

import { token } from '@atlaskit/tokens';



export default () => (

	<Skeleton

		width="200px"

		height="16px"

		color={token('color.background.accent.gray.subtle')}

		ShimmeringEndColor={token('color.background.accent.gray.bolder')}

		testId="skeleton"

	/>

);
```

---

[View Original Documentation](https://atlassian.design/components/skeleton/examples)
