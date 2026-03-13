# Link button

A button for navigation and URL changes.

---

## Default

A button that triggers a link rather than an action. This will render an <a> tag instead of a <button>. It accepts anchor tag HTML attributes, including href. The default appearance is for secondary actions or general actions that aren't the most important in the area. 

```jsx
import React from 'react';



import { LinkButton } from '@atlaskit/button/new';



const LinkButtonDefaultExample = () => {

	return <LinkButton href="https://atlassian.com/">Default Link button</LinkButton>;

};



export default LinkButtonDefaultExample;
```

### Routing

Link button consumes the router link component configured in the app provider when possible. This means router links are configured once across an application (replacing the component prop). External links, non-HTTP-based links (mailto:, sms:), and anchor or hash links (#) won't use the configured router link when passed to href. These render a standard <a> tag. 

### Advanced href usage with TypeScript

Link button accepts a generic type containing the configured router link's props. This is only for advanced usage to pass an object to href. 

```jsx
import React from 'react';



import { LinkButton } from '@atlaskit/button/new';



type MyRouterLinkConfig = {

	to: string;

	replace?: boolean;

};



const LinkButtonWithRoutingExample = () => {

	return (

		<LinkButton<MyRouterLinkConfig>

			href={{

				to: '/about',

				replace: true,

			}}

		>

			Link button

		</LinkButton>

	);

};



export default LinkButtonWithRoutingExample;
```

## Appearance

### Primary

Use a primary link button when the main call to action is to navigate to a new page or URL. 

```jsx
import React from 'react';



import { LinkButton } from '@atlaskit/button/new';



const LinkButtonPrimaryExample = () => {

	return (

		<LinkButton appearance="primary" href="https://atlassian.com/">

			Primary link button

		</LinkButton>

	);

};



export default LinkButtonPrimaryExample;
```

### Subtle

Use subtle buttons when the surrounding context makes it clear the text is interactive, like in navigation areas. 

```jsx
import React from 'react';



import { LinkButton } from '@atlaskit/button/new';



const LinkButtonSubtleExample = () => {

	return (

		<LinkButton appearance="subtle" href="https://atlassian.com/">

			Subtle link button

		</LinkButton>

	);

};



export default LinkButtonSubtleExample;
```

### Warning

Warning appearances are designed to confirm someone wants to proceed despite a potentially unintended or inconvenient (but reversible) outcome. In general, try to avoid these unclear outcomes in the first place. 

```jsx
import React from 'react';



import { LinkButton } from '@atlaskit/button/new';



const LinkButtonWarningExample = () => {

	return (

		<LinkButton appearance="warning" href="https://atlassian.com/">

			Warning link button

		</LinkButton>

	);

};



export default LinkButtonWarningExample;
```

### Danger

Danger appearances are similar to warnings, but these should be reserved for situations with severe consequences, such as a permanent loss of data or an action that affects many users. 

```jsx
import React from 'react';



import { LinkButton } from '@atlaskit/button/new';



const LinkButtonDangerExample = () => {

	return (

		<LinkButton appearance="danger" href="https://atlassian.com/">

			Danger link button

		</LinkButton>

	);

};



export default LinkButtonDangerExample;
```

## Icon

Buttons can include an icon before or after the text label. Only use icons if it is necessary to aid comprehension. Most of the time, a text label alone is clearer. For buttons that open a link in a new tab or external website, use a link button with an icon after the text. 

```jsx
import React from 'react';



import { LinkButton } from '@atlaskit/button/new';

import ShortcutIcon from '@atlaskit/icon/glyph/add-item';



const LinkButtonIconExample = () => {

	return (

		<LinkButton iconAfter={ShortcutIcon} href="https://atlassian.com/">

			Icon after

		</LinkButton>

	);

};



export default LinkButtonIconExample;
```

## States

### Disabled

Standard buttons use the disabled HTML attribute, however this doesn't exist for anchor <a> tags, so link buttons are disabled by removing the href attribute and adding aria-disabled="true" and role="link". 

```jsx
import React from 'react';



import { LinkButton } from '@atlaskit/button/new';



const LinkButtonDisabledExample = () => {

	return (

		<LinkButton href="https://atlassian.com/" appearance="primary" isDisabled>

			Disabled link button

		</LinkButton>

	);

};



export default LinkButtonDisabledExample;
```

---

[View Original Documentation](https://atlassian.design/components/button/link-button/examples)
