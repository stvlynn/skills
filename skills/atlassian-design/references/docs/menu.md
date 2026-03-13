# Menu

A list of options to help users navigate, or perform actions.

---

## Default

The menu is a collection of composable menu components intended for use as product wayfinding. 

```jsx
import React from 'react';



import { ButtonItem, MenuGroup, Section } from '@atlaskit/menu';

import ImgIcon from '../common/img-icon';

import MenuGroupContainer from '../common/menu-group-container';

import battery from '../icons/battery.png';

import cloud from '../icons/cloud.png';

import Drill from '../icons/drill.png';

import koala from '../icons/koala.png';

import ui from '../icons/ui.png';

import wallet from '../icons/wallet.png';

import Yeti from '../icons/yeti.png';



export default () => (

	<MenuGroupContainer>

		<MenuGroup>

			<Section title="Starred">

				<ButtonItem

					iconBefore={<ImgIcon src={Yeti} alt={'Yeti'} />}

					description="Next-gen software project"

				>

					Navigation System

				</ButtonItem>

				<ButtonItem

					iconBefore={<ImgIcon src={Drill} alt={'Drill'} />}

					description="Next-gen service desk"

				>

					Analytics Platform

				</ButtonItem>

			</Section>

			<Section title="Recent">

				<ButtonItem

					iconBefore={<ImgIcon src={battery} alt={'Battery'} />}

					description="Next-gen software project"

				>

					Fabric Editor

				</ButtonItem>

				<ButtonItem

					iconBefore={<ImgIcon src={cloud} alt={'Cloud'} />}

					description="Classic business project"

				>

					Content Services

				</ButtonItem>

				<ButtonItem

					iconBefore={<ImgIcon src={wallet} alt={'Wallet'} />}

					description="Next-gen software project"

				>

					Trinity Mobile

				</ButtonItem>

				<ButtonItem

					iconBefore={<ImgIcon src={koala} alt={'Koala'} />}

					description="Classic service desk"

				>

					Customer Feedback

				</ButtonItem>

				<ButtonItem

					iconBefore={<ImgIcon src={ui} alt={'UI icon'} />}

					description="Classic software project"

				>

					Design System

				</ButtonItem>

			</Section>

			<Section hasSeparator>

				<ButtonItem>View all projects</ButtonItem>

				<ButtonItem>Create project</ButtonItem>

			</Section>

		</MenuGroup>

	</MenuGroupContainer>

);
```

## Menu structure

Use menu groups, sections and heading items to structure the menu. 

```jsx
import React from 'react';



import { ButtonItem, HeadingItem, MenuGroup, Section } from '@atlaskit/menu';

import ImgIcon from '../common/img-icon';

import MenuGroupContainer from '../common/menu-group-container';

import battery from '../icons/battery.png';

import cloud from '../icons/cloud.png';

import Drill from '../icons/drill.png';

import koala from '../icons/koala.png';

import ui from '../icons/ui.png';

import wallet from '../icons/wallet.png';

import Yeti from '../icons/yeti.png';



export default () => (

	<MenuGroupContainer>

		<MenuGroup>

			<Section title="Starred">

				<ButtonItem

					iconBefore={<ImgIcon src={Yeti} alt={'Yeti'} />}

					description="Next-gen software project"

				>

					Navigation System

				</ButtonItem>

				<ButtonItem

					iconBefore={<ImgIcon src={Drill} alt={'Drill'} />}

					description="Next-gen service desk"

				>

					Analytics Platform

				</ButtonItem>

			</Section>

			<Section title="Recent">

				<ButtonItem

					iconBefore={<ImgIcon src={battery} alt={'Battery'} />}

					description="Next-gen software project"

				>

					Fabric Editor

				</ButtonItem>

				<ButtonItem

					iconBefore={<ImgIcon src={cloud} alt={'Cloud'} />}

					description="Classic business project"

				>

					Content Services

				</ButtonItem>

				<ButtonItem

					iconBefore={<ImgIcon src={wallet} alt={'Wallet'} />}

					description="Next-gen software project"

				>

					Trinity Mobile

				</ButtonItem>

				<ButtonItem

					iconBefore={<ImgIcon src={koala} alt={'Koala'} />}

					description="Classic service desk"

				>

					Customer Feedback

				</ButtonItem>

				<ButtonItem

					iconBefore={<ImgIcon src={ui} alt={'UI icon'} />}

					description="Classic software project"

				>

					Design System

				</ButtonItem>

			</Section>

			<Section hasSeparator>

				<HeadingItem>Projects</HeadingItem>

				<ButtonItem>View all projects</ButtonItem>

				<ButtonItem>Create project</ButtonItem>

			</Section>

		</MenuGroup>

	</MenuGroupContainer>

);
```

