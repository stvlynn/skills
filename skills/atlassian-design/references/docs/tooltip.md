# Tooltip

A tooltip is a floating, non-actionable label used to explain a user interface element or feature.

---

## Default

The default form of a tooltip. 

```jsx
import React from 'react';



import Button from '@atlaskit/button/new';

import Tooltip from '@atlaskit/tooltip';



export default () => (

	<Tooltip content="This is a tooltip">

		{(tooltipProps) => (

			<Button appearance="primary" {...tooltipProps}>

				Hover or keyboard focus on me

			</Button>

		)}

	</Tooltip>

);
```

## Positioning

Use the position prop to set a preferred position (auto, top, right, left, or bottom). The tooltip will move automatically if it's near the edge of the screen. Using a position of auto will place the tooltip on the side with the most space available. If set to mouse, the tooltip will display next to the mouse pointer. Use mousePosition to customize where the tooltip shows in relation to the mouse. 

```jsx
import React from 'react';



import Button from '@atlaskit/button/new';

import { cssMap } from '@atlaskit/css';

import { placements } from '@atlaskit/popper';

import { Box } from '@atlaskit/primitives/compiled';

import { token } from '@atlaskit/tokens';

import Tooltip from '@atlaskit/tooltip';



const placementGridPositions = cssMap({

	'top-start': {

		gridColumn: 2,

		gridRow: 1,

	},

	top: {

		gridColumn: 3,

		gridRow: 1,

	},

	'top-end': {

		gridColumn: 4,

		gridRow: 1,

	},

	'bottom-start': {

		gridColumn: 2,

		gridRow: 5,

	},

	bottom: {

		gridColumn: 3,

		gridRow: 5,

	},

	'bottom-end': {

		gridColumn: 4,

		gridRow: 5,

	},

	'right-start': {

		gridColumn: 5,

		gridRow: 2,

	},

	right: {

		gridColumn: 5,

		gridRow: 3,

	},

	'right-end': {

		gridColumn: 5,

		gridRow: 4,

	},

	'left-start': {

		gridColumn: 1,

		gridRow: 2,

	},

	left: {

		gridColumn: 1,

		gridRow: 3,

	},

	'left-end': {

		gridColumn: 1,

		gridRow: 4,

	},

	'auto-start': {

		gridColumn: 3,

		gridRow: 2,

	},

	auto: {

		gridColumn: 3,

		gridRow: 3,

	},

	'auto-end': {

		gridColumn: 3,

		gridRow: 4,

	},

});



const buttonGridStyles = cssMap({

	root: {

		display: 'grid',

		gap: token('space.100'),

		gridTemplate: 'repeat(5, 1fr) / repeat(5, 1fr)',

		justifyItems: 'stretch',

	},

});



const PositionExample = () => {

	return (

		<Box xcss={buttonGridStyles.root}>

			{placements.map((placement) => (

				<Box key={placement} xcss={placementGridPositions[placement]}>

					<Tooltip position={placement} content={placement}>

						{(tooltipProps) => (

							<Button {...tooltipProps} shouldFitContainer>

								{placement}

							</Button>

						)}

					</Tooltip>

				</Box>

			))}

		</Box>

	);

};



export default PositionExample;
```

```jsx
import React, { useState } from 'react';



import Button from '@atlaskit/button/new';

import Tooltip, { type PositionType } from '@atlaskit/tooltip';



const VALID_POSITIONS: PositionType[] = ['mouse', 'top', 'right', 'bottom', 'left'];



const PositionMouseExample = () => {

	const [position, setPosition] = useState(0);

	const positionText = VALID_POSITIONS[position];



	return (

		<Tooltip content={positionText} position={positionText}>

			{(tooltipProps) => (

				<Button

					{...tooltipProps}

					appearance="primary"

					onClick={() => {

						setPosition((position + 1) % VALID_POSITIONS.length);

					}}

				>

					Hover over me

				</Button>

			)}

		</Tooltip>

	);

};



export default PositionMouseExample;
```

## Customizing tooltip

