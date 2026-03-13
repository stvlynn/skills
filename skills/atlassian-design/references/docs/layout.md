# Layout

Layout components define consistent areas for navigation menus and other elements in the page structure.

---

## Layout

The full page layout with all areas rendered has the structure depicted below. When composing your page layout ensure that: 

## Layout areas

These are the distinct areas in the navigation layout. These components are designed to contain other components and content. 

### Root

The root component of the navigation system, wrapping the entire view. It provides the React contexts that power the layout. 

### Banner

Use the Banner area to render a banner component. It will always be displayed at the top of the screen. 

```jsx
import React from 'react';



import Banner from '@atlaskit/banner';

import WarningIcon from '@atlaskit/icon/glyph/warning';

import { Banner as PageLayoutBanner } from '@atlassian/navigation-system/layout/banner';

import { Root as PageLayoutRoot } from '@atlassian/navigation-system/layout/root';



export const BannerLayoutExample = () => (

	<PageLayoutRoot>

		<PageLayoutBanner>

			<Banner icon={<WarningIcon label="Warning" />}>

				Payment details needed. To stay on your current plan, add payment details by June 30, 2020.

			</Banner>

		</PageLayoutBanner>

	</PageLayoutRoot>

);
```

### Top bar

Use the TopBar to render top navigation items. It will display at the top of the screen, below the banner if one is present. 

```jsx
import React from 'react';



import { Root } from '@atlassian/navigation-system/layout/root';

import { TopBar } from '@atlassian/navigation-system/layout/top-bar';

import { CommonActions, HomeActions, UserActions } from '@atlassian/navigation-system/top-nav';



export const TopBarLayoutExample = () => (

	<Root>

		<TopBar>

			<HomeActions>123</HomeActions>

			<CommonActions>456</CommonActions>

			<UserActions>789</UserActions>

		</TopBar>

	</Root>

);
```

### Side nav

Use the SideNav area to render side navigation items. It will show on the left of the screen. Use the side nav area components to position content within areas of the side nav. You can optionally render a panel splitter as a child to make the side navigation slot resizable. There are two hooks available for toggling the side nav. 

```jsx
import React from 'react';



import { Root } from '@atlassian/navigation-system/layout/root';

import { SideNav, SideNavContent } from '@atlassian/navigation-system/layout/side-nav';

import { MenuLinkItem } from '@atlassian/navigation-system/side-nav/menu-link-item';

import { MenuList } from '@atlassian/navigation-system/side-nav/menu-list';

import {

	MenuSection,

	MenuSectionHeading,

} from '@atlassian/navigation-system/side-nav/menu-section';



export const SideNavLayoutExample = () => (

	<Root>

		<SideNav>

			<SideNavContent>

				<MenuList>

					<MenuSection>

						<MenuSectionHeading>Section</MenuSectionHeading>

						<MenuList>

							<MenuLinkItem href="/">Item</MenuLinkItem>

						</MenuList>

					</MenuSection>

				</MenuList>

			</SideNavContent>

		</SideNav>

	</Root>

);
```

## Usage

Returns a function that will expand the side nav. This can be useful for ensuring the side nav is expanded before displaying an onboarding spotlight, for example. If the side nav is already expanded, it will simply no-op. Returns a function that will toggle the side nav. This is useful for toggling the side nav based on a keyboard shortcut. 

```jsx
import React, { useCallback } from 'react';



import Button from '@atlaskit/button/new';

import { useExpandSideNav } from '@atlassian/navigation-system/layout/side-nav';



export function ExpandSideNavButtonExample({ onClick }: { onClick: () => void }) {

	const expandSideNav = useExpandSideNav();



	const handleLaunchSpotlight = useCallback(() => {

		expandSideNav();

		onClick();

	}, [onClick, expandSideNav]);



	return <Button onClick={handleLaunchSpotlight}>Launch spotlight</Button>;

}
```

```jsx
import { useEffect } from 'react';



import { bind } from 'bind-event-listener';



import { useToggleSideNav } from '@atlassian/navigation-system/layout/side-nav';



// This could be a hook too

export function ToggleSideNavKeyboardShortcutExample(): void {

	const toggleSideNav = useToggleSideNav();



	useEffect(() => {

		const toggle = (event: KeyboardEvent) => {

			if (event.key === '[') {

				toggleSideNav();

			}

		};



		return bind(document, {

			type: 'keydown',

			listener: toggle,

		});

	}, [toggleSideNav]);

}
```

### Side nav areas

The side nav has three layout components that you can use to position components within the side nav flexbox. The top part of the side nav. The middle part of the side nav. It acts as a scroll container. It will grow to take up the available space in the side nav — this is used to push the footer to the bottom of the side nav. The bottom part of the side nav. Note: make sure to render SideNavContent as well to ensure that the footer is positioned at the bottom of the side nav, simulating a sticky footer. 

