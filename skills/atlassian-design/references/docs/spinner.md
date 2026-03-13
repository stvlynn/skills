# Spinner

A spinner is an animated spinning icon that lets users know content is being loaded.

---

## Default

The default form of spinner. 

```jsx
import React from 'react';



import Spinner from '@atlaskit/spinner';



export default () => <Spinner testId="spinner" interactionName="load" label="Loading" />;
```

## Sizes

```jsx
/**

 * @jsxRuntime classic

 * @jsx jsx

 */



import { css, jsx } from '@compiled/react';



import Lozenge from '@atlaskit/lozenge';

import Spinner, { type Size } from '@atlaskit/spinner';

import { token } from '@atlaskit/tokens';



const sizes: Size[] = ['xsmall', 'small', 'medium', 'large', 'xlarge', 80];



const containerStyles = css({

	display: 'flex',

	gap: token('space.200', '16px'),

	flexWrap: 'wrap',

});



const itemStyles = css({

	display: 'flex',

	alignItems: 'center',

	justifyContent: 'flex-end',

	gap: token('space.100', '8px'),

	flexDirection: 'column',

});



export default function Example() {

	return (

		<div css={containerStyles}>

			{sizes.map((size: Size) => (

				<div key={size} css={itemStyles}>

					<Spinner size={size} label="Loading" />

					{typeof size === 'number' ? (

						<Lozenge appearance="new">custom</Lozenge>

					) : (

						<Lozenge appearance="success">{size}</Lozenge>

					)}

				</div>

			))}

		</div>

	);

}
```

## Animation

A spinner will always animate itself in. For graceful exit animations we recommend that you use <FadeIn /> from motion 

```jsx
/**

 * @jsxRuntime classic

 * @jsx jsx

 */

import React, { useEffect, useState } from 'react';



import { css, jsx } from '@compiled/react';



import Avatar from '@atlaskit/avatar';

import Button from '@atlaskit/button/new';

import { ExitingPersistence, FadeIn } from '@atlaskit/motion';

import Spinner from '@atlaskit/spinner';

import { token } from '@atlaskit/tokens';

import VisuallyHidden from '@atlaskit/visually-hidden';



type Phase = 'stopped' | 'loading' | 'ready';



const layoutStyles = css({

	display: 'flex',

	justifyContent: 'center',

	gap: token('space.200', '16px'),

});



const columnStyles = css({

	display: 'flex',

	alignItems: 'center',

	flexDirection: 'column',

});



const headingStyles = css({

	marginBlockEnd: token('space.200', '16px'),

});



const loadingContainerStyles = css({

	display: 'flex',

	width: 200,

	height: 200,

	alignItems: 'center',

	justifyContent: 'center',

});



const spinnerStyles = css({ position: 'absolute' });



function Harness({

	children,

	title,

	buttonLabel,

}: {

	children: (phase: Phase) => React.ReactElement;

	title: string;

	buttonLabel: string;

}) {

	const [phase, setPhase] = useState<Phase>('stopped');

	const liveRegionAnnouncement = (() => {

		switch (phase) {

			case 'loading':

				return 'Loading';

			case 'ready':

				return 'Avatar loading completed';

			default:

				return null;

		}

	})();



	useEffect(

		function onPhaseChange() {

			if (phase === 'loading') {

				const id = window.setTimeout(() => setPhase('ready'), 2000);

				return () => window.clearTimeout(id);

			}

		},

		[phase],

	);



	return (

		<div css={columnStyles}>

			<h4 css={headingStyles}>{title}</h4>

			<VisuallyHidden>

				<div aria-live="polite">{liveRegionAnnouncement}</div>

			</VisuallyHidden>

			<Button onClick={() => setPhase('loading')} isDisabled={phase === 'loading'}>

				{buttonLabel}

			</Button>

			<div css={loadingContainerStyles}>{children(phase)}</div>

		</div>

	);

}



function NotAnimated() {

	return (

		<Harness title="No exit animation" buttonLabel="Load avatar without animation">

			{(phase: Phase) => (

				<React.Fragment>

					{phase === 'ready' && <Avatar size="xlarge" />}

					{phase === 'loading' && (

						<span css={spinnerStyles}>

							<Spinner size="xlarge" label="Loading" />

						</span>

					)}

				</React.Fragment>

			)}

		</Harness>

	);

}



function Animated() {

	return (

		<Harness title="With cross fading" buttonLabel="Load avatar with animation">

			{(phase: Phase) => (

				<React.Fragment>

					<ExitingPersistence appear>

						{phase === 'ready' && (

							<FadeIn>

								{(props) => (

									<span {...props}>

										<Avatar size="xlarge" />

									</span>

								)}

							</FadeIn>

						)}

					</ExitingPersistence>

					<ExitingPersistence>

						{phase === 'loading' && (

							<FadeIn onFinish={(value) => console.log('fade in finished', value)}>

								{(props) => (

									<span {...props} css={spinnerStyles}>

										<Spinner size="xlarge" label="Loading" />

									</span>

								)}

							</FadeIn>

						)}

					</ExitingPersistence>

				</React.Fragment>

			)}

		</Harness>

	);

}



export default function Example() {

	return (

		<div css={layoutStyles}>

			<NotAnimated />

			<Animated />

		</div>

	);

}
```

