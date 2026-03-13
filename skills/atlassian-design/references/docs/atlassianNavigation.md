# Atlassian navigation

A horizontal navigation component for Atlassian products.

---

## Default

A basic Atlassian navigation. 

```jsx
import React from 'react';



import { AtlassianIcon, AtlassianLogo } from '@atlaskit/logo';



import { AtlassianNavigation, PrimaryButton, PrimaryDropdownButton, ProductHome } from '@atlaskit/atlassian-navigation';



const AtlassianProductHome = () => <ProductHome icon={AtlassianIcon} logo={AtlassianLogo} />;



const DefaultExample = () => (

	<AtlassianNavigation

		label="site"

		primaryItems={[

			<PrimaryButton>Your work</PrimaryButton>,

			<PrimaryDropdownButton>Work items</PrimaryDropdownButton>,

			<PrimaryDropdownButton>Projects</PrimaryDropdownButton>,

			<PrimaryButton>Repositories</PrimaryButton>,

		]}

		renderProductHome={AtlassianProductHome}

	/>

);



export default DefaultExample;
```

## Primary items

### Button

Add top-level navigation items using PrimaryButton. 

```jsx
import React from 'react';



import { AtlassianNavigation, PrimaryButton } from '@atlaskit/atlassian-navigation';



const PrimaryButtonExample = () => (

	<AtlassianNavigation

		label="site"

		renderProductHome={() => null}

		primaryItems={[

			<PrimaryButton>Explore</PrimaryButton>,

			<PrimaryButton>Work items</PrimaryButton>,

			<PrimaryButton>Services</PrimaryButton>,

		]}

	/>

);



export default PrimaryButtonExample;
```

### Dropdown menu

Add menu items to a primary button using the PrimaryDropdownButton component. 

```jsx
import React from 'react';



import { AtlassianNavigation, PrimaryDropdownButton } from '@atlaskit/atlassian-navigation';



const PrimaryDropdownExample = () => (

	<AtlassianNavigation

		label="site"

		renderProductHome={() => null}

		primaryItems={[

			<PrimaryDropdownButton>Explore</PrimaryDropdownButton>,

			<PrimaryDropdownButton>Work items</PrimaryDropdownButton>,

			<PrimaryDropdownButton>Services</PrimaryDropdownButton>,

		]}

	/>

);



export default PrimaryDropdownExample;
```

## Sections

The navigation bar is divided into two areas (primary and secondary) and several sections. 

### Product home

The ProductHome component displays the product visual identity composed of: a logo, an icon, and optional text.
The logo and icon visuals are never displayed at the same time. The icon is used only when space is restricted. 

```jsx
import React from 'react';



import { JiraIcon, JiraLogo } from '@atlaskit/logo';



import { AtlassianNavigation, ProductHome } from '@atlaskit/atlassian-navigation';



const ExampleHome = () => (

	<ProductHome href="#" siteTitle="Hello" icon={JiraIcon} logo={JiraLogo} />

);



const ProductHomeExample = () => (

	<AtlassianNavigation label="site" renderProductHome={ExampleHome} primaryItems={[]} />

);



export default ProductHomeExample;
```

### Custom product home

Use CustomProductHome to provide a custom logo and icon with URLs. Custom logos have a default max width of 260px, but this can be overridden with the logoMaxWidth prop. 

```jsx
import React from 'react';



import { AtlassianNavigation, CustomProductHome } from '@atlaskit/atlassian-navigation';

import customIcon from '../shared/assets/atlassian-icon.png';

import customLogo from '../shared/assets/custom-logo-wide.png';



const CustomHome = () => (

	<CustomProductHome

		href="#"

		iconAlt="Atlassian documentation home"

		iconUrl={customIcon}

		logoAlt="Atlassian documentation home"

		logoUrl={customLogo}

		logoMaxWidth={300}

	/>

);



const CustomHomeExample = () => (

	<AtlassianNavigation label="site" renderProductHome={CustomHome} primaryItems={[]} />

);



export default CustomHomeExample;
```