```jsx
import React from 'react';



import { Root } from '@atlassian/navigation-system/layout/root';

import {

	SideNav,

	SideNavContent,

	SideNavFooter,

	SideNavHeader,

} from '@atlassian/navigation-system/layout/side-nav';



export const SideNavSlotsExample = () => (

	<Root>

		<SideNav>

			<SideNavHeader>Header</SideNavHeader>

			<SideNavContent>Content</SideNavContent>

			<SideNavFooter>Footer</SideNavFooter>

		</SideNav>

	</Root>

);
```

### Side nav flyout

The SideNav has a flyout feature - where it will overlay on top of the main content when the user hovers over the SideNavToggleButton in the top bar, if the side nav was collapsed. The expansion and collapse of the side nav flyout is animated on supported browsers. Currently, Firefox does not support the animation. Instead, it will instantly expand and collapse. 

### Main

Use the Main area for the main page content. It has a fluid width and will expand to fill available space. 

```jsx
import React from 'react';



import { Main } from '@atlassian/navigation-system/layout/main';

import { Root } from '@atlassian/navigation-system/layout/root';



export const MainLayoutExample = () => (

	<Root>

		<Main>Main content</Main>

	</Root>

);
```

### Aside

The Aside is rendered to the right of the Main area. You can optionally render a panel splitter as a child to make the aside area resizable. 

```jsx
import React from 'react';



import { Aside } from '@atlassian/navigation-system/layout/aside';

import { Root } from '@atlassian/navigation-system/layout/root';



export const AsideLayoutExample = () => (

	<Root>

		<Aside>Aside content</Aside>

	</Root>

);
```

### Panel

The Panel is rendered to the right of the Main and Aside areas. You can optionally render a panel splitter as a child to make the panel area resizable. 

```jsx
import React from 'react';



import { Panel } from '@atlassian/navigation-system/layout/panel';

import { Root } from '@atlassian/navigation-system/layout/root';



export const PanelLayoutExample = () => (

	<Root>

		<Panel>Panel content</Panel>

	</Root>

);
```

## Resizable areas

Render PanelSplitter in a layout area to make it resizable. Resizing is supported for the following areas: 

```jsx
import React from 'react';



import { PanelSplitter } from '@atlassian/navigation-system/layout/panel-splitter';

import { Root } from '@atlassian/navigation-system/layout/root';

import { SideNav } from '@atlassian/navigation-system/layout/side-nav';



export const PanelSplitterLayoutExample = () => (

	<Root>

		<SideNav>

			<PanelSplitter label="Resize side nav" />

		</SideNav>

	</Root>

);
```

## Advanced layouts

## Use with caution

Advanced layouts can be created inside of the main area. 

## Main content

### Section

Lorem ipsum dolor sit amet consectetur adipisicing elit. Eligendi nemo quo soluta sapiente delectus beatae tenetur, voluptatibus sit temporibus ullam illum aut voluptas dolorum inventore ex, dolorem natus impedit? Sequi. Lorem ipsum dolor, sit amet consectetur adipisicing elit. Minus quae laboriosam tempore sit inventore, temporibus atque praesentium sed molestiae adipisci architecto ipsam reiciendis unde dicta! Corporis nam repellat nostrum harum? Lorem ipsum dolor sit amet consectetur adipisicing elit. A vero maiores aperiam harum vel pariatur nesciunt eius fugit aliquid molestias dolorem voluptates et, exercitationem maxime esse molestiae ipsum quibusdam sint. 

### Section

Lorem ipsum dolor sit amet consectetur adipisicing elit. Eligendi nemo quo soluta sapiente delectus beatae tenetur, voluptatibus sit temporibus ullam illum aut voluptas dolorum inventore ex, dolorem natus impedit? Sequi. Lorem ipsum dolor, sit amet consectetur adipisicing elit. Minus quae laboriosam tempore sit inventore, temporibus atque praesentium sed molestiae adipisci architecto ipsam reiciendis unde dicta! Corporis nam repellat nostrum harum? Lorem ipsum dolor sit amet consectetur adipisicing elit. A vero maiores aperiam harum vel pariatur nesciunt eius fugit aliquid molestias dolorem voluptates et, exercitationem maxime esse molestiae ipsum quibusdam sint. 

### Section