## Menu items

### Button item

The button item component renders a menu item wrapped in a button tag <button>. Use this component when you have an action that does something other than navigating to a new page or context. 

```jsx
/**

 * @jsxRuntime classic

 * @jsx jsx

 */



import { cssMap, jsx } from '@compiled/react';



import { B400, B50, N10, N30, N500 } from '@atlaskit/theme/colors';

import { token } from '@atlaskit/tokens';



import { ButtonItem } from '@atlaskit/menu';

import ImgIcon from '../common/img-icon';

import Yeti from '../icons/yeti.png';



// Mimics overrides in side-navigation

const styles = cssMap({

	root: {

		paddingBlockStart: token('space.100'),

		paddingInlineEnd: token('space.300'),

		paddingBlockEnd: token('space.100'),

		paddingInlineStart: token('space.300'),

		borderRadius: '3px',

		backgroundColor: N10,

		color: N500,

		'&:hover': {

			backgroundColor: N30,

			textDecoration: 'none',

			color: N500,

		},

		'&:active': {

			color: B400,

			backgroundColor: B50,

			boxShadow: 'none',

		},

		// eslint-disable-next-line @atlaskit/ui-styling-standard/no-nested-selectors

		'[data-item-elem-before]': {

			display: 'flex',

			height: 8 * 1.25,

			width: 8 * 1.25,

			alignItems: 'center',

			justifyContent: 'center',

			marginRight: token('space.200'),

		},

	},

	disabled: {

		color: token('color.text.disabled'),

		backgroundColor: N10,

		'&:hover, &:active': {

			backgroundColor: N10,

			color: token('color.text.disabled'),

		},

	},

});



export default () => (

	<div data-testid="button-items">

		<ButtonItem isSelected>Activate</ButtonItem>

		<ButtonItem isDisabled>Activate</ButtonItem>

		<ButtonItem>Activate</ButtonItem>

		<ButtonItem description="Next-gen software project">Activate</ButtonItem>

		<ButtonItem description="Legacy software project" isDisabled>

			Activate

		</ButtonItem>

		<ButtonItem iconBefore={<ImgIcon src={Yeti} alt="" />} description="Next-gen software project">

			Activate

		</ButtonItem>

		<ButtonItem css={styles.root} description="Style overrides">

			Activate

		</ButtonItem>

		<ButtonItem isDisabled css={[styles.root, styles.disabled]} description="Style overrides">

			Activate

		</ButtonItem>

		<ButtonItem css={styles.root} description="Style overrides">

			Activate

		</ButtonItem>

	</div>

);
```

### Link item

The link item component renders a menu item wrapped in an anchor tag <a>. This is the most common type of menu item, as most menu items are used to send people to another location. For menu items that do something else, use the button item component instead. If you need to use a specific router component for route transitions, you'll want to compose them together using the custom item component. 

