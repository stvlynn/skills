# Inline message

An inline message lets users know when important information is available or when an action is required.

---

## Default

By default, inline messages contain an icon. Adding a title is recommended. You can also include secondaryText depending on the use case. 

```jsx
import React from 'react';



import InlineMessage from '@atlaskit/inline-message';



const InlineMessageDefaultExample = () => {

	return (

		<InlineMessage title="Title" secondaryText="Secondary text">

			<p>Default type dialog</p>

		</InlineMessage>

	);

};



export default InlineMessageDefaultExample;
```

## Title

This is the text to display first. It's bolded for emphasis. 

```jsx
import React from 'react';



import InlineMessage from '@atlaskit/inline-message';



const InlineMessageTitleExample = () => {

	return (

		<InlineMessage title="This page may be out of date">

			<p>This page was last updated 65 days ago. See the version history for more details.</p>

		</InlineMessage>

	);

};



export default InlineMessageTitleExample;
```

## Secondary text

Use secondary text if the title alone isn't enough to convey what the inline message is about. It appears after the title. 

```jsx
import React from 'react';



import InlineMessage from '@atlaskit/inline-message';



const InlineMessageSecondaryTextExample = () => {

	return (

		<InlineMessage title="Software update" secondaryText="You've been upgraded to version 5.2">

			<p>

				We've updated you to the latest version, with added stability and new security features.

			</p>

		</InlineMessage>

	);

};



export default InlineMessageSecondaryTextExample;
```

## Placement

By default, the inline dialog opens at the bottom at the beginning of the text. Use placement to open the dialog from a different place in relation to the text. 

```jsx
import React from 'react';



import InlineMessage from '@atlaskit/inline-message';



const InlineMessagePlacementExample = () => {

	return (

		<InlineMessage placement="right" title="Title" secondaryText="Secondary text">

			<p>Dialog to the right</p>

		</InlineMessage>

	);

};



export default InlineMessagePlacementExample;
```

## Appearance

### Warning

Warning messages appear before we ask people to take action. This is usually in anticipation of a significant change. Warnings should also be used for authentication issues. 

```jsx
import React from 'react';



import InlineMessage from '@atlaskit/inline-message';



const InlineMessageWarningExample = () => {

	return (

		<InlineMessage appearance="warning" secondaryText="Your bill may increase">

			<p>

				<strong>Adding new users</strong>

			</p>

			<p>

				You are adding 5 new users to your selected product, if they don’t already have access to

				this product your bill may increase.

			</p>

		</InlineMessage>

	);

};



export default InlineMessageWarningExample;
```

### Error

Error messages let people know that something has gone wrong after they've tried to do something. You can also use them to advise people of connectivity issues. 

```jsx
import React from 'react';



import InlineMessage from '@atlaskit/inline-message';



const InlineMessageErrorExample = () => {

	return (

		<InlineMessage

			appearance="error"

			iconLabel="Error! This name is already in use. Try another."

			secondaryText="Username taken"

		>

			<p>This name is already in use. Try another.</p>

		</InlineMessage>

	);

};



export default InlineMessageErrorExample;
```

### Confirmation

Confirmation messages let people know that they have completed an action. 

```jsx
import React from 'react';



import InlineMessage from '@atlaskit/inline-message';

import Link from '@atlaskit/link';



const InlineMessageConfirmation = () => {

	return (

		<InlineMessage appearance="confirmation" secondaryText="Files have been added">

			<p>You have successfully uploaded 3 files.</p>

			<p>

				<Link href="atlassian.design">View files</Link>

			</p>

		</InlineMessage>

	);

};



export default InlineMessageConfirmation;
```

### Info

Info messages give people additional information without requiring an action. 

```jsx
import React from 'react';



import InlineMessage from '@atlaskit/inline-message';

import Link from '@atlaskit/link';



const InlineMessageInfoExample = () => {

	return (

		<InlineMessage appearance="info">

			<p>

				<strong>Test drive your new search</strong>

			</p>

			<p>We've turbocharged your search results so you can get back to doing what you do best.</p>

			<p>

				<Link href="http://www.atlassian.com">Learn more about Atlassian</Link>

			</p>

		</InlineMessage>

	);

};



export default InlineMessageInfoExample;
```

### Connectivity

Connectivity messages let people know that they will need to log in to get more information. Only use this when warning and error are not appropriate. 

```jsx
import React from 'react';



import InlineMessage from '@atlaskit/inline-message';

import Link from '@atlaskit/link';



const InlineMessageConnectivityExample = () => {

	return (

		<InlineMessage appearance="connectivity" iconLabel="Log in to see more information">

			<p>

				<Link href="atlassian.design">Log in</Link> to access your account information

			</p>

		</InlineMessage>

	);

};



export default InlineMessageConnectivityExample;
```

---

[View Original Documentation](https://atlassian.design/components/inline-message/examples)
