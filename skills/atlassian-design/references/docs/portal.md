# Portal

A wrapper for rendering components in React portals.

---

## Default

The default example of a portal. See React portals documentation for details. Portals render parts of a React component tree into a different part of the DOM. This is useful for UI components that need to appear over the top of other components, such as modal dialog, flag and tooltip. 

```jsx
import React from 'react';



import Portal from '@atlaskit/portal';



const PortalDefaultExample = () => {

	return (

		<h1>

			<Portal>

				<b>I am a child of the h1 element in the code but in the DOM I am not.</b>

			</Portal>

			Heading text

		</h1>

	);

};



export default PortalDefaultExample;
```

## Stacking context

Each portal component creates a new stacking context. Elements rendered with z-indexes inside the portal are scoped to that context. 

```jsx
/**

 * @jsxRuntime classic

 * @jsx jsx

 */

// eslint-disable-next-line @atlaskit/ui-styling-standard/use-compiled -- Ignored via go/DSP-18766

import { css, jsx } from '@emotion/react';



import Portal from '@atlaskit/portal';

import { Box, xcss } from '@atlaskit/primitives';

import { token } from '@atlaskit/tokens';



const containerStyles = xcss({

	marginBlockStart: 'space.1000',

});



const figcaptionStyles = css({

	padding: token('space.100'),

	position: 'absolute',

	background: token('color.background.neutral'),

	insetBlockEnd: token('space.0'),

});



const figureStyles = css({

	position: 'absolute',

	border: `1px solid ${token('color.blanket')}`,

	filter: 'drop-shadow(-12px 12px 8px)',

});



const topSquareStyles = css({

	width: '372px',

	height: '482px',

	background: token('color.background.accent.purple.bolder'),

});



const bottomSquareStyles = css({

	width: '372px',

	height: '492px',

	background: token('color.background.accent.blue.subtler'),

});



const topSquarePositionStyles = css({

	insetBlockStart: token('space.0'),

	insetInlineStart: '256px',

});



const topSquareIndexStyles = css({

	zIndex: 1,

});



const bottomSquareIndexStyles = css({

	zIndex: 1000,

});



const PortalStackingContextExample = () => {

	return (

		<Box xcss={containerStyles}>

			<Portal zIndex={100}>

				<figure css={[figureStyles, bottomSquareIndexStyles]}>

					<div css={bottomSquareStyles} />

					<figcaption css={figcaptionStyles}>

						I am a bottom square. I appear below because my z-index is lower. My child z-index is

						only relevant in my stacking context.

					</figcaption>

				</figure>

			</Portal>

			<Portal zIndex={200}>

				<figure css={[figureStyles, topSquarePositionStyles, topSquareIndexStyles]}>

					<div css={topSquareStyles} />

					<figcaption css={figcaptionStyles}>

						I am a top square. I appear above because my z-index is higher. My sibling's child

						z-index is only relevant in it's parent stacking context.

					</figcaption>

				</figure>

			</Portal>

		</Box>

	);

};



export default PortalStackingContextExample;
```

## Portal events

Mount and unmount events fire when portal elements are added or removed. These events contain the type of element and its z-index. This package exports PORTAL_MOUNT_EVENT and PORTAL_UNMOUNT_EVENT constants, as well as the type of the event itself, PortalEvent. Due to custom events not being supported in IE11, we create a native event and add a detail object manually to the event. 

```jsx
/**

 * @jsxRuntime classic

 * @jsx jsx

 */

import { useEffect, useState } from 'react';



// eslint-disable-next-line @atlaskit/ui-styling-standard/use-compiled -- Ignored via go/DSP-18766

import { css, jsx } from '@emotion/react';

import { bindAll, type UnbindFn } from 'bind-event-listener';



import Button from '@atlaskit/button/new';

import { CodeBlock } from '@atlaskit/code';

import Portal, {

	PORTAL_MOUNT_EVENT,

	PORTAL_UNMOUNT_EVENT,

	type PortalEvent,

} from '@atlaskit/portal';

import { Box, xcss } from '@atlaskit/primitives';

import SectionMessage from '@atlaskit/section-message';

import { token } from '@atlaskit/tokens';



const containerStyles = xcss({

	margin: 'space.200',

});



const verticalSpaceContainerStyles = xcss({

	marginBlockEnd: 'space.200',

});



const portalContentStyles = css({

	margin: `${token('space.0')} ${token('space.200')} ${token('space.200')}`,

});



const figureStyles = css({

	margin: token('space.0'),

});



const PortalEventExample = () => {

	const [isMounted, setIsMounted] = useState(false);

	const [customEventData, setCustomEventData] = useState('');



	useEffect(() => {

		const portalEventListener = ((event: PortalEvent) => {

			const { type, detail } = event;



			setCustomEventData(JSON.stringify({ type, detail }));

		}) as EventListener;



		const unbind: UnbindFn = bindAll(window, [

			{

				type: PORTAL_MOUNT_EVENT,

				listener: portalEventListener,

			},

			{

				type: PORTAL_UNMOUNT_EVENT,

				listener: portalEventListener,

			},

		]);



		return unbind;

	}, []);



	return (

		<Box xcss={containerStyles}>

			<Box xcss={verticalSpaceContainerStyles}>

				<Button appearance="primary" onClick={() => setIsMounted(!isMounted)}>

					{isMounted ? 'Unmount' : 'Mount'} portal

				</Button>

			</Box>

			<div>

				<figure css={figureStyles}>

					<figcaption>PortalEvent specific data:</figcaption>

					<CodeBlock language="JSON" text={customEventData} />

				</figure>

			</div>

			{isMounted && (

				<Portal>

					<div css={portalContentStyles}>

						<SectionMessage>I am inside portal!</SectionMessage>

					</div>

				</Portal>

			)}

		</Box>

	);

};



export default PortalEventExample;
```