The tooltip component accepts a component prop, which you can use to customize the look and feel of the tooltip area. Never put links or other interactive components in tooltips because this isn't accessible. You can use the TooltipPrimitive component to customize the style of the default tooltip. 

```jsx
/**

 * @jsxRuntime classic

 * @jsx jsx

 */

import { forwardRef } from 'react';



import Button from '@atlaskit/button/new';

import { cssMap, jsx } from '@atlaskit/css';

import { token } from '@atlaskit/tokens';

import Tooltip, { TooltipPrimitive, TooltipPrimitiveProps } from '@atlaskit/tooltip';



const styles = cssMap({

	root: {

		backgroundColor: token('elevation.surface'),

		borderRadius: token('border.radius'),

		boxShadow: token('elevation.shadow.overlay'),

		color: token('color.text'),

		maxHeight: '300px',

		maxWidth: '300px',

		paddingBlockStart: token('space.100'),

		paddingBlockEnd: token('space.100'),

		paddingInlineStart: token('space.150'),

		paddingInlineEnd: token('space.150'),

	},

});



const CustomTooltip = forwardRef<HTMLDivElement, TooltipPrimitiveProps>(function CustomTooltip(

	{ children, className, ...rest },

	ref,

) {

	return (

		<TooltipPrimitive

			{...rest}

			// Manually passing on `className` so it gets merged correctly in the build output.

			// The passed classname is mostly used for integration testing (`.Tooltip`)

			// eslint-disable-next-line @atlaskit/design-system/no-unsafe-style-overrides, @atlaskit/ui-styling-standard/no-classname-prop

			className={className}

			// "css" does not "exist" - it gets transformed into "className" by compiled

			css={styles.root}

			ref={ref}

		>

			{children}

		</TooltipPrimitive>

	);

});



export default function TooltipCustomizationExample() {

	return (

		<Tooltip component={CustomTooltip} content="This is a customized tooltip">

			{(tooltipProps) => <Button {...tooltipProps}>Hover or keyboard focus on me</Button>}

		</Tooltip>

	);

}
```

## Accessibility issues using 'title'

A tooltip is often used to specify extra information when a person hovers or keyboard focuses on an element, which matches the behavior of the HTML title attribute. Avoid using the HTML title attribute in any children of the tooltip or you may see double tooltips displayed. The title attribute isn't supported consistently across screen readers, and is inaccessible to all keyboard-only users and mobile phone users. 

```jsx
import React from 'react';



import Button from '@atlaskit/button/new';

import Tooltip from '@atlaskit/tooltip';



export default () => (

	<Tooltip

		content="Never use the title attribute. Double tooltips will be displayed."

		position="right"

	>

		{(tooltipProps) => (

			<Button

				appearance="primary"

				title="This is a native tooltip from the title attribute. Don't do this, it isn't accessible."

				{...tooltipProps}

			>

				Hover to reveal my tooltip and title attribute

			</Button>

		)}

	</Tooltip>

);
```

## Updating tooltip position

When the content of a visible tooltip changes, its' position isn't recalculated and the tooltip may become misaligned. If you need the tooltip to recalculate its position you can control this manually using the update render prop. 

```jsx
import React from 'react';



import Button from '@atlaskit/button/new';

import Tooltip from '@atlaskit/tooltip';



const shortMessage = "I'm a short tooltip";

const longMessage = 'I am a longer tooltip with a decent amount of content inside';



export default () => {

	const [message, setMessage] = React.useState(shortMessage);

	const updateTooltip = React.useRef<() => void>();



	React.useLayoutEffect(() => {

		updateTooltip.current?.();

	}, [message]);



	return (

		<Tooltip

			content={({ update }) => {

				updateTooltip.current = update;

				return message;

			}}

		>

			{({ onClick, ...tooltipProps }) => (

				<Button

					onClick={() => setMessage(message === shortMessage ? longMessage : shortMessage)}

					{...tooltipProps}

				>

					Click to toggle tooltip

				</Button>

			)}

		</Tooltip>

	);

};
```

## Preventing tooltip interactions