```jsx
import React, { type MouseEvent, useState } from 'react';



import { Box } from '@atlaskit/primitives';



import { LinkItem, type LinkItemProps } from '@atlaskit/menu';

import ImgIcon from '../common/img-icon';

import koala from '../icons/koala.png';



const useLinkItemComputedProps = (initialSelectedHref?: string) => {

	const [currentHref, setCurrentHref] = useState<string | undefined>(initialSelectedHref);



	const getComputedProps = ({ href, ...restProps }: LinkItemProps) => ({

		href,

		...restProps,

		isSelected: currentHref === href,

		onClick: () => setCurrentHref(href),

	});



	return getComputedProps;

};



export default () => {

	const getComputedProps = useLinkItemComputedProps('#link-item2');



	return (

		/**

		 * It is not normally acceptable to add click handlers to non-interactive elements

		 * as this is an accessibility anti-pattern. However, because this instance is

		 * for performance reasons (to avoid multiple click handlers) and not creating an

		 * inaccessible custom element, we can add role="presentation" so that there is

		 * no negative impacts to assistive technologies.

		 */

		// eslint-disable-next-line @atlassian/a11y/interactive-element-not-keyboard-focusable

		<Box onClick={(e: MouseEvent) => e.preventDefault()} role="presentation">

			<LinkItem {...getComputedProps({ href: '#link-item1' })}>Customer Feedback</LinkItem>

			<LinkItem {...getComputedProps({ href: '#link-item2' })}>Customer Feedback</LinkItem>

			<LinkItem {...getComputedProps({ href: '#link-item3' })} isDisabled>

				Customer Feedback

			</LinkItem>

			<LinkItem {...getComputedProps({ href: '#link-item4' })} description="Classic service desk">

				Customer Feedback

			</LinkItem>

			<LinkItem

				{...getComputedProps({ href: '#link-item5' })}

				iconBefore={<ImgIcon src={koala} alt={'A koala'} />}

				description="Classic service desk"

			>

				Customer Feedback

			</LinkItem>

			<LinkItem {...getComputedProps({ href: 'https://atlassian.design' })} testId="link-item">

				Atlassian Design

			</LinkItem>

		</Box>

	);

};
```

### Custom item

Use custom item when you want to create a item using a your own component that inherits the look and feel of a menu item. For example, to use your own router link component. Your custom component will be given all overflow props passed to the custom item component. 

```jsx
/**

 * @jsxRuntime classic

 * @jsx jsx

 */

import { cssMap, jsx } from '@compiled/react';



import Icon from '@atlaskit/icon';

import { Box } from '@atlaskit/primitives/compiled';

import { B100 } from '@atlaskit/theme/colors';



import { CustomItem, type CustomItemComponentProps } from '@atlaskit/menu';

import Slack from '../icons/slack';



type CustomComponentWithHrefProps = CustomItemComponentProps & {

	href: string;

};



const CustomComponent = ({ children, href, ...props }: CustomComponentWithHrefProps) => {

	return (

		// eslint-disable-next-line @repo/internal/react/no-unsafe-spread-props, @atlaskit/design-system/no-html-anchor, @atlaskit/design-system/no-html-anchor

		<a href={href} {...props}>

			{children}

		</a>

	);

};



const styles = cssMap({

	root: {

		position: 'relative',

		overflow: 'hidden',

		userSelect: 'none',

	},

	interactive: {

		'&::before': {

			content: '""',

			position: 'absolute',

			left: 0,

			top: 0,

			bottom: 0,

			width: 3,

			transform: 'translateX(-1px)',

			transition: 'transform 70ms ease-in-out',

			backgroundColor: B100,

		},

		'&:hover::before': {

			transform: 'translateX(0)',

		},

	},

});



export default () => (

	/**

	 * It is not normally acceptable to add click handlers to non-interactive elements

	 * as this is an accessibility anti-pattern. However, because this instance is

	 * for performance reasons (to avoid multiple click handlers) and not creating an

	 * inaccessible custom element, we can add role="presentation" so that there is

	 * no negative impacts to assistive technologies.

	 */

	// eslint-disable-next-line @atlassian/a11y/interactive-element-not-keyboard-focusable

	<Box onClick={(e: React.MouseEvent) => e.preventDefault()} role="presentation">

		<CustomItem

			href="/navigation-system"

			component={CustomComponent}

			css={[styles.root, styles.interactive]}

		>

			CustomItem

		</CustomItem>

		<CustomItem

			href="/navigation-system-1"

			isSelected

			component={CustomComponent}

			css={[styles.root, styles.interactive]}

		>

			isSelected CustomItem

		</CustomItem>

		<CustomItem

			href="/navigation-system-2"

			isDisabled

			component={CustomComponent}

			css={styles.root}

		>

			isDisabled CustomItem

		</CustomItem>

		<CustomItem

			href="/navigation-system-3"

			component={CustomComponent}

			iconBefore={<Icon glyph={Slack} label="" />}

			css={[styles.root, styles.interactive]}

		>

			iconBefore CustomItem

		</CustomItem>

		<CustomItem

			href="/navigation-system-4"

			component={CustomComponent}

			iconBefore={<Icon glyph={Slack} label="" />}

			description="Next-gen software project"

			css={[styles.root, styles.interactive]}

		>

			iconBefore and description CustomItem

		</CustomItem>

	</Box>

);
```

