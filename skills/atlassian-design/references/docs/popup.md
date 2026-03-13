# Popup

A popup displays brief content in an overlay.

---

## Default

This is the simplest form of a popup. The popup opens from a trigger element. 

```jsx
/**

 * @jsxRuntime classic

 * @jsx jsx

 */

import { useState } from 'react';



import { jsx } from '@compiled/react';



import Button from '@atlaskit/button/new';

import { cssMap } from '@atlaskit/css';

import Popup from '@atlaskit/popup';

import { Box } from '@atlaskit/primitives/compiled';

import { token } from '@atlaskit/tokens';



const contentStyles = cssMap({

	root: {

		paddingInlineStart: token('space.200'),

		paddingInlineEnd: token('space.200'),

		paddingBlockStart: token('space.200'),

		paddingBlockEnd: token('space.200'),

	},

});



const PopupDefaultExample = () => {

	const [isOpen, setIsOpen] = useState(false);



	return (

		<Popup

			shouldRenderToParent

			isOpen={isOpen}

			onClose={() => setIsOpen(false)}

			placement="bottom-start"

			content={() => <Box xcss={contentStyles.root}>Content</Box>}

			trigger={(triggerProps) => (

				<Button

					{...triggerProps}

					appearance="primary"

					isSelected={isOpen}

					onClick={() => setIsOpen(!isOpen)}

				>

					{isOpen ? 'Close' : 'Open'} popup{' '}

				</Button>

			)}

		/>

	);

};



export default PopupDefaultExample;
```

## Placement

Use the placement prop to set a preferred position (auto, top, right, left, or bottom). The popup will move automatically if it's near the edge of the screen. Using the auto placement will place the popup on the side with the most space available. 

```jsx
/**

 * @jsxRuntime classic

 * @jsx jsx

 */

import { useState } from 'react';



import { css, jsx } from '@compiled/react';



import Button from '@atlaskit/button/new';

import { cssMap } from '@atlaskit/css';

import { type Placement, placements } from '@atlaskit/popper';

import Popup from '@atlaskit/popup';

import { Box } from '@atlaskit/primitives/compiled';

import { token } from '@atlaskit/tokens';



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



const contentStyles = css({

	maxWidth: '220px',

	paddingBlockEnd: token('space.200'),

	paddingBlockStart: token('space.200'),

	paddingInlineEnd: token('space.200'),

	paddingInlineStart: token('space.200'),

});



const buttonGridStyles = css({

	display: 'grid',

	gap: token('space.100'),

	gridTemplate: 'repeat(5, 1fr) / repeat(5, 1fr)',

	justifyItems: 'stretch',

});



const PopupPlacementExample = () => {

	const [openPlacement, setOpenPlacement] = useState<Placement | null>(null);



	return (

		<div css={buttonGridStyles}>

			{placements.map((placement) => {

				const isOpen = openPlacement === placement;



				return (

					<Popup

						shouldRenderToParent

						key={placement}

						placement={placement}

						isOpen={isOpen}

						onClose={() => {

							if (isOpen) {

								setOpenPlacement(null);

							}

						}}

						content={() => (

							<div css={contentStyles}>

								Lorem ipsum dolor sit amet, consectetur adipiscing elit. Ut aliquam massa ac risus

								scelerisque, in iaculis magna semper. Phasellus sagittis congue elit, non suscipit

								nulla rhoncus vitae.

							</div>

						)}

						trigger={(triggerProps) => (

							<Box xcss={placementGridPositions[placement]}>

								<Button

									{...triggerProps}

									shouldFitContainer

									isSelected={isOpen}

									onClick={() => setOpenPlacement(isOpen ? null : placement)}

								>

									{placement}

								</Button>

							</Box>

						)}

					/>

				);

			})}

		</div>

	);

};



export default PopupPlacementExample;
```

## Multiple

You can use popups multiple times on the same page. 

