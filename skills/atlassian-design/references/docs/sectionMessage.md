# Section message

A section message is used to alert users to a particular section of the screen.

---

## Appearance

By default, all section message come with an icon and an area for content. You can optionally add a title and actions. 

### Information

The information section message is the default appearance used to signify a change in state or important information. 

## Editing is restricted

You're not allowed to change these restrictions. It's either due to the restrictions on the page, or permission settings for this space. 

```jsx
import React from 'react';



import SectionMessage, { SectionMessageAction } from '@atlaskit/section-message';



export default () => (

	<SectionMessage

		title="Editing is restricted"

		actions={[

			<SectionMessageAction href="#">Request edit access</SectionMessageAction>,

			<SectionMessageAction href="#">About permissions</SectionMessageAction>,

		]}

	>

		<p>

			You're not allowed to change these restrictions. It's either due to the restrictions on the

			page, or permission settings for this space.

		</p>

	</SectionMessage>

);
```

### Warning

Use a warning section message to help people: How to write warning messages 

## Cannot connect to the database

We're unable to save any progress at this time. Please try again later. 

```jsx
import React from 'react';



import SectionMessage from '@atlaskit/section-message';



export default () => (

	<SectionMessage title="Cannot connect to the database" appearance="warning">

		<p>We're unable to save any progress at this time. Please try again later.</p>

	</SectionMessage>

);
```

### Success

Use a success section message to let the user know that an action or event has happened successfully. The file has been uploaded. 

```jsx
import React from 'react';



import SectionMessage from '@atlaskit/section-message';



export default () => (

	<SectionMessage appearance="success">

		<p>The file has been uploaded.</p>

	</SectionMessage>

);
```

### Error

Use an error section message to let people know when: How to write error messages 

## This account has been permanently deleted

The user `IanAtlas` no longer has access to Atlassian services. 

```jsx
import React from 'react';



import SectionMessage from '@atlaskit/section-message';



export default () => (

	<SectionMessage title="This account has been permanently deleted" appearance="error">

		<p>The user `IanAtlas` no longer has access to Atlassian services.</p>

	</SectionMessage>

);
```

### Discovery

Use a discovery section message to signify an update to the UI or provide information around new features and onboarding. 

## Your managed accounts now include Trello access

Some users haven't started using their Atlassian account for Trello. Changes you make to an account are reflected only if the user starts using the account for Trello. 

```jsx
import React from 'react';



import SectionMessage, { SectionMessageAction } from '@atlaskit/section-message';



export default () => (

	<SectionMessage

		title="Your managed accounts now include Trello access"

		appearance="discovery"

		actions={<SectionMessageAction href="#">See who's using Trello</SectionMessageAction>}

	>

		<p>

			Some users haven't started using their Atlassian account for Trello. Changes you make to an

			account are reflected only if the user starts using the account for Trello.

		</p>

	</SectionMessage>

);
```

## Actions

Use the actions prop to let people act on the content in the section message. The SectionMessageAction component is designed to work with the actions prop. In most cases you should use the section message action, but you can also use any JSX element in the actions array. An action will render a button if you supply an onClick handler, or a link if you supply an href. You can override the default link component using the linkComponent prop; this works well with router libraries. 

## Merged pull request

Pull request #10146 merged after a successful build 

```jsx
import React from 'react';



import SectionMessage, { SectionMessageAction } from '@atlaskit/section-message';



export default () => (

	<SectionMessage

		title="Merged pull request"

		appearance="success"

		actions={[

			<SectionMessageAction href="#">View commit</SectionMessageAction>,

			<SectionMessageAction onClick={() => {}}>Dismiss</SectionMessageAction>,

		]}

	>

		<p>Pull request #10146 merged after a successful build</p>

	</SectionMessage>

);
```

---

[View Original Documentation](https://atlassian.design/components/section-message/examples)