### App switcher

To show the app switcher in the Atlassian navigation, use the renderAppSwitcher prop with the AppSwitcher component. 

```jsx
import React from 'react';



import { AppSwitcher, AtlassianNavigation } from '@atlaskit/atlassian-navigation';



const DefaultAppSwitcher = () => <AppSwitcher tooltip="Switch to..." />;



const AppSwitcherExample = () => (

	<AtlassianNavigation

		label="site"

		renderProductHome={() => null}

		renderAppSwitcher={DefaultAppSwitcher}

		primaryItems={[]}

	/>

);



export default AppSwitcherExample;
```

### Create

Use the Create component to add a call to action button which is shown after all primary buttons. 

```jsx
import React from 'react';



import { JiraIcon, JiraLogo } from '@atlaskit/logo';



import { AtlassianNavigation, Create, ProductHome } from '@atlaskit/atlassian-navigation';



const CreateButton = () => (

	<Create

		buttonTooltip="Create a new page"

		iconButtonTooltip="Create a new page"

		text="Create"

		href="#"

	/>

);



const Home = () => <ProductHome icon={JiraIcon} logo={JiraLogo} />;



const CreateButtonExample = () => (

	<AtlassianNavigation

		label="site"

		renderProductHome={Home}

		renderCreate={CreateButton}

		primaryItems={[]}

	/>

);



export default CreateButtonExample;
```

### Profile

Use the Profile component to add a profile button which takes an icon/avatar component. 

```jsx
import React from 'react';



import Avatar from '@atlaskit/avatar';



import { AtlassianNavigation, Profile } from '@atlaskit/atlassian-navigation';



const avatarUrl =

	'data:image/png;base64,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';



const onClick = (...args: any[]) => {

	console.log('profile click', ...args);

};



const DefaultProfile = () => (

	<Profile

		icon={<Avatar size="small" src={avatarUrl} name="Atlassian account: Emil Rottmayer" />}

		onClick={onClick}

		tooltip="Your profile and settings"

	/>

);



const ProfileExample = () => (

	<AtlassianNavigation

		label="site"

		renderProductHome={() => null}

		renderProfile={DefaultProfile}

		primaryItems={[]}

	/>

);



export default ProfileExample;
```

### Search

Use the Search component to add a search input field to the navigation. 

```jsx
import React, { useState } from 'react';



import { AtlassianNavigation, Search } from '@atlaskit/atlassian-navigation';



const SearchExample = () => {

	const DefaultSearch = () => {

		const [value, setValue] = useState('');

		const onChange = (event: any) => {

			console.log('search clicked with value: ', event.target.value);

			setValue(event.target.value);

		};



		return (

			<Search

				onClick={onChange}

				placeholder="Search..."

				tooltip="Search"

				label="Search"

				value={value}

			/>

		);

	};



	return (

		<AtlassianNavigation

			label="site"

			renderProductHome={() => null}

			renderSearch={DefaultSearch}

			primaryItems={[]}

		/>

	);

};



export default SearchExample;
```

### Settings

Use the Settings component to add a settings button. 

```jsx
import React from 'react';



import { AtlassianNavigation, Settings } from '@atlaskit/atlassian-navigation';



const DefaultSettings = () => <Settings tooltip="Product settings" />;



const SettingsExample = () => (

	<AtlassianNavigation

		label="site"

		renderProductHome={() => null}

		renderSettings={DefaultSettings}

		primaryItems={[]}

	/>

);



export default SettingsExample;
```

### Sign in

Use the SignIn component to add a sign in button. 

```jsx
import React from 'react';



import { AtlassianNavigation, SignIn } from '@atlaskit/atlassian-navigation';



const DefaultSignIn = () => <SignIn href="#" tooltip="Sign in" />;



const SignInExample = () => (

	<AtlassianNavigation

		label="site"

		renderProductHome={() => null}

		renderSignIn={DefaultSignIn}

		primaryItems={[]}

	/>

);



export default SignInExample;
```

