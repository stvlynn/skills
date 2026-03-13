# Avatar group

An avatar group displays a number of avatars grouped together in a stack or grid.

---

## Appearance

You can display a group of avatars in a stack or a grid. 

### Stack

Stacked avatar groups can contain up to five avatars, and should only be used with small or medium sized avatars. 

```jsx
import React from 'react';



import AvatarGroup from '@atlaskit/avatar-group';



import { getFreeToUseAvatarImage, RANDOM_USERS } from '../../examples-util/data';



const AvatarGroupStackExample = () => {

	const data = RANDOM_USERS.map((d, i) => ({

		key: d.email,

		name: d.name,

		href: '#',

		src: getFreeToUseAvatarImage(i),

	}));



	return <AvatarGroup appearance="stack" data={data} />;

};



export default AvatarGroupStackExample;
```

### Grid

Avatar groups displayed in a grid can contain up to 11 avatars spread across its rows. 

```jsx
import React from 'react';



import AvatarGroup from '@atlaskit/avatar-group';

import { cssMap } from '@atlaskit/css';

import { Box } from '@atlaskit/primitives/compiled';



import { getFreeToUseAvatarImage, RANDOM_USERS } from '../../examples-util/data';



const styles = cssMap({

	container: {

		maxWidth: '200px',

	},

});



const AvatarGroupGridExample = () => {

	const data = RANDOM_USERS.map((d, i) => ({

		key: d.email,

		name: d.name,

		href: '#',

		src: getFreeToUseAvatarImage(i),

	}));



	return (

		<Box xcss={styles.container}>

			<AvatarGroup appearance="grid" data={data} />

		</Box>

	);

};



export default AvatarGroupGridExample;
```

## Max count

Use the maxCount prop to customize the maximum number of avatars allowed in the list. 

```jsx
import React from 'react';



import AvatarGroup from '@atlaskit/avatar-group';

import { cssMap } from '@atlaskit/css';

import { Box } from '@atlaskit/primitives/compiled';



import { getFreeToUseAvatarImage, RANDOM_USERS } from '../../examples-util/data';



const styles = cssMap({

	container: {

		maxWidth: '200px',

	},

});



const AvatarGroupMaxCountExample = () => {

	const data = RANDOM_USERS.map((d, i) => ({

		key: d.email,

		name: d.name,

		href: '#',

		src: getFreeToUseAvatarImage(i),

	}));



	return (

		<Box xcss={styles.container}>

			<AvatarGroup appearance="grid" maxCount={14} data={data} />

		</Box>

	);

};



export default AvatarGroupMaxCountExample;
```

## Border color

The color of the border around the avatar. Any color that the CSS border-color property accepts can be used. 

```jsx
import React from 'react';



import AvatarGroup from '@atlaskit/avatar-group';



import { getFreeToUseAvatarImage, RANDOM_USERS } from '../../examples-util/data';



const AvatarGroupBorderColorExample = () => {

	const data = RANDOM_USERS.map((d, i) => ({

		key: d.email,

		name: d.name,

		href: '#',

		src: getFreeToUseAvatarImage(i),

	}));



	return <AvatarGroup data={data} borderColor="#FF6347" />;

};



export default AvatarGroupBorderColorExample;
```

## Overrides

Custom components can be passed in via the overrides prop. For example, you can add extra behavior into the overflow menu using the overrides prop. Select the example overflow avatar and you'll see a load more button powered by our custom AvatarGroupItem. 

```jsx
import React, { Fragment, useEffect, useRef, useState } from 'react';



import { type AppearanceType, type SizeType } from '@atlaskit/avatar';

import AvatarGroup from '@atlaskit/avatar-group';

import Button from '@atlaskit/button/new';

import { cssMap } from '@atlaskit/css';

import { Box } from '@atlaskit/primitives/compiled';

import { token } from '@atlaskit/tokens';



import { getFreeToUseAvatarImage, RANDOM_USERS } from '../../examples-util/data';



const styles = cssMap({

	container: {

		marginTop: token('space.100'),

		marginRight: token('space.100'),

		marginBottom: token('space.100'),

		marginLeft: token('space.100'),

		textAlign: 'center',

	},

});



const INITIAL_NUMBER_VISIBLE_AVATARS = 8;



const AvatarGroupOverridesExample = () => {

	const lastAvatarItemRef = useRef<HTMLElement>(null);

	const [range, setRange] = useState(INITIAL_NUMBER_VISIBLE_AVATARS);

	const data = RANDOM_USERS.slice(0, range).map((d, i) => ({

		key: d.email,

		name: d.name,

		href: '#',

		appearance: 'circle' as AppearanceType,

		size: 'medium' as SizeType,

		src: getFreeToUseAvatarImage(i),

	}));



	useEffect(() => {

		lastAvatarItemRef.current?.focus();

	}, [range]);



	return (

		<AvatarGroup

			testId="overrides"

			appearance="stack"

			data={data}

			size="large"

			// eslint-disable-next-line @repo/internal/react/no-unsafe-overrides

			overrides={{

				AvatarGroupItem: {

					render: (Component, props, index) =>

						index === data.length - 1 ? (

							<Fragment key={`${index}-overridden`}>

								<Component {...props} key={index} ref={lastAvatarItemRef} />

								<Box xcss={styles.container} testId="load-more-actions">

									<Button

										testId="load-more"

										isDisabled={range >= RANDOM_USERS.length}

										onClick={() => {

											setRange(range + 1);

										}}

									>

										Load more users

									</Button>

								</Box>

							</Fragment>

						) : (

							<Component {...props} key={index} />

						),

				},

			}}

		/>

	);

};



export default AvatarGroupOverridesExample;
```

## Size

Avatars are available in multiple sizes. See avatar for information on which size to use when. Note the xsmall size is not available for AvatarGroup due to its size being too small to render certain elements in an accessible manner. 

```jsx
import React from 'react';



import AvatarGroup from '@atlaskit/avatar-group';

import { Stack } from '@atlaskit/primitives/compiled';



import { getFreeToUseAvatarImage, RANDOM_USERS } from '../../examples-util/data';



const AvatarGroupSizeExample = () => {

	const data = RANDOM_USERS.slice(0, 8).map((d, i) => ({

		key: d.email,

		name: d.name,

		href: '#',

		src: getFreeToUseAvatarImage(i),

	}));



	return (

		<Stack space="space.100">

			<AvatarGroup data={data} size="small" />

			<AvatarGroup data={data} size="medium" />

			<AvatarGroup data={data} size="large" />

			<AvatarGroup data={data} size="xlarge" />

			<AvatarGroup data={data} size="xxlarge" />

		</Stack>

	);

};



export default AvatarGroupSizeExample;
```

---

[View Original Documentation](https://atlassian.design/components/avatar-group/examples)
