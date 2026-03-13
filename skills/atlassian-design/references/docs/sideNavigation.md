# Side navigation

Menu items and elements for the side nav area.

---

## Menu items

### Link menu item

The link item component renders a menu item wrapped in an anchor tag <a>. This is the most common type of menu item, as most menu items are used to send people to another location. For menu items that do something else, use the button item component instead. Use the app provider to specify a custom router link component. 

```jsx
import React from 'react';



import Badge from '@atlaskit/badge';

import ClockIcon from '@atlaskit/icon/glyph/recent';

import HomeIcon from '@atlaskit/icon/glyph/home';

import PageIcon from '@atlaskit/icon/glyph/page';

import StarUnstarredIcon from '@atlaskit/icon/glyph/star';

import TasksIcon from '@atlaskit/icon/core/tasks';

import SubtaskIcon from '@atlaskit/icon/glyph/subtask';

import { SideNavContent } from '@atlassian/navigation-system/layout/side-nav';

import { MenuLinkItem } from '@atlassian/navigation-system/side-nav/menu-link-item';

import { MenuList } from '@atlassian/navigation-system/side-nav/menu-list';



import { MockSideNav } from './common/mock-side-nav';



export const MenuLinkItemExample = () => (

	<MockSideNav>

		<SideNavContent>

			<MenuList>

				<MenuLinkItem

					href="#"

					elemBefore={<HomeIcon label="" />}

				>

					Overview

				</MenuLinkItem>

				<MenuLinkItem href="#" elemBefore={<ClockIcon label="" />}>

					Recent

				</MenuLinkItem>

				<MenuLinkItem href="#" elemBefore={<StarUnstarredIcon label="" />}>

					Starred

				</MenuLinkItem>

				<MenuLinkItem href="#" elemBefore={<PageIcon label="" />}>

					Drafts

				</MenuLinkItem>

				<MenuLinkItem

					href="#"

					elemBefore={<TasksIcon label="" color="currentColor" LEGACY_fallbackIcon={SubtaskIcon} />}

					elemAfter={<Badge>{13}</Badge>}

				>

					Tasks

				</MenuLinkItem>

			</MenuList>

		</SideNavContent>

	</MockSideNav>

);
```

### Button menu item

The button item component renders a menu item wrapped in a button tag <button>. Use this component when you have an action that does something other than navigating to a new page or context. When disabled, content in the actions and actionsOnHover props will not be rendered. 

```jsx
import React from 'react';



import CustomizeIcon from '@atlaskit/icon/core/customize';

import { SideNavContent } from '@atlassian/navigation-system/layout/side-nav';

import { MenuButtonItem } from '@atlassian/navigation-system/side-nav/menu-button-item';

import { MenuList } from '@atlassian/navigation-system/side-nav/menu-list';



import { MockSideNav } from './common/mock-side-nav';



export const MenuButtonItemDisabledExample = () => (

	<MockSideNav>

		<SideNavContent>

			<MenuList>

				<MenuButtonItem elemBefore={<CustomizeIcon label="" color="currentColor" />} isDisabled>

					Customize sidebar

				</MenuButtonItem>

			</MenuList>

		</SideNavContent>

	</MockSideNav>

);
```

### Expandable menu item

The expandable item component allows you to nest menu items. Use this component to form navigation hierarchies. 

```jsx
import React from 'react';



import ProjectIcon from '@atlaskit/icon/core/project';

import IssuesIcon from '@atlaskit/icon/glyph/issues';

import { SideNavContent } from '@atlassian/navigation-system/layout/side-nav';

import { ContainerAvatar } from '@atlassian/navigation-system/side-nav/container-avatar';

import {

	ExpandableMenuItem,

	ExpandableMenuItemContent,

	ExpandableMenuItemTrigger,

} from '@atlassian/navigation-system/side-nav/expandable-menu-item';

import { MenuLinkItem } from '@atlassian/navigation-system/side-nav/menu-link-item';

import { MenuList } from '@atlassian/navigation-system/side-nav/menu-list';



import KoalaIcon from '../../images/koala.svg';

import MoneyIcon from '../../images/money.svg';



import { MockSideNav } from './common/mock-side-nav';



export const ExpandableMenuItemExample = () => (

	<MockSideNav>

		<SideNavContent>

			<MenuList>

				<ExpandableMenuItem isDefaultExpanded>

					<ExpandableMenuItemTrigger

						elemBefore={

							<ProjectIcon label="" color="currentColor" LEGACY_fallbackIcon={IssuesIcon} />

						}

					>

						Projects

					</ExpandableMenuItemTrigger>

					<ExpandableMenuItemContent>

						<MenuLinkItem href="#" elemBefore={<ContainerAvatar src={MoneyIcon} />}>

							Commerce

						</MenuLinkItem>

						<MenuLinkItem href="#" elemBefore={<ContainerAvatar src={KoalaIcon} />}>

							Koala-ty assurance

						</MenuLinkItem>

					</ExpandableMenuItemContent>

				</ExpandableMenuItem>

			</MenuList>

		</SideNavContent>

	</MockSideNav>

);
```

