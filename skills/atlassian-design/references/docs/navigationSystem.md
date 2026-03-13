# Navigation system

The latest navigation system for Atlassian products.

---

## Overview

Atlassian’s navigation is made of these basic parts: These layout and menu areas contain the app switcher, search, and other key features in Atlassian products. 

## Required: Compiled CSS configuration

Compiled CSS must be configured in your application to ensure styles are correctly applied. See the get started page for steps. For Atlassian staff, you can also refer to go/configure-compiled﻿
, (opens new window) 

## Basic example

To see in full-screen, open the code sandbox below. 

## Help

```jsx
import React, { useReducer } from 'react';



import Breadcrumbs, { BreadcrumbsItem } from '@atlaskit/breadcrumbs';

import { IconButton } from '@atlaskit/button/new';

import DropdownMenu, { DropdownItem, DropdownItemGroup } from '@atlaskit/dropdown-menu';

import Heading from '@atlaskit/heading';

import CloseIcon from '@atlaskit/icon/glyph/cross';

import NotificationIcon from '@atlaskit/icon/glyph/notification';

import PageIcon from '@atlaskit/icon/glyph/page';

import PersonIcon from '@atlaskit/icon/glyph/person';

import ProjectIcon from '@atlaskit/icon/core/project';

import IssuesIcon from '@atlaskit/icon/glyph/issues';

import { JiraIcon, JiraLogo } from '@atlaskit/logo';

import { LinkItem, MenuGroup, Section } from '@atlaskit/menu';

import PageHeader from '@atlaskit/page-header';

import { Popup, PopupContent, PopupTrigger } from '@atlaskit/popup/experimental';

import { Box, Inline, Stack } from '@atlaskit/primitives';

import Skeleton from '@atlaskit/skeleton';

import {

	CreateButton,

	Help,

	NavLogo,

	Root,

	SideNav,

	SideNavContent,

	SideNavFooter,

} from '@atlassian/navigation-system';

import { Aside } from '@atlassian/navigation-system/layout/aside';

import { Main } from '@atlassian/navigation-system/layout/main';

import { Panel } from '@atlassian/navigation-system/layout/panel';

import { PanelSplitter } from '@atlassian/navigation-system/layout/panel-splitter';

import { SideNavToggleButton } from '@atlassian/navigation-system/layout/side-nav';

import { TopBar } from '@atlassian/navigation-system/layout/top-bar';

import {

	ExpandableMenuItem,

	ExpandableMenuItemContent,

	ExpandableMenuItemTrigger,

} from '@atlassian/navigation-system/side-nav/expandable-menu-item';

import { MenuLinkItem } from '@atlassian/navigation-system/side-nav/menu-link-item';

import { MenuList } from '@atlassian/navigation-system/side-nav/menu-list';

import {

	CommonActions,

	HomeActions,

	Search,

	Settings,

	UserActions,

} from '@atlassian/navigation-system/top-nav';



export const IntegrationLayoutExample = () => {

	const [isPanelVisible, toggleIsPanelVisible] = useReducer((isVisible) => !isVisible, true);

	const [isSettingsOpen, toggleIsSettingsOpen] = useReducer((isOpen) => !isOpen, false);



	return (

		<Root>

			<TopBar>

				<HomeActions>

					<SideNavToggleButton collapseLabel="Collapse sidebar" expandLabel="Expand sidebar" />

					<NavLogo

						href="https://jira.atlassian.com"

						logo={JiraLogo}

						icon={JiraIcon}

						label="Home page"

					/>

				</HomeActions>

				<CommonActions>

					<Search label="Search" />

					<CreateButton>Create</CreateButton>

				</CommonActions>

				<UserActions>

					<Help label="Help" onClick={toggleIsPanelVisible} />

					<Popup isOpen={isSettingsOpen}>

						<PopupTrigger>

							{({ ref }) => <Settings ref={ref} onClick={toggleIsSettingsOpen} label="Settings" />}

						</PopupTrigger>

						<PopupContent onClose={toggleIsSettingsOpen} placement="bottom">

							{() => (

								<MenuGroup>

									<Section title="Personal Jira settings">

										<LinkItem

											href="/"

											description="Manage language, time zone, and other personal preferences"

											iconBefore={<PersonIcon label="" />}

										>

											General settings

										</LinkItem>

										<LinkItem

											href="/"

											description="Manage email and in-product notifications from Jira"

											iconBefore={<NotificationIcon label="" />}

										>

											Notification settings

										</LinkItem>

									</Section>

									<Section title="Atlassian admin settings">

										<LinkItem

											href="/"

											description="Update your billing details, manage subscriptions, and more"

											iconBefore={<PageIcon label="" />}

										>

											Billing

										</LinkItem>

									</Section>

								</MenuGroup>

							)}

						</PopupContent>

					</Popup>

				</UserActions>

			</TopBar>

			<SideNav defaultWidth={100}>

				<SideNavContent>

					<MenuList>

						<MenuLinkItem href="#">Your work</MenuLinkItem>

						<ExpandableMenuItem isDefaultExpanded>

							<ExpandableMenuItemTrigger

								elemBefore={

									<ProjectIcon label="" LEGACY_fallbackIcon={IssuesIcon} color="currentColor" />

								}

							>

								Projects

							</ExpandableMenuItemTrigger>

							<ExpandableMenuItemContent>

								<MenuLinkItem href="#" isSelected>

									Design System

								</MenuLinkItem>

							</ExpandableMenuItemContent>

						</ExpandableMenuItem>

					</MenuList>

				</SideNavContent>

				<SideNavFooter>Give feedback</SideNavFooter>

				<PanelSplitter label="Resize side nav" />

			</SideNav>

			<Main>

				<Box paddingInline="space.300">

					<PageHeader

						breadcrumbs={

							<Breadcrumbs>

								<BreadcrumbsItem text="Projects" key="Projects" />

								<BreadcrumbsItem text="Design System" key="Design System" />

							</Breadcrumbs>

						}

					>

						Issue name

					</PageHeader>

					<Stack space="space.300">

						<Stack space="space.100">

							<Skeleton width="100%" height={16} borderRadius={3} />

							<Skeleton width="100%" height={16} borderRadius={3} />

							<Skeleton width="66%" height={16} borderRadius={3} />

						</Stack>

						<Stack space="space.100">

							<Skeleton width="100%" height={16} borderRadius={3} />

							<Skeleton width="100%" height={16} borderRadius={3} />

							<Skeleton width="100%" height={16} borderRadius={3} />

							<Skeleton width="33%" height={16} borderRadius={3} />

						</Stack>

					</Stack>

				</Box>

			</Main>

			<Aside defaultWidth={100}>

				<Box paddingBlock="space.300">

					<DropdownMenu trigger="To do" shouldRenderToParent>

						<DropdownItemGroup>

							<DropdownItem>To do</DropdownItem>

							<DropdownItem>In progress</DropdownItem>

							<DropdownItem>Done</DropdownItem>

						</DropdownItemGroup>

					</DropdownMenu>

				</Box>

			</Aside>

			{isPanelVisible && (

				<Panel defaultWidth={200}>

					<Box padding="space.150">

						<Stack space="space.200">

							<Inline alignBlock="center" spread="space-between">

								<Heading size="small" as="h2">

									Help

								</Heading>

								<IconButton

									icon={CloseIcon}

									label=""

									appearance="subtle"

									onClick={toggleIsPanelVisible}

								/>

							</Inline>

							<Stack space="space.300">

								<Stack space="space.100">

									<Skeleton width="100%" height={16} borderRadius={3} />

									<Skeleton width="100%" height={16} borderRadius={3} />

									<Skeleton width="66%" height={16} borderRadius={3} />

								</Stack>

								<Stack space="space.100">

									<Skeleton width="100%" height={16} borderRadius={3} />

									<Skeleton width="100%" height={16} borderRadius={3} />

									<Skeleton width="100%" height={16} borderRadius={3} />

									<Skeleton width="33%" height={16} borderRadius={3} />

								</Stack>

							</Stack>

						</Stack>

					</Box>

				</Panel>

			)}

		</Root>

	);

};
```

---

[View Original Documentation](https://atlassian.design/components/navigation-system/examples)