## Section and heading item

When there are a large number of items in a menu, allowing users who navigate with a screen reader to skip over sections can greatly improve the user experience. This behavior is done by default with this component by setting a group role and label. 

```jsx
import React from 'react';



import { ButtonItem, MenuGroup, Section } from '@atlaskit/menu';

import MenuGroupContainer from '../common/menu-group-container';



export default () => (

	<MenuGroupContainer>

		<MenuGroup>

			<Section title="Actions">

				<ButtonItem>Create article</ButtonItem>

			</Section>

			<Section>

				<ButtonItem>Create article</ButtonItem>

			</Section>

		</MenuGroup>

	</MenuGroupContainer>

);
```

### Custom heading item

It may be necessary to manually set the HeadingItem; in these cases the below code provides an example of how to maintain accessibility. 

```jsx
import React from 'react';



import { ButtonItem, HeadingItem, MenuGroup, Section } from '@atlaskit/menu';

import MenuGroupContainer from '../common/menu-group-container';



export default () => (

	<MenuGroupContainer>

		<MenuGroup>

			<Section aria-labelledby="actions">

				<HeadingItem id="actions" aria-hidden>

					Actions

				</HeadingItem>

				<ButtonItem>Create article</ButtonItem>

			</Section>

		</MenuGroup>

	</MenuGroupContainer>

);
```

### Heading item level

Using headingLevel prop to change the level of the heading. The default heading level is h2. Make sure that headings are in the correct order relative to the pages the menu is on, and don’t skip levels. 

```jsx
import React from 'react';



import { HeadingItem, MenuGroup, Section } from '@atlaskit/menu';

import MenuGroupContainer from '../common/menu-group-container';



export default () => (

	<MenuGroupContainer>

		<MenuGroup>

			<Section>

				<HeadingItem>Heading level 2 (default)</HeadingItem>

			</Section>

			<Section>

				<HeadingItem headingLevel={3}>Heading level 3</HeadingItem>

			</Section>

			<Section>

				<HeadingItem headingLevel={4}>Heading level 4</HeadingItem>

			</Section>

			<Section>

				<HeadingItem headingLevel={5}>Heading level 5</HeadingItem>

			</Section>

			<Section>

				<HeadingItem headingLevel={6}>Heading level 6</HeadingItem>

			</Section>

		</MenuGroup>

	</MenuGroupContainer>

);
```

## Density

The menu group can be configured to accept different spacing values. Applying a compact spacing value will trim the gutters and whitespace, for higher density content. 

```jsx
import React from 'react';



import { ButtonItem, MenuGroup, Section } from '@atlaskit/menu';

import ImgIcon from '../common/img-icon';

import MenuGroupContainer from '../common/menu-group-container';

import battery from '../icons/battery.png';

import cloud from '../icons/cloud.png';

import Drill from '../icons/drill.png';

import koala from '../icons/koala.png';

import ui from '../icons/ui.png';

import wallet from '../icons/wallet.png';

import Yeti from '../icons/yeti.png';



export default () => (

	<MenuGroupContainer>

		<MenuGroup spacing="compact">

			<Section title="Starred">

				<ButtonItem

					iconBefore={<ImgIcon src={Yeti} alt={'Yeti'} />}

					description="Next-gen software project"

				>

					Navigation System

				</ButtonItem>

				<ButtonItem

					iconBefore={<ImgIcon src={Drill} alt={'Drill'} />}

					description="Next-gen service desk"

				>

					Analytics Platform

				</ButtonItem>

			</Section>

			<Section title="Recent">

				<ButtonItem

					iconBefore={<ImgIcon src={battery} alt={'Battery'} />}

					description="Next-gen software project"

				>

					Fabric Editor

				</ButtonItem>

				<ButtonItem

					iconBefore={<ImgIcon src={cloud} alt={'Cloud'} />}

					description="Classic business project"

				>

					Content Services

				</ButtonItem>

				<ButtonItem

					iconBefore={<ImgIcon src={wallet} alt={'Wallet'} />}

					description="Next-gen software project"

				>

					Trinity Mobile

				</ButtonItem>

				<ButtonItem

					iconBefore={<ImgIcon src={koala} alt={'Koala'} />}

					description="Classic service desk"

				>

					Customer Feedback

				</ButtonItem>

				<ButtonItem

					iconBefore={<ImgIcon src={ui} alt={'UI icon'} />}

					description="Classic software project"

				>

					Design System

				</ButtonItem>

			</Section>

			<Section hasSeparator>

				<ButtonItem>View all projects</ButtonItem>

				<ButtonItem>Create project</ButtonItem>

			</Section>

		</MenuGroup>

	</MenuGroupContainer>

);
```