## Spinner over content

When using a spinner directly over content, apply the opacity.loading token to the content container to de-emphasize the content and increase the visibility of the spinner. 

```jsx
import React, { useState } from 'react';



import Button from '@atlaskit/button/new';

import { DynamicTableStateless } from '@atlaskit/dynamic-table';

import { type HeadType, type RowType } from '@atlaskit/dynamic-table/types';



const head: HeadType = {

	cells: [

		{

			key: 'name',

			content: 'Name',

		},

		{

			key: 'size',

			content: 'Size',

		},

		{

			key: 'last-commit',

			content: 'Last commit',

		},

		{

			key: 'message',

			content: 'Message',

		},

	],

};



const rows: RowType[] = [

	{

		cells: [

			{ content: '.editorconfig' },

			{ content: '189 B' },

			{ content: '2018-02-97' },

			{

				content: 'Add .editorconfig to easily configure standard editor settings',

			},

		],

	},

	{

		cells: [

			{ content: '.eslintignore' },

			{ content: '1.21 KB' },

			{ content: '2022-08-17' },

			{

				content: 'DSP-3204 chore: deleted icon-priority',

			},

		],

	},

	{

		cells: [

			{ content: 'eslint.config.cjs' },

			{ content: '28.62 KB' },

			{ content: '2022-08-17' },

			{

				content: 'DSP-3204 chore: deleted icon-priority',

			},

		],

	},

	{

		cells: [

			{ content: '.gitattributes' },

			{ content: '951 B' },

			{ content: '2022-09-05' },

			{

				content: 'DSP-6586 add correct docs delta',

			},

		],

	},

	{

		cells: [

			{ content: '.gitignore' },

			{ content: '2.67 KB' },

			{ content: '2022-09-12' },

			{

				content: 'NO-ISSUE scope gitignore reports to contact folder',

			},

		],

	},

];



const SpinnerOverContentExample = () => {

	const [isLoading, setIsLoading] = useState(false);



	return (

		<>

			<Button onClick={() => setIsLoading((loading) => !loading)}>Toggle loading</Button>

			<DynamicTableStateless

				head={head}

				rows={rows}

				rowsPerPage={5}

				page={1}

				isLoading={isLoading}

			/>

		</>

	);

};



export default SpinnerOverContentExample;
```