### Help

Use the Help component to add a help button. 

```jsx
import React from 'react';



import { AtlassianNavigation, Help } from '@atlaskit/atlassian-navigation';



const HelpButtonExample = () => (

	<AtlassianNavigation

		label="site"

		renderProductHome={() => null}

		renderHelp={() => <Help tooltip="Get help" />}

		primaryItems={[]}

	/>

);



export default HelpButtonExample;
```

### Notifications

Use the Notifications component to add a notifications button with an indicator. 

```jsx
import React from 'react';



import { NotificationIndicator } from '@atlaskit/notification-indicator';



import { AtlassianNavigation, Notifications } from '@atlaskit/atlassian-navigation';



const NotificationsBadge = () => (

	<NotificationIndicator

		onCountUpdated={console.log}

		notificationLogProvider={Promise.resolve({}) as any}

	/>

);



const NotificationsExample = () => (

	<AtlassianNavigation

		label="site"

		renderProductHome={() => null}

		renderNotifications={() => <Notifications badge={NotificationsBadge} tooltip="Notifications" />}

		primaryItems={[]}

	/>

);



export default NotificationsExample;
```

## Routing

Atlassian navigation buttons extend all props from @atlaskit/button/custom-theme-button. This includes the component prop, which allows you to pass in a custom element to render, such as the <Link> component from popular routing libraries. 

```jsx
import Link from '@popular/routing-library';
import { PrimaryButton } from '@atlaskit/atlassian-navigation';

// Set a custom component
<PrimaryButton component={Link}>Your Work</PrimaryButton>;
```

```jsx
import Link from '@popular/routing-library';
import { PrimaryButton } from '@atlaskit/atlassian-navigation';

// Set a custom component
<PrimaryButton component={Link}>Your Work</PrimaryButton>;
```

## Responsive

If there are too many menu items to display on small viewports the overflowing items should collapse into a dropdown menu. 

```jsx
import React from 'react';



import ChevronDownIcon from '@atlaskit/icon/glyph/chevron-down';

import { ButtonItem } from '@atlaskit/menu';



import {

	AtlassianNavigation,

	Create,

	PrimaryButton,

	type PrimaryButtonProps,

	PrimaryDropdownButton,

	type PrimaryDropdownButtonProps,

	useOverflowStatus,

} from '@atlaskit/atlassian-navigation';



const ResponsivePrimaryButton = (props: PrimaryButtonProps) => {

	const overflowStatus = useOverflowStatus();



	return overflowStatus.isVisible ? (

		<PrimaryButton>{props.children}</PrimaryButton>

	) : (

		<ButtonItem>{props.children}</ButtonItem>

	);

};



const ResponsivePrimaryDropdownButton = (props: PrimaryDropdownButtonProps) => {

	const overflowStatus = useOverflowStatus();



	return overflowStatus.isVisible ? (

		<PrimaryDropdownButton>{props.children}</PrimaryDropdownButton>

	) : (

		<ButtonItem iconAfter={<ChevronDownIcon label="" />}>

			{props.children}

		</ButtonItem>

	);

};



const OverflowMenuExample = () => {

	return (

		// eslint-disable-next-line @atlaskit/ui-styling-standard/enforce-style-prop -- Ignored via go/DSP-18766

		<div style={{ width: '50%', minWidth: 180 }}>

			<AtlassianNavigation

				label="site"

				renderProductHome={() => null}

				renderCreate={() => <Create onClick={console.log} text="Create" />}

				primaryItems={[

					<ResponsivePrimaryButton>Explore</ResponsivePrimaryButton>,

					<ResponsivePrimaryButton>Projects</ResponsivePrimaryButton>,

					<ResponsivePrimaryButton>Dashboards</ResponsivePrimaryButton>,

					<ResponsivePrimaryDropdownButton>Favorites</ResponsivePrimaryDropdownButton>,

				]}

			/>

		</div>

	);

};



export default OverflowMenuExample;
```

