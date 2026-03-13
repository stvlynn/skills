# Avatar content

Avatar content can be used with the Avatar component to create a customized avatar.

---

The AvatarContent component allows you to create avatars with custom content, such as text or icons. It is used as a child of the Avatar component and can also be composed with other elements. When using AvatarContent, the props from the Avatar component still apply. For example, you can use the size prop to set the size of the avatar.

```jsx
/**

 * @jsxRuntime classic

 * @jsx jsx

 */



import Avatar, { AvatarContent } from '@atlaskit/avatar';

import { css, jsx } from '@atlaskit/css';

import PeopleGroupIcon from '@atlaskit/icon/glyph/people-group';

import { token } from '@atlaskit/tokens';



const styles = {

	iconContainer: css({

		display: 'grid',

		height: '100%',

		backgroundColor: token('elevation.surface'),

		placeItems: 'center',

	}),

};



function AvatarContentExample() {

	return (

		<Avatar size="large" borderColor={token('color.background.brand.bold')}>

			<AvatarContent>

				<div css={styles.iconContainer}>

					<PeopleGroupIcon label="More users" />

				</div>

			</AvatarContent>

		</Avatar>

	);

}



export default AvatarContentExample;
```

---

[View Original Documentation](https://atlassian.design/components/avatar/avatar-content/examples)