There are situations where the tooltip persisting on hover of the tooltip itself can obstruct interactions with another element. Set ignoreTooltipPointerEvents to true to prevent mouse interactions with the tooltip. This sets pointer-events: none on the tooltip. Tooltip is interactive Tooltip is not interactive 

```jsx
import React from 'react';



import Button from '@atlaskit/button/new';

import { Inline, Stack } from '@atlaskit/primitives/compiled';

import Tooltip from '@atlaskit/tooltip';



export default () => (

	<Stack space="space.100">

		<Stack space="space.100">

			<p>Tooltip is interactive</p>

			<Inline space="space.100">

				<Tooltip content="This is a tooltip" position="right">

					{(tooltipProps) => (

						<Button appearance="primary" {...tooltipProps}>

							Hover me first

						</Button>

					)}

				</Tooltip>

				<Button>Hover me second</Button>

			</Inline>

		</Stack>

		<Stack space="space.100">

			<p>Tooltip is not interactive</p>

			<Inline space="space.100">

				<Tooltip content="This is a tooltip" position="right" ignoreTooltipPointerEvents>

					{(tooltipProps) => (

						<Button appearance="primary" {...tooltipProps}>

							Hover me first

						</Button>

					)}

				</Tooltip>

				<Button>Hover me second</Button>

			</Inline>

		</Stack>

	</Stack>

);
```

## Accessibility

In order for screen readers to get access to content within tooltips, a hidden element is created that contains the content of a tooltip. The trigger of a tooltip (the children of <Tooltip>) is provided with aria-describedby to connect the hidden element to the trigger. To disable the usage of a hidden element for screen reader announcements, use the isScreenReaderAnnouncementDisabled prop. This is useful when the content of a tooltip matches the content of the trigger as no hidden element would be needed. Icon Click to update Component in content Position 

```jsx
/**

 * @jsxRuntime classic

 * @jsx jsx

 */

import React, { forwardRef, Fragment, useState } from 'react';



import Button, { IconButton } from '@atlaskit/button/new';

import { cssMap, jsx } from '@atlaskit/css';

import AddIcon from '@atlaskit/icon/glyph/add';

import { token } from '@atlaskit/tokens';

import Tooltip, {

	type PositionType,

	TooltipPrimitive,

	TooltipPrimitiveProps,

} from '@atlaskit/tooltip';



const VALID_POSITIONS: PositionType[] = ['mouse', 'top', 'right', 'bottom', 'left'];



const shortMessage = "I'm a short tooltip";

const longMessage = 'I am a longer tooltip with a decent amount of content inside';



const styles = cssMap({

	root: {

		backgroundColor: token('elevation.surface'),

		borderRadius: token('border.radius'),

		boxShadow: token('elevation.shadow.overlay'),

		color: token('color.text'),

		maxHeight: '300px',

		maxWidth: '300px',

		paddingBlockStart: token('space.100'),

		paddingBlockEnd: token('space.100'),

		paddingInlineStart: token('space.150'),

		paddingInlineEnd: token('space.150'),

	},

});



const CustomTooltip = forwardRef<HTMLDivElement, TooltipPrimitiveProps>(function CustomTooltip(

	{ children, className, ...rest },

	ref,

) {

	return (

		<TooltipPrimitive

			{...rest}

			// Manually passing on `className` so it gets merged correctly in the build output.

			// The passed classname is mostly used for integration testing (`.Tooltip`)

			// eslint-disable-next-line @atlaskit/design-system/no-unsafe-style-overrides, @atlaskit/ui-styling-standard/no-classname-prop

			className={className}

			// "css" does not "exist" - it gets transformed into "className" by compiled

			css={styles.root}

			ref={ref}

		>

			{children}

		</TooltipPrimitive>

	);

});



export default function TooltipRenderPropsExample() {

	const [message, setMessage] = React.useState(shortMessage);

	const [position, setPosition] = useState(0);



	const updateTooltip = React.useRef<() => void>();



	const changeDirection = () => {

		setPosition((position + 1) % VALID_POSITIONS.length);

	};



	const handleOnMouseDown = (event: React.MouseEvent<HTMLElement>) => console.log(event);



	const positionText = VALID_POSITIONS[position];



	React.useLayoutEffect(() => {

		updateTooltip.current?.();

	}, [message]);



	return (

		<Fragment>

			<p>Icon</p>

			<Tooltip content="Add content">

				{(tooltipProps) => <IconButton icon={AddIcon} label="Add" testId="add" {...tooltipProps} />}

			</Tooltip>

			<p>Click to update</p>

			<Tooltip

				content={({ update }) => {

					updateTooltip.current = update;

					return message;

				}}

			>

				{(tooltipProps) => (

					<Button

						{...tooltipProps}

						onClick={() => setMessage(message === shortMessage ? longMessage : shortMessage)}

						onMouseDown={(e) => {

							tooltipProps.onMouseDown(e);

							handleOnMouseDown(e);

						}}

					>

						Click to toggle tooltip

					</Button>

				)}

			</Tooltip>

			<p>Component in content</p>

			<Tooltip component={CustomTooltip} content="Hello World">

				{(tooltipProps) => (

					<Button appearance="primary" {...tooltipProps}>

						Hover or keyboard focus on me

					</Button>

				)}

			</Tooltip>

			<p>Position</p>

			<div

				style={{

					padding: `${token('space.500')} ${token('space.500')}`,

				}}

			>

				<Tooltip content={positionText} position={positionText}>

					{(tooltipProps) => (

						<Button {...tooltipProps} onClick={changeDirection}>

							Target

						</Button>

					)}

				</Tooltip>

			</div>

		</Fragment>

	);

}
```