## Scrolling

### Scrollable menu

Menus can be scrollable to fit a fixed height or space. 

```jsx
import React from 'react';



import { ButtonItem, MenuGroup, Section } from '@atlaskit/menu';

import ImgIcon from '../common/img-icon';

import MenuGroupContainer from '../common/menu-group-container';

import battery from '../icons/battery.png';

import cloud from '../icons/cloud.png';

import Drill from '../icons/drill.png';

import koala from '../icons/koala.png';

import ui from '../icons/ui.png';

import wallet from '../icons/wallet.png';

import Yeti from '../icons/yeti.png';



export default () => {

	return (

		<MenuGroupContainer>

			<MenuGroup maxHeight={300}>

				<Section title="starred">

					<ButtonItem

						iconBefore={<ImgIcon src={Yeti} alt={'Yeti'} />}

						description="Next-gen software project"

					>

						Navigation System

					</ButtonItem>

					<ButtonItem

						iconBefore={<ImgIcon src={Drill} alt={'Drill'} />}

						description="Next-gen service desk"

					>

						Analytics Platform

					</ButtonItem>

				</Section>

				<Section title="Recent">

					<ButtonItem

						iconBefore={<ImgIcon src={battery} alt={'Battery'} />}

						description="Next-gen software project"

					>

						Fabric Editor

					</ButtonItem>

					<ButtonItem

						iconBefore={<ImgIcon src={cloud} alt={'Cloud'} />}

						description="Classic business project"

					>

						Content Services

					</ButtonItem>

					<ButtonItem

						iconBefore={<ImgIcon src={wallet} alt={'Wallet'} />}

						description="Next-gen software project"

					>

						Trinity Mobile

					</ButtonItem>

					<ButtonItem

						iconBefore={<ImgIcon src={koala} alt={'Koala'} />}

						description="Classic service desk"

					>

						Customer Feedback

					</ButtonItem>

					<ButtonItem

						iconBefore={<ImgIcon src={ui} alt={'UI'} />}

						description="Classic software project"

					>

						Design System

					</ButtonItem>

				</Section>

				<Section hasSeparator>

					<ButtonItem>View all projects</ButtonItem>

					<ButtonItem>Create project</ButtonItem>

				</Section>

			</MenuGroup>

		</MenuGroupContainer>

	);

};
```

### Scrollable sections

For menus with distinct sections, it's possible to have some scrollable sections. Scrollable sections don't have as much visual affordance, and should be reserved for user-generated content where the number of menu items isn't known. To defer loading the entire menu, the contents can be rendered as skeleton placeholders while the items load asynchronously. 

```jsx
import React from 'react';



import { ButtonItem, MenuGroup, Section } from '@atlaskit/menu';

import ImgIcon from '../common/img-icon';

import MenuGroupContainer from '../common/menu-group-container';

import battery from '../icons/battery.png';

import cloud from '../icons/cloud.png';

import koala from '../icons/koala.png';

import ui from '../icons/ui.png';

import wallet from '../icons/wallet.png';



export default () => {

	return (

		<MenuGroupContainer>

			<MenuGroup maxHeight={300}>

				<Section title="Recent" isScrollable>

					<ButtonItem

						iconBefore={<ImgIcon src={battery} alt="Battery" />}

						description="Next-gen software project"

					>

						Fabric Editor

					</ButtonItem>

					<ButtonItem

						iconBefore={<ImgIcon src={cloud} alt="Cloud" />}

						description="Classic business project"

					>

						Content Services

					</ButtonItem>

					<ButtonItem

						iconBefore={<ImgIcon src={wallet} alt="Wallet" />}

						description="Next-gen software project"

					>

						Trinity Mobile

					</ButtonItem>

					<ButtonItem

						iconBefore={<ImgIcon src={koala} alt="Koala" />}

						description="Classic service desk"

					>

						Customer Feedback

					</ButtonItem>

					<ButtonItem

						iconBefore={<ImgIcon src={ui} alt="UI logo" />}

						description="Classic software project"

					>

						Design System

					</ButtonItem>

				</Section>

				<Section hasSeparator>

					<ButtonItem>View all projects</ButtonItem>

					<ButtonItem>Create project</ButtonItem>

				</Section>

			</MenuGroup>

		</MenuGroupContainer>

	);

};
```

