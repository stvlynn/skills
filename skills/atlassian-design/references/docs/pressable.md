# Pressable

A pressable is a primitive for building custom buttons.

---

## Installation

Pressable is a primitive for building custom buttons with Atlassian Design System styling and built-in event tracking. It renders a <button> element. Use pressable when existing buttons can't be customized to fit your needs.

### Package installation information

#### Install

`yarn add @atlaskit/primitives`

#### Source

[Bitbucket.org﻿, (opens new window)](https://bitbucket.org/atlassian/atlassian-frontend-mirror/src/master/design-system/primitives)

npm

[@atlaskit/primitives﻿, (opens new window)](https://www.npmjs.com/package/@atlaskit/primitives)

Bundle

[unpkg.com﻿, (opens new window)](https://unpkg.com/@atlaskit/primitives/dist/)

## Default

Pressable is unstyled by default, aside from basic focus styles.

```jsx
import React, { useCallback } from 'react';



import Pressable from '@atlaskit/primitives/pressable';



export default function Default() {

	const handleClick = useCallback(() => {

		console.log('Clicked');

	}, []);



	return <Pressable onClick={handleClick}>Pressable</Pressable>;

}
```

## Basic styling with XCSS

Pressable can be styled further using the design system styling API, XCSS. Make sure styling indicates the interaction state using :hover and :active pseudo-classes.

```jsx
import React, { useCallback } from 'react';



import { Pressable, xcss } from '@atlaskit/primitives';



const pressableStyles = xcss({

	color: 'color.text.subtle',

	fontWeight: 'font.weight.medium',

	backgroundColor: 'color.background.neutral.subtle',



	':hover': {

		textDecoration: 'underline',

		backgroundColor: 'color.background.neutral.subtle.hovered',

	},

	':active': {

		color: 'color.text',

		backgroundColor: 'color.background.neutral.subtle.pressed',

	},

});



export default function Basic() {

	const handleClick = useCallback(() => {

		console.log('Clicked');

	}, []);



	return (

		<Pressable onClick={handleClick} padding="space.0" xcss={pressableStyles}>

			Edit comment

		</Pressable>

	);

}
```

## Advanced styling

Use a combination of XCSS and other primitives for more complex designs.

```jsx
import React from 'react';



import { Flex, Grid, Pressable, type TextColor, xcss } from '@atlaskit/primitives';

import Box from '@atlaskit/primitives/box';

import { media } from '@atlaskit/primitives/responsive';

import Stack from '@atlaskit/primitives/stack';

import Text from '@atlaskit/primitives/text';



const pressableStyles = xcss({

	borderRadius: '3px',

	borderColor: 'color.border',

	borderWidth: 'border.width',

	borderStyle: 'solid',

	color: 'color.text',

	backgroundColor: 'color.background.neutral.subtle',



	':hover': {

		backgroundColor: 'color.background.neutral.subtle.hovered',

	},

	':active': {

		backgroundColor: 'color.background.neutral.subtle.pressed',

	},

});



const valueStyles = xcss({

	font: 'font.heading.xlarge',

});



const gridStyles = xcss({

	[media.above.sm]: {

		gridTemplateColumns: '1fr 1fr',

	},

	[media.above.md]: {

		gridTemplateColumns: '1fr 1fr 1fr',

	},

});



const ProjectStatus = ({

	value,

	title,

	subtitle,

	color,

}: {

	value: number;

	title: string;

	subtitle: string;

	color: TextColor;

}) => {

	return (

		<Pressable xcss={pressableStyles} padding="space.150">

			<Flex as="span" gap="space.150" alignItems="center">

				<Text color={color}>

					<Box as="span" xcss={valueStyles}>

						{value}

					</Box>

				</Text>

				<Stack as="span" space="space.0" alignInline="start">

					<Text weight="semibold">{title}</Text>

					<Text size="small" color="color.text.subtlest">

						{subtitle}

					</Text>

				</Stack>

			</Flex>

		</Pressable>

	);

};



export default function Styled() {

	return (

		<Stack space="space.150">

			<Text weight="bold" size="large">

				You're following 5 active projects, here's the breakdown.

			</Text>

			<Grid rowGap="space.100" columnGap="space.100" templateColumns="1fr" xcss={gridStyles}>

				<ProjectStatus

					value={2}

					title="On track"

					subtitle="-1 from last week"

					color="color.text.success"

				/>

				<ProjectStatus

					value={1}

					title="At risk"

					subtitle="+1 from last week"

					color="color.text.warning"

				/>

				<ProjectStatus value={0} title="Off track" subtitle="No change" color="color.text.danger" />

				<ProjectStatus

					value={2}

					title="No update"

					subtitle="+2 from last week"

					color="color.text.discovery"

				/>

				<ProjectStatus value={0} title="Cancelled" subtitle="No change" color="color.text.subtle" />

				<ProjectStatus

					value={1}

					title="Completed"

					subtitle="+1 from last week"

					color="color.text.information"

				/>

			</Grid>

		</Stack>

	);

}
```

## Disabled

You can disable pressable buttons with the isDisabled prop. Disabled styles should be applied and defined conditionally using XCSS. Disabled buttons can cause accessibility issues (disabled elements are not in the tab order) so wherever possible, avoid using isDisabled. Instead, use validation or other techniques to show users how to proceed.

```jsx
import React, { useCallback, useState } from 'react';



import { Inline, Pressable, Stack, xcss } from '@atlaskit/primitives';

import Toggle from '@atlaskit/toggle';



const pressableStyles = xcss({

	fontWeight: 'font.weight.medium',

	backgroundColor: 'color.background.neutral.subtle',

});



const enabledStyles = xcss({

	color: 'color.text.subtle',



	':hover': {

		textDecoration: 'underline',

		backgroundColor: 'color.background.neutral.subtle.hovered',

	},

	':active': {

		color: 'color.text',

		backgroundColor: 'color.background.neutral.subtle.pressed',

	},

});



const disabledStyles = xcss({

	color: 'color.text.disabled',

});



export default function Disabled() {

	const handleClick = useCallback(() => {

		console.log('Clicked');

	}, []);



	const [isDisabled, setIsDisabled] = useState(true);

	const toggleDisabled = useCallback((event: React.ChangeEvent<HTMLInputElement>) => {

		setIsDisabled(event.currentTarget.checked);

	}, []);

	return (

		<Stack space="space.200" alignInline="start">

			<Inline alignBlock="center" space="space.100">

				<Toggle isChecked={isDisabled} id="is-disabled" onChange={toggleDisabled} />

				<label htmlFor="is-disabled">Disabled</label>

			</Inline>

			<Pressable

				isDisabled={isDisabled}

				onClick={handleClick}

				padding="space.0"

				xcss={[pressableStyles, isDisabled ? disabledStyles : enabledStyles]}

			>

				Edit comment

			</Pressable>

		</Stack>

	);

}
```

## Buttons without visible labels

For buttons without visible labels such as icon buttons, make an accessible label available using the visually hidden component. This renders hidden text inside the button for assistive technologies, which is preferable to an aria-label attribute because not all screen readers translate these between languages. Also, consider providing a tooltip to help sighted users understand the button's purpose.

```jsx
import React from 'react';



import { ButtonGroup } from '@atlaskit/button';

import EmojiAddIcon from '@atlaskit/icon/glyph/emoji-add';

import { Pressable, Text, xcss } from '@atlaskit/primitives';

import { token } from '@atlaskit/tokens';

import Tooltip from '@atlaskit/tooltip';

import VisuallyHidden from '@atlaskit/visually-hidden';



import { ReactionsList } from '../../utils/reactions';



const pressableStyles = xcss({

	backgroundColor: 'color.background.neutral.subtle',

	borderWidth: 'border.width',

	borderStyle: 'solid',

	borderColor: 'color.border',

	borderRadius: '8px',

	paddingInline: 'space.100',

	height: '27px',

	display: 'flex',

	alignItems: 'center',



	':hover': {

		backgroundColor: 'color.background.neutral.subtle.hovered',

	},

	':active': {

		backgroundColor: 'color.background.neutral.subtle.pressed',

	},

});



type ReactionButtonProps = {

	emoji?: string;

	name?: string;

	reactions?: number;

};



const ReactionButton = ({ emoji, name, reactions }: ReactionButtonProps) => {

	return (

		<Tooltip

			content={

				name && reactions ? (

					<p>

						<strong>{name}</strong>

						<ReactionsList reactions={reactions} />

					</p>

				) : (

					'Add a reaction'

				)

			}

		>

			<Pressable xcss={pressableStyles}>

				{emoji ? (

					<Text size="small" color="color.text.subtle">

						{emoji} {reactions}

					</Text>

				) : (

					<EmojiAddIcon

						size="small"

						primaryColor={token('color.icon')}

						label=""

					/>

				)}

				<VisuallyHidden>Add a {name && `${name} `}reaction</VisuallyHidden>

			</Pressable>

		</Tooltip>

	);

};



export default function IconButtons() {

	return (

		<ButtonGroup label="Reactions">

			<ReactionButton emoji="👏" name="Clap" reactions={26} />

			<ReactionButton emoji="❤️" name="Heart" reactions={4} />

			<ReactionButton emoji="👍" name="Thumbs up" reactions={17} />

			<ReactionButton />

		</ButtonGroup>

	);

}
```

## HTML attributes

Pressable passes all valid HTML attributes to the underlying <button> element. The type attribute defaults to button to prevent unintentionally submitting forms.

```jsx
import React from 'react';



import Pressable from '@atlaskit/primitives/pressable';



export default function HtmlAttributes() {

	return <Pressable type="submit">Submit form</Pressable>;

}
```

## Event tracking

Pressable has utilities to make tracking events easier. Events won't be captured unless listeners are set up to handle them.

### Track events for any analytics provider

Pressable comes with built-in Atlaskit analytics support using the Analytics next package, and fires events for available listeners. Currently this is only available for onClick. Events always fire on the atlaskit channel. To fire events on other channels as well, use the provided analyticsEvent in onClick. To configure event data, use componentName (defaults to 'Pressable') and use analyticsContext to pass other metadata. See the event data in the console.

```jsx
import React, { useCallback } from 'react';



import { AnalyticsListener, type UIAnalyticsEvent } from '@atlaskit/analytics-next';

import { ButtonGroup } from '@atlaskit/button';

import Pressable from '@atlaskit/primitives/pressable';



export default function Analytics() {

	const handleEvent = useCallback((event: UIAnalyticsEvent, channel?: string) => {

		console.log(`Channel: '${channel}'`, event);

	}, []);



	return (

		<AnalyticsListener channel="*" onEvent={handleEvent}>

			<ButtonGroup label="Pressable buttons with analytics">

				<Pressable>Default</Pressable>

				<Pressable

					onClick={(_, analyticsEvent) => {

						analyticsEvent.fire('my-channel');

					}}

				>

					Fires on "my-channel"

				</Pressable>

				<Pressable

					componentName="MyButton"

					analyticsContext={{

						color: 'blue',

						someId: 937458,

					}}

				>

					Customized event data

				</Pressable>

			</ButtonGroup>

		</AnalyticsListener>

	);

}
```

### Track events for Atlassian internal services

The Atlassian analytics bridge makes Atlaskit analytics events compatible with GASv3 (Global Analytics Service). This can also inject an actionSubjectId to the event if required. See the event data in the console. By default, pressable fires React UFO (Unified Frontend Observability) press interactions for available listeners. This helps Atlassian measure performance and reliability. You can provide more detail using the interactionName prop.

```jsx
import React, { useCallback } from 'react';



import { AnalyticsListener, type UIAnalyticsEvent } from '@atlaskit/analytics-next';

import Pressable from '@atlaskit/primitives/pressable';

import {

	ANALYTICS_BRIDGE_CHANNEL,

	extractAWCDataFromEvent,

	fireUIAnalytics,

} from '@atlassian/analytics-bridge';



export default function AnalyticsGASv3() {

	const handleEvent = useCallback((event: UIAnalyticsEvent, channel?: string) => {

		console.log(`Channel: '${channel}'`, extractAWCDataFromEvent(event));

	}, []);



	const handleClick = useCallback(

		(_: React.MouseEvent<HTMLButtonElement, MouseEvent>, analyticsEvent: UIAnalyticsEvent) => {

			fireUIAnalytics(analyticsEvent, 'theActionSubjectId');

		},

		[],

	);



	return (

		<AnalyticsListener channel={ANALYTICS_BRIDGE_CHANNEL} onEvent={handleEvent}>

			<Pressable

				onClick={handleClick}

				analyticsContext={{

					attributes: {

						color: 'blue',

						someId: 937458,

					},

				}}

			>

				Fire GASv3 compatible event

			</Pressable>

		</AnalyticsListener>

	);

}
```

```jsx
import React, { useState } from 'react';



import __noop from '@atlaskit/ds-lib/noop';

import { FlagsProvider, useFlags } from '@atlaskit/flag';

import Heading from '@atlaskit/heading';

import CheckMarkIcon from '@atlaskit/icon/glyph/check';

import InformationIcon from '@atlaskit/icon/glyph/info';

import InteractionContext from '@atlaskit/interaction-context';

import { ZoomIn } from '@atlaskit/motion';

import { Box, Inline, Pressable, Stack, xcss } from '@atlaskit/primitives';

import { token } from '@atlaskit/tokens';

import Tooltip from '@atlaskit/tooltip';

import VisuallyHidden from '@atlaskit/visually-hidden';



const baseStyles = xcss({

	borderWidth: 'border.width',

	borderStyle: 'solid',

	borderColor: 'color.border',

	borderRadius: '3px',

	height: '44px',

	width: '44px',

	display: 'flex',

	alignItems: 'center',

	justifyContent: 'center',

});



type ColorButtonProps = {

	color: keyof typeof colorMap;

	isSelected?: boolean;

	onClick?(): void;

};



const ColorButton = ({ color, isSelected, onClick }: ColorButtonProps) => {

	return (

		<Tooltip content={color}>

			<Pressable

				interactionName={`color-${color.toLowerCase()}`}

				xcss={[baseStyles, colorMap[color]]}

				aria-pressed={isSelected}

				onClick={onClick}

			>

				{isSelected && (

					<ZoomIn>

						{(props) => (

							<div {...props}>

								<CheckMarkIcon

									label=""

									size="large"

									primaryColor={token('color.icon.inverse')}

								/>

							</div>

						)}

					</ZoomIn>

				)}

				<VisuallyHidden>{color}</VisuallyHidden>

			</Pressable>

		</Tooltip>

	);

};



const ColorPaletteButtons = () => {

	const [selectedColor, setSelectedColor] = useState<keyof typeof colorMap | null>('Red');



	const { showFlag } = useFlags();



	return (

		<InteractionContext.Provider

			value={{

				hold: __noop,

				tracePress: (name) => {

					showFlag({

						title: `Traced a press!`,

						description: name,

						icon: (

							<InformationIcon

								label="Info"

								primaryColor={token('color.icon.information')}

							/>

						),

						isAutoDismiss: true,

					});

				},

			}}

		>

			<Stack space="space.150" alignInline="start">

				<Heading size="small" id="epic-heading">

					Change epic color

				</Heading>

				<Box role="group" aria-labelledby="epic-heading">

					<Inline space="space.100">

						{Object.keys(colorMap).map((color) => {

							const keyColor = color as keyof typeof colorMap;

							return (

								<ColorButton

									key={keyColor}

									color={keyColor}

									isSelected={selectedColor === keyColor}

									onClick={() => setSelectedColor(keyColor)}

								/>

							);

						})}

					</Inline>

				</Box>

			</Stack>

		</InteractionContext.Provider>

	);

};



export default function PressTracing() {

	return (

		<FlagsProvider>

			<ColorPaletteButtons />

		</FlagsProvider>

	);

}



const colorMap = {

	Red: xcss({

		backgroundColor: 'color.background.accent.red.subtle',



		':hover': {

			backgroundColor: 'color.background.accent.red.subtle.hovered',

		},

		':active': {

			backgroundColor: 'color.background.accent.red.subtle.pressed',

		},

	}),

	Orange: xcss({

		backgroundColor: 'color.background.accent.orange.subtle',



		':hover': {

			backgroundColor: 'color.background.accent.orange.subtle.hovered',

		},

		':active': {

			backgroundColor: 'color.background.accent.orange.subtle.pressed',

		},

	}),

	Yellow: xcss({

		backgroundColor: 'color.background.accent.yellow.subtle',



		':hover': {

			backgroundColor: 'color.background.accent.yellow.subtle.hovered',

		},

		':active': {

			backgroundColor: 'color.background.accent.yellow.subtle.pressed',

		},

	}),

	Lime: xcss({

		backgroundColor: 'color.background.accent.lime.subtle',



		':hover': {

			backgroundColor: 'color.background.accent.lime.subtle.hovered',

		},

		':active': {

			backgroundColor: 'color.background.accent.lime.subtle.pressed',

		},

	}),

	Green: xcss({

		backgroundColor: 'color.background.accent.green.subtle',



		':hover': {

			backgroundColor: 'color.background.accent.green.subtle.hovered',

		},

		':active': {

			backgroundColor: 'color.background.accent.green.subtle.pressed',

		},

	}),

	Teal: xcss({

		backgroundColor: 'color.background.accent.teal.subtle',



		':hover': {

			backgroundColor: 'color.background.accent.teal.subtle.hovered',

		},

		':active': {

			backgroundColor: 'color.background.accent.teal.subtle.pressed',

		},

	}),

	Blue: xcss({

		backgroundColor: 'color.background.accent.blue.subtle',



		':hover': {

			backgroundColor: 'color.background.accent.blue.subtle.hovered',

		},

		':active': {

			backgroundColor: 'color.background.accent.blue.subtle.pressed',

		},

	}),

	Purple: xcss({

		backgroundColor: 'color.background.accent.purple.subtle',



		':hover': {

			backgroundColor: 'color.background.accent.purple.subtle.hovered',

		},

		':active': {

			backgroundColor: 'color.background.accent.purple.subtle.pressed',

		},

	}),

	Magenta: xcss({

		backgroundColor: 'color.background.accent.magenta.subtle',



		':hover': {

			backgroundColor: 'color.background.accent.magenta.subtle.hovered',

		},

		':active': {

			backgroundColor: 'color.background.accent.magenta.subtle.pressed',

		},

	}),

};
```

---

[View Original Documentation](https://atlassian.design/components/primitives/pressable/examples)