```jsx
/**

 * @jsxRuntime classic

 * @jsx jsx

 */

import { type FC, useState } from 'react';



import { jsx } from '@compiled/react';



import ButtonGroup from '@atlaskit/button/button-group';

import Button from '@atlaskit/button/new';

import { cssMap } from '@atlaskit/css';

import Popup from '@atlaskit/popup';

import { Box } from '@atlaskit/primitives/compiled';

import { token } from '@atlaskit/tokens';



const contentStyles = cssMap({

	root: {

		paddingInlineStart: token('space.200'),

		paddingInlineEnd: token('space.200'),

		paddingBlockStart: token('space.200'),

		paddingBlockEnd: token('space.200'),

	},

});



type PopupExampleProps = {

	index: number;

};



const PopupExample: FC<PopupExampleProps> = ({ index }) => {

	const [isOpen, setIsOpen] = useState(false);



	return (

		<Popup

			shouldRenderToParent

			isOpen={isOpen}

			onClose={() => setIsOpen(false)}

			content={() => <Box xcss={contentStyles.root}>Content</Box>}

			trigger={(triggerProps) => (

				<Button {...triggerProps} isSelected={isOpen} onClick={() => setIsOpen(!isOpen)}>

					{isOpen ? 'Close' : 'Open'} popup {index + 1}

				</Button>

			)}

			placement="bottom-start"

		/>

	);

};



const PopupMultipleExample = () => (

	<ButtonGroup label="Open required popup">

		{Array.from(Array(3)).map((_, index) => (

			<PopupExample index={index} />

		))}

	</ButtonGroup>

);



export default PopupMultipleExample;
```

## Nested

Nesting popups inside other popups works out of the box. However, be mindful that nested popups quickly become confusing, inaccessible, and difficult to navigate. If you’re nesting a lot of content, it’s time to move your experience to a new page instead. This example has additional code to prevent the parent popup closing when interacting with the child popup. 

```jsx
/**

 * @jsxRuntime classic

 * @jsx jsx

 */

import { useState } from 'react';



import { jsx } from '@compiled/react';



import Button from '@atlaskit/button/new';

import { cssMap } from '@atlaskit/css';

import ArrowRight from '@atlaskit/icon/glyph/arrow-right';

import MenuIcon from '@atlaskit/icon/glyph/menu';

import { ButtonItem, Section } from '@atlaskit/menu';

import Popup from '@atlaskit/popup';

import { Box, Stack } from '@atlaskit/primitives/compiled';



const nestedPopupStyles = cssMap({

	root: {

		maxWidth: '800px',

		minWidth: '320px',

	},

});



const NestedPopup = () => {

	const [isOpen, setIsOpen] = useState(false);



	return (

		// eslint-disable-next-line @atlassian/a11y/interactive-element-not-keyboard-focusable

		<Box onClick={(e: React.MouseEvent) => e.stopPropagation()}>

			<Stack xcss={nestedPopupStyles.root}>

				<Section title="Projects">

					<ButtonItem>Create project</ButtonItem>

					<ButtonItem>View all projects</ButtonItem>

				</Section>

				<Section hasSeparator>

					<Popup

						isOpen={isOpen}

						placement="right-start"

						shouldRenderToParent

						onClose={() => setIsOpen(false)}

						content={() => <NestedPopup />}

						trigger={(triggerProps) => (

							<ButtonItem

								{...triggerProps}

								isSelected={isOpen}

								onClick={() => setIsOpen(true)}

								iconAfter={<ArrowRight label="" />}

							>

								More actions

							</ButtonItem>

						)}

					/>

				</Section>

			</Stack>

		</Box>

	);

};



const PopupNestedExample = () => {

	const [isOpen, setIsOpen] = useState(false);



	return (

		<Popup

			isOpen={isOpen}

			onClose={() => setIsOpen(false)}

			content={() => <NestedPopup />}

			placement="bottom-start"

			shouldRenderToParent

			trigger={(triggerProps) => (

				<Button

					{...triggerProps}

					isSelected={isOpen}

					iconBefore={MenuIcon}

					onClick={() => setIsOpen(!isOpen)}

				>

					Menu

				</Button>

			)}

		/>

	);

};



export default PopupNestedExample;
```

## Content updates

