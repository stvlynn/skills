# Onboarding (spotlight)

An onboarding spotlight introduces new features to users through focused messages or multi-step tours.

---

## Default

SpotlightTransition will handle the animation of spotlights as they render in. It should wrap any Spotlight components. SpotlightTarget should wrap your spotlight target. 

```jsx
import React, { useState } from 'react';



import Button, { IconButton } from '@atlaskit/button/new';

import CommentAddIcon from '@atlaskit/icon/glyph/media-services/add-comment';

import {

	Spotlight,

	SpotlightManager,

	SpotlightTarget,

	SpotlightTransition,

} from '@atlaskit/onboarding';

import { N0 } from '@atlaskit/theme/colors';

import { token } from '@atlaskit/tokens';



const SpotlightTourExample = () => {

	const [isSpotlightActive, setIsSpotlightActive] = useState(false);

	const start = () => setIsSpotlightActive(true);

	const end = () => setIsSpotlightActive(false);

	return (

		<SpotlightManager>

			<SpotlightTarget name="comment">

				<IconButton icon={CommentAddIcon} label="comment" />

			</SpotlightTarget>

			{/* eslint-disable-next-line @atlaskit/ui-styling-standard/enforce-style-prop -- Ignored via go/DSP-18766 */}

			<div style={{ marginTop: token('space.200') }}>

				<Button appearance="primary" onClick={() => start()}>

					Show example spotlight

				</Button>

			</div>

			<SpotlightTransition>

				{isSpotlightActive && (

					<Spotlight

						actions={[

							{

								onClick: () => end(),

								text: 'OK',

							},

						]}

						heading="Add a comment"

						target="comment"

						key="comment"

						targetRadius={3}

						targetBgColor={N0}

					>

						Quickly add a comment to the issue.

					</Spotlight>

				)}

			</SpotlightTransition>

		</SpotlightManager>

	);

};



export default SpotlightTourExample;
```

## Tours

You can connect spotlights in multi-step onboarding tours. Only one spotlight should be shown at a time. 

```jsx
import React, { useState } from 'react';



import ButtonGroup from '@atlaskit/button/button-group';

import Button, { IconButton } from '@atlaskit/button/new';

import CommentAddIcon from '@atlaskit/icon/glyph/media-services/add-comment';

import CopyIcon from '@atlaskit/icon/glyph/copy';

import {

	Spotlight,

	SpotlightManager,

	SpotlightTarget,

	SpotlightTransition,

} from '@atlaskit/onboarding';

import { N0 } from '@atlaskit/theme/colors';

import { token } from '@atlaskit/tokens';



const SpotlightTourExample = () => {

	const [activeSpotlight, setActiveSpotlight] = useState<null | number>(null);

	const start = () => setActiveSpotlight(0);

	const next = () => setActiveSpotlight((activeSpotlight || 0) + 1);

	const back = () => setActiveSpotlight((activeSpotlight || 1) - 1);

	const end = () => setActiveSpotlight(null);



	const renderActiveSpotlight = () => {

		const spotlights = [

			<Spotlight

				actions={[

					{

						onClick: () => next(),

						text: 'Next',

					},

					{ onClick: () => end(), text: 'Dismiss', appearance: 'subtle' },

				]}

				heading="Add a comment"

				target="comment"

				key="comment"

				targetRadius={3}

				targetBgColor={N0}

			>

				Quickly add a comment to the issue.

			</Spotlight>,

			<Spotlight

				actions={[

					{ onClick: () => end(), text: 'OK' },

					{ onClick: () => back(), text: 'Go back', appearance: 'subtle' },

				]}

				heading="Copy code"

				target="copy"

				key="copy"

				targetRadius={3}

				targetBgColor={N0}

			>

				Trying to bring one of our components into your project? Click to copy the example code,

				then go ahead paste it in your editor.

			</Spotlight>,

		];



		if (activeSpotlight === null) {

			return null;

		}



		return spotlights[activeSpotlight];

	};



	return (

		<SpotlightManager>

			<ButtonGroup label="Choose spotlight options">

				<SpotlightTarget name="comment">

					<IconButton icon={CommentAddIcon} label="comment" />

				</SpotlightTarget>

				<SpotlightTarget name="copy">

					<IconButton icon={CopyIcon} label="Copy" />

				</SpotlightTarget>

			</ButtonGroup>

			{/* eslint-disable-next-line @atlaskit/ui-styling-standard/enforce-style-prop -- Ignored via go/DSP-18766 */}

			<div style={{ marginTop: token('space.200') }}>

				<Button appearance="primary" onClick={() => start()}>

					Start example tour

				</Button>

			</div>

			<SpotlightTransition>{renderActiveSpotlight()}</SpotlightTransition>

		</SpotlightManager>

	);

};



export default SpotlightTourExample;
```

## Blanket tint

If you prefer the spotlight to appear without the tinted blanket background, set the blanketIsTinted prop to false on the SpotlightManager component. 