Lorem ipsum dolor sit amet consectetur adipisicing elit. Eligendi nemo quo soluta sapiente delectus beatae tenetur, voluptatibus sit temporibus ullam illum aut voluptas dolorum inventore ex, dolorem natus impedit? Sequi. Lorem ipsum dolor, sit amet consectetur adipisicing elit. Minus quae laboriosam tempore sit inventore, temporibus atque praesentium sed molestiae adipisci architecto ipsam reiciendis unde dicta! Corporis nam repellat nostrum harum? Lorem ipsum dolor sit amet consectetur adipisicing elit. A vero maiores aperiam harum vel pariatur nesciunt eius fugit aliquid molestias dolorem voluptates et, exercitationem maxime esse molestiae ipsum quibusdam sint. 

### Section

Lorem ipsum dolor sit amet consectetur adipisicing elit. Eligendi nemo quo soluta sapiente delectus beatae tenetur, voluptatibus sit temporibus ullam illum aut voluptas dolorum inventore ex, dolorem natus impedit? Sequi. Lorem ipsum dolor, sit amet consectetur adipisicing elit. Minus quae laboriosam tempore sit inventore, temporibus atque praesentium sed molestiae adipisci architecto ipsam reiciendis unde dicta! Corporis nam repellat nostrum harum? Lorem ipsum dolor sit amet consectetur adipisicing elit. A vero maiores aperiam harum vel pariatur nesciunt eius fugit aliquid molestias dolorem voluptates et, exercitationem maxime esse molestiae ipsum quibusdam sint. 

## Aside

### Section

Lorem ipsum dolor sit amet consectetur adipisicing elit. Eligendi nemo quo soluta sapiente delectus beatae tenetur, voluptatibus sit temporibus ullam illum aut voluptas dolorum inventore ex, dolorem natus impedit? Sequi. Lorem ipsum dolor, sit amet consectetur adipisicing elit. Minus quae laboriosam tempore sit inventore, temporibus atque praesentium sed molestiae adipisci architecto ipsam reiciendis unde dicta! Corporis nam repellat nostrum harum? Lorem ipsum dolor sit amet consectetur adipisicing elit. A vero maiores aperiam harum vel pariatur nesciunt eius fugit aliquid molestias dolorem voluptates et, exercitationem maxime esse molestiae ipsum quibusdam sint. 

### Section

Lorem ipsum dolor sit amet consectetur adipisicing elit. Eligendi nemo quo soluta sapiente delectus beatae tenetur, voluptatibus sit temporibus ullam illum aut voluptas dolorum inventore ex, dolorem natus impedit? Sequi. Lorem ipsum dolor, sit amet consectetur adipisicing elit. Minus quae laboriosam tempore sit inventore, temporibus atque praesentium sed molestiae adipisci architecto ipsam reiciendis unde dicta! Corporis nam repellat nostrum harum? Lorem ipsum dolor sit amet consectetur adipisicing elit. A vero maiores aperiam harum vel pariatur nesciunt eius fugit aliquid molestias dolorem voluptates et, exercitationem maxime esse molestiae ipsum quibusdam sint. 

### Section

Lorem ipsum dolor sit amet consectetur adipisicing elit. Eligendi nemo quo soluta sapiente delectus beatae tenetur, voluptatibus sit temporibus ullam illum aut voluptas dolorum inventore ex, dolorem natus impedit? Sequi. Lorem ipsum dolor, sit amet consectetur adipisicing elit. Minus quae laboriosam tempore sit inventore, temporibus atque praesentium sed molestiae adipisci architecto ipsam reiciendis unde dicta! Corporis nam repellat nostrum harum? Lorem ipsum dolor sit amet consectetur adipisicing elit. A vero maiores aperiam harum vel pariatur nesciunt eius fugit aliquid molestias dolorem voluptates et, exercitationem maxime esse molestiae ipsum quibusdam sint. 

### Section

Lorem ipsum dolor sit amet consectetur adipisicing elit. Eligendi nemo quo soluta sapiente delectus beatae tenetur, voluptatibus sit temporibus ullam illum aut voluptas dolorum inventore ex, dolorem natus impedit? Sequi. Lorem ipsum dolor, sit amet consectetur adipisicing elit. Minus quae laboriosam tempore sit inventore, temporibus atque praesentium sed molestiae adipisci architecto ipsam reiciendis unde dicta! Corporis nam repellat nostrum harum? Lorem ipsum dolor sit amet consectetur adipisicing elit. A vero maiores aperiam harum vel pariatur nesciunt eius fugit aliquid molestias dolorem voluptates et, exercitationem maxime esse molestiae ipsum quibusdam sint. 