When changing the content inside the popup, call the update() function to reposition the popup. Make sure to call this in the same callback or update step to ensure everything happens in the same animation frame. 

```jsx
/**

 * @jsxRuntime classic

 * @jsx jsx

 */

import { useEffect, useState } from 'react';



import { jsx } from '@compiled/react';



import Button from '@atlaskit/button/new';

import { cssMap } from '@atlaskit/css';

import noop from '@atlaskit/ds-lib/noop';

import Heading from '@atlaskit/heading';

import Popup from '@atlaskit/popup';

import { Box, Stack, Text } from '@atlaskit/primitives/compiled';

import Toggle from '@atlaskit/toggle';

import { token } from '@atlaskit/tokens';



import { data } from './data';



const wrapperStyles = cssMap({

	root: {

		display: 'flex',

		alignItems: 'center',

		justifyContent: 'space-between',

	},

});



const contentStyles = cssMap({

	root: {

		maxWidth: '350px',

		paddingInlineStart: token('space.200'),

		paddingInlineEnd: token('space.200'),

		paddingBlockStart: token('space.200'),

		paddingBlockEnd: token('space.200'),

		textAlign: 'center',

	},

});



const Values = ({ onUpdate }: { onUpdate: () => void }) => {

	const [textIndex, setTextIndex] = useState(0);



	useEffect(() => {

		const intervalId = setInterval(() => {

			setTextIndex((prevIndex) => (prevIndex + 1) % data.length);

			onUpdate();

		}, 15000);



		return () => clearInterval(intervalId);

	}, [onUpdate]);



	return (

		<Box xcss={contentStyles.root} aria-live="assertive" aria-atomic="true">

			<Stack space="space.100">

				<Heading size="large">{data[textIndex].title}</Heading>

				<Box as="blockquote">

					<Text>{data[textIndex].description}</Text>

				</Box>

			</Stack>

		</Box>

	);

};



const PopupContentUpdateExample = () => {

	const [isOpen, setIsOpen] = useState(false);

	const [isUpdateOn, setIsUpdateOn] = useState(true);



	return (

		<Box xcss={wrapperStyles.root}>

			<Popup

				shouldRenderToParent

				isOpen={isOpen}

				onClose={() => setIsOpen(false)}

				content={(props) => <Values onUpdate={isUpdateOn ? props.update : noop} />}

				placement="right"

				trigger={(triggerProps) => (

					<Button

						{...triggerProps}

						appearance="primary"

						isSelected={isOpen}

						onClick={() => setIsOpen(!isOpen)}

					>

						Open popup

					</Button>

				)}

			/>

			<Box>

				<Text>Updates {isUpdateOn ? 'on' : 'off'}</Text>

				<Toggle

					size="large"

					label="Updates toggle switch controls"

					isChecked={isUpdateOn}

					onChange={(e) => setIsUpdateOn(e.currentTarget.checked)}

				/>

			</Box>

		</Box>

	);

};



export default PopupContentUpdateExample;
```

## Customization

You can customize the popup using a component override with the popupComponent prop. Make sure to forward the ref to the underlying DOM node, or the positioning of the popup won't work correctly. 