```jsx
import React, { useEffect, useState } from 'react';



import Button from '@atlaskit/button/new';

import Icon from '@atlaskit/icon';

import StarStarredIcon from '@atlaskit/icon/glyph/star-filled';

import StarUnstarredIcon from '@atlaskit/icon/glyph/star';

import { Box, Stack, xcss } from '@atlaskit/primitives';

import { token } from '@atlaskit/tokens';



import {

	ButtonItem,

	type ButtonItemProps,

	HeadingItem,

	MenuGroup,

	Section,

	SkeletonHeadingItem,

	SkeletonItem,

} from '@atlaskit/menu';

import MenuGroupContainer from '../common/menu-group-container';

import Invision from '../icons/invision';

import Portfolio from '../icons/portfolio';

import Slack from '../icons/slack';

import Tempo from '../icons/tempo';



const iconContainerStyles = xcss({

	height: 'size.200',

	width: 'size.200',

	background: 'linear-gradient(180deg, #4E86EE 0%, #3562C1 100%), #4E86EE',

	borderRadius: '3px',

});



const buttonContainerStyles = xcss({

	display: 'flex',

	justifyContent: 'center',

});



const Item = ({ isLoading, ...props }: ButtonItemProps & { isLoading?: boolean }) => {

	if (isLoading) {

		return <SkeletonItem hasIcon isShimmering />;

	}



	// eslint-disable-next-line @repo/internal/react/no-unsafe-spread-props

	return <ButtonItem {...props} />;

};



const Heading = ({ isLoading, ...props }: any) => {

	if (isLoading) {

		return <SkeletonHeadingItem isShimmering />;

	}



	// eslint-disable-next-line @repo/internal/react/no-unsafe-spread-props

	return <HeadingItem {...props} />;

};



export default () => {

	const [isLoading, setIsLoading] = useState(true);

	const [retryLoading, setRetryLoading] = useState(true);



	useEffect(() => {

		if (!retryLoading) {

			return;

		}



		setIsLoading(true);



		setTimeout(() => {

			setRetryLoading(false);

			setIsLoading(false);

		}, 1500);

	}, [retryLoading]);



	return (

		<Stack space="space.200">

			<MenuGroupContainer>

				<MenuGroup>

					<Section aria-labelledby={isLoading ? '' : 'apps'}>

						<Heading aria-hidden id="apps" isLoading={isLoading}>

							Apps

						</Heading>

						<Item

							isLoading={isLoading}

							iconBefore={

								<Box xcss={iconContainerStyles}>

									<Icon glyph={Portfolio} primaryColor={token('color.icon.brand')} label="" />

								</Box>

							}

							iconAfter={

								<StarStarredIcon

									primaryColor={token('color.icon.warning')}

									label=""

								/>

							}

						>

							Portfolio

						</Item>

						<Item

							isLoading={isLoading}

							iconBefore={<Icon glyph={Tempo} label="" />}

							iconAfter={

								<StarStarredIcon

									primaryColor={token('color.icon.warning')}

									label=""

								/>

							}

						>

							Tempo timesheets

						</Item>

						<Item

							isLoading={isLoading}

							iconBefore={<Icon glyph={Invision} label="" />}

							iconAfter={<StarUnstarredIcon label="" />}

						>

							Invision

						</Item>

						<Item isLoading={isLoading} iconBefore={<Icon glyph={Slack} label="" />}>

							Slack

						</Item>

					</Section>

					<Section hasSeparator>

						<Item>Find new apps</Item>

						<Item>Manage your apps</Item>

					</Section>

				</MenuGroup>

			</MenuGroupContainer>

			<Box xcss={buttonContainerStyles}>

				<Button testId="toggle-loading" onClick={() => setRetryLoading(true)}>

					Reload

				</Button>

			</Box>

		</Stack>

	);

};
```

---

[View Original Documentation](https://atlassian.design/components/menu/examples)
