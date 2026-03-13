# Spotlight card

A spotlight card is for onboarding messages that need a more flexible layout, or don't require a dialog.

---

## Default

A spotlight card shows onboarding messages without requiring a dialog and target element the way spotlight does. Spotlight cards are generally more flexible, so you can design more bespoke experiences as seen in the other examples below. 

```jsx
import React from 'react';



import { SpotlightCard } from '@atlaskit/onboarding';



const SpotlightCardDefaultExample = () => {

	return (

		<SpotlightCard>

			Select the project name and icon to quickly switch between your most recent projects.

		</SpotlightCard>

	);

};



export default SpotlightCardDefaultExample;
```

## Rich text

To display rich text messages, wrap the content with a block level element, such as a div. 

```jsx
import React from 'react';



import { SpotlightCard } from '@atlaskit/onboarding';



const SpotlightCardRichTextExample = () => {

	return (

		<SpotlightCard>

			<div>

				All your <strong>Projects</strong> and <strong>Issues</strong>, including the ones you've

				just created can be found in the sidebar.

			</div>

		</SpotlightCard>

	);

};



export default SpotlightCardRichTextExample;
```

## Flat

To remove the elevation styles from the spotlight card, set the isFlat prop to true. This is useful for situations where you want to place the card as part of a focused onboarding or discovery layout, rather than it being positioned in a dialog above a core UI experience. 

## Welcome to Jira

Tell us about your team so we can personalise your project for you. 

### Why are you trying Jira Software?

```jsx
/**

 * @jsxRuntime classic

 * @jsx jsx

 */

import { type ReactNode } from 'react';



import Button from '@atlaskit/button/new';

import { css, cssMap, jsx } from '@atlaskit/css';

import { SpotlightCard } from '@atlaskit/onboarding';

import { Box } from '@atlaskit/primitives/compiled';

import { ProgressIndicator } from '@atlaskit/progress-indicator';

import { token } from '@atlaskit/tokens';



const wrapperStyles = css({

	display: 'flex',

	alignItems: 'center',

	justifyContent: 'center',

	flexDirection: 'column',

});



const headingStyles = css({

	display: 'flex',

	alignItems: 'center',

	justifyContent: 'space-between',

});



const taglineStyles = css({

	paddingBlockEnd: token('space.200'),

});



const optionStyles = cssMap({

	root: {

		paddingTop: token('space.050'),

		paddingRight: token('space.050'),

		paddingBottom: token('space.050'),

		paddingLeft: token('space.050'),

	},

});



const Option = ({ children }: { children: ReactNode }) => (

	<Box xcss={optionStyles.root}>{children}</Box>

);

const SpotlightCardIsFlat = () => {

	return (

		<div css={wrapperStyles}>

			<div>

				<div css={headingStyles}>

					<h2>Welcome to Jira</h2>

					<ProgressIndicator values={[1, 2, 3]} selectedIndex={0} />

				</div>

				<p css={taglineStyles}>

					Tell us about your team so we can personalise your project for you.

				</p>

				<SpotlightCard heading="Why are you trying Jira Software?" headingLevel={3} isFlat>

					<Option>

						<Button>Learn about agile</Button>

					</Option>

					<Option>

						<Button>Explore the product</Button>

					</Option>

					<Option>

						<Button>How to set up Jira for your team</Button>

					</Option>

				</SpotlightCard>

			</div>

		</div>

	);

};



export default SpotlightCardIsFlat;
```

## Actions

Spotlight card actions work in a similar way to spotlight. You can set the appearance of action buttons to either default (primary), subtle, or subtle-link. 

```jsx
import React from 'react';



import __noop from '@atlaskit/ds-lib/noop';

import { SpotlightCard } from '@atlaskit/onboarding';



const SpotlightCardActionsExample = () => {

	return (

		<SpotlightCard

			actions={[

				{ text: 'Next', onClick: __noop },

				{ text: 'Dismiss', onClick: __noop, appearance: 'subtle' },

			]}

		>

			Select the project name and icon to quickly switch between your most recent projects.

		</SpotlightCard>

	);

};



export default SpotlightCardActionsExample;
```

## Actions before element

To add a left-aligned element before the action buttons, use the actionsBeforeElement prop. 

```jsx
import React from 'react';



import __noop from '@atlaskit/ds-lib/noop';

import { SpotlightCard } from '@atlaskit/onboarding';



const SpotlightCardActionsBeforeExample = () => {

	return (

		<SpotlightCard

			actionsBeforeElement="1/3"

			actions={[

				{ text: 'Next', onClick: __noop },

				{ text: 'Dismiss', onClick: __noop, appearance: 'subtle' },

			]}

		>

			Select the project name and icon to quickly switch between your most recent projects.

		</SpotlightCard>

	);

};



export default SpotlightCardActionsBeforeExample;
```