```jsx
/**

 * @jsxRuntime classic

 * @jsx jsx

 */

import { forwardRef, useState } from 'react';



import { css, jsx } from '@compiled/react';



import { IconButton } from '@atlaskit/button/new';

import ShowMoreHorizontalIcon from '@atlaskit/icon/glyph/more';

import Popup, { type PopupComponentProps } from '@atlaskit/popup';

import { Box } from '@atlaskit/primitives/compiled';

import { token } from '@atlaskit/tokens';



const containerStyles = css({

	backgroundColor: token('color.background.brand.bold'),

	borderRadius: token('border.radius'),

	color: token('color.text.inverse'),

	paddingBlockEnd: token('space.200'),

	paddingBlockStart: token('space.200'),

	paddingInlineEnd: token('space.200'),

	paddingInlineStart: token('space.200'),

});



const CustomPopupContainer = forwardRef<HTMLDivElement, PopupComponentProps>(

	({ children, 'data-testid': testId, xcss: _xcss, ...props }, ref) => (

		<div

			css={containerStyles}

			test-id={testId}

			{...props}

			// eslint-disable-next-line @atlaskit/ui-styling-standard/no-classname-prop

			className={props.className}

			ref={ref}

		>

			{children}

		</div>

	),

);



const PopupCustomExample = () => {

	const [isOpen, setIsOpen] = useState(false);



	return (

		<Popup

			shouldRenderToParent

			isOpen={isOpen}

			testId="popup-custom-example"

			onClose={() => setIsOpen(false)}

			placement="bottom-start"

			popupComponent={CustomPopupContainer}

			content={() => <Box>Customized popup</Box>}

			trigger={(triggerProps) => (

				<IconButton

					{...triggerProps}

					isSelected={isOpen}

					onClick={() => setIsOpen(!isOpen)}

					icon={ShowMoreHorizontalIcon}

					label="More"

				/>

			)}

		/>

	);

};



export default PopupCustomExample;
```

## Focus

### Set focus

You can focus a specific element when opening the popup. The content render props provide a ref setInitialFocusRef to be set on the desired element. Only set focus to an element at the start of the popup, otherwise people who use assistive technology may miss the content. Select a button to focus 

```jsx
/**

 * @jsxRuntime classic

 * @jsx jsx

 */

import { Fragment, useState } from 'react';



import { jsx } from '@compiled/react';



import ButtonGroup from '@atlaskit/button/button-group';

import Button from '@atlaskit/button/new';

import { cssMap } from '@atlaskit/css';

import Popup from '@atlaskit/popup';

import { Box } from '@atlaskit/primitives/compiled';

import { RadioGroup } from '@atlaskit/radio';

import { token } from '@atlaskit/tokens';



const radioValues = [

	{ name: 'None', value: '0', label: 'None' },

	{ name: 'Button 1', value: '1', label: 'Button 1' },

	{ name: 'Button 2', value: '2', label: 'Button 2' },

	{ name: 'Button 3', value: '3', label: 'Button 3' },

];



const contentStyles = cssMap({

	root: {

		paddingBlockEnd: token('space.200'),

		paddingBlockStart: token('space.200'),

		paddingInlineEnd: token('space.200'),

		paddingInlineStart: token('space.200'),

	},

});



const PopupFocusExample = () => {

	const [isOpen, setIsOpen] = useState(false);

	const [buttonToFocus, setButtonToFocus] = useState('0');



	return (

		<Fragment>

			<p>

				<strong>Select a button to focus</strong>

			</p>

			<RadioGroup

				onChange={({ currentTarget: { value } }) => setButtonToFocus(value)}

				defaultValue={radioValues[0].value}

				options={radioValues}

			/>

			<Popup

				shouldRenderToParent

				isOpen={isOpen}

				onClose={() => setIsOpen(false)}

				content={({ setInitialFocusRef }) => {

					return (

						<Box xcss={contentStyles.root}>

							<ButtonGroup label="Show selected focus">

								{radioValues.map(

									({ value, label }) =>

										value !== '0' && (

											<Button

												key={value}

												ref={value === buttonToFocus ? setInitialFocusRef : undefined}

											>

												{label}

											</Button>

										),

								)}

							</ButtonGroup>

						</Box>

					);

				}}

				trigger={(triggerProps) => (

					<Button

						{...triggerProps}

						appearance="primary"

						isSelected={isOpen}

						onClick={() => setIsOpen(!isOpen)}

					>

						{isOpen ? 'Close' : 'Open'} popup

					</Button>

				)}

				placement="bottom-start"

			/>

		</Fragment>

	);

};



export default PopupFocusExample;
```

### Disable autofocus

If an element is focused, setting the autofocus prop to false will ensure it keeps focus when the popup is opened. 