```jsx
import React, { useState } from 'react';



import Button, { IconButton } from '@atlaskit/button/new';

import CommentAddIcon from '@atlaskit/icon/glyph/media-services/add-comment';

import {

	Spotlight,

	SpotlightManager,

	SpotlightTarget,

	SpotlightTransition,

} from '@atlaskit/onboarding';

import { N0 } from '@atlaskit/theme/colors';

import { token } from '@atlaskit/tokens';



const SpotlightBlanketIsTintedExample = () => {

	const [isSpotlightActive, setIsSpotlightActive] = useState(false);

	const start = () => setIsSpotlightActive(true);

	const end = () => setIsSpotlightActive(false);

	return (

		<SpotlightManager blanketIsTinted={false}>

			<SpotlightTarget name="comment">

				<IconButton icon={CommentAddIcon} label="comment" />

			</SpotlightTarget>

			{/* eslint-disable-next-line @atlaskit/ui-styling-standard/enforce-style-prop -- Ignored via go/DSP-18766 */}

			<div style={{ marginTop: token('space.200') }}>

				<Button appearance="primary" onClick={() => start()}>

					Show example spotlight

				</Button>

			</div>

			<SpotlightTransition>

				{isSpotlightActive && (

					<Spotlight

						actions={[

							{

								onClick: () => end(),

								text: 'OK',

							},

						]}

						heading="Add a comment"

						target="comment"

						key="comment"

						targetRadius={3}

						targetBgColor={N0}

					>

						Quickly add a comment to the issue.

					</Spotlight>

				)}

			</SpotlightTransition>

		</SpotlightManager>

	);

};



export default SpotlightBlanketIsTintedExample;
```

## Actions

### Appearance

You can change the default action button appearance to subtle or subtle-link with the appearance property on the action object. Spotlights should have only one default action that leads people through the onboarding process or prompts an action, with other actions such as "Skip" using the subtle appearance. 

```jsx
import React, { useState } from 'react';



import Button, { IconButton } from '@atlaskit/button/new';

import SearchIcon from '@atlaskit/icon/glyph/search';

import {

	Spotlight,

	SpotlightManager,

	SpotlightTarget,

	SpotlightTransition,

} from '@atlaskit/onboarding';

import { N0 } from '@atlaskit/theme/colors';

import { token } from '@atlaskit/tokens';



const SpotlightActionsAppearance = () => {

	const [isSpotlightActive, setIsSpotlightActive] = useState(false);

	const start = () => setIsSpotlightActive(true);

	const end = () => setIsSpotlightActive(false);

	return (

		<SpotlightManager>

			<SpotlightTarget name="action-button-appearances">

				<IconButton icon={SearchIcon} label="Example" />

			</SpotlightTarget>

			{/* eslint-disable-next-line @atlaskit/ui-styling-standard/enforce-style-prop -- Ignored via go/DSP-18766 */}

			<div style={{ marginTop: token('space.200') }}>

				<Button appearance="primary" onClick={() => start()}>

					Show example spotlight

				</Button>

			</div>

			<SpotlightTransition>

				{isSpotlightActive && (

					<Spotlight

						actions={[

							{ onClick: () => end(), text: 'Default' },

							{

								appearance: 'subtle',

								onClick: () => end(),

								text: 'Subtle',

							},

							{

								appearance: 'subtle-link',

								onClick: () => end(),

								text: 'Subtle link',

							},

						]}

						heading="Action button appearances"

						key="action-button-appearances"

						target="action-button-appearances"

						targetRadius={3}

						targetBgColor={N0}

					>

						You can change the default action button appearance to `subtle` or `subtle-link`.

					</Spotlight>

				)}

			</SpotlightTransition>

		</SpotlightManager>

	);

};



export default SpotlightActionsAppearance;
```

### Actions before element

To add a left-aligned element before the action buttons, use the actionsBeforeElement prop. One use case for this is adding a step number to an onboarding tour with 3 or more steps. 