## Heading

Use the heading prop to add a heading to a spotlight card. 

## Switch it up

```jsx
import React from 'react';



import __noop from '@atlaskit/ds-lib/noop';

import { SpotlightCard } from '@atlaskit/onboarding';



const SpotlightCardHeadingExample = () => {

	return (

		<SpotlightCard

			heading="Switch it up"

			headingLevel={2}

			actionsBeforeElement="1/3"

			actions={[

				{ text: 'Next', onClick: __noop },

				{ text: 'Dismiss', onClick: __noop, appearance: 'subtle' },

			]}

		>

			Select the project name and icon to quickly switch between your most recent projects.

		</SpotlightCard>

	);

};



export default SpotlightCardHeadingExample;
```

## Heading after element

The headingAfterElement prop allows you to place an element to the right of the heading. 

## Switch it up

```jsx
import React from 'react';



import Button from '@atlaskit/button';

import __noop from '@atlaskit/ds-lib/noop';

import CloseIcon from '@atlaskit/icon/glyph/cross';

import { SpotlightCard } from '@atlaskit/onboarding';

import { N0 } from '@atlaskit/theme/colors';

import { token } from '@atlaskit/tokens';



const SpotlightCardHeadingAfterExample = () => {

	return (

		<SpotlightCard

			headingAfterElement={

				<Button

					iconBefore={

						<CloseIcon label="Close" primaryColor={N0} />

					}

					appearance="subtle"

				/>

			}

			heading="Switch it up"

			headingLevel={2}

			actions={[{ text: 'Next', onClick: __noop }]}

		>

			Select the project name and icon to quickly switch between your most recent projects.

		</SpotlightCard>

	);

};



export default SpotlightCardHeadingAfterExample;
```

## Image

You can add an image to a spotlight with the image prop. Although we have an illustration library that you can make use of, please keep in mind that most of those illustrations are designed to work with neutral backgrounds, and you may need further design support to implement an ideal spotlight image. 

## Switch it up

```jsx
import React from 'react';



import __noop from '@atlaskit/ds-lib/noop';

import { SpotlightCard } from '@atlaskit/onboarding';



import spotlightImage from '../assets/this-is-new-jira.png';



const SpotlightCardHeadingExample = () => {

	return (

		<SpotlightCard

			image={<img src={spotlightImage} alt="" width="400" />}

			heading="Switch it up"

			headingLevel={2}

			actions={[

				{ text: 'Next', onClick: __noop },

				{ text: 'Dismiss', onClick: __noop, appearance: 'subtle' },

			]}

		>

			Select the project name and icon to quickly switch between your most recent projects.

		</SpotlightCard>

	);

};



export default SpotlightCardHeadingExample;
```

## Width

The width prop sets the width of the card in pixels. 

## Switch it up

## Switch it up

## Switch it up

```jsx
import React from 'react';



import __noop from '@atlaskit/ds-lib/noop';

import { SpotlightCard } from '@atlaskit/onboarding';

import { token } from '@atlaskit/tokens';



const SpotlightCardWidth = () => {

	return (

		<div

			style={{

				// eslint-disable-next-line @atlaskit/ui-styling-standard/enforce-style-prop -- Ignored via go/DSP-18766

				display: 'flex',

				// eslint-disable-next-line @atlaskit/ui-styling-standard/enforce-style-prop -- Ignored via go/DSP-18766

				flexDirection: 'column',

				// eslint-disable-next-line @atlaskit/ui-styling-standard/enforce-style-prop -- Ignored via go/DSP-18766

				gap: token('space.300'),

			}}

		>

			<SpotlightCard

				width={200}

				heading="Switch it up"

				headingLevel={2}

				actions={[

					{ text: 'Next', onClick: __noop },

					{ text: 'Dismiss', onClick: __noop, appearance: 'subtle' },

				]}

			>

				Select the project name and icon to quickly switch between your most recent projects.

			</SpotlightCard>

			<SpotlightCard

				width={400}

				heading="Switch it up"

				headingLevel={2}

				actions={[

					{ text: 'Next', onClick: __noop },

					{ text: 'Dismiss', onClick: __noop, appearance: 'subtle' },

				]}

			>

				Select the project name and icon to quickly switch between your most recent projects.

			</SpotlightCard>{' '}

			<SpotlightCard

				width={600}

				heading="Switch it up"

				headingLevel={2}

				actions={[

					{ text: 'Next', onClick: __noop },

					{ text: 'Dismiss', onClick: __noop, appearance: 'subtle' },

				]}

			>

				Select the project name and icon to quickly switch between your most recent projects.

			</SpotlightCard>

		</div>

	);

};



export default SpotlightCardWidth;
```

---

[View Original Documentation](https://atlassian.design/components/onboarding/spotlight-card/examples)
