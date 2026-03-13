# Flag

A flag is used for confirmations, alerts, and acknowledgments that require minimal user interaction, often displayed using a flag group.

---

## Default

All flags require a title and an icon. Make sure the icon and color match the intent of your message, such as warning, error, information, or success. A dismiss button will auto-display on the first flag in a FlagGroup or when the appearance prop is set. Flags are often used within a flag group. 

## New version published

```jsx
import React from 'react';



import Flag from '@atlaskit/flag';

import InformationIcon from '@atlaskit/icon/glyph/info';

import { token } from '@atlaskit/tokens';



const FlagDefaultExample = () => {

	return (

		<Flag

			icon={

				<InformationIcon

					primaryColor={token('color.icon.information')}

					label="Info"

				/>

			}

			description="Scott Farquhar published a new version of this page. Refresh to see the changes."

			id="1"

			key="1"

			title="New version published"

		/>

	);

};



export default FlagDefaultExample;
```

## Actions

Use actions to show a clickable action at the bottom of the flag. For flags where the appearance is normal, the action will show as a link. For all other appearances the actions will be buttons. 

## Issue START-42 was created successfully

```jsx
import React from 'react';



import Flag from '@atlaskit/flag';

import SuccessIcon from '@atlaskit/icon/glyph/check-circle';

import { token } from '@atlaskit/tokens';



const FlagActionsExample = () => {

	return (

		<Flag

			icon={

				<SuccessIcon

					primaryColor={token('color.icon.success')}

					label="Success"

				/>

			}

			id="1"

			key="1"

			title="Issue START-42 was created successfully"

			actions={[

				{

					content: 'View issue',

					onClick: () => {

						console.log('flag action clicked');

					},

				},

				{

					content: 'Add to next sprint',

					href: '/components/flag/examples#actions',

				},

			]}

		/>

	);

};



export default FlagActionsExample;
```

## Appearance

Unlike normal flags, setting an appearance gives the flag a bold color. Bold appearance flags don't have a dismiss button, so they require a more direct interaction from people. 

### Information

Information messages alert people to additional information without requiring an action. You can also use them for loading states. 

## There’s no one in this project

```jsx
import React from 'react';



import noop from '@atlaskit/ds-lib/noop';

import Flag from '@atlaskit/flag';

import InformationIcon from '@atlaskit/icon/glyph/info';

import { token } from '@atlaskit/tokens';



const FlagInfoExample = () => {

	return (

		<Flag

			appearance="info"

			icon={

				<InformationIcon

					label="Info"

					secondaryColor={token('color.background.neutral.bold')}

				/>

			}

			id="info"

			key="info"

			title="There’s no one in this project"

			description="Add yourself or your team to get the party started."

			actions={[

				{ content: 'Add teammates', onClick: noop },

				{ content: 'Close', onClick: noop },

			]}

		/>

	);

};



export default FlagInfoExample;
```

### Warning

Warning messages appear before we request people to take action. This is usually in anticipation of a significant change. Never set warning flags to auto dismiss. Give people enough time to read your message and decide what to do. 

## This page is visible to people outside your organization

```jsx
import React from 'react';



import noop from '@atlaskit/ds-lib/noop';

import Flag from '@atlaskit/flag';

import WarningIcon from '@atlaskit/icon/glyph/warning';

import { token } from '@atlaskit/tokens';



const FlagWarningExample = () => {

	return (

		<Flag

			appearance="warning"

			icon={

				<WarningIcon

					label="Warning"

					secondaryColor={token('color.background.warning.bold')}

				/>

			}

			id="warning"

			key="warning"

			title="This page is visible to people outside your organization"

			description="Are you sure you want to publish?"

			actions={[

				{ content: 'Publish', onClick: noop },

				{ content: 'Go back', onClick: noop },

			]}

		/>

	);

};



export default FlagWarningExample;
```

### Error

Error messages let people know that something has gone wrong after they've tried to do something or if there are connectivity issues. Never set error flags to auto dismiss. Give people enough time to read your message and understand the problem. 

## We're having trouble connecting

```jsx
import React from 'react';



import noop from '@atlaskit/ds-lib/noop';

import Flag from '@atlaskit/flag';

import ErrorIcon from '@atlaskit/icon/glyph/error';

import { token } from '@atlaskit/tokens';



const FlagErrorExample = () => {

	return (

		<Flag

			appearance="error"

			icon={

				<ErrorIcon

					label="Error"

					secondaryColor={token('color.background.danger.bold')}

				/>

			}

			id="error"

			key="error"

			title="We're having trouble connecting"

			description="Check your internet connection and try again."

			actions={[{ content: 'Try again', onClick: noop }]}

		/>

	);

};



export default FlagErrorExample;
```

### Success

Success messages let people know they have completed an action. 

## Welcome to the room

```jsx
import React from 'react';



import noop from '@atlaskit/ds-lib/noop';

import Flag from '@atlaskit/flag';

import SuccessIcon from '@atlaskit/icon/glyph/check-circle';

import { token } from '@atlaskit/tokens';



const FlagSuccessExample = () => {

	return (

		<Flag

			appearance="success"

			icon={

				<SuccessIcon

					label="Success"

					secondaryColor={token('color.background.success.bold')}

				/>

			}

			id="success"

			key="success"

			title="Welcome to the room"

			description="You’re now part of Coffee Club."

			actions={[{ content: 'Join the conversation', onClick: noop }]}

		/>

	);

};



export default FlagSuccessExample;
```

---

[View Original Documentation](https://atlassian.design/components/flag/examples)