```jsx
import React, { useState } from 'react';



import ButtonGroup from '@atlaskit/button/button-group';

import Button, { IconButton } from '@atlaskit/button/new';

import CommentAddIcon from '@atlaskit/icon/glyph/media-services/add-comment';

import CopyIcon from '@atlaskit/icon/glyph/copy';

import FullscreenEnterIcon from '@atlaskit/icon/glyph/vid-full-screen-on';

import {

	Spotlight,

	SpotlightManager,

	SpotlightTarget,

	SpotlightTransition,

} from '@atlaskit/onboarding';

import { N0 } from '@atlaskit/theme/colors';

import { token } from '@atlaskit/tokens';



const SpotlightActionsBefore = () => {

	const [activeSpotlight, setActiveSpotlight] = useState<null | number>(null);

	const start = () => setActiveSpotlight(0);

	const next = () => setActiveSpotlight((activeSpotlight || 0) + 1);

	const back = () => setActiveSpotlight((activeSpotlight || 1) - 1);

	const end = () => setActiveSpotlight(null);



	const renderActiveSpotlight = () => {

		const spotlights = [

			<Spotlight

				actionsBeforeElement="1/3"

				actions={[

					{

						onClick: () => next(),

						text: 'Next',

					},

					{ onClick: () => end(), text: 'Dismiss', appearance: 'subtle' },

				]}

				heading="Add a comment"

				target="comment"

				key="comment"

				targetRadius={3}

				targetBgColor={N0}

			>

				Quickly add a comment to the issue.

			</Spotlight>,

			<Spotlight

				actionsBeforeElement="2/3"

				actions={[

					{ onClick: () => next(), text: 'Next' },

					{ onClick: () => back(), text: 'Go back', appearance: 'subtle' },

					{ onClick: () => end(), text: 'Dismiss', appearance: 'subtle' },

				]}

				heading="Copy code"

				target="copy"

				key="copy"

				targetRadius={3}

				targetBgColor={N0}

			>

				Trying to bring one of our components into your project? Click to copy the example code,

				then go ahead paste it in your editor.

			</Spotlight>,

			<Spotlight

				actionsBeforeElement="3/3"

				actions={[

					{ onClick: () => end(), text: 'OK' },

					{ onClick: () => back(), text: 'Go back', appearance: 'subtle' },

				]}

				heading="Expand to full screen"

				target="expand"

				key="expand"

				targetRadius={3}

				targetBgColor={N0}

			>

				For a focused view of the example, you can expand to full screen.

			</Spotlight>,

		];



		if (activeSpotlight === null) {

			return null;

		}



		return spotlights[activeSpotlight];

	};



	return (

		<SpotlightManager>

			<ButtonGroup label="Choose spotlight options">

				<SpotlightTarget name="comment">

					<IconButton icon={CommentAddIcon} label="comment" />

				</SpotlightTarget>

				<SpotlightTarget name="copy">

					<IconButton icon={CopyIcon} label="Copy" />

				</SpotlightTarget>

				<SpotlightTarget name="expand">

					<IconButton icon={FullscreenEnterIcon} label="Full screen" />

				</SpotlightTarget>

			</ButtonGroup>

			{/* eslint-disable-next-line @atlaskit/ui-styling-standard/enforce-style-prop -- Ignored via go/DSP-18766 */}

			<div style={{ marginTop: token('space.200') }}>

				<Button appearance="primary" onClick={() => start()}>

					Start example tour

				</Button>

			</div>

			<SpotlightTransition>{renderActiveSpotlight()}</SpotlightTransition>

		</SpotlightManager>

	);

};



export default SpotlightActionsBefore;
```

## Heading

To add a heading to a spotlight, use the heading prop. For content guidance, see the usage tab. 

### Heading after element

The headingAfterElement prop allows you to place an element to the right of the heading. This is sometimes used to implement a close icon button in a spotlight. 

```jsx
import React, { useState } from 'react';



import Button, { IconButton } from '@atlaskit/button/new';

import CloseIcon from '@atlaskit/icon/glyph/cross';

import CommentAddIcon from '@atlaskit/icon/glyph/media-services/add-comment';

import {

	Spotlight,

	SpotlightManager,

	SpotlightTarget,

	SpotlightTransition,

} from '@atlaskit/onboarding';

import { N0 } from '@atlaskit/theme/colors';

import { token } from '@atlaskit/tokens';



const SpotlightHeadingAfterElement = () => {

	const [isSpotlightActive, setIsSpotlightActive] = useState(false);

	const start = () => setIsSpotlightActive(true);

	const end = () => setIsSpotlightActive(false);

	return (

		<SpotlightManager>

			<SpotlightTarget name="comment">

				<IconButton icon={CommentAddIcon} label="comment" />

			</SpotlightTarget>

			{/* eslint-disable-next-line @atlaskit/ui-styling-standard/enforce-style-prop -- Ignored via go/DSP-18766 */}

			<div style={{ marginTop: token('space.200') }}>

				<Button appearance="primary" onClick={() => start()}>

					Show example spotlight

				</Button>

			</div>

			<SpotlightTransition>

				{isSpotlightActive && (

					<Spotlight

						headingAfterElement={

							<IconButton

								icon={CloseIcon}

								appearance="subtle"

								onClick={() => end()}

								label="Close"

							/>

						}

						actions={[

							{

								onClick: () => end(),

								text: 'OK',

							},

						]}

						heading="Add a comment"

						target="comment"

						key="comment"

						targetRadius={3}

						targetBgColor={N0}

					>

						Quickly add a comment to the issue.

					</Spotlight>

				)}

			</SpotlightTransition>

		</SpotlightManager>

	);

};



export default SpotlightHeadingAfterElement;
```

## Image

You can add an image to a spotlight with the image prop. Most Atlassian illustrations are designed to work with neutral backgrounds, so you may need brand design support to implement an ideal spotlight image. 