```jsx
/**

 * @jsxRuntime classic

 * @jsx jsx

 */

import { useState } from 'react';



import { jsx } from '@compiled/react';



import Button from '@atlaskit/button/new';

import { cssMap } from '@atlaskit/css';

import Popup from '@atlaskit/popup';

import { Box } from '@atlaskit/primitives/compiled';

import Textfield from '@atlaskit/textfield';

import { token } from '@atlaskit/tokens';



const wrapperStyles = cssMap({

	root: {

		display: 'grid',

		alignItems: 'center',

		gap: token('space.200'),

		gridTemplateColumns: '1fr auto',

	},

});



const contentStyles = cssMap({

	root: {

		maxWidth: '200px',

		paddingInlineStart: token('space.200'),

		paddingInlineEnd: token('space.200'),

		paddingBlockStart: token('space.200'),

		paddingBlockEnd: token('space.200'),

	},

});



const PopupDisableAutofocusExample = () => {

	const [isOpen, setIsOpen] = useState(false);



	return (

		<Box xcss={wrapperStyles.root}>

			<Textfield placeholder="This should stay focused when the popup opens" />

			<Popup

				shouldRenderToParent

				// eslint-disable-next-line jsx-a11y/no-autofocus

				autoFocus={false}

				isOpen={isOpen}

				onClose={() => setIsOpen(false)}

				content={() => (

					<Box xcss={contentStyles.root}>

						Lorem ipsum dolor sit amet, consectetur adipiscing elit. Ut aliquam massa ac risus

						scelerisque, in iaculis magna semper. Phasellus sagittis congue elit, non suscipit nulla

						rhoncus vitae.

					</Box>

				)}

				trigger={(triggerProps) => (

					<Button

						{...triggerProps}

						appearance="primary"

						isSelected={isOpen}

						onClick={() => setIsOpen(!isOpen)}

					>

						{isOpen ? 'Close' : 'Open'} popup

					</Button>

				)}

				placement="bottom"

			/>

		</Box>

	);

};



export default PopupDisableAutofocusExample;
```

## Surface detection

The current surface CSS variable is set to the surface color of the popup. You can use the utility.elevation.surface.current design token to style children with the current surface color. 

```jsx
/**

 * @jsxRuntime classic

 * @jsx jsx

 */

import { useState } from 'react';



import { css, jsx } from '@compiled/react';



import Button from '@atlaskit/button/new';

import Popup from '@atlaskit/popup';

import { Flex } from '@atlaskit/primitives/compiled';

import { token } from '@atlaskit/tokens';



const contentStyles = css({

	maxWidth: '220px',

	backgroundColor: token('utility.elevation.surface.current'),

	paddingBlockEnd: token('space.200'),

	paddingBlockStart: token('space.200'),

	paddingInlineEnd: token('space.200'),

	paddingInlineStart: token('space.200'),

});



const SurfaceAwareBox = () => {

	return (

		<div css={contentStyles}>

			A surface aware box - the background color depends on the surface it's placed on.

		</div>

	);

};



const PopupSurfaceDetectionExample = () => {

	const [isOpen, setIsOpen] = useState(false);



	return (

		<Flex gap="space.200">

			<Popup

				shouldRenderToParent

				isOpen={isOpen}

				onClose={() => setIsOpen(false)}

				placement="bottom-start"

				content={SurfaceAwareBox}

				trigger={(triggerProps) => (

					<Button

						{...triggerProps}

						appearance="primary"

						isSelected={isOpen}

						onClick={() => setIsOpen(!isOpen)}

					>

						{isOpen ? 'Close' : 'Open'} popup

					</Button>

				)}

			/>

			<SurfaceAwareBox />

		</Flex>

	);

};



export default PopupSurfaceDetectionExample;
```

## Content wrapping

By default, the popup content is rendered inside React.Portal. Use shouldRenderToParent prop to render the content directly after the trigger element. 

