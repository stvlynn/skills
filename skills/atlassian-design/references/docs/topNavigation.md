# Top navigation

Actions and items for the top bar of the navigation.

---

## Home actions

Home actions are displayed in the left of the top bar. 

```jsx
import React from 'react';



import { JiraIcon, JiraLogo } from '@atlaskit/logo';

import { SideNavToggleButton } from '@atlassian/navigation-system/layout/side-nav';

import { AppSwitcher, HomeActions, NavLogo } from '@atlassian/navigation-system/top-nav';



import { MockTopBar } from './common/mock-top-bar';



export const HomeActionsLayoutExample = () => {

	return (

		<MockTopBar>

			<HomeActions>

				<SideNavToggleButton

					defaultCollapsed

					collapseLabel="Collapse sidebar"

					expandLabel="Expand sidebar"

				/>

				<AppSwitcher label="App switcher" />

				<NavLogo

					href="https://jira.atlassian.com"

					logo={JiraLogo}

					icon={JiraIcon}

					label="Home page"

				/>

			</HomeActions>

		</MockTopBar>

	);

};
```

## Common actions

Use CommonActions for actions which are common between products. These are displayed in the center of the top bar. This area will grow and shrink with the available space. The search bar must be the first child in CommonActions, in line with our design specifications. If this is not the case, you may see unexpected layout behavior. 

```jsx
import React from 'react';



import { CreateButton } from '@atlassian/navigation-system';

import { CommonActions, Search } from '@atlassian/navigation-system/top-nav';



import { MockTopBar } from './common/mock-top-bar';



export const CommonActionsLayoutExample = () => {

	return (

		<MockTopBar>

			<CommonActions>

				<Search label="Search" />

				<CreateButton>Create</CreateButton>

			</CommonActions>

		</MockTopBar>

	);

};
```

## User actions

Use UserActions for actions related to the current user. These are displayed in the right of the top bar. 

```jsx
import React from 'react';



import Badge from '@atlaskit/badge';

import { Help } from '@atlassian/navigation-system';

import { Notifications, Settings, UserActions } from '@atlassian/navigation-system/top-nav';



import { MockTopBar } from './common/mock-top-bar';



export const UserActionsLayoutExample = () => {

	return (

		<MockTopBar>

			<UserActions>

				<Notifications

					label="Notifications"

					badge={() => <Badge appearance="important">{3}</Badge>}

				/>

				<Help label="Help" />

				<Settings label="Settings" />

			</UserActions>

		</MockTopBar>

	);

};
```

## Navigation logo

Use the NavLogo component to display a logo in the top bar. It will switch to an icon at small viewport widths. 

```jsx
import React from 'react';



import { JiraIcon, JiraLogo } from '@atlaskit/logo';

import { HomeActions, NavLogo } from '@atlassian/navigation-system/top-nav';



import { MockTopBar } from './common/mock-top-bar';



export const NavLogoExample = () => {

	return (

		<MockTopBar>

			<HomeActions>

				<NavLogo

					href="https://jira.atlassian.com"

					logo={JiraLogo}

					icon={JiraIcon}

					label="Home page"

				/>

			</HomeActions>

		</MockTopBar>

	);

};
```

### Custom logos

Do not provide explicit width and height values when using custom logos. Otherwise they will not respect the container size. 

```jsx
import React from 'react';



import { HomeActions, NavLogo } from '@atlassian/navigation-system/top-nav';



import customLogoSrc from '../../images/200x20.png';

import customIconSrc from '../../images/20x20.png';



import { MockTopBar } from './common/mock-top-bar';



const CustomLogo = () => <img src={customLogoSrc} alt="" />;

const CustomIcon = () => <img src={customIconSrc} alt="" />;



export const CustomNavLogoExample = () => {

	return (

		<MockTopBar>

			<HomeActions>

				<NavLogo

					href="https://jira.atlassian.com"

					logo={CustomLogo}

					icon={CustomIcon}

					label="Home page"

				/>

			</HomeActions>

		</MockTopBar>

	);

};
```