```jsx
import React, { useState } from 'react';



import Button from '@atlaskit/button/new';

import {

	Spotlight,

	SpotlightManager,

	SpotlightTarget,

	SpotlightTransition,

} from '@atlaskit/onboarding';

import { N0 } from '@atlaskit/theme/colors';

import { token } from '@atlaskit/tokens';



import spotlightImage from '../assets/this-is-new-jira.png';



const SpotlightImageExample = () => {

	const [isSpotlightActive, setIsSpotlightActive] = useState(false);

	const start = () => setIsSpotlightActive(true);

	const end = () => setIsSpotlightActive(false);

	return (

		<SpotlightManager>

			<SpotlightTarget name="switch">

				<Button>Switch projects</Button>

			</SpotlightTarget>

			{/* eslint-disable-next-line @atlaskit/ui-styling-standard/enforce-style-prop -- Ignored via go/DSP-18766 */}

			<div style={{ marginTop: token('space.200') }}>

				<Button appearance="primary" onClick={() => start()}>

					Show example spotlight

				</Button>

			</div>

			<SpotlightTransition>

				{isSpotlightActive && (

					<Spotlight

						image={spotlightImage}

						actions={[

							{

								onClick: () => end(),

								text: 'OK',

							},

						]}

						target="switch"

						label="Switch projects"

						key="switch"

						targetRadius={3}

						targetBgColor={N0}

					>

						Select the project name and icon to quickly switch between your most recent projects.

					</Spotlight>

				)}

			</SpotlightTransition>

		</SpotlightManager>

	);

};



export default SpotlightImageExample;
```

## Pulse

When spotlights are active, a pulsing outline helps draw attention to the target. It's possible for you to use this spotlight pulse in custom ways. For example, you can apply the pulse on the target element before the spotlight is active, and trigger the spotlight the first time a person interacts with it. 

```jsx
import React, { useState } from 'react';



import ButtonGroup from '@atlaskit/button/button-group';

import Button from '@atlaskit/button/new';

import {

	Spotlight,

	SpotlightManager,

	SpotlightPulse,

	SpotlightTarget,

	SpotlightTransition,

} from '@atlaskit/onboarding';

import { N0 } from '@atlaskit/theme/colors';



const SpotlightPulseExample = () => {

	const [isSpotlightActive, setIsSpotlightActive] = useState(false);

	const start = () => setIsSpotlightActive(true);

	const end = () => setIsSpotlightActive(false);

	return (

		<SpotlightManager>

			<ButtonGroup label="Choose spotlight options">

				<SpotlightTarget name="new">

					<SpotlightPulse radius={3} pulse={isSpotlightActive ? false : true}>

						<Button onClick={() => start()}>New feature</Button>

					</SpotlightPulse>

				</SpotlightTarget>

				<SpotlightTarget name="copy">

					<Button>Existing feature</Button>

				</SpotlightTarget>

			</ButtonGroup>



			<SpotlightTransition>

				{isSpotlightActive && (

					<Spotlight

						actions={[

							{

								onClick: () => end(),

								text: 'OK',

							},

						]}

						heading="Spotlight pulse"

						target="new"

						key="new"

						targetRadius={3}

						targetBgColor={N0}

					>

						Announcing new features with a spotlight pulse is an onboarding pattern that you can

						explore.

					</Spotlight>

				)}

			</SpotlightTransition>

		</SpotlightManager>

	);

};



export default SpotlightPulseExample;
```

### Turning off the pulse

You can turn off the pulsing animation by setting the pulse prop to false. 

```jsx
import React, { useState } from 'react';



import ButtonGroup from '@atlaskit/button/button-group';

import Button from '@atlaskit/button/new';

import {

	Spotlight,

	SpotlightManager,

	SpotlightPulse,

	SpotlightTarget,

	SpotlightTransition,

} from '@atlaskit/onboarding';

import { N0 } from '@atlaskit/theme/colors';



const SpotlightPulseExample = () => {

	const [isSpotlightActive, setIsSpotlightActive] = useState(false);

	const start = () => setIsSpotlightActive(true);

	const end = () => setIsSpotlightActive(false);

	return (

		<SpotlightManager>

			<ButtonGroup label="Choose spotlight options">

				<SpotlightTarget name="new">

					<SpotlightPulse radius={3} pulse={false}>

						<Button onClick={() => start()}>New feature</Button>

					</SpotlightPulse>

				</SpotlightTarget>

				<SpotlightTarget name="copy">

					<Button>Existing feature</Button>

				</SpotlightTarget>

			</ButtonGroup>



			<SpotlightTransition>

				{isSpotlightActive && (

					<Spotlight

						actions={[

							{

								onClick: () => end(),

								text: 'OK',

							},

						]}

						heading="Spotlight pulse"

						target="new"

						key="new"

						targetRadius={3}

						targetBgColor={N0}

						pulse={false}

					>

						Announcing new features with a spotlight pulse is an onboarding pattern that you can

						explore.

					</Spotlight>

				)}

			</SpotlightTransition>

		</SpotlightManager>

	);

};



export default SpotlightPulseExample;
```

## Dialog placement

By default, a spotlight dialog will be positioned to the "bottom left" relative to the target. You can change this by setting your desired position in the dialogPlacement prop. 