```jsx
/**

 * @jsxRuntime classic

 * @jsx jsx

 */

import { useState } from 'react';



import { jsx } from '@compiled/react';



import Button from '@atlaskit/button/new';

import { cssMap } from '@atlaskit/css';

import Popup from '@atlaskit/popup';

import { Box } from '@atlaskit/primitives/compiled';

import { token } from '@atlaskit/tokens';



const contentStyles = cssMap({

	root: {

		paddingInlineStart: token('space.200'),

		paddingInlineEnd: token('space.200'),

		paddingBlockStart: token('space.200'),

		paddingBlockEnd: token('space.200'),

	},

});



const PopupContentWithoutPortalExample = () => {

	const [isOpen, setIsOpen] = useState(false);



	return (

		<Popup

			isOpen={isOpen}

			onClose={() => setIsOpen(false)}

			placement="bottom-start"

			content={() => <Box xcss={contentStyles.root}>Content</Box>}

			shouldRenderToParent

			trigger={(triggerProps) => (

				<Button

					{...triggerProps}

					appearance="primary"

					isSelected={isOpen}

					onClick={() => setIsOpen(!isOpen)}

				>

					{isOpen ? 'Close' : 'Open'} popup{' '}

				</Button>

			)}

		/>

	);

};



export default PopupContentWithoutPortalExample;
```

## Role

Use the role prop to set a role for the popup content. We do not forbid passing any of the aria roles, but we strongly recommend using only menu or dialog. When the role="dialog" property is passed, one of the following properties must also be added: label or titleId. 

```jsx
/**

 * @jsxRuntime classic

 * @jsx jsx

 */

import { useState } from 'react';



import { jsx } from '@compiled/react';



import Button from '@atlaskit/button/new';

import { cssMap } from '@atlaskit/css';

import Popup from '@atlaskit/popup';

import { Box } from '@atlaskit/primitives/compiled';

import { token } from '@atlaskit/tokens';



const contentStyles = cssMap({

	root: {

		paddingInlineStart: token('space.200'),

		paddingInlineEnd: token('space.200'),

		paddingBlockStart: token('space.200'),

		paddingBlockEnd: token('space.200'),

	},

});



const PopupWithRoleExample = () => {

	const [isOpen, setIsOpen] = useState(false);



	return (

		<Popup

			shouldRenderToParent

			isOpen={isOpen}

			onClose={() => setIsOpen(false)}

			placement="bottom-start"

			content={() => <Box xcss={contentStyles.root}>Content</Box>}

			role="dialog"

			label="Popup with role dialog example"

			trigger={(triggerProps) => (

				<Button

					{...triggerProps}

					appearance="primary"

					isSelected={isOpen}

					onClick={() => setIsOpen(!isOpen)}

				>

					{isOpen ? 'Close' : 'Open'} popup{' '}

				</Button>

			)}

		/>

	);

};



export default PopupWithRoleExample;
```

## Full width

Use shouldFitContainer to fit the popup width to its parent's width. When set to true, the trigger and popup elements will be wrapped in a div with position: relative. The popup will be rendered as a sibling to the trigger element, and will be full width. 

```jsx
/**

 * @jsxRuntime classic

 * @jsx jsx

 */

import { useState } from 'react';



import { jsx } from '@compiled/react';



import Button from '@atlaskit/button/new';

import { cssMap } from '@atlaskit/css';

import Popup from '@atlaskit/popup';

import { Box } from '@atlaskit/primitives/compiled';

import { token } from '@atlaskit/tokens';



const contentStyles = cssMap({

	root: {

		paddingInlineStart: token('space.200'),

		paddingInlineEnd: token('space.200'),

		paddingBlockStart: token('space.200'),

		paddingBlockEnd: token('space.200'),

	},

});



const PopupFullWidth = () => {

	const [isOpen, setIsOpen] = useState(false);



	return (

		<Popup

			shouldRenderToParent

			content={() => <Box xcss={contentStyles.root}>Content</Box>}

			isOpen={isOpen}

			onClose={() => setIsOpen(false)}

			placement="bottom-start"

			shouldFitContainer

			trigger={(triggerProps) => (

				<Button

					{...triggerProps}

					appearance="primary"

					isSelected={isOpen}

					onClick={() => setIsOpen(!isOpen)}

					shouldFitContainer

				>

					{isOpen ? 'Close' : 'Open'} popup{' '}

				</Button>

			)}

		/>

	);

};



export default PopupFullWidth;
```

---

[View Original Documentation](https://atlassian.design/components/popup/examples)