## Custom theming

Top navigation supports custom theming through the UNSAFE_theme prop. Enable custom theming by providing both: Both of these colors should be provided as RGB objects, which can be derived using our color string parsing utilities. White or black text is automatically chosen to maximize contrast. 

```jsx
import React from 'react';



import { TopBar } from '@atlassian/navigation-system/layout/top-bar';



import { MockRoot } from '../../utils/mock-root';



import { MockContent } from './common/mock-content';



export const CustomThemingRgbObjectExample = () => (

	<MockRoot>

		<TopBar

			UNSAFE_theme={{

				backgroundColor: { r: 248, g: 238, b: 254 },

				highlightColor: { r: 150, g: 74, b: 192 },

			}}

		>

			<MockContent />

		</TopBar>

	</MockRoot>

);
```

### Color string parsing

Custom theme colors should be provided as RGB objects, but are typically obtained from users as strings. We provide a number of utilities for parsing color strings into an RGB object format. These parsing utilities are completely optional, and you are able to create your own. Use parseHex to parse a CSS hex color string into an RGB object. It will return null on failure. If an alpha channel is present it will be ignored. Use parseRgb to parse a CSS rgb color string into an RGB object. It will return null on failure. The fractional parts of non-integer values will be ignored, and only the legacy comma-separated syntax is supported. Use parseHsl to parse a CSS hsl color string into an RGB object. It will return null on failure. The fractional parts of non-integer values will be ignored, and only the legacy comma-separated syntax is supported. Use parseUserColor to parse a CSS color string without knowing the format used. It will return null on failure. Supported CSS color string formats are: 

```jsx
import React from 'react';



import { parseHex } from '@atlassian/navigation-system/experimental/color-utils/parse-hex';

import { TopBar } from '@atlassian/navigation-system/layout/top-bar';



import { MockRoot } from '../../utils/mock-root';



import { MockContent } from './common/mock-content';



export const CustomThemingParseHexExample = () => (

	<MockRoot>

		<TopBar

			UNSAFE_theme={{ backgroundColor: parseHex('#F8EEFE'), highlightColor: parseHex('#964AC0') }}

		>

			<MockContent />

		</TopBar>

	</MockRoot>

);
```

```jsx
import React from 'react';



import { parseRgb } from '@atlassian/navigation-system/experimental/color-utils/parse-rgb';

import { TopBar } from '@atlassian/navigation-system/layout/top-bar';



import { MockRoot } from '../../utils/mock-root';



import { MockContent } from './common/mock-content';



export const CustomThemingParseRgbExample = () => (

	<MockRoot>

		<TopBar

			UNSAFE_theme={{

				backgroundColor: parseRgb('rgb(248, 238, 254)'),

				highlightColor: parseRgb('rgb(150, 74, 192)'),

			}}

		>

			<MockContent />

		</TopBar>

	</MockRoot>

);
```

```jsx
import React from 'react';



import { parseHsl } from '@atlassian/navigation-system/experimental/color-utils/parse-hsl';

import { TopBar } from '@atlassian/navigation-system/layout/top-bar';



import { MockRoot } from '../../utils/mock-root';



import { MockContent } from './common/mock-content';



export const CustomThemingParseHslExample = () => (

	<MockRoot>

		<TopBar

			UNSAFE_theme={{

				backgroundColor: parseHsl('hsl(278, 89%, 97%)'),

				highlightColor: parseHsl('hsl(279, 48%, 52%)'),

			}}

		>

			<MockContent />

		</TopBar>

	</MockRoot>

);
```

```jsx
import React from 'react';



import { parseUserColor } from '@atlassian/navigation-system/experimental/color-utils/parse-user-color';

import { TopBar } from '@atlassian/navigation-system/layout/top-bar';



import { MockRoot } from '../../utils/mock-root';



import { MockContent } from './common/mock-content';



export const CustomThemingParseUserColorExample = () => (

	<MockRoot>

		<TopBar

			UNSAFE_theme={{

				backgroundColor: parseUserColor('#F8EEFE'),

				highlightColor: parseUserColor('rgb(150, 74, 192)'),

			}}

		>

			<MockContent />

		</TopBar>

	</MockRoot>

);
```