```jsx
import React, { useState } from 'react';



import Button from '@atlaskit/button/standard-button';

import CloseIcon from '@atlaskit/icon/glyph/cross';

import {

	Spotlight,

	SpotlightManager,

	SpotlightTarget,

	SpotlightTransition,

} from '@atlaskit/onboarding';

import { N0 } from '@atlaskit/theme/colors';

import { token } from '@atlaskit/tokens';



type Placement = (typeof options)[number];



const options = [

	'top right',

	'top center',

	'top left',

	'right bottom',

	'right middle',

	'right top',

	'bottom left',

	'bottom center',

	'bottom right',

	'left top',

	'left middle',

	'left bottom',

] as const;



const SpotlightDialogPlacement = () => {

	const [isSpotlightActive, setIsSpotlightActive] = useState(false);

	const [dialogPlacement, setDialogPlacement] = useState(0);

	const start = () => setIsSpotlightActive(true);

	const end = () => setIsSpotlightActive(false);

	const shiftPlacementOption = () => {

		if (dialogPlacement !== options.length - 1) {

			return setDialogPlacement(dialogPlacement + 1);

		}

		return setDialogPlacement(0);

	};

	const placement = options[dialogPlacement];



	return (

		<SpotlightManager>

			<SpotlightTarget name="placement">

				<Button>Example target</Button>

			</SpotlightTarget>

			{/* eslint-disable-next-line @atlaskit/ui-styling-standard/enforce-style-prop -- Ignored via go/DSP-18766 */}

			<div style={{ marginTop: token('space.200') }}>

				<Button appearance="primary" onClick={() => start()}>

					Show example spotlight

				</Button>

			</div>

			<SpotlightTransition>

				{isSpotlightActive ? (

					<Spotlight

						heading={`Dialog placement: ${placement}`}

						headingAfterElement={

							<Button

								iconBefore={

									<CloseIcon

										label="Close"

										primaryColor={N0}

									/>

								}

								onClick={() => end()}

							/>

						}

						actions={[

							{

								onClick: () => shiftPlacementOption(),

								text: 'Shift dialog placement',

							},

						]}

						dialogPlacement={placement as Placement}

						target="placement"

						key="placement"

						targetRadius={3}

						targetBgColor={N0}

					>

						You can set where the dialog should appear relative to the contents of the children. Try

						out the options by clicking the action below.

					</Spotlight>

				) : null}

			</SpotlightTransition>

		</SpotlightManager>

	);

};



export default SpotlightDialogPlacement;
```

## Dialog width

You can set a dialog width for a spotlight dialog with the dialogWidth prop. The minimum supported width is 160px, and the maximum is 600px. 

```jsx
import React, { useState } from 'react';



import ButtonGroup from '@atlaskit/button/button-group';

import Button, { IconButton } from '@atlaskit/button/new';

import CommentAddIcon from '@atlaskit/icon/glyph/media-services/add-comment';

import CopyIcon from '@atlaskit/icon/glyph/copy';

import FullscreenEnterIcon from '@atlaskit/icon/glyph/vid-full-screen-on';

import {

	Spotlight,

	SpotlightManager,

	SpotlightTarget,

	SpotlightTransition,

} from '@atlaskit/onboarding';

import { N0 } from '@atlaskit/theme/colors';

import { token } from '@atlaskit/tokens';



const SpotlightDialogWidth = () => {

	const [activeSpotlight, setActiveSpotlight] = useState<null | number>(null);

	const start = () => setActiveSpotlight(0);

	const next = () => setActiveSpotlight((activeSpotlight || 0) + 1);

	const back = () => setActiveSpotlight((activeSpotlight || 1) - 1);

	const end = () => setActiveSpotlight(null);



	const renderActiveSpotlight = () => {

		const spotlights = [

			<Spotlight

				dialogWidth={600}

				actionsBeforeElement="1/3"

				actions={[

					{

						onClick: () => next(),

						text: 'Next',

					},

					{ onClick: () => end(), text: 'Dismiss', appearance: 'subtle' },

				]}

				heading="Add a comment"

				target="comment"

				key="comment"

				targetRadius={3}

				targetBgColor={N0}

			>

				Quickly add a comment to the issue.

			</Spotlight>,

			<Spotlight

				dialogWidth={400}

				actionsBeforeElement="2/3"

				actions={[

					{ onClick: () => next(), text: 'Next' },

					{ onClick: () => back(), text: 'Go back', appearance: 'subtle' },

					{ onClick: () => end(), text: 'Dismiss', appearance: 'subtle' },

				]}

				heading="Copy code"

				target="copy"

				key="copy"

				targetRadius={3}

				targetBgColor={N0}

			>

				Trying to bring one of our components into your project? Click to copy the example code,

				then go ahead paste it in your editor.

			</Spotlight>,

			<Spotlight

				dialogWidth={250}

				actionsBeforeElement="3/3"

				actions={[

					{ onClick: () => end(), text: 'OK' },

					{ onClick: () => back(), text: 'Go back', appearance: 'subtle' },

				]}

				heading="Expand to full screen"

				target="expand"

				key="expand"

				targetRadius={3}

				targetBgColor={N0}

			>

				For a focused view of the example, you can expand to full screen.

			</Spotlight>,

		];



		if (activeSpotlight === null) {

			return null;

		}



		return spotlights[activeSpotlight];

	};



	return (

		<SpotlightManager>

			<ButtonGroup label="Choose spotlight options">

				<SpotlightTarget name="comment">

					<IconButton icon={CommentAddIcon} label="comment" />

				</SpotlightTarget>

				<SpotlightTarget name="copy">

					<IconButton icon={CopyIcon} label="Copy" />

				</SpotlightTarget>

				<SpotlightTarget name="expand">

					<IconButton icon={FullscreenEnterIcon} label="Full screen" />

				</SpotlightTarget>

			</ButtonGroup>

			{/* eslint-disable-next-line @atlaskit/ui-styling-standard/enforce-style-prop -- Ignored via go/DSP-18766 */}

			<div style={{ marginTop: token('space.200') }}>

				<Button appearance="primary" onClick={() => start()}>

					Start example tour

				</Button>

			</div>

			<SpotlightTransition>{renderActiveSpotlight()}</SpotlightTransition>

		</SpotlightManager>

	);

};



export default SpotlightDialogWidth;
```

