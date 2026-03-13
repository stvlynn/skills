# Anchor

An anchor is a primitive for building custom links.

---

## Installation

Anchor is a primitive for building custom links with Atlassian Design System styling, routing support, and built-in event tracking. It renders an anchor <a> element.

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

Anchor is unstyled besides a default underline and consistent Atlassian Design System focus styles. If you are using the CSS reset, anchor will also inherit some global styles.

```jsx
import React from 'react';



import Anchor from '@atlaskit/primitives/anchor';



export default function Default() {

	return <Anchor href="/components/primitives/overview">Anchor</Anchor>;

}
```

## Basic styling with XCSS

Anchor can be styled further using the design system styling API, XCSS.

```jsx
import React from 'react';



import Image from '@atlaskit/image';

import Lozenge from '@atlaskit/lozenge';

import { Anchor, Box, xcss } from '@atlaskit/primitives';



import ButtonIcon from '../../images/button.png';



const anchorStyles = xcss({

	color: 'color.link',

	backgroundColor: 'elevation.surface',

	textDecoration: 'none',

	borderWidth: 'border.width',

	borderStyle: 'solid',

	borderColor: 'color.border',

	borderRadius: '3px',

	display: 'inline-flex',

	alignItems: 'center',

	gap: 'space.100',

	paddingInline: 'space.050',

	paddingBlock: 'space.025',



	':hover': {

		backgroundColor: 'elevation.surface.hovered',

		textDecoration: 'none',

	},

	':active': {

		color: 'color.link.pressed',

		backgroundColor: 'elevation.surface.pressed',

	},

	':visited': {

		color: 'color.link.visited',

	},

	':visited:active': {

		color: 'color.link.visited.pressed',

	},

});



const iconContainerStyles = xcss({

	width: '16px',

	display: 'flex',

});



export default function Basic() {

	return (

		<Anchor

			href="https://www.atlassian.com/software/atlas"

			interactionName="atlas-link"

			xcss={anchorStyles}

			target="_blank"

			rel="noopener noreferrer"

		>

			<Box xcss={iconContainerStyles}>

				<Image src={ButtonIcon} alt="" />

			</Box>

			Evolving Button: Open beta to GA

			<Lozenge appearance="success">On track</Lozenge>

		</Anchor>

	);

}
```

## Advanced styling

Use a combination of XCSS and other primitives for more complex designs.

## Pick up where you left off

### Anchor primitive is now in beta!

### Impact & release planning

### How to implement dark mode

### New Bitbucket pull requests

```jsx
import React from 'react';



import Heading from '@atlaskit/heading';

import { type IconProps } from '@atlaskit/icon';

import Blog24Icon from '@atlaskit/icon-object/glyph/blog/24';

import Improvement24Icon from '@atlaskit/icon-object/glyph/improvement/24';

import Page24Icon from '@atlaskit/icon-object/glyph/page/24';

import { Anchor, Box, Grid, Inline, Stack, Text, xcss } from '@atlaskit/primitives';

import { media } from '@atlaskit/primitives/responsive';



const anchorStyles = xcss({

	color: 'color.text',

	backgroundColor: 'elevation.surface',

	padding: 'space.200',

	textDecoration: 'none',

	borderColor: 'color.border',

	borderStyle: 'solid',

	borderWidth: 'border.width',

	borderRadius: '3px',



	':hover': {

		backgroundColor: 'elevation.surface.hovered',

		textDecoration: 'none',

	},

	':active': {

		backgroundColor: 'elevation.surface.pressed',

	},

});



const iconContainerStyles = xcss({

	width: '24px',

	display: 'flex',

});



const gridStyles = xcss({

	[media.above.sm]: {

		gridTemplateColumns: '1fr 1fr',

	},

});



type PageLinkProps = {

	href: string;

	title: string;

	space: string;

	lastVisited: string;

	icon: React.ComponentType<IconProps>;

};



const PageLink = ({ href, title, space, lastVisited, icon: Icon }: PageLinkProps) => {

	return (

		<Anchor href={href} xcss={anchorStyles}>

			<Stack space="space.100">

				<Inline space="space.150" alignBlock="center">

					<Box xcss={iconContainerStyles}>

						<Icon label="" />

					</Box>

					<Stack>

						<Heading as="h3" size="small">

							{title}

						</Heading>

						<Text color="color.text.subtle" size="small">

							{space}

						</Text>

					</Stack>

				</Inline>

				<Text color="color.text.subtle" size="small">

					Visited {lastVisited}

				</Text>

			</Stack>

		</Anchor>

	);

};



export default function Styled() {

	return (

		<Stack space="space.200">

			<Heading as="h2" size="small">

				Pick up where you left off

			</Heading>

			<Grid rowGap="space.100" columnGap="space.100" templateColumns="1fr" xcss={gridStyles}>

				<PageLink

					href="/components/primitives/overview"

					icon={Blog24Icon}

					title="Anchor primitive is now in beta!"

					space="Design System Team"

					lastVisited="1 hour ago"

				/>

				<PageLink

					href="/components/primitives/overview"

					icon={Page24Icon}

					title="Impact & release planning"

					space="Design System Team"

					lastVisited="1 day ago"

				/>

				<PageLink

					href="/components/primitives/overview"

					icon={Page24Icon}

					title="How to implement dark mode"

					space="Design System Team"

					lastVisited="12 May 2024"

				/>

				<PageLink

					href="/components/primitives/overview"

					icon={Improvement24Icon}

					title="New Bitbucket pull requests"

					space="Bitbucket Cloud"

					lastVisited="10 May 2024"

				/>

			</Grid>

		</Stack>

	);

}
```