```jsx
/**

 * @jsxRuntime classic

 * @jsx jsx

 */



import Breadcrumbs, { BreadcrumbsItem } from '@atlaskit/breadcrumbs';

import { cssMap, jsx } from '@atlaskit/css';

import Heading from '@atlaskit/heading';

import { AtlassianIcon, AtlassianLogo } from '@atlaskit/logo';

import PageHeader from '@atlaskit/page-header';

import { Stack } from '@atlaskit/primitives/compiled';

import { token } from '@atlaskit/tokens';

import { Main } from '@atlassian/navigation-system/layout/main';

import { Root } from '@atlassian/navigation-system/layout/root';

import { TopBar } from '@atlassian/navigation-system/layout/top-bar';

import { HomeActions, NavLogo } from '@atlassian/navigation-system/top-nav';



const advancedLayoutStyles = cssMap({

	root: {

		display: 'grid',

		height: '100%',

		width: '100%',

		gridTemplateAreas: `

				"header"

				"main"

				"aside"

			`,

		gridTemplateRows: 'auto auto auto',

		gridTemplateColumns: '1fr',

		'@media (min-width: 90rem)': {

			gridTemplateAreas: `

				"header header"

				"main aside"

			`,

			gridTemplateRows: 'auto 1fr',

			gridTemplateColumns: '1fr 400px',

		},

	},

	header: {

		gridArea: 'header',

		borderBlockEndColor: token('color.border'),

		borderBlockEndStyle: 'solid',

		borderBlockEndWidth: token('border.width'),

		paddingInline: token('space.400'),

	},

	main: {

		gridArea: 'main',

		paddingInline: token('space.400'),

		paddingBlock: token('space.400'),

		'@media (min-width: 90rem)': {

			overflow: 'auto',

		},

	},

	aside: {

		gridArea: 'aside',

		paddingInline: token('space.400'),

		paddingBlock: token('space.400'),



		borderColor: token('color.border'),

		borderWidth: token('border.width'),

		borderBlockStartStyle: 'solid',

		'@media (min-width: 90rem)': {

			borderBlockStartStyle: 'none',

			borderInlineStartStyle: 'solid',

			overflow: 'auto',

		},

	},

});



function LoremSection() {

	return (

		<div>

			<Heading as="h3" size="small">

				Section

			</Heading>

			<p>

				Lorem ipsum dolor sit amet consectetur adipisicing elit. Eligendi nemo quo soluta sapiente

				delectus beatae tenetur, voluptatibus sit temporibus ullam illum aut voluptas dolorum

				inventore ex, dolorem natus impedit? Sequi.

			</p>

			<p>

				Lorem ipsum dolor, sit amet consectetur adipisicing elit. Minus quae laboriosam tempore sit

				inventore, temporibus atque praesentium sed molestiae adipisci architecto ipsam reiciendis

				unde dicta! Corporis nam repellat nostrum harum?

			</p>

			<p>

				Lorem ipsum dolor sit amet consectetur adipisicing elit. A vero maiores aperiam harum vel

				pariatur nesciunt eius fugit aliquid molestias dolorem voluptates et, exercitationem maxime

				esse molestiae ipsum quibusdam sint.

			</p>

		</div>

	);

}



export const AdvancedLayoutExample = () => (

	<Root>

		<TopBar>

			<HomeActions>

				<NavLogo href="" logo={AtlassianLogo} icon={AtlassianIcon} label="Home page" />

			</HomeActions>

		</TopBar>

		<Main isFixed>

			<div css={advancedLayoutStyles.root}>

				<div css={advancedLayoutStyles.header}>

					<PageHeader

						breadcrumbs={

							<Breadcrumbs>

								<BreadcrumbsItem text="Projects" />

								<BreadcrumbsItem text="ABC-123" />

							</Breadcrumbs>

						}

					>

						My project

					</PageHeader>

				</div>

				<div css={advancedLayoutStyles.main}>

					<Stack space="space.400">

						<Heading as="h2" size="medium">

							Main content

						</Heading>

						<LoremSection />

						<LoremSection />

						<LoremSection />

						<LoremSection />

					</Stack>

				</div>

				<aside css={advancedLayoutStyles.aside}>

					<Stack space="space.400">

						<Heading as="h2" size="medium">

							Aside

						</Heading>

						<LoremSection />

						<LoremSection />

						<LoremSection />

						<LoremSection />

					</Stack>

				</aside>

			</div>

		</Main>

	</Root>

);
```

### Custom skip links

Use useSkipLink to register custom skip links where appropriate. The useSkipLink hook accepts an optional third argument to manually specify the index of the skip link in the list. You can also optionally use the useSkipLinkId hook to retrieve a unique ID for use for your skip link. 

```jsx
import React from 'react';



import { useSkipLink, useSkipLinkId } from '@atlassian/navigation-system/layout/skip-links';



export function CustomSkipLinkExample() {

	const id = useSkipLinkId();

	useSkipLink(id, 'Landmark name');



	return <div id={id} />;

}
```

---

[View Original Documentation](https://atlassian.design/components/navigation-system/layout/examples)