### Skeleton button

Skeleton buttons are lightweight HTML button elements with CSS used as a representation of their heavier interactive counterparts. These can be used when parts of the navigation are loaded dynamically. If the full navigation is delayed, use the skeleton loader pattern below instead. 

```jsx
/**

 * @jsxRuntime classic

 * @jsx jsx

 */

import { Fragment } from 'react';



// eslint-disable-next-line @atlaskit/ui-styling-standard/use-compiled -- Ignored via go/DSP-18766

import { jsx } from '@emotion/react';



import { JiraIcon, JiraLogo } from '@atlaskit/logo';



import { AtlassianNavigation, ProductHome } from '@atlaskit/atlassian-navigation';

import {

	SkeletonCreateButton,

	SkeletonIconButton,

	SkeletonPrimaryButton,

} from '@atlaskit/atlassian-navigation/skeleton';

import { SkeletonHelpButton } from '../../src/skeleton-help-button';

import { SkeletonNotificationButton } from '@atlaskit/atlassian-navigation/skeleton-notification-button';

import { SkeletonSettingsButton } from '../../src/skeleton-settings-button';

import { SkeletonSwitcherButton } from '@atlaskit/atlassian-navigation/skeleton-switcher-button';

import { avatarUrl } from '../shared/profile-popup';



const SkeletonCreate = () => <SkeletonCreateButton text="Create"></SkeletonCreateButton>;

const SkeletonProfileButton = () => (

	<SkeletonIconButton>

		<img src={avatarUrl} alt="Your profile and settings" />

	</SkeletonIconButton>

);

const skeletonPrimaryItems = [

	<SkeletonPrimaryButton>Home</SkeletonPrimaryButton>,

	<SkeletonPrimaryButton isDropdownButton text="Projects" />,

	<SkeletonPrimaryButton isDropdownButton isHighlighted text="Filters &amp; work items" />,

	<SkeletonPrimaryButton isDropdownButton text="Dashboards" />,

	<SkeletonPrimaryButton isDropdownButton text="Apps" testId="apps-skeleton" />,

];



const AtlassianNavigationSkeletonButtons = () => {

	return (

		<Fragment>

			<AtlassianNavigation

				label="site"

				moreLabel="More"

				primaryItems={skeletonPrimaryItems}

				renderAppSwitcher={() => <SkeletonSwitcherButton label="switcher button" />}

				renderCreate={SkeletonCreate}

				renderProductHome={() => <ProductHome icon={JiraIcon} logo={JiraLogo} siteTitle="Hello" />}

				renderProfile={SkeletonProfileButton}

				renderSettings={() => <SkeletonSettingsButton label="settings button" />}

				renderHelp={() => <SkeletonHelpButton label="help button" />}

				renderNotifications={() => <SkeletonNotificationButton label="notifications button" />}

				testId="atlassian-navigation"

			/>

		</Fragment>

	);

};



export default AtlassianNavigationSkeletonButtons;
```

### Skeleton loader

Use loading skeletons to reduce the perceived loading time of heavier full-page experiences. 

```jsx
/**

 * @jsxRuntime classic

 * @jsx jsx

 */

// eslint-disable-next-line @atlaskit/ui-styling-standard/use-compiled -- Ignored via go/DSP-18766

import { jsx } from '@emotion/react';



import { NavigationSkeleton } from '@atlaskit/atlassian-navigation/skeleton';



const InteractiveSkeletonExample = () => {

	return (

		<NavigationSkeleton primaryItemsCount={2} secondaryItemsCount={1} shouldShowSearch={true} />

	);

};



export default InteractiveSkeletonExample;
```

---

[View Original Documentation](https://atlassian.design/components/atlassian-navigation/examples)
