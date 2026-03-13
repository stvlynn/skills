# Auto dismiss flag

A flag that is dismissed automatically after eight seconds.

---

## Default

Use AutoDismissFlag to create a flag that will be dismissed automatically in eight seconds. Add flag 

```jsx
import React from 'react';



import Button from '@atlaskit/button/new';

import { AutoDismissFlag, FlagGroup } from '@atlaskit/flag';

import SuccessIcon from '@atlaskit/icon/glyph/check-circle';

import { Box } from '@atlaskit/primitives/compiled';

import { token } from '@atlaskit/tokens';



const AutoDismissFlagDefaultExample = () => {

	const [flags, setFlags] = React.useState<Array<number>>([]);



	const addFlag = () => {

		const newFlagId = flags.length + 1;

		const newFlags = flags.slice();

		newFlags.splice(0, 0, newFlagId);



		setFlags(newFlags);

	};



	const handleDismiss = () => {

		setFlags(flags.slice(1));

	};



	return (

		<Box>

			{/* eslint-disable-next-line @atlaskit/ui-styling-standard/enforce-style-prop -- Ignored via go/DSP-18766 */}

			<p style={{ padding: token('space.200') }}>

				<Button appearance="primary" onClick={addFlag}>

					Add flag

				</Button>

			</p>

			<FlagGroup onDismissed={handleDismiss}>

				{flags.map((flagId) => {

					return (

						<AutoDismissFlag

							id={flagId}

							icon={

								<SuccessIcon

									label="Success"

									primaryColor={token('color.icon.success')}

									size="medium"

								/>

							}

							key={flagId}

							title={`#${flagId} Your changes were saved`}

							description="I will auto dismiss after 8 seconds."

						/>

					);

				})}

			</FlagGroup>

		</Box>

	);

};



export default AutoDismissFlagDefaultExample;
```

## Appearance

You can style the auto dismiss flag with any of the appearance props. However, we recommend only creating auto dismissing flags that use the info or success appearance and messaging. Don't create warning or error flags that auto dismiss, as people may miss their important notification. 

### Information

Use appearance="info" to alert people to additional information without requiring an action. These are also used for loading states. Add flag 

```jsx
import React from 'react';



import Button from '@atlaskit/button/new';

import { AutoDismissFlag, FlagGroup } from '@atlaskit/flag';

import InformationIcon from '@atlaskit/icon/glyph/info';

import { Box } from '@atlaskit/primitives/compiled';

import { token } from '@atlaskit/tokens';



const AutoDismissFlagInfoExample = () => {

	const [flags, setFlags] = React.useState<Array<number>>([]);



	const addFlag = () => {

		const newFlagId = flags.length + 1;

		const newFlags = flags.slice();

		newFlags.splice(0, 0, newFlagId);



		setFlags(newFlags);

	};



	const handleDismiss = () => {

		setFlags(flags.slice(1));

	};



	return (

		<Box>

			{/* eslint-disable-next-line @atlaskit/ui-styling-standard/enforce-style-prop -- Ignored via go/DSP-18766 */}

			<p style={{ padding: token('space.200') }}>

				<Button appearance="primary" onClick={addFlag}>

					Add flag

				</Button>

			</p>

			<FlagGroup onDismissed={handleDismiss}>

				{flags.map((flagId) => {

					return (

						<AutoDismissFlag

							appearance="info"

							id={flagId}

							icon={

								<InformationIcon

									label="Info"

									secondaryColor={token('color.background.neutral.bold')}

								/>

							}

							key={flagId}

							title={`#${flagId} Where is everybody?`}

							description="I will auto dismiss after 8 seconds."

						/>

					);

				})}

			</FlagGroup>

		</Box>

	);

};



export default AutoDismissFlagInfoExample;
```

### Success

Use appearance="success" to let people know that they have completed an action. Reaffirm the outcome and let the user continue. Add flag 

```jsx
import React from 'react';



import Button from '@atlaskit/button/new';

import { AutoDismissFlag, FlagGroup } from '@atlaskit/flag';

import SuccessIcon from '@atlaskit/icon/glyph/check-circle';

import { Box } from '@atlaskit/primitives/compiled';

import { token } from '@atlaskit/tokens';



const AutoDismissFlagSuccessExample = () => {

	const [flags, setFlags] = React.useState<Array<number>>([]);



	const addFlag = () => {

		const newFlagId = flags.length + 1;

		const newFlags = flags.slice();

		newFlags.splice(0, 0, newFlagId);



		setFlags(newFlags);

	};



	const handleDismiss = () => {

		setFlags(flags.slice(1));

	};



	return (

		<Box>

			{/* eslint-disable-next-line @atlaskit/ui-styling-standard/enforce-style-prop -- Ignored via go/DSP-18766 */}

			<p style={{ padding: token('space.200') }}>

				<Button appearance="primary" onClick={addFlag}>

					Add flag

				</Button>

			</p>

			<FlagGroup onDismissed={handleDismiss}>

				{flags.map((flagId) => {

					return (

						<AutoDismissFlag

							appearance="success"

							id={flagId}

							icon={

								<SuccessIcon

									label="Success"

									secondaryColor={token('color.background.success.bold')}

								/>

							}

							key={flagId}

							title={`#${flagId} Welcome to the room`}

							description="I will auto dismiss after 8 seconds."

						/>

					);

				})}

			</FlagGroup>

		</Box>

	);

};



export default AutoDismissFlagSuccessExample;
```

## Actions

Use actions to show a clickable action at the bottom of the flag. For flags where the appearance is normal, the action will be shown as a link. For all other appearances the action will be shown as a button. Be mindful that many people won't be able to read and decide to select a link within the eight seconds that an auto dismiss flag is available to them. If it's important that people can select the link, use a regular flag instead. Add flag 

```jsx
import React from 'react';



import Button from '@atlaskit/button/new';

import { AutoDismissFlag, FlagGroup } from '@atlaskit/flag';

import SuccessIcon from '@atlaskit/icon/glyph/check-circle';

import { Box } from '@atlaskit/primitives/compiled';

import { token } from '@atlaskit/tokens';



const AutoDismissFlagActionsExample = () => {

	const [flags, setFlags] = React.useState<Array<number>>([]);



	const addFlag = () => {

		const newFlagId = flags.length + 1;

		const newFlags = flags.slice();

		newFlags.splice(0, 0, newFlagId);



		setFlags(newFlags);

	};



	const handleDismiss = () => {

		setFlags(flags.slice(1));

	};



	return (

		<Box>

			{/* eslint-disable-next-line @atlaskit/ui-styling-standard/enforce-style-prop -- Ignored via go/DSP-18766 */}

			<p style={{ padding: token('space.200') }}>

				<Button appearance="primary" onClick={addFlag}>

					Add flag

				</Button>

			</p>

			<FlagGroup onDismissed={handleDismiss}>

				{flags.map((flagId) => {

					return (

						<AutoDismissFlag

							id={flagId}

							icon={

								<SuccessIcon

									label="Success"

									size="medium"

									primaryColor={token('color.icon.information')}

								/>

							}

							key={flagId}

							title={`#${flagId} Hola`}

							description="I will auto dismiss after 8 seconds"

							actions={[

								{

									content: 'with onClick',

									onClick: () => {

										console.log('flag action clicked');

									},

								},

								{

									content: 'with href',

									href: 'https://atlaskit.atlassian.com/',

									target: '_blank',

								},

							]}

						/>

					);

				})}

			</FlagGroup>

		</Box>

	);

};



export default AutoDismissFlagActionsExample;
```

---

[View Original Documentation](https://atlassian.design/components/flag/auto-dismiss-flag/examples)
