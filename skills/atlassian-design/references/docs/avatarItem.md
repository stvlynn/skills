# Avatar item

An avatar item is a wrapper that goes around an avatar when it's displayed alongside text, such as a name or status.

---

## Background color

Use a backgroundColor to change the background color of the avatar. 

```jsx
import React from 'react';



import Avatar, { AvatarItem } from '@atlaskit/avatar';



const AvatarItemBackgroundColorExample = () => (

	<AvatarItem

		backgroundColor="pink"

		avatar={

			<Avatar

				name="Scott Farquhar"

				src="https://pbs.twimg.com/profile_images/803832195970433027/aaoG6PJI_400x400.jpg"

				presence="online"

				label="Scott Farquhar (online)"

			/>

		}

	/>

);



export default AvatarItemBackgroundColorExample;
```

## States

### Disabled

Use isDisabled to put the avatar into a disabled state. This will make the avatar non-interactive. Avoid using disabled UI. This can cause accessibility problems, because disabled UI does not give enough information to people about what went wrong and how to proceed. 

```jsx
import React from 'react';



import Avatar, { AvatarItem } from '@atlaskit/avatar';



const AvatarItemIsDisabledExample = () => {

	const presence = 'online';

	return (

		<AvatarItem

			isDisabled

			avatar={

				<Avatar

					src="https://pbs.twimg.com/profile_images/803832195970433027/aaoG6PJI_400x400.jpg"

					presence={presence}

					name="Scott Farquhar"

				/>

			}

		/>

	);

};



export default AvatarItemIsDisabledExample;
```

## Text

### Primary text

Use primaryText to style the avatar text as primary text. 

```jsx
import React from 'react';



import Avatar, { AvatarItem } from '@atlaskit/avatar';



const AvatarPrimaryTextExample = () => {

	return (

		<AvatarItem

			avatar={<Avatar name="Mike Cannon-Brookes" presence="online" />}

			primaryText="Mike Cannon-Brookes"

		/>

	);

};



export default AvatarPrimaryTextExample;
```

### Secondary text

Use secondaryText to style the avatar text as secondary text. 

```jsx
import React from 'react';



import Avatar, { AvatarItem } from '@atlaskit/avatar';



const AvatarSecondaryTextExample = () => {

	return (

		<AvatarItem

			avatar={<Avatar name="Scott Farquhar" presence="online" />}

			secondaryText="Scott Farquhar"

		/>

	);

};



export default AvatarSecondaryTextExample;
```

### Composing text

primaryText and secondaryText can be composed together. 

```jsx
import React from 'react';



import Avatar, { AvatarItem } from '@atlaskit/avatar';



const AvatarItemTextExample = () => {

	return (

		<AvatarItem

			avatar={<Avatar name="Atlassian CEO" presence="online" />}

			primaryText="Atlassian CEO"

			secondaryText="CEO@atlassian.com"

		/>

	);

};



export default AvatarItemTextExample;
```

## Truncation

If overflowing text exceeds the width of its container, it is truncated by default. Use isTruncationDisabled to disable this. To be accessible, avoid truncating useful text wherever possible. 

```jsx
import React from 'react';



import Avatar, { AvatarItem } from '@atlaskit/avatar';



const AvatarItemIsTruncationDisabled = () => {

	return (

		// eslint-disable-next-line @atlaskit/ui-styling-standard/enforce-style-prop -- Ignored via go/DSP-18766

		<div style={{ maxWidth: 120, border: '1px solid pink' }}>

			<AvatarItem

				avatar={

					<Avatar

						src="https://pbs.twimg.com/profile_images/803832195970433027/aaoG6PJI_400x400.jpg"

						name="Scott Farquhar"

					/>

				}

				primaryText="Scott"

				secondaryText="scott@atlassian.com"

				isTruncationDisabled={true}

			/>

			<AvatarItem

				avatar={

					<Avatar

						src="https://pbs.twimg.com/profile_images/803832195970433027/aaoG6PJI_400x400.jpg"

						name="Scott Farquhar"

					/>

				}

				primaryText="Scott"

				secondaryText="Scott@atlassian.com"

				isTruncationDisabled={false}

			/>

		</div>

	);

};



export default AvatarItemIsTruncationDisabled;
```

---

[View Original Documentation](https://atlassian.design/components/avatar/avatar-item/examples)