## Target border radius

The border radius of the spotlight target needs to be explicitly set. In the next example, the first spotlight applies the default behavior, the second spotlight sets targetRadius to 3 to match a target button, and the final spotlight has targetRadius to 24 to match a round target. 

```jsx
import React, { useState } from 'react';



import Avatar from '@atlaskit/avatar';

import ButtonGroup from '@atlaskit/button/button-group';

import Button, { IconButton } from '@atlaskit/button/new';

import CommentAddIcon from '@atlaskit/icon/glyph/media-services/add-comment';

import CopyIcon from '@atlaskit/icon/glyph/copy';

import {

	Spotlight,

	SpotlightManager,

	SpotlightTarget,

	SpotlightTransition,

} from '@atlaskit/onboarding';

import { N0 } from '@atlaskit/theme/colors';

import { token } from '@atlaskit/tokens';



const SpotlightTargetRadius = () => {

	const [activeSpotlight, setActiveSpotlight] = useState<null | number>(null);

	const start = () => setActiveSpotlight(0);

	const next = () => setActiveSpotlight((activeSpotlight || 0) + 1);

	const back = () => setActiveSpotlight((activeSpotlight || 1) - 1);

	const end = () => setActiveSpotlight(null);



	const renderActiveSpotlight = () => {

		const spotlights = [

			<Spotlight

				actions={[

					{

						onClick: () => next(),

						text: 'Next',

					},

					{ onClick: () => end(), text: 'Dismiss', appearance: 'subtle' },

				]}

				heading="Add a comment"

				target="comment"

				key="comment"

				targetBgColor={N0}

			>

				Quickly add a comment to the issue.

			</Spotlight>,

			<Spotlight

				targetRadius={3}

				actions={[

					{ onClick: () => next(), text: 'Next' },

					{ onClick: () => back(), text: 'Go back', appearance: 'subtle' },

					{ onClick: () => end(), text: 'Dismiss', appearance: 'subtle' },

				]}

				heading="Copy code"

				target="copy"

				key="copy"

				targetBgColor={N0}

			>

				Trying to bring one of our components into your project? Click to copy the example code,

				then go ahead paste it in your editor.

			</Spotlight>,

			<Spotlight

				targetRadius={24}

				actions={[

					{ onClick: () => end(), text: 'OK' },

					{ onClick: () => back(), text: 'Go back', appearance: 'subtle' },

				]}

				heading="Upload a profile picture"

				target="avatar"

				key="avatar"

				targetBgColor={N0}

			>

				Having a profile picture helps you and your team by making your contributions more

				identifiable. If you'd rather remain mysterious, that's okay too! You do you.

			</Spotlight>,

		];



		if (activeSpotlight === null) {

			return null;

		}



		return spotlights[activeSpotlight];

	};



	return (

		<SpotlightManager>

			<ButtonGroup label="Choose spotlight options">

				<SpotlightTarget name="comment">

					<IconButton icon={CommentAddIcon} label="comment" />

				</SpotlightTarget>

				<SpotlightTarget name="copy">

					<IconButton icon={CopyIcon} label="Copy" />

				</SpotlightTarget>

			</ButtonGroup>

			<SpotlightTarget name="avatar">

				<Avatar />

			</SpotlightTarget>

			{/* eslint-disable-next-line @atlaskit/ui-styling-standard/enforce-style-prop -- Ignored via go/DSP-18766 */}

			<div style={{ marginTop: token('space.200') }}>

				<Button appearance="primary" onClick={() => start()}>

					Start example tour

				</Button>

			</div>

			<SpotlightTransition>{renderActiveSpotlight()}</SpotlightTransition>

		</SpotlightManager>

	);

};



export default SpotlightTargetRadius;
```

## Target background color