### Flyout menu item

The flyout menu item renders a popup with the menu item as the trigger. Use this component to render children that aren't menu items, such as search bars and filters. You can also render additional menu items within the flyout. For these, you should use the other menu items from the @atlassian/navigation-system package. 

```jsx
import React from 'react';



import { IconButton } from '@atlaskit/button/new';

import Heading from '@atlaskit/heading';

import AlignTextLeftIcon from '@atlaskit/icon/glyph/editor/align-left';

import BoardIcon from '@atlaskit/icon/glyph/board';

import ClockIcon from '@atlaskit/icon/glyph/recent';

import FilterIcon from '@atlaskit/icon/glyph/filter';

import SearchIcon from '@atlaskit/icon/glyph/search';

import { Box, Inline } from '@atlaskit/primitives';

import Textfield from '@atlaskit/textfield';

import { SideNavContent } from '@atlassian/navigation-system/layout/side-nav';

import { ContainerAvatar } from '@atlassian/navigation-system/side-nav/container-avatar';

import {

	FlyoutMenuItem,

	FlyoutMenuItemContent,

	FlyoutMenuItemTrigger,

} from '@atlassian/navigation-system/side-nav/flyout-menu-item';

import { MenuLinkItem } from '@atlassian/navigation-system/side-nav/menu-link-item';

import { MenuList } from '@atlassian/navigation-system/side-nav/menu-list';

import {

	Divider,

	MenuSection,

	MenuSectionHeading,

} from '@atlassian/navigation-system/side-nav/menu-section';



import CDProjectIcon from '../../images/cd.svg';



import { MockSideNav } from './common/mock-side-nav';



export const FlyoutMenuItemExample = () => (

	<MockSideNav>

		<SideNavContent>

			<MenuList>

				<FlyoutMenuItem>

					<FlyoutMenuItemTrigger elemBefore={<ClockIcon label="" />}>

						Recent

					</FlyoutMenuItemTrigger>

					<FlyoutMenuItemContent>

						<Box paddingInlineStart="space.075" paddingBlock="space.100">

							<Heading size="xsmall" as="span">

								Recent

							</Heading>

						</Box>

						<Box paddingInline="space.050" paddingBlock="space.075">

							<Inline space="space.100">

								<Textfield

									isCompact

									elemBeforeInput={

										<Box

											paddingInlineStart="space.075"

											paddingInlineEnd="space.025"

											paddingBlockStart="space.025"

										>

											<SearchIcon label="" />

										</Box>

									}

									placeholder="Search recent items"

								/>

								<IconButton icon={FilterIcon} label="" />

							</Inline>

						</Box>

						<MenuSection>

							<MenuSectionHeading>Today</MenuSectionHeading>

							<MenuList>

								<MenuLinkItem

									href="#"

									elemBefore={<BoardIcon label="" />}

									description="Board • 3 hours ago"

								>

									Mitigate the risk

								</MenuLinkItem>

								<MenuLinkItem

									href="#"

									elemBefore={<ContainerAvatar src={CDProjectIcon} />}

									description="Projects • Yesterday"

								>

									Important tasks

								</MenuLinkItem>

							</MenuList>

						</MenuSection>

						<Divider />

						<MenuList>

							<MenuLinkItem

								href="#"

								elemBefore={<AlignTextLeftIcon label="" />}

							>

								View all recent items

							</MenuLinkItem>

						</MenuList>

					</FlyoutMenuItemContent>

				</FlyoutMenuItem>

			</MenuList>

		</SideNavContent>

	</MockSideNav>

);
```

### Composing menus

You can use the actions or actionsOnHover props to compose your own menus. If you want to render additional menu items within these menus, you should use either: You shouldn't use @atlassian/navigation-system menu items within these menus. 