## HTML attributes

Anchor can pass all valid anchor HTML attributes, such as rel or download, to the underlying <a> element.

```jsx
import React from 'react';



import Anchor from '@atlaskit/primitives/anchor';



export default function AnchorHTMLAttributes() {

	return (

		<Anchor href="https://www.atlassian.com/" target="_blank" rel="noopener noreferrer">

			Visit the Atlassian website

		</Anchor>

	);

}
```

## Router links

Routing libraries often supply link components enhanced with routing support. You can configure this in the AppProvider context, and anchor will automatically use it. This example shows a configuration for React Resource Router, however any routing library can be used. Using this method, anchor accepts href as a string for standard usage. For advanced usage, an object can be passed. Anchor will only render a router link if:

```jsx
import React, { forwardRef, type Ref } from 'react';



import { Link, type LinkProps, RouteComponent, Router } from 'react-resource-router';



import AppProvider, { type RouterLinkComponentProps } from '@atlaskit/app-provider';

import Anchor from '@atlaskit/primitives/anchor';



export type ReactResourceRouterLinkConfig = Pick<LinkProps, 'to' | 'href' | 'replace'>;



const HomePage = () => {

	return (

		<>

			{/* Internal link: Will render a router link */}

			<Anchor href="/about">Internal link</Anchor>

			{/* Advanced usage */}

			<Anchor<ReactResourceRouterLinkConfig>

				href={{

					to: '/about',

					replace: true,

				}}

			>

				Advanced link

			</Anchor>

			{/* External link: Will not render a router link */}

			<Anchor href="https://www.atlassian.com">External link</Anchor>

			{/* Non-HTTP-based: Will not render a router link */}

			<Anchor href="mailto:test@example.com">Email link</Anchor>

		</>

	);

};



/**

 * Configures a router link for the app provider.

 */

const MyRouterLinkComponent = forwardRef(

	(

		{ href, children, ...rest }: RouterLinkComponentProps<ReactResourceRouterLinkConfig>,

		ref: Ref<HTMLAnchorElement>,

	) => {

		// A basic link by passing a string as the component's `href` prop.

		if (typeof href === 'string') {

			return (

				<Link ref={ref} href={href} {...rest}>

					{children}

				</Link>

			);

		}



		// Advanced link configuration by passing an object as the

		// component's `href` prop

		return (

			<Link ref={ref} href={href.href} to={href.to} replace={href.replace} {...rest}>

				{children}

			</Link>

		);

	},

);



export default function RouterLinkConfiguration() {

	return (

		<AppProvider routerLinkComponent={MyRouterLinkComponent}>

			<Router

				routes={[

					{

						name: 'home',

						path: '',

						exact: true,

						component: HomePage,

					},

				]}

			>

				<RouteComponent />

			</Router>

		</AppProvider>

	);

}
```

## Event tracking

Anchor has utilities to make tracking events easier. Events won't be captured unless listeners are set up to handle them.

### Track events for any analytics provider

Anchor comes with built-in Atlaskit analytics support using the Analytics next package, and fires events for available listeners. Currently this is only available for onClick. Events always fire on the atlaskit channel. To fire events on other channels as well, use the provided analyticsEvent in onClick. To configure event data, use componentName (defaults to 'Anchor') and use analyticsContext to pass other metadata. See the event data in the console.