| Name | Size | Last commit | Message |
| --- | --- | --- | --- |
| .editorconfig | 189 B | 2018-02-97 | Add .editorconfig to easily configure standard editor settings |
| .eslintignore | 1.21 KB | 2022-08-17 | DSP-3204 chore: deleted icon-priority |
| eslint.config.cjs | 28.62 KB | 2022-08-17 | DSP-3204 chore: deleted icon-priority |
| .gitattributes | 951 B | 2022-09-05 | DSP-6586 add correct docs delta |
| .gitignore | 2.67 KB | 2022-09-12 | NO-ISSUE scope gitignore reports to contact folder |

## Delaying a spinner

Sometimes you might want to delay showing a spinner when loading something asynchronously. The <Spinner /> is only visible to a user after 150-200ms of being rendered because of it's opacity fade in. There is no need to delay a spinner to prevent it quickly flashing on an initial load. If you are concerned about having a spinner flash quickly and then harshly be removed, we recommend that you use <FadeIn /> from motion to gracefully animate the unmount of a spinner. Sometimes you will want to delay a spinner from showing for a longer period of time. A spinner has a delay prop that can be used to achieve a long pause. You can set the value to 500-1000+ ms to prevent a spinner from being shown for a longer period of time. For best results, use <FadeIn /> from motion to fade out the spinner. It's still possible for the spinner to show briefly when your async operation takes slightly longer than your long delay. Fading out your spinner will always look best. No fadeout of spinner Cross fading out the spinners exit with content 