```jsx
import React, { useState } from 'react';



import { IconButton } from '@atlaskit/button/new';

import DropdownMenu, { DropdownItem, DropdownItemGroup } from '@atlaskit/dropdown-menu';

import FilterIcon from '@atlaskit/icon/glyph/filter';

import StarUnstarredIcon from '@atlaskit/icon/glyph/star';

import ShowMoreHorizontal from '@atlaskit/icon/glyph/more';

import { ButtonItem, MenuGroup, Section } from '@atlaskit/menu';

import Popup from '@atlaskit/popup';

import { SideNavContent } from '@atlassian/navigation-system/layout/side-nav';

import { MenuButtonItem } from '@atlassian/navigation-system/side-nav/menu-button-item';

import { MenuList } from '@atlassian/navigation-system/side-nav/menu-list';



import { MockSideNav } from './common/mock-side-nav';



export const ComposingMenus = () => {

	const [isPopupOpen, setIsPopupOpen] = useState(false);



	return (

		<MockSideNav>

			<SideNavContent>

				<MenuList>

					{/* Example of composing with a dropdown menu */}

					<MenuButtonItem

						elemBefore={<StarUnstarredIcon label="" />}

						actions={

							<DropdownMenu

								shouldRenderToParent

								trigger={({ triggerRef, ...props }) => (

									<IconButton

										ref={triggerRef}

										{...props}

										spacing="compact"

										appearance="subtle"

										label="Open"

										icon={ShowMoreHorizontal}

									/>

								)}

							>

								<DropdownItemGroup>

									<DropdownItem>Manage starred</DropdownItem>

									<DropdownItem>Export</DropdownItem>

								</DropdownItemGroup>

							</DropdownMenu>

						}

					>

						Starred

					</MenuButtonItem>



					{/* Example of composing with a popup */}

					<MenuButtonItem

						elemBefore={<FilterIcon label="" />}

						actions={

							<Popup

								shouldRenderToParent

								isOpen={isPopupOpen}

								onClose={() => setIsPopupOpen(false)}

								placement="bottom-start"

								content={() => (

									<MenuGroup>

										<Section>

											<ButtonItem>Manage filters</ButtonItem>

											<ButtonItem>Export</ButtonItem>

										</Section>

									</MenuGroup>

								)}

								trigger={(triggerProps) => (

									<IconButton

										{...triggerProps}

										icon={ShowMoreHorizontal}

										label="Open"

										appearance="subtle"

										spacing="compact"

										onClick={() => setIsPopupOpen(!isPopupOpen)}

										isSelected={isPopupOpen}

									/>

								)}

							/>

						}

					>

						Filters

					</MenuButtonItem>

				</MenuList>

			</SideNavContent>

		</MockSideNav>

	);

};
```

## Sections

Use MenuSection to group related items. Screen readers will convey these groupings. Optionally compose with MenuSectionHeading to label the group, and Divider to render a separator. 

## Starred

## Recent

```jsx
import React from 'react';



import AlignTextLeftIcon from '@atlaskit/icon/glyph/editor/align-left';

import ProjectIcon from '@atlaskit/icon/core/project';

import IssuesIcon from '@atlaskit/icon/glyph/issues';

import { SideNavContent } from '@atlassian/navigation-system/layout/side-nav';

import { ContainerAvatar } from '@atlassian/navigation-system/side-nav/container-avatar';

import {

	ExpandableMenuItem,

	ExpandableMenuItemContent,

	ExpandableMenuItemTrigger,

} from '@atlassian/navigation-system/side-nav/expandable-menu-item';

import { MenuLinkItem } from '@atlassian/navigation-system/side-nav/menu-link-item';

import { MenuList } from '@atlassian/navigation-system/side-nav/menu-list';

import { MenuListItem } from '@atlassian/navigation-system/side-nav/menu-list-item';

import {

	Divider,

	MenuSection,

	MenuSectionHeading,

} from '@atlassian/navigation-system/side-nav/menu-section';



import KoalaIcon from '../../images/koala.svg';

import MoneyIcon from '../../images/money.svg';



import { MockSideNav } from './common/mock-side-nav';



export const MenuSectionExample = () => (

	<MockSideNav>

		<SideNavContent>

			<MenuList>

				<ExpandableMenuItem isDefaultExpanded>

					<ExpandableMenuItemTrigger

						elemBefore={

							<ProjectIcon label="" LEGACY_fallbackIcon={IssuesIcon} color="currentColor" />

						}

					>

						Projects

					</ExpandableMenuItemTrigger>

					<ExpandableMenuItemContent>

						<MenuListItem>

							<MenuSection>

								<MenuSectionHeading>Starred</MenuSectionHeading>

								<MenuList>

									<MenuLinkItem href="#" elemBefore={<ContainerAvatar src={MoneyIcon} />}>

										Commerce

									</MenuLinkItem>

								</MenuList>

							</MenuSection>

							<MenuSection>

								<MenuSectionHeading>Recent</MenuSectionHeading>

								<MenuList>

									<MenuLinkItem href="#" elemBefore={<ContainerAvatar src={KoalaIcon} />}>

										Koala-ty assurance

									</MenuLinkItem>

								</MenuList>

								<Divider />

							</MenuSection>

							<MenuLinkItem

								href="#"

								elemBefore={<AlignTextLeftIcon label="" />}

							>

								View all projects

							</MenuLinkItem>

						</MenuListItem>

					</ExpandableMenuItemContent>

				</ExpandableMenuItem>

			</MenuList>

		</SideNavContent>

	</MockSideNav>

);
```