## Conditional tooltips

A tooltip can be conditionally shown by leveraging the canAppear prop. This is helpful when you have an element where you only want to show the tooltip of the content of the element is concatenated. 

```jsx
/**

 * @jsxRuntime classic

 * @jsx jsx

 */



import { useRef } from 'react';



import { jsx } from '@compiled/react';

import invariant from 'tiny-invariant';



import { cssMap, cx } from '@atlaskit/css';

import { Box, Stack, Text } from '@atlaskit/primitives/compiled';

import { token } from '@atlaskit/tokens';

import Tooltip from '@atlaskit/tooltip';



const styles = cssMap({

	root: {

		paddingTop: token('space.100'),

		paddingRight: token('space.100'),

		paddingBottom: token('space.100'),

		paddingLeft: token('space.100'),

		borderColor: token('color.border'),

		borderRadius: token('border.radius'),

		borderStyle: 'solid',

		borderWidth: token('border.width'),

	},

});



const smallStyles = cssMap({

	root: {

		width: '200px',

	},

});



const content = {

	first: 'Tooltip shown on this item as it is concatenated',

	second: 'No tooltip shown as this item is not being concatenated',

};



export default function Example() {

	const firstRef = useRef<HTMLElement | null>(null);

	const secondRef = useRef<HTMLElement | null>(null);



	return (

		<Stack space="space.100">

			<Tooltip

				content={content.first}

				// don't need a screen reader announcement as the

				// tooltip content is the same as the items content

				isScreenReaderAnnouncementDisabled

				canAppear={() => {

					const element = firstRef.current;

					invariant(element);

					// Only showing the tooltip for this item when

					// the element has been clamped.

					return element.scrollHeight > element.clientHeight;

				}}

			>

				{(props) => (

					<Box {...props} xcss={cx(styles.root, smallStyles.root)}>

						<Text ref={firstRef} maxLines={1}>

							{content.first}

						</Text>

					</Box>

				)}

			</Tooltip>

			<Tooltip

				content={content.second}

				// don't need a screen reader announcement as the

				// tooltip content is the same as the items content

				canAppear={() => {

					const element = secondRef.current;

					invariant(element);

					// Only showing the tooltip for this item when

					// the element has been clamped.

					return element.scrollHeight > element.clientHeight;

				}}

			>

				{(props) => (

					<Box {...props} xcss={styles.root}>

						<Text ref={secondRef} maxLines={1}>

							{content.second}

						</Text>

					</Box>

				)}

			</Tooltip>

		</Stack>

	);

}
```

---

[View Original Documentation](https://atlassian.design/components/tooltip/examples)