### Logos

Logos and icons from the Logo package will automatically consume the theme when used with the NavLogo component. Custom logos uploaded by organization admins are unaffected by theming. 

```jsx
import React from 'react';



import { AtlassianIcon, AtlassianLogo } from '@atlaskit/logo';

import { HomeActions, NavLogo } from '@atlassian/navigation-system';

import { parseHex } from '@atlassian/navigation-system/experimental/color-utils/parse-hex';

import { TopBar } from '@atlassian/navigation-system/layout/top-bar';



import { MockRoot } from '../../utils/mock-root';



export const CustomThemingLogoExample = () => (

	<MockRoot>

		<TopBar

			UNSAFE_theme={{ backgroundColor: parseHex('#964AC0'), highlightColor: parseHex('#F8EEFE') }}

		>

			<HomeActions>

				<NavLogo

					icon={AtlassianIcon}

					logo={AtlassianLogo}

					label="Home page"

					href="https://atlassian.design"

				/>

			</HomeActions>

		</TopBar>

	</MockRoot>

);
```

### Search

Use the useLegacySearchTheme() hook to obtain a theme value that is compatible with existing Search Platform components. 

## Use sparingly

Do not create new components that rely on the useLegacySearchTheme() hook. It is only intended for backwards compatibility, and may be deprecated if the Search Platform evolves. 

```jsx
import React from 'react';



import { CommonActions } from '@atlassian/navigation-system';

import { parseHex } from '@atlassian/navigation-system/experimental/color-utils/parse-hex';

import { useLegacySearchTheme } from '@atlassian/navigation-system/experimental/use-legacy-search-theme';

import { TopBar } from '@atlassian/navigation-system/layout/top-bar';



import { MockRoot } from '../../utils/mock-root';

import { MockSearch } from '../../utils/mock-search';



const ThemedSearch = () => {

	const searchTheme = useLegacySearchTheme();

	return <MockSearch theme={searchTheme} />;

};



export const CustomThemingSearchExample = () => (

	<MockRoot>

		<TopBar

			UNSAFE_theme={{ backgroundColor: parseHex('#964AC0'), highlightColor: parseHex('#F8EEFE') }}

		>

			<CommonActions>

				<ThemedSearch />

			</CommonActions>

		</TopBar>

	</MockRoot>

);
```

### Buttons

Do not use Button inside of the top navigation. Use the action components exported from this package (such as AppSwitcher and Create) as they will automatically consume the custom theme. Custom actions can be created using UserAction for icon buttons and TopNavButton for buttons with visible text. 

```jsx
import React from 'react';



import AngleBracketsIcon from '@atlaskit/icon/glyph/code';

import { RovoIcon } from '@atlaskit/logo';

import { UserAction, UserActions } from '@atlassian/navigation-system';

import { parseHex } from '@atlassian/navigation-system/experimental/color-utils/parse-hex';

import { TopNavButton } from '@atlassian/navigation-system/experimental/top-nav-button';

import { TopBar } from '@atlassian/navigation-system/layout/top-bar';



import { MockRoot } from '../../utils/mock-root';



export const CustomThemingButtonsExample = () => (

	<MockRoot>

		<TopBar

			UNSAFE_theme={{ backgroundColor: parseHex('#964AC0'), highlightColor: parseHex('#F8EEFE') }}

		>

			<UserActions>

				<TopNavButton iconBefore={(props) => <RovoIcon {...props} size="xsmall" label="" />}>

					Chat

				</TopNavButton>

				<UserAction icon={AngleBracketsIcon} label="Dev tools" />

			</UserActions>

		</TopBar>

	</MockRoot>

);
```

---

[View Original Documentation](https://atlassian.design/components/navigation-system/top-navigation/examples)