```jsx
import React, { useCallback } from 'react';



import { AnalyticsListener, type UIAnalyticsEvent } from '@atlaskit/analytics-next';

import { Inline } from '@atlaskit/primitives';

import Anchor from '@atlaskit/primitives/anchor';



export default function Analytics() {

	const handleEvent = useCallback((event: UIAnalyticsEvent, channel?: string) => {

		console.log(`Channel: '${channel}'`, event);

	}, []);



	return (

		<AnalyticsListener channel="*" onEvent={handleEvent}>

			<Inline space="space.100">

				<Anchor href="/components/primitives/overview" target="_blank">

					Default

				</Anchor>

				<Anchor

					href="/components/primitives/overview"

					target="_blank"

					onClick={(_, analyticsEvent) => {

						analyticsEvent.fire('my-channel');

					}}

				>

					Fires on "my-channel"

				</Anchor>

				<Anchor

					href="/components/primitives/overview"

					target="_blank"

					componentName="MyButton"

					analyticsContext={{

						color: 'blue',

						someId: 937458,

					}}

				>

					Customized event data

				</Anchor>

			</Inline>

		</AnalyticsListener>

	);

}
```

### Track events for Atlassian internal services

The Atlassian analytics bridge makes Atlaskit analytics events compatible with GASv3 (Global Analytics Service). This can also inject an actionSubjectId to the event if required. See the event data in the console. By default, anchor fires React UFO (Unified Frontend Observability) press interactions for available listeners. This helps Atlassian measure performance and reliability. You can provide more detail using the interactionName prop.

```jsx
import React, { useCallback } from 'react';



import { AnalyticsListener, type UIAnalyticsEvent } from '@atlaskit/analytics-next';

import Anchor from '@atlaskit/primitives/anchor';

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

		(_: React.MouseEvent<HTMLAnchorElement, MouseEvent>, analyticsEvent: UIAnalyticsEvent) => {

			fireUIAnalytics(analyticsEvent, 'theActionSubjectId');

		},

		[],

	);



	return (

		<AnalyticsListener channel={ANALYTICS_BRIDGE_CHANNEL} onEvent={handleEvent}>

			<Anchor

				href="/components/primitives/overview"

				target="_blank"

				onClick={handleClick}

				analyticsContext={{

					attributes: {

						color: 'blue',

						someId: 937458,

					},

				}}

			>

				Fire GASv3 compatible event

			</Anchor>

		</AnalyticsListener>

	);

}
```

## Your projects

```jsx
import React from 'react';



import __noop from '@atlaskit/ds-lib/noop';

import { FlagsProvider, useFlags } from '@atlaskit/flag';

import Heading from '@atlaskit/heading';

import InformationIcon from '@atlaskit/icon/glyph/info';

import Image from '@atlaskit/image';

import InteractionContext from '@atlaskit/interaction-context';

import { Anchor, Box, Inline, Stack, xcss } from '@atlaskit/primitives';

import { token } from '@atlaskit/tokens';



import ButtonIcon from '../../images/button.png';

import ThemesIcon from '../../images/themes.png';

import WatermelonIcon from '../../images/watermelon.png';



const anchorStyles = xcss({

	color: 'color.text',

	textDecoration: 'none',



	':hover': {

		color: 'color.text',

		textDecoration: 'underline',

	},

	':active': {

		textDecoration: 'none',

	},

	':visited': {

		color: 'color.link.visited',

	},

	':visited:active': {

		color: 'color.link.visited.pressed',

	},

});



const iconContainerStyles = xcss({

	width: '24px',

	display: 'flex',

});



type ProjectLinkProps = {

	children: string;

	icon: string;

	id: string;

};



const ProjectLink = ({ children, icon, id }: ProjectLinkProps) => {

	return (

		<Anchor href="#" xcss={anchorStyles} interactionName={`anchor-${id}`}>

			<Inline space="space.150" alignBlock="center">

				<Box xcss={iconContainerStyles}>

					<Image src={icon} alt="" />

				</Box>

				{children}

			</Inline>

		</Anchor>

	);

};



const Projects = () => {

	const { showFlag } = useFlags();



	return (

		<InteractionContext.Provider

			value={{

				hold: __noop,

				tracePress: (name) => {

					console.log('Traced a press!', name);

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

			<Stack space="space.200">

				<Heading as="h2" size="small">

					Your projects

				</Heading>

				<Stack space="space.100">

					<ProjectLink icon={ButtonIcon} id="evolving-button">

						Evolving Button: Open beta to GA

					</ProjectLink>

					<ProjectLink icon={ThemesIcon} id="increased-contrast-themes">

						Increased contrast themes

					</ProjectLink>

					<ProjectLink icon={WatermelonIcon} id="typography">

						ADS Typography

					</ProjectLink>

				</Stack>

			</Stack>

		</InteractionContext.Provider>

	);

};



export default function PressTracing() {

	return (

		<FlagsProvider>

			<Projects />

		</FlagsProvider>

	);

}
```

---

[View Original Documentation](https://atlassian.design/components/primitives/anchor/examples)
