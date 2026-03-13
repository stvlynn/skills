# Link icon button

An icon-only button that helps people navigate to a common link or page location.

---

## Default

For buttons that are links for navigation rather than on-page actions. Link icon buttons render an <a> tag instead of a <button>. They accept anchor tag HTML attributes, including href. 

```jsx
import React from 'react';



import { LinkIconButton } from '@atlaskit/button/new';

import QuestionCircleIcon from '@atlaskit/icon/glyph/question-circle';



const LinkIconButtonDefaultExample = () => {

	return (

		<LinkIconButton href="https://atlassian.com" icon={QuestionCircleIcon} label="View help" />

	);

};



export default LinkIconButtonDefaultExample;
```

## Routing

When available, link icon button will consume the router link component configured in the app provider. This allows router links to be configured once across an entire application. (This replaces the component prop). These links won't use the configured router link component when passed to href, and instead render a standard <a> tag: If your application doesn't have an existing app provider or routerLinkComponent configuration, see how to set this up in the app provider documentation. 

## Tooltips

Set isTooltipDisabled to false to enable the tooltip. The value of label will be used for the tooltip content. 

```jsx
import React from 'react';



import { LinkIconButton } from '@atlaskit/button/new';

import PersonAvatarIcon from '@atlaskit/icon/glyph/user-avatar-circle';



const LinkIconButtonTooltipExample = () => {

	return (

		<LinkIconButton

			href="https://atlassian.com"

			icon={PersonAvatarIcon}

			label="View profile"

			isTooltipDisabled={false}

		/>

	);

};



export default LinkIconButtonTooltipExample;
```

### Overriding tooltip props

Use the tooltip prop to override the default tooltip props. It accepts all tooptip props, excluding children. 

```jsx
import React from 'react';



import { LinkIconButton, type LinkIconButtonProps } from '@atlaskit/button/new';

import PersonAvatarIcon from '@atlaskit/icon/glyph/user-avatar-circle';



const tooltipOptions: LinkIconButtonProps['tooltip'] = {

	position: 'right',

	hideTooltipOnClick: true,

};



const LinkIconButtonTooltipOptionsExample = () => {

	return (

		<LinkIconButton

			href="https://atlassian.com"

			icon={PersonAvatarIcon}

			label="View profile"

			isTooltipDisabled={false}

			tooltip={tooltipOptions}

		/>

	);

};



export default LinkIconButtonTooltipOptionsExample;
```

## Appearance

### Primary

A primary button calls attention to the most important action on a page or in an area. Primary icon buttons aren't common because critical actions should typically use a button with a label for clarity. 

```jsx
import React from 'react';



import { LinkIconButton } from '@atlaskit/button/new';

import AddIcon from '@atlaskit/icon/glyph/add';



const LinkIconButtonPrimaryExample = () => {

	return (

		<LinkIconButton

			href="https://atlassian.com"

			icon={AddIcon}

			label="Add new blog"

			appearance="primary"

		/>

	);

};



export default LinkIconButtonPrimaryExample;
```

### Subtle

Use a subtle icon button for secondary actions. 

```jsx
import React from 'react';



import { LinkIconButton } from '@atlaskit/button/new';

import SettingsIcon from '@atlaskit/icon/glyph/settings';



const LinkIconButtonSubtleExample = () => {

	return (

		<LinkIconButton

			href="https://atlassian.com"

			appearance="subtle"

			icon={SettingsIcon}

			label="View settings"

		/>

	);

};



export default LinkIconButtonSubtleExample;
```

## Spacing

Icon button spacing depends on the surrounding UI. Default spacing is used for most use cases and compact for tables or smaller spaces. 

```jsx
import React from 'react';



import { LinkIconButton } from '@atlaskit/button/new';

import QuestionCircleIcon from '@atlaskit/icon/glyph/question-circle';

import { Inline } from '@atlaskit/primitives';



const LinkIconButtonSpacingExample = () => {

	return (

		<Inline space="space.200">

			<LinkIconButton href="https://atlassian.com" icon={QuestionCircleIcon} label="View help" />

			<LinkIconButton

				href="https://atlassian.com"

				icon={QuestionCircleIcon}

				spacing="compact"

				label="View help"

			/>

		</Inline>

	);

};



export default LinkIconButtonSpacingExample;
```

## Shape

### Circle

Only use circle icon buttons in the top navigation or other areas that already have circular buttons. 

```jsx
import React from 'react';



import { LinkIconButton } from '@atlaskit/button/new';

import QuestionCircleIcon from '@atlaskit/icon/glyph/question-circle';



const LinkIconButtonCircleExample = () => {

	return (

		<LinkIconButton

			href="https://atlassian.com"

			shape="circle"

			icon={QuestionCircleIcon}

			label="View help"

		/>

	);

};



export default LinkIconButtonCircleExample;
```

## Overriding icon props

Use the icon render prop to override the default icon props. 

```jsx
import React from 'react';



import { LinkIconButton } from '@atlaskit/button/new';

import CompassIcon from '@atlaskit/icon/glyph/discover';

import { token } from '@atlaskit/tokens';



const LinkIconButtonOverridesExample = () => {

	return (

		<LinkIconButton

			href="https://atlassian.com"

			appearance="subtle"

			icon={(iconProps) => (

				<CompassIcon

					{...iconProps}

					primaryColor={token('color.icon.discovery')}

				/>

			)}

			label="Learn about new features"

		/>

	);

};



export default LinkIconButtonOverridesExample;
```

## Advanced href usage with TypeScript

Link button accepts a generic type containing the configured router link's props. This is only required for advanced usage to allow an object to be passed to href. 

```jsx
import React from 'react';



import { LinkIconButton } from '@atlaskit/button/new';

import PersonAvatarIcon from '@atlaskit/icon/glyph/user-avatar-circle';



type MyRouterLinkConfig = {

	to: string;

	replace?: boolean;

};



const LinkIconButtonWithRoutingExample = () => {

	return (

		<LinkIconButton<MyRouterLinkConfig>

			href={{

				to: '/profile',

				replace: true,

			}}

			icon={PersonAvatarIcon}

			label="View profile"

		/>

	);

};



export default LinkIconButtonWithRoutingExample;
```

## States

### Disabled

The disabled HTML attribute does not exist for anchor <a> tags, so link buttons are disabled using this accessible technique: 

```jsx
import React from 'react';



import { LinkIconButton } from '@atlaskit/button/new';

import QuestionCircleIcon from '@atlaskit/icon/glyph/question-circle';



const LinkIconButtonDisabledExample = () => {

	return (

		<LinkIconButton

			href="https://atlassian.com"

			appearance="subtle"

			icon={QuestionCircleIcon}

			label="View profile"

			isDisabled

		/>

	);

};



export default LinkIconButtonDisabledExample;
```

### Selected

Set isSelected to indicate the button is selected. 

```jsx
import React from 'react';



import { LinkIconButton } from '@atlaskit/button/new';

import PullRequestIcon from '@atlaskit/icon/glyph/bitbucket/pullrequests';



const LinkIconButtonSelectedExample = () => {

	return (

		<LinkIconButton

			href="https://atlassian.com"

			icon={PullRequestIcon}

			label="View pull requests"

			isSelected

		/>

	);

};



export default LinkIconButtonSelectedExample;
```

---

[View Original Documentation](https://atlassian.design/components/button/link-icon-button/examples)
