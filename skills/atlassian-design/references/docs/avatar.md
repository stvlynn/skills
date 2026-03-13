# Avatar

An avatar is a visual representation of a user or entity.

---

## Default

When the image source is unavailable (for example, when there's a problem displaying the image due to an error), or the source is unspecified, the avatar component will display a default image. When an avatar is not given any useful context via the name, presence, or status attributes like in this example, it will be hidden for assistive technologies as it does not convey any meaningful information. 

```jsx
import React from 'react';



import Avatar from '@atlaskit/avatar';



const AvatarDefaultExample = () => {

	return <Avatar />;

};



export default AvatarDefaultExample;
```

## Appearance

### Circle

Use a circle avatar to represent a person. 

```jsx
import React from 'react';



import Avatar from '@atlaskit/avatar';



const AvatarCircleExample = () => {

	return (

		<Avatar

			appearance="circle"

			src="https://pbs.twimg.com/profile_images/803832195970433027/aaoG6PJI_400x400.jpg"

			size="large"

			name="Scott Farquhar"

		/>

	);

};



export default AvatarCircleExample;
```

### Square

Use square avatars to represent an entity, such as a project, repository or space. 

```jsx
import React from 'react';



import Avatar from '@atlaskit/avatar';



import ExampleImg from '../../examples-util/nucleus.png';



const AvatarSquareExample = () => {

	return <Avatar appearance="square" size="medium" src={ExampleImg} name="Nucleus" />;

};



export default AvatarSquareExample;
```

## States

### Disabled

Set isDisabled to disable an avatar that isn't usable. This sets the avatar image to 40% opacity using the opacity.disabled token. Avoid using disabled UI. This can cause accessibility problems, because disabled UI doesn't give enough information to the user about what went wrong and how to proceed, and will not appear in the tab order. 

```jsx
import React from 'react';



import Avatar from '@atlaskit/avatar';



const AvatarDisabledExample = () => {

	return (

		<Avatar

			src="https://pbs.twimg.com/profile_images/803832195970433027/aaoG6PJI_400x400.jpg"

			name="Scott Farquhar"

			isDisabled

		/>

	);

};



export default AvatarDisabledExample;
```

## Status

Indicates contextual information by showing a small icon on the avatar. Takes precedence over presence. 

### Approved

```jsx
import React from 'react';



import Avatar from '@atlaskit/avatar';



const AvatarStatusApprovedExample = () => {

	return <Avatar name="John Smith" status="approved" />;

};



export default AvatarStatusApprovedExample;
```

### Declined

```jsx
import React from 'react';



import Avatar from '@atlaskit/avatar';



const AvatarStatusDeclinedExample = () => {

	return <Avatar name="John Smith" status="declined" />;

};



export default AvatarStatusDeclinedExample;
```

### Locked

```jsx
import React from 'react';



import Avatar from '@atlaskit/avatar';



const AvatarStatusLockedExample = () => {

	return <Avatar name="John Smith" status="locked" />;

};



export default AvatarStatusLockedExample;
```

## Presence

Indicates a user's online status by showing a small icon on the avatar. 

### Busy

```jsx
import React from 'react';



import Avatar from '@atlaskit/avatar';



const AvatarPresenceBusyExample = () => {

	return <Avatar name="John Smith" presence="busy" />;

};



export default AvatarPresenceBusyExample;
```

### Focus

```jsx
import React from 'react';



import Avatar from '@atlaskit/avatar';



const AvatarPresenceFocusExample = () => {

	return <Avatar name="John Smith" presence="focus" />;

};



export default AvatarPresenceFocusExample;
```

### Offline

```jsx
import React from 'react';



import Avatar from '@atlaskit/avatar';



const AvatarPresenceOfflineExample = () => {

	return <Avatar name="John Smith" presence="offline" />;

};



export default AvatarPresenceOfflineExample;
```

### Online

```jsx
import React from 'react';



import Avatar from '@atlaskit/avatar';



const AvatarPresenceOnlineExample = () => {

	return <Avatar name="John Smith" presence="online" />;

};



export default AvatarPresenceOnlineExample;
```

## Size

### xxlarge

Use xxlarge circle avatars in places where larger avatars are needed. For example, the Atlassian People Directory. This size isn't used for square avatars. 

```jsx
import React from 'react';



import Avatar from '@atlaskit/avatar';



import ExampleImg from '../../examples-util/nucleus.png';



const AvatarXXLargeExample = () => {

	return (

		<div>

			<Avatar

				size="xxlarge"

				src="https://pbs.twimg.com/profile_images/803832195970433027/aaoG6PJI_400x400.jpg"

				name="Scott Farquhar"

			/>

			<Avatar size="xxlarge" appearance="square" src={ExampleImg} name="Nucleus" />

		</div>

	);

};



export default AvatarXXLargeExample;
```

### xlarge

Use xlarge circle avatars where they’re needed to display prominently on a page. This size isn't used for square avatars. 

```jsx
import React from 'react';



import Avatar from '@atlaskit/avatar';



import ExampleImg from '../../examples-util/nucleus.png';



const AvatarXLargeExample = () => {

	return (

		<div>

			<Avatar

				size="xlarge"

				src="https://pbs.twimg.com/profile_images/803832195970433027/aaoG6PJI_400x400.jpg"

				name="Scott Farquhar"

			/>

			<Avatar size="xlarge" appearance="square" src={ExampleImg} name="Nucleus" />

		</div>

	);

};



export default AvatarXLargeExample;
```

### large

Use large circle avatars to represent people for main page titles, like a user's account settings. Use large square avatars to represent main entity titles like Jira projects or Confluence spaces. 

```jsx
import React from 'react';



import Avatar from '@atlaskit/avatar';



import ExampleImg from '../../examples-util/nucleus.png';



const AvatarLargeExample = () => {

	return (

		<div>

			<Avatar

				size="large"

				src="https://pbs.twimg.com/profile_images/803832195970433027/aaoG6PJI_400x400.jpg"

				name="Scott Farquhar"

			/>

			<Avatar size="large" appearance="square" src={ExampleImg} name="Nucleus" />

		</div>

	);

};



export default AvatarLargeExample;
```

### medium

Use medium circle avatars in activity streams or comments. Use medium square avatars in table views for project listings. 

```jsx
import React from 'react';



import Avatar from '@atlaskit/avatar';



import ExampleImg from '../../examples-util/nucleus.png';



const AvatarMediumExample = () => {

	return (

		<div>

			<Avatar

				size="medium"

				src="https://pbs.twimg.com/profile_images/803832195970433027/aaoG6PJI_400x400.jpg"

				name="Scott Farquhar"

			/>

			<Avatar size="medium" appearance="square" src={ExampleImg} name="Nucleus" />

		</div>

	);

};



export default AvatarMediumExample;
```

### small

Use small circle avatars in small areas like 40px text fields, and square avatars for use in things like dropdown menus. 

```jsx
import React from 'react';



import Avatar from '@atlaskit/avatar';



import ExampleImg from '../../examples-util/nucleus.png';



const AvatarSmallExample = () => {

	return (

		<div>

			<Avatar

				size="small"

				src="https://pbs.twimg.com/profile_images/803832195970433027/aaoG6PJI_400x400.jpg"

				name="Scott Farquhar"

			/>

			<Avatar size="small" appearance="square" src={ExampleImg} name="Nucleus" />

		</div>

	);

};



export default AvatarSmallExample;
```

### xsmall

Use xsmall circle and square avatars for onscreen metadata such as in Jira issues or dropdown menus. 

```jsx
import React from 'react';



import Avatar from '@atlaskit/avatar';



import ExampleImg from '../../examples-util/nucleus.png';



const AvatarXSmallExample = () => {

	return (

		<div>

			<Avatar

				size="xsmall"

				src="https://pbs.twimg.com/profile_images/803832195970433027/aaoG6PJI_400x400.jpg"

				name="Scott Farquhar"

			/>

			<Avatar size="xsmall" appearance="square" src={ExampleImg} name="Nucleus" />

		</div>

	);

};



export default AvatarXSmallExample;
```

## Displaying a tooltip

You can display a tooltip with an avatar on focus or hover. The tooltip content should be set to the same value as the avatar label. Don't use a tooltip with an avatar unless it is interactive. For more information, see the avatar component accessibilty guidelines. 

```jsx
import React from 'react';



import Avatar from '@atlaskit/avatar';

import Tooltip from '@atlaskit/tooltip';



const AvatarTooltipExample = () => {

	const presence = 'online';

	const name = 'Mike Cannon-Brookes';

	const label = `${name} (${presence})`;

	return (

		<Tooltip content={label}>

			<Avatar

				name={name}

				src="https://pbs.twimg.com/profile_images/568401563538841600/2eTVtXXO_400x400.jpeg"

				size="large"

				onClick={console.log}

				presence={presence}

			/>

		</Tooltip>

	);

};



export default AvatarTooltipExample;
```

---

[View Original Documentation](https://atlassian.design/components/avatar/examples)