## Complex layering

This example shows off all components that rely on portalling and layering to appear in the expected order. 

```jsx
/**

 * @jsxRuntime classic

 * @jsx jsx

 */

import { Fragment, type ReactNode, useState } from 'react';



// eslint-disable-next-line @atlaskit/ui-styling-standard/use-compiled -- Ignored via go/DSP-18766

import { css, jsx } from '@emotion/react';



import Button from '@atlaskit/button/new';

import Flag, { FlagGroup } from '@atlaskit/flag';

import EmojiIcon from '@atlaskit/icon/glyph/emoji';

import InlineDialog from '@atlaskit/inline-dialog';

import ModalDialog, {

	ModalBody,

	ModalFooter,

	ModalHeader,

	ModalTitle,

	ModalTransition,

} from '@atlaskit/modal-dialog';

import {

	Spotlight,

	SpotlightManager,

	SpotlightTarget,

	SpotlightTransition,

} from '@atlaskit/onboarding';

import { token } from '@atlaskit/tokens';

import Tooltip from '@atlaskit/tooltip';



const tooltipContainerStyles = css({

	backgroundColor: token('color.background.neutral'),

});



const TooltipButton = ({

	children,

	onClick,

	id,

}: {

	children: ReactNode;

	onClick: () => void;

	id?: string;

}) => (

	<div css={tooltipContainerStyles}>

		<Tooltip content="Click me">

			<Button id={id} onClick={onClick}>

				{children}

			</Button>

		</Tooltip>

	</div>

);



const spotlightContainerStyles = css({

	display: 'flex',

	padding: token('space.300'),

	justifyContent: 'space-between',

});



type SpotlightProps = {

	stepOne: ReactNode;

	stepTwo: ReactNode;

	stepThree: ReactNode;

	isOpen: boolean;

	onFinish: () => void;

};



const ThreeStepSpotlight = (props: SpotlightProps) => {

	const [step, setStep] = useState(1);

	const { stepOne, stepTwo, stepThree, isOpen, onFinish } = props;



	const next = () => {

		const nextStep = step + 1;

		if (nextStep > 3) {

			setStep(1);

			onFinish();

		} else {

			setStep(nextStep);

		}

	};



	return (

		<SpotlightManager>

			<div css={spotlightContainerStyles}>

				<SpotlightTarget name="1">{stepOne}</SpotlightTarget>

				<SpotlightTarget name="2">{stepTwo}</SpotlightTarget>

				<SpotlightTarget name="3">{stepThree}</SpotlightTarget>

			</div>

			<SpotlightTransition>

				{isOpen && (

					<Spotlight

						actions={[{ onClick: next, text: step === 3 ? 'Close' : 'Next' }]}

						heading={`Here is step ${step} of 3`}

						key={`${step}`}

						target={`${step}`}

					/>

				)}

			</SpotlightTransition>

		</SpotlightManager>

	);

};



type ModalProps = {

	onClose: () => void;

};



const Modal = (props: ModalProps) => {

	const [onboardingOpen, setOnboardingOpen] = useState(false);

	const [inlineOpen, setInlineOpen] = useState(false);

	const [flags, setFlags] = useState<number[]>([]);



	const toggleOnboarding = (onboardingOpen: boolean) => setOnboardingOpen(onboardingOpen);



	const toggleInline = (inlineOpen: boolean) => setInlineOpen(inlineOpen);



	const addFlag = () => setFlags([flags.length, ...flags]);



	const removeFlag = (id: number | string) => setFlags(flags.filter((v) => v !== id));



	const { onClose } = props;



	return (

		<Fragment>

			<ModalDialog onClose={onClose} testId="modal">

				<ModalHeader hasCloseButton>

					<ModalTitle>Modal dialog</ModalTitle>

				</ModalHeader>

				<ModalBody>

					<p>This dialog has three great features:</p>

					<ThreeStepSpotlight

						isOpen={onboardingOpen}

						onFinish={() => toggleOnboarding(false)}

						stepOne={

							<TooltipButton onClick={() => toggleOnboarding(true)} id={'showOnboardingBtn'}>

								Show onboarding

							</TooltipButton>

						}

						stepTwo={

							<InlineDialog content="This button is very nice" isOpen={inlineOpen}>

								<TooltipButton onClick={() => toggleInline(!inlineOpen)}>

									Show an inline dialog

								</TooltipButton>

							</InlineDialog>

						}

						stepThree={

							<TooltipButton onClick={() => addFlag()} id={'showFlagBtn'}>

								Show a flag

							</TooltipButton>

						}

					/>

				</ModalBody>

				<ModalFooter>

					<Button appearance="primary" onClick={onClose}>

						Close

					</Button>

				</ModalFooter>

			</ModalDialog>

			<FlagGroup onDismissed={(id: number | string) => removeFlag(id)}>

				{flags.map((id) => (

					<Flag

						id={id}

						key={`${id}`}

						icon={<EmojiIcon label="Smiley face" />}

						title={`${id + 1}: Whoa a new flag!`}

					/>

				))}

			</FlagGroup>

		</Fragment>

	);

};



const PortalComplexLayeringExample = () => {

	const [modals, setModals] = useState<number[]>([]);



	return (

		<Fragment>

			<ModalTransition>

				{modals.map((id: number) => (

					<Modal key={id} onClose={() => setModals(modals.filter((i: number) => i !== id))} />

				))}

			</ModalTransition>

			<TooltipButton id={'openDialogBtn'} onClick={() => setModals([1])}>

				Open Dialog

			</TooltipButton>

		</Fragment>

	);

};



export default PortalComplexLayeringExample;
```

---

[View Original Documentation](https://atlassian.design/components/portal/examples)