```jsx
/**

 * @jsxRuntime classic

 * @jsx jsx

 */

import React, { useCallback, useContext, useEffect, useMemo, useState } from 'react';



import { css, jsx } from '@compiled/react';



import Avatar from '@atlaskit/avatar';

import Button from '@atlaskit/button/new';

import { Label } from '@atlaskit/form';

import { ExitingPersistence, FadeIn } from '@atlaskit/motion';

import Select, { type ValueType } from '@atlaskit/select';

import Spinner from '@atlaskit/spinner';

import { token } from '@atlaskit/tokens';



type Delays = {

	spinner: number;

	content: number;

};

const DelayContext = React.createContext<Delays>({ spinner: 0, content: 0 });



type Phase = 'stopped' | 'loading' | 'ready';



const layoutStyles = css({

	display: 'grid',

	justifyContent: 'center',

	gridTemplateColumns: 'repeat(auto-fit, minmax(0, 300px))',

	marginBlockStart: token('space.400', '32px'),

});



const controlContainerStyles = css({

	display: 'flex',

	maxWidth: 300,

	margin: '0 auto',

	gap: token('space.100', '8px'),

	flexDirection: 'column',

});



const columnStyles = css({

	display: 'flex',

	alignItems: 'center',

	flexDirection: 'column',

	textAlign: 'center',

});



const columnInfoStyles = css({ minHeight: 70 });



const loadingContainerStyles = css({

	display: 'flex',

	width: 200,

	height: 200,

	alignItems: 'center',

	justifyContent: 'center',

});



const spinnerStyles = css({ position: 'absolute' });



function Harness({

	children,

	title,

	description,

}: {

	children: (phase: Phase, delays: Delays) => React.ReactElement;

	title: string;

	description: string;

}) {

	const [phase, setPhase] = useState<Phase>('stopped');

	const delays: Delays = useContext(DelayContext);



	useEffect(

		function onPhaseChange() {

			if (phase === 'loading') {

				const id = window.setTimeout(() => setPhase('ready'), delays.content);

				return () => window.clearTimeout(id);

			}

		},

		[delays.content, phase],

	);



	return (

		<div css={columnStyles}>

			<h4>{title}</h4>

			<p css={columnInfoStyles}>{description}</p>

			<Button onClick={() => setPhase('loading')} isDisabled={phase === 'loading'}>

				{phase === 'loading' ? 'running' : 'start'}

			</Button>

			<div css={loadingContainerStyles}>{children(phase, delays)}</div>

		</div>

	);

}



function Basic() {

	return (

		<Harness title="Default" description="No fadeout of spinner">

			{(phase: Phase, delays: Delays) => (

				<React.Fragment>

					{phase === 'ready' && <Avatar size="xlarge" />}

					{phase === 'loading' && (

						<span css={spinnerStyles}>

							<Spinner size="xlarge" delay={delays.spinner} label="Loading" />

						</span>

					)}

				</React.Fragment>

			)}

		</Harness>

	);

}



function CrossFade() {

	return (

		<Harness title="Cross fade" description="Cross fading out the spinners exit with content">

			{(phase: Phase, delays: Delays) => (

				<React.Fragment>

					<ExitingPersistence appear>

						{phase === 'ready' && (

							<FadeIn>

								{(props) => (

									<span {...props}>

										<Avatar size="xlarge" />

									</span>

								)}

							</FadeIn>

						)}

					</ExitingPersistence>

					<ExitingPersistence>

						{phase === 'loading' && (

							<FadeIn>

								{(props) => (

									<span {...props} css={spinnerStyles}>

										<Spinner size="xlarge" delay={delays.spinner} label="Loading" />

									</span>

								)}

							</FadeIn>

						)}

					</ExitingPersistence>

				</React.Fragment>

			)}

		</Harness>

	);

}



type Option = { value: string; label: string };



const contentDelayOptions: Option[] = [

	{ value: '10', label: 'Content load time: tiny (10ms)' },

	{ value: '50', label: 'Content load time: small (50ms)' },

	{ value: '100', label: 'Content load time: medium (100ms)' },

	{ value: '500', label: 'Content load time: long (500ms)' },

	{ value: '2000', label: 'Content load time: super long (2000ms)' },

];

const defaultContentDelay: Option = contentDelayOptions[1];



const spinnerDelayOptions: Option[] = [

	{ value: '0', label: 'Spinner delay: none (default)' },

	{ value: '100', label: 'Spinner delay: too short (100ms)' },

	{ value: '500', label: 'Spinner delay: medium (500ms)' },

	{ value: '1000', label: 'Spinner delay: long (1000ms)' },

];

const defaultSpinnerDelay: Option = spinnerDelayOptions[0];



function Example() {

	const [contentDelay, setContentDelay] = useState(Number(defaultContentDelay.value));

	const onContentDelayChange = useCallback((result: ValueType<Option>) => {

		if (result != null && !Array.isArray(result)) {

			// doing a cast to Option as Array.isArray is not narrowing the type

			setContentDelay(Number((result as Option).value));

		}

	}, []);



	const [spinnerDelay, setSpinnerDelay] = useState(Number(defaultContentDelay.value));

	const onSpinnerDelayChange = useCallback((result: ValueType<Option>) => {

		if (result != null && !Array.isArray(result)) {

			// doing a cast to Option as Array.isArray is not narrowing the type

			setSpinnerDelay(Number((result as Option).value));

		}

	}, []);



	const delay: Delays = useMemo(

		() => ({

			content: contentDelay,

			spinner: spinnerDelay,

		}),

		[contentDelay, spinnerDelay],

	);



	return (

		<DelayContext.Provider value={delay}>

			<div css={controlContainerStyles}>

				<div>

					<Label htmlFor="input-content-delay-options">Content delay options</Label>

					<Select

						inputId="input-content-delay-options"

						options={contentDelayOptions}

						defaultValue={defaultContentDelay}

						onChange={onContentDelayChange}

					/>

				</div>

				<div>

					<Label htmlFor="input-spinner-delay-options">Spinner delay options</Label>

					<Select

						inputId="input-spinner-delay-options"

						options={spinnerDelayOptions}

						defaultValue={defaultSpinnerDelay}

						onChange={onSpinnerDelayChange}

					/>

				</div>

			</div>

			<div css={layoutStyles}>

				<Basic />

				<CrossFade />

			</div>

		</DelayContext.Provider>

	);

}



export default () => <Example />;
```

---

[View Original Documentation](https://atlassian.design/components/spinner/examples)