## Global app shortcuts

Global app shortcuts allow quick access to related apps. 

## Global app icon tiles

We are looking into making global app icon tiles easier to consume, but there is currently no platform offering. 

### Spacing

Use TopLevelSpacer to create spacing between: 

## TopLevelSpacer usage

Only use this component in the top level of the menu, and exercise caution when using it in new situations. This component exists to fulfil product design requirements but has not yet been consolidated into the wider navigation system. It may not exist in the future when global apps are no longer in the side navigation. 

```jsx
import React from 'react';



import AppsIcon from '@atlaskit/icon/core/apps';

import InboxIcon from '@atlaskit/icon/glyph/tray';

import LinkExternalIcon from '@atlaskit/icon/glyph/shortcut';

import ShowMoreHorizontalIcon from '@atlaskit/icon/glyph/more';

import AppSwitcherIcon from '@atlaskit/icon/glyph/app-switcher';

import { ConfluenceIcon, JiraIcon } from '@atlaskit/logo';

import { SideNavContent } from '@atlassian/navigation-system/layout/side-nav';

import {

	FlyoutMenuItem,

	FlyoutMenuItemContent,

	FlyoutMenuItemTrigger,

} from '@atlassian/navigation-system/side-nav/flyout-menu-item';

import { MenuButtonItem } from '@atlassian/navigation-system/side-nav/menu-button-item';

import { MenuLinkItem } from '@atlassian/navigation-system/side-nav/menu-link-item';

import { MenuList } from '@atlassian/navigation-system/side-nav/menu-list';

import { TopLevelSpacer } from '@atlassian/navigation-system/side-nav/top-level-spacer';



import { GlobalAppIconTile } from './common/global-app-icon-tile';

import { MockSideNav } from './common/mock-side-nav';



export const GlobalAppsExample = () => (

	<MockSideNav>

		<SideNavContent>

			<MenuList>

				<MenuLinkItem href="#" elemBefore={<InboxIcon label="" />}>

					For you

				</MenuLinkItem>

				<MenuLinkItem

					href="#"

					elemBefore={<AppsIcon LEGACY_fallbackIcon={AppSwitcherIcon} label="" />}

				>

					Apps

				</MenuLinkItem>



				<TopLevelSpacer />



				<MenuLinkItem

					href="#"

					elemBefore={<GlobalAppIconTile logo={JiraIcon} />}

					elemAfter={

						<LinkExternalIcon label="" size="small" />

					}

					description="My site"

				>

					Jira

				</MenuLinkItem>

				<FlyoutMenuItem>

					<FlyoutMenuItemTrigger elemBefore={<GlobalAppIconTile logo={ConfluenceIcon} />}>

						Confluence

					</FlyoutMenuItemTrigger>

					<FlyoutMenuItemContent>

						<MenuList>

							<MenuLinkItem

								href="#"

								elemBefore={<GlobalAppIconTile logo={ConfluenceIcon} />}

								elemAfter={

									<LinkExternalIcon label="" size="small" />

								}

								description="Site A"

							>

								Confluence

							</MenuLinkItem>

							<MenuLinkItem

								href="#"

								elemBefore={<GlobalAppIconTile logo={ConfluenceIcon} />}

								elemAfter={

									<LinkExternalIcon label="" size="small" />

								}

								description="Site B"

							>

								Confluence

							</MenuLinkItem>

							<MenuLinkItem

								href="#"

								elemBefore={<GlobalAppIconTile logo={ConfluenceIcon} />}

								elemAfter={

									<LinkExternalIcon label="" size="small" />

								}

								description="Site C"

							>

								Confluence

							</MenuLinkItem>

						</MenuList>

					</FlyoutMenuItemContent>

				</FlyoutMenuItem>



				<TopLevelSpacer />



				<MenuButtonItem elemBefore={<ShowMoreHorizontalIcon label="" />}>More</MenuButtonItem>

			</MenuList>

		</SideNavContent>

	</MockSideNav>

);



export default GlobalAppsExample;
```

---

[View Original Documentation](https://atlassian.design/components/navigation-system/side-navigation/examples)