Sometimes the blanket can affect the background color of the target element. For example, subtle buttons are semi-transparent, which causes them to look darker when the blanket is applied. In cases like this, you can pass a color value to targetBgColor to make your target stand out properly. 

```jsx
import React, { useState } from 'react';



import ButtonGroup from '@atlaskit/button/button-group';

import Button, { IconButton } from '@atlaskit/button/new';

import CommentAddIcon from '@atlaskit/icon/glyph/media-services/add-comment';

import CopyIcon from '@atlaskit/icon/glyph/copy';

import {

	Spotlight,

	SpotlightManager,

	SpotlightTarget,

	SpotlightTransition,

} from '@atlaskit/onboarding';

import { N0 } from '@atlaskit/theme/colors';

import { token } from '@atlaskit/tokens';



const SpotlightTargetBackground = () => {

	const [activeSpotlight, setActiveSpotlight] = useState<null | number>(null);

	const start = () => setActiveSpotlight(0);

	const next = () => setActiveSpotlight((activeSpotlight || 0) + 1);

	const back = () => setActiveSpotlight((activeSpotlight || 1) - 1);

	const end = () => setActiveSpotlight(null);



	const renderActiveSpotlight = () => {

		const spotlights = [

			<Spotlight

				actions={[

					{

						onClick: () => next(),

						text: 'Next',

					},

					{ onClick: () => end(), text: 'Dismiss', appearance: 'subtle' },

				]}

				heading="No targetBgColor set"

				target="comment"

				key="comment"

				targetRadius={3}

			>

				You can see that even though the spotlight pulse surrounds the button, it no longer stands

				out on the page.

			</Spotlight>,

			<Spotlight

				targetBgColor={N0}

				actions={[

					{ onClick: () => end(), text: 'OK' },

					{ onClick: () => back(), text: 'Go back', appearance: 'subtle' },

				]}

				heading="With targetBg set"

				target="copy"

				key="copy"

				targetRadius={3}

			>

				Setting the `targetBgColor` ensures that the cloned spotlight target has all the context it

				needs to stand out properly.

			</Spotlight>,

		];



		if (activeSpotlight === null) {

			return null;

		}



		return spotlights[activeSpotlight];

	};



	return (

		<SpotlightManager>

			<ButtonGroup label="Choose spotlight options">

				<SpotlightTarget name="comment">

					<IconButton icon={CommentAddIcon} label="comment" />

				</SpotlightTarget>

				<SpotlightTarget name="copy">

					<IconButton icon={CopyIcon} label="Copy" />

				</SpotlightTarget>

			</ButtonGroup>

			{/* eslint-disable-next-line @atlaskit/ui-styling-standard/enforce-style-prop -- Ignored via go/DSP-18766 */}

			<div style={{ marginTop: token('space.200') }}>

				<Button appearance="primary" onClick={() => start()}>

					Start example tour

				</Button>

			</div>

			<SpotlightTransition>{renderActiveSpotlight()}</SpotlightTransition>

		</SpotlightManager>

	);

};



export default SpotlightTargetBackground;
```

## Target replacement

You can replace the original target with another component using the targetReplacement prop. 

```jsx
/**

 * @jsxRuntime classic

 * @jsx jsx

 */

import { type ImgHTMLAttributes, useState } from 'react';



import { css, jsx } from '@compiled/react';



import Button from '@atlaskit/button/new';

import {

	Spotlight,

	SpotlightManager,

	SpotlightPulse,

	SpotlightTarget,

	SpotlightTransition,

} from '@atlaskit/onboarding';

import { token } from '@atlaskit/tokens';



import logoInverted from '../assets/logo-inverted.png';

import logo from '../assets/logo.png';



const Replacement = (rect: any) => {

	const style = { overflow: 'hidden', ...rect };



	return (

		// eslint-disable-next-line @atlaskit/ui-styling-standard/enforce-style-prop -- Ignored via go/DSP-18766

		<SpotlightPulse style={style}>

			<Image alt="I replace the target element." src={logoInverted} />

		</SpotlightPulse>

	);

};



const imageStyles = css({

	width: '128px',

	height: '128px',

});



const Image = ({ alt, src }: ImgHTMLAttributes<HTMLImageElement>) => (

	<img src={src} alt={alt} css={imageStyles} />

);



const SpotlightTargetReplacementExample = () => {

	const [isSpotlightActive, setIsSpotlightActive] = useState(false);

	const start = () => setIsSpotlightActive(true);

	const end = () => setIsSpotlightActive(false);

	return (

		<SpotlightManager>

			{/* eslint-disable-next-line @atlaskit/ui-styling-standard/enforce-style-prop -- Ignored via go/DSP-18766 */}

			<img alt="hidden" src={logoInverted} style={{ display: 'none' }} />

			<SpotlightTarget name="target-replacement-example">

				<Image alt="I will be replaced..." src={logo} />

			</SpotlightTarget>

			{/* eslint-disable-next-line @atlaskit/ui-styling-standard/enforce-style-prop -- Ignored via go/DSP-18766 */}

			<div style={{ marginTop: token('space.200') }}>

				<Button appearance="primary" onClick={() => start()}>

					Show example spotlight

				</Button>

			</div>

			<SpotlightTransition>

				{isSpotlightActive && (

					<Spotlight

						targetReplacement={Replacement}

						actions={[{ onClick: () => end(), text: 'OK' }]}

						dialogPlacement="bottom left"

						key="target-replacement-example"

						heading="Target replacement"

						target="target-replacement-example"

						targetRadius={3}

					>

						You can replace the original target with another component using the `targetReplacement`

						prop.

					</Spotlight>

				)}

			</SpotlightTransition>

		</SpotlightManager>

	);

};



export default SpotlightTargetReplacementExample;
```

## Conditional spotlight targets

You can use the useSpotlight hook to check if a spotlight target is rendered or not. This allows you to conditionally add steps into a spotlight tour. 

```jsx
import React, { useState } from 'react';



import ButtonGroup from '@atlaskit/button/button-group';

import Button, { IconButton } from '@atlaskit/button/new';

import CommentAddIcon from '@atlaskit/icon/glyph/media-services/add-comment';

import CopyIcon from '@atlaskit/icon/glyph/copy';

import FullscreenEnterIcon from '@atlaskit/icon/glyph/vid-full-screen-on';

import {

	Spotlight,

	SpotlightManager,

	SpotlightTarget,

	SpotlightTransition,

	useSpotlight,

} from '@atlaskit/onboarding';

import { N0 } from '@atlaskit/theme/colors';

import { token } from '@atlaskit/tokens';



const SpotlightWithConditionalTargets = () => {

	const [active, setActive] = useState<number | null>(null);

	const [isSecondTargetVisible, setIsSecondTargetVisible] = useState(true);

	const { isTargetRendered } = useSpotlight();



	const start = () => setActive(0);

	const next = () => setActive((active || 0) + 1);

	const back = () => setActive((active || 0) - 1);

	const end = () => setActive(null);



	const renderActiveSpotlight = () => {

		if (active == null) {

			return null;

		}



		const spotlights = [

			{

				target: 'comment',

				element: (

					<Spotlight

						actions={[

							{

								onClick: () => next(),

								text: 'Next',

							},

							{ onClick: () => end(), text: 'Dismiss', appearance: 'subtle' },

						]}

						heading="Add a comment"

						target="comment"

						key="comment"

						targetRadius={3}

						targetBgColor={N0}

					>

						Quickly add a comment to the issue.

					</Spotlight>

				),

			},

			{

				target: 'copy',

				element: (

					<Spotlight

						actions={[

							{ onClick: () => next(), text: 'Next' },

							{ onClick: () => back(), text: 'Go back', appearance: 'subtle' },

							{ onClick: () => end(), text: 'Dismiss', appearance: 'subtle' },

						]}

						heading="Copy code"

						target="copy"

						key="copy"

						targetRadius={3}

						targetBgColor={N0}

					>

						Trying to bring one of our components into your project? Click to copy the example code,

						then go ahead paste it in your editor.

					</Spotlight>

				),

			},

			{

				target: 'expand',

				element: (

					<Spotlight

						actions={[

							{ onClick: () => end(), text: 'OK' },

							{ onClick: () => back(), text: 'Go back', appearance: 'subtle' },

						]}

						heading="Expand to full screen"

						target="expand"

						key="expand"

						targetRadius={3}

						targetBgColor={N0}

					>

						For a focused view of the example, you can expand to full screen.

					</Spotlight>

				),

			},

		]

			.filter(({ target }) => isTargetRendered(target))

			.map(({ element }) => element);



		return spotlights[active];

	};



	return (

		<>

			<ButtonGroup label="Choose spotlight options">

				<SpotlightTarget name="comment">

					<IconButton icon={CommentAddIcon} label="comment" />

				</SpotlightTarget>

				{isSecondTargetVisible && (

					<SpotlightTarget name="copy">

						<IconButton icon={CopyIcon} label="Copy" />

					</SpotlightTarget>

				)}

				<SpotlightTarget name="expand">

					<IconButton icon={FullscreenEnterIcon} label="Full screen" />

				</SpotlightTarget>

			</ButtonGroup>

			{/* eslint-disable-next-line @atlaskit/ui-styling-standard/enforce-style-prop -- Ignored via go/DSP-18766 */}

			<div style={{ marginTop: token('space.200') }}>

				<ButtonGroup label="Choose spotlight options">

					<Button appearance="primary" onClick={() => start()}>

						Start example tour

					</Button>

					<Button onClick={() => setIsSecondTargetVisible(!isSecondTargetVisible)}>

						Show/hide second spotlight target

					</Button>

				</ButtonGroup>

			</div>

			<SpotlightTransition>{renderActiveSpotlight()}</SpotlightTransition>

		</>

	);

};



export default function SpotlightWithConditionalTargetsExample() {

	return (

		<SpotlightManager>

			<SpotlightWithConditionalTargets />

		</SpotlightManager>

	);

}
```

---

[View Original Documentation](https://atlassian.design/components/onboarding/examples)
