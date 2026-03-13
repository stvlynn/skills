# Page layout

A collection of components which let you compose an application's page layout.

---

## Basic

PageLayout wraps an entire app view and helps split the viewport into sections where you can render components in slots, such as TopNavigation, Main, LeftSidebar, and more. This is a customisable and more interactive example to demonstrate the page layout slots. 

```jsx
/**

 * @jsxRuntime classic

 * @jsx jsx

 */



// eslint-disable-next-line @atlaskit/ui-styling-standard/use-compiled -- Ignored via go/DSP-18766

import { jsx } from '@emotion/react';



import {

	Banner,

	Content,

	LeftSidebarWithoutResize,

	Main,

	PageLayout,

	RightPanel,

	TopNavigation,

} from '@atlaskit/page-layout';

import { token } from '@atlaskit/tokens';



import { SlotLabel, SlotWrapper } from '../common';



const BasicGrid = () => {

	return (

		<PageLayout>

			{

				<Banner testId="banner" id="banner" skipLinkTitle="Banner" height={60} isFixed={false}>

					<SlotWrapper borderColor={token('color.border.accent.yellow')}>

						<SlotLabel>Banner</SlotLabel>

					</SlotWrapper>

				</Banner>

			}

			{

				<TopNavigation

					testId="topNavigation"

					id="product-navigation"

					skipLinkTitle="Product Navigation"

					height={60}

					isFixed={false}

				>

					<SlotWrapper borderColor={token('color.border.accent.blue')}>

						<SlotLabel>Product Navigation</SlotLabel>

					</SlotWrapper>

				</TopNavigation>

			}

			<Content testId="content">

				{

					<LeftSidebarWithoutResize

						testId="leftSidebar"

						id="space-navigation"

						skipLinkTitle="Project Navigation"

						isFixed={false}

						width={125}

					>

						<SlotWrapper borderColor={token('color.border.accent.green')} hasExtraPadding>

							<SlotLabel isSmall>Space Navigation</SlotLabel>

						</SlotWrapper>

					</LeftSidebarWithoutResize>

				}

				{

					<Main testId="main" id="main" skipLinkTitle="Main Content">

						<SlotWrapper borderColor={token('color.border')} minHeight={400}>

							<SlotLabel isSmall>Main Content</SlotLabel>

							<p>Visit the first focusable element on the page to see the skip links menu</p>

						</SlotWrapper>

					</Main>

				}

			</Content>

			{

				<RightPanel

					testId="rightPanel"

					id="help-panel"

					skipLinkTitle="Help Panel"

					isFixed={false}

					width={125}

				>

					<SlotWrapper borderColor={token('color.border.accent.orange')}>

						<SlotLabel>Help Panel</SlotLabel>

					</SlotWrapper>

				</RightPanel>

			}

		</PageLayout>

	);

};



export default BasicGrid;
```

```jsx
/**

 * @jsxRuntime classic

 * @jsx jsx

 */

import { Fragment, useCallback, useState } from 'react';



// eslint-disable-next-line @atlaskit/ui-styling-standard/use-compiled -- Ignored via go/DSP-18766

import { jsx } from '@emotion/react';



import {

	Banner,

	Content,

	LeftPanel,

	LeftSidebarWithoutResize,

	Main,

	PageLayout,

	RightPanel,

	RightSidebar,

	TopNavigation,

} from '@atlaskit/page-layout';

import { token } from '@atlaskit/tokens';



import {

	ScrollableContent,

	SlotLabel,

	SlotWrapper,

	Toggle,

	ToggleBox,

	toKebabCase,

} from '../common';



type SlotName =

	| 'Banner'

	| 'TopNavigation'

	| 'LeftPanel'

	| 'LeftSidebar'

	| 'Main'

	| 'RightSidebar'

	| 'RightPanel';



const initialState = {

	isBannerShown: true,

	isTopNavigationShown: true,

	isLeftPanelShown: true,

	isLeftSidebarShown: true,

	isMainShown: true,

	isRightSidebarShown: true,

	isRightPanelShown: true,

	isBannerFixed: true,

	isTopNavigationFixed: true,

	isLeftPanelFixed: false,

	isLeftPanelScrollable: false,

	isLeftSidebarFixed: true,

	isLeftSidebarScrollable: false,

	isMainScrollable: false,

	isMainExtraWide: false,

	isRightSidebarFixed: false,

	isRightSidebarScrollable: false,

	isRightPanelFixed: false,

	isRightPanelScrollable: false,

};



const BasicGrid = () => {

	const [gridState, setGridState] = useState(initialState);



	const ToggleFixed = useCallback(

		({ slotName }: { slotName: SlotName }) => {

			const gridKey = `is${slotName}Fixed` as keyof typeof gridState;

			return (

				<Toggle

					id={`${slotName}--fixed`}

					isChecked={gridState[gridKey]}

					onChange={() => setGridState({ ...gridState, [gridKey]: !gridState[gridKey] })}

				>

					Toggle fixed

				</Toggle>

			);

		},

		[gridState],

	);



	const ToggleScrollable = useCallback(

		({ slotName }: { slotName: SlotName }) => {

			const gridKey = `is${slotName}Scrollable` as keyof typeof gridState;

			return (

				<Fragment>

					<Toggle

						id={`${slotName}--scrollable`}

						isChecked={gridState[gridKey]}

						onChange={() => setGridState({ ...gridState, [gridKey]: !gridState[gridKey] })}

					>

						Toggle scrollable content

					</Toggle>

					{gridState[gridKey] && <ScrollableContent />}

				</Fragment>

			);

		},

		[gridState],

	);



	const ToggleShown = useCallback(

		({ slotName }: { slotName: SlotName }) => {

			const gridKey = `is${slotName}Shown` as keyof typeof gridState;

			return (

				<Toggle

					id={`toggle-${toKebabCase(slotName)}`}

					onChange={() => setGridState({ ...gridState, [gridKey]: !gridState[gridKey] })}

					isChecked={!gridState[gridKey]}

				>{`${gridState[gridKey] ? 'Hide' : 'Show'} ${slotName}`}</Toggle>

			);

		},

		[gridState],

	);



	const ToggleExtraWide = useCallback(

		() => (

			<Fragment>

				<Toggle

					id={`toggle--extra-wide`}

					onChange={() =>

						setGridState({

							...gridState,

							isMainExtraWide: !gridState.isMainExtraWide,

						})

					}

					isChecked={gridState.isMainExtraWide}

				>

					Toggle extra-wide content

				</Toggle>

				{gridState.isMainExtraWide && (

					<img

						src="https://picsum.photos/seed/picsum/1600"

						alt="wide placeholder"

						title="wide placeholder image"

					/>

				)}

			</Fragment>

		),

		[gridState],

	);



	return (

		<PageLayout>

			{gridState.isBannerShown && (

				<Banner

					testId="banner"

					id="banner"

					skipLinkTitle="Banner"

					height={100}

					isFixed={gridState.isBannerFixed}

				>

					<SlotWrapper borderColor={token('color.border.accent.yellow')}>

						<SlotLabel>Banner</SlotLabel>

						<b>Visit the first focusable element on the page to see the skip links menu</b>

						<ToggleFixed slotName="Banner" />

					</SlotWrapper>

				</Banner>

			)}

			{gridState.isTopNavigationShown && (

				<TopNavigation

					testId="topNavigation"

					id="top-navigation"

					skipLinkTitle="Top Navigation"

					height={60}

					isFixed={gridState.isTopNavigationFixed}

				>

					<SlotWrapper borderColor={token('color.border.accent.blue')}>

						<SlotLabel>TopNavigation</SlotLabel>

						<ToggleFixed slotName="TopNavigation" />

					</SlotWrapper>

				</TopNavigation>

			)}

			{gridState.isLeftPanelShown && (

				<LeftPanel

					testId="leftPanel"

					id="left-panel"

					skipLinkTitle="Left Panel"

					isFixed={gridState.isLeftPanelFixed}

					width={200}

				>

					<SlotWrapper borderColor={token('color.border.accent.orange')}>

						<SlotLabel>LeftPanel</SlotLabel>

						<ToggleFixed slotName="LeftPanel" />

						<ToggleScrollable slotName="LeftPanel" />

					</SlotWrapper>

				</LeftPanel>

			)}

			<Content testId="content">

				{gridState.isLeftSidebarShown && (

					<LeftSidebarWithoutResize

						testId="leftSidebar"

						id="left-sidebar"

						skipLinkTitle="Project Navigation"

						isFixed={gridState.isLeftSidebarFixed}

						width={250}

					>

						<SlotWrapper borderColor={token('color.border.accent.green')} hasExtraPadding>

							<SlotLabel>LeftSidebar</SlotLabel>

							<ToggleFixed slotName="LeftSidebar" />

							<ToggleScrollable slotName="LeftSidebar" />

						</SlotWrapper>

					</LeftSidebarWithoutResize>

				)}

				{gridState.isMainShown && (

					<Main testId="main" id="main" skipLinkTitle="Main Content">

						<SlotWrapper borderColor={token('color.border')}>

							<SlotLabel>Main</SlotLabel>

							<ToggleExtraWide />

							<ToggleScrollable slotName="Main" />

						</SlotWrapper>

					</Main>

				)}

				{gridState.isRightSidebarShown && (

					<RightSidebar

						testId="rightSidebar"

						id="right-sidebar"

						skipLinkTitle="Right Sidebar"

						isFixed={gridState.isRightSidebarFixed}

						width={200}

					>

						<SlotWrapper borderColor={token('color.border.accent.green')}>

							<SlotLabel>RightSidebar</SlotLabel>

							<ToggleFixed slotName="RightSidebar" />

							<ToggleScrollable slotName="RightSidebar" />

						</SlotWrapper>

					</RightSidebar>

				)}

			</Content>

			{gridState.isRightPanelShown && (

				<RightPanel

					testId="rightPanel"

					id="right-panel"

					skipLinkTitle="Right Panel"

					isFixed={gridState.isRightPanelFixed}

					width={200}

				>

					<SlotWrapper borderColor={token('color.border.accent.orange')}>

						<SlotLabel>RightPanel</SlotLabel>

						<ToggleFixed slotName="RightPanel" />

						<ToggleScrollable slotName="RightPanel" />

					</SlotWrapper>

				</RightPanel>

			)}

			<ToggleBox>

				<ToggleShown slotName="Banner" />

				<ToggleShown slotName="TopNavigation" />

				<ToggleShown slotName="LeftPanel" />

				<ToggleShown slotName="LeftSidebar" />

				<ToggleShown slotName="Main" />

				<ToggleShown slotName="RightSidebar" />

				<ToggleShown slotName="RightPanel" />

			</ToggleBox>

		</PageLayout>

	);

};



export default BasicGrid;
```

## Integrated

PageLayout is designed to work in tandem with the Atlassian navigation and side navigation components. This is an example where these components are used together. 

```jsx
/**

 * @jsxRuntime classic

 * @jsx jsx

 */

import { useState } from 'react';



// eslint-disable-next-line @atlaskit/ui-styling-standard/use-compiled -- Ignored via go/DSP-18766

import { jsx } from '@emotion/react';



import {

	AtlassianNavigation,

	Create,

	Help,

	PrimaryButton,

	ProductHome,

} from '@atlaskit/atlassian-navigation';

import noop from '@atlaskit/ds-lib/noop';

import { ConfluenceIcon, ConfluenceLogo } from '@atlaskit/logo';

import { ButtonItem, MenuGroup, Section } from '@atlaskit/menu';

import { Content, LeftSidebar, Main, PageLayout, TopNavigation } from '@atlaskit/page-layout';

import Popup from '@atlaskit/popup';

import {

	Header,

	NavigationHeader,

	NestableNavigationContent,

	NestingItem,

	SideNavigation,

} from '@atlaskit/side-navigation';



import { SlotLabel, SlotWrapper } from '../common';



export default function ProductLayout() {

	return (

		<PageLayout>

			<TopNavigation

				isFixed={true}

				id="confluence-navigation"

				skipLinkTitle="Confluence Navigation"

			>

				<TopNavigationContents />

			</TopNavigation>

			<Content testId="content">

				<LeftSidebar

					isFixed={false}

					width={450}

					id="project-navigation"

					skipLinkTitle="Project Navigation"

					testId="left-sidebar"

					resizeGrabAreaLabel="Resize Current project sidebar"

					resizeButtonLabel="Current project sidebar"

					valueTextLabel="Width"

				>

					<SideNavigationContent />

				</LeftSidebar>

				<Main id="main-content" skipLinkTitle="Main Content">

					<SlotWrapper>

						<SlotLabel>Main Content</SlotLabel>

					</SlotWrapper>

				</Main>

			</Content>

		</PageLayout>

	);

}



function TopNavigationContents() {

	return (

		<AtlassianNavigation

			label="site"

			moreLabel="More"

			primaryItems={[

				<PrimaryButton isHighlighted>Item 1</PrimaryButton>,

				<PrimaryButton>Item 2</PrimaryButton>,

				<PrimaryButton>Item 3</PrimaryButton>,

				<PrimaryButton>Item 4</PrimaryButton>,

			]}

			renderProductHome={ProductHomeExample}

			renderCreate={DefaultCreate}

			renderHelp={HelpPopup}

		/>

	);

}



const SideNavigationContent = () => {

	return (

		<SideNavigation label="Project navigation" testId="side-navigation">

			<NavigationHeader>

				<Header description="Sidebar header description">Sidebar Header</Header>

			</NavigationHeader>

			<NestableNavigationContent initialStack={[]}>

				<Section>

					<NestingItem id="1" title="Nested Item">

						<Section title="Group 1">

							<ButtonItem>Item 1</ButtonItem>

							<ButtonItem>Item 2</ButtonItem>

						</Section>

					</NestingItem>

				</Section>

			</NestableNavigationContent>

		</SideNavigation>

	);

};



/*

 * Components for composing top and side navigation

 */



export const DefaultCreate = () => (

	<Create buttonTooltip="Create" iconButtonTooltip="Create" onClick={noop} text="Create" />

);



const ProductHomeExample = () => (

	<ProductHome

		onClick={console.log}

		icon={ConfluenceIcon}

		logo={ConfluenceLogo}

		siteTitle="Product"

	/>

);



export const HelpPopup = () => {

	const [isOpen, setIsOpen] = useState(false);



	const onClick = () => {

		setIsOpen(!isOpen);

	};



	const onClose = () => {

		setIsOpen(false);

	};



	return (

		<Popup

			shouldRenderToParent

			placement="bottom-start"

			content={HelpPopupContent}

			isOpen={isOpen}

			onClose={onClose}

			trigger={(triggerProps) => (

				<Help isSelected={isOpen} onClick={onClick} tooltip="Help" {...triggerProps} />

			)}

		/>

	);

};



const HelpPopupContent = () => (

	<MenuGroup>

		<Section title={'Menu Heading'}>

			<ButtonItem>Item 1</ButtonItem>

			<ButtonItem>Item 2</ButtonItem>

			<ButtonItem>Item 3</ButtonItem>

			<ButtonItem>Item 4</ButtonItem>

		</Section>

		<Section title="Menu Heading with separator" hasSeparator>

			<ButtonItem>Item 5</ButtonItem>

			<ButtonItem>Item 6</ButtonItem>

		</Section>

	</MenuGroup>

);
```

## Left sidebar

The left sidebar houses all the navigation components for the current space a user is in. PageLayout lets people choose to resize, collapse or expand the sidebar. This lets people get more screen space to do work when needed. The left sidebar: In this example, the left sidebar can be resized and even collapsed to give more screen space to the main content: 

```jsx
/**

 * @jsxRuntime classic

 * @jsx jsx

 */

import { Fragment, useCallback, useState } from 'react';



// eslint-disable-next-line @atlaskit/ui-styling-standard/use-compiled -- Ignored via go/DSP-18766

import { jsx } from '@emotion/react';



import {

	Banner,

	Content,

	LeftPanel,

	LeftSidebar,

	type LeftSidebarState,

	Main,

	PageLayout,

	RightPanel,

	RightSidebar,

	TopNavigation,

} from '@atlaskit/page-layout';

import { token } from '@atlaskit/tokens';

import Tooltip from '@atlaskit/tooltip';



import {

	ExpandLeftSidebarKeyboardShortcut,

	ScrollableContent,

	SlotLabel,

	SlotWrapper,

	Toggle,

	ToggleBox,

} from '../common';



type SlotName =

	| 'Banner'

	| 'TopNavigation'

	| 'LeftPanel'

	| 'LeftSidebar'

	| 'Main'

	| 'RightSidebar'

	| 'RightPanel'

	| 'PageLayout';



const initialState = {

	isBannerShown: false,

	isTopNavigationShown: true,

	isLeftPanelShown: false,

	isLeftSidebarShown: true,

	isMainShown: true,

	isRightSidebarShown: false,

	isRightPanelShown: false,

	isBannerFixed: true,

	isTopNavigationFixed: true,

	isLeftPanelFixed: false,

	isLeftPanelScrollable: false,

	isLeftSidebarFixed: true,

	isLeftSidebarScrollable: false,

	isMainScrollable: false,

	isMainExtraWide: false,

	isRightSidebarFixed: false,

	isRightSidebarScrollable: false,

	isRightPanelFixed: false,

	isRightPanelScrollable: false,

	isPageLayoutShown: true,

};



const BasicGrid = () => {

	const [gridState, setGridState] = useState(initialState);



	const ToggleFixed = useCallback(

		({ slotName }: { slotName: SlotName }) => {

			const gridKey = `is${slotName}Fixed` as keyof typeof gridState;

			return (

				<Toggle

					id={`${slotName}--fixed`}

					isChecked={gridState[gridKey]}

					onChange={() => setGridState({ ...gridState, [gridKey]: !gridState[gridKey] })}

				>

					Toggle fixed

				</Toggle>

			);

		},

		[gridState],

	);



	const ToggleScrollable = useCallback(

		({ slotName }: { slotName: SlotName }) => {

			const gridKey = `is${slotName}Scrollable` as keyof typeof gridState;

			return (

				<Fragment>

					<Toggle

						data-toggle-scrollable

						id={`${slotName}--scrollable`}

						isChecked={gridState[gridKey]}

						onChange={() => setGridState({ ...gridState, [gridKey]: !gridState[gridKey] })}

					>

						Toggle scrollable content

					</Toggle>

					{gridState[gridKey] && <ScrollableContent />}

				</Fragment>

			);

		},

		[gridState],

	);



	const ToggleShown = useCallback(

		({ slotName }: { slotName: SlotName }) => {

			const gridKey = `is${slotName}Shown` as keyof typeof gridState;

			return (

				<Toggle

					id={`${slotName}--shown`}

					onChange={() => setGridState({ ...gridState, [gridKey]: !gridState[gridKey] })}

					isChecked={gridState[gridKey] !== initialState[gridKey]}

				>{`${gridState[gridKey] ? 'Unmount' : 'Mount'} ${slotName}`}</Toggle>

			);

		},

		[gridState],

	);



	const ToggleExtraWide = useCallback(

		() => (

			<Fragment>

				<Toggle

					id={`toggle--extra-wide`}

					onChange={() =>

						setGridState({

							...gridState,

							isMainExtraWide: !gridState.isMainExtraWide,

						})

					}

					isChecked={gridState.isMainExtraWide}

				>

					Toggle extra-wide content

				</Toggle>

				{gridState.isMainExtraWide && (

					<img

						src="https://picsum.photos/seed/picsum/1600"

						alt="wide placeholder"

						title="wide placeholder image"

					/>

				)}

			</Fragment>

		),

		[gridState],

	);



	return (

		<Fragment>

			{gridState.isPageLayoutShown && (

				<PageLayout

					onLeftSidebarExpand={(state: LeftSidebarState) => console.log('onExpand', state)}

					onLeftSidebarCollapse={(state: LeftSidebarState) => console.log('onCollapse', state)}

				>

					{gridState.isBannerShown && (

						<Banner height={60} isFixed={gridState.isBannerFixed}>

							<SlotWrapper borderColor={token('color.border.accent.yellow')}>

								<SlotLabel>Banner</SlotLabel>

								<ToggleFixed slotName="Banner" />

							</SlotWrapper>

						</Banner>

					)}

					{gridState.isTopNavigationShown && (

						<TopNavigation height={60} isFixed={gridState.isTopNavigationFixed}>

							<SlotWrapper borderColor={token('color.border.accent.blue')}>

								<SlotLabel>TopNavigation</SlotLabel>

								<ToggleFixed slotName="TopNavigation" />

							</SlotWrapper>

						</TopNavigation>

					)}

					{gridState.isLeftPanelShown && (

						<LeftPanel isFixed={gridState.isLeftPanelFixed} width={200}>

							<SlotWrapper borderColor={token('color.border.accent.orange')}>

								<SlotLabel>LeftPanel</SlotLabel>

								<ToggleFixed slotName="LeftPanel" />

								<ToggleScrollable slotName="LeftPanel" />

							</SlotWrapper>

						</LeftPanel>

					)}

					<Content testId="content">

						{gridState.isLeftSidebarShown && (

							<LeftSidebar

								testId="left-sidebar"

								id="left-sidebar"

								skipLinkTitle="Project Navigation"

								isFixed={gridState.isLeftSidebarFixed}

								onResizeStart={(state: LeftSidebarState) => console.log('onResizeStart', state)}

								onResizeEnd={(state: LeftSidebarState) => console.log('onResizeEnd', state)}

								onFlyoutExpand={() => console.log('onFlyoutExpand')}

								onFlyoutCollapse={() => console.log('onFlyoutCollapse')}

								resizeGrabAreaLabel="Resize Current project sidebar"

								resizeButtonLabel="Current project sidebar"

								valueTextLabel="Width"

								// eslint-disable-next-line @repo/internal/react/no-unsafe-overrides

								overrides={{

									ResizeButton: {

										render: (Component, props) => (

											<Tooltip

												content={'Left Sidebar'}

												hideTooltipOnClick

												position="right"

												testId="tooltip"

											>

												<Component {...props} />

											</Tooltip>

										),

									},

								}}

							>

								<SlotWrapper hasExtraPadding hasHorizontalScrollbar={false}>

									<SlotLabel>LeftSidebar</SlotLabel>

									<ToggleFixed slotName="LeftSidebar" />

									<ToggleScrollable slotName="LeftSidebar" />

								</SlotWrapper>



								<ExpandLeftSidebarKeyboardShortcut />

							</LeftSidebar>

						)}

						{gridState.isMainShown && (

							<Main id="main" skipLinkTitle="Main">

								<SlotWrapper>

									<SlotLabel>Main</SlotLabel>

									<ToggleExtraWide />

									<ToggleScrollable slotName="Main" />

								</SlotWrapper>

							</Main>

						)}

						{gridState.isRightSidebarShown && (

							<RightSidebar isFixed={gridState.isRightSidebarFixed} width={200}>

								<SlotWrapper borderColor={token('color.border.accent.green')}>

									<SlotLabel>RightSidebar</SlotLabel>

									<ToggleFixed slotName="RightSidebar" />

									<ToggleScrollable slotName="RightSidebar" />

								</SlotWrapper>

							</RightSidebar>

						)}

					</Content>

					{gridState.isRightPanelShown && (

						<RightPanel isFixed={gridState.isRightPanelFixed} width={200}>

							<SlotWrapper borderColor={token('color.border.accent.orange')}>

								<SlotLabel>RightPanel</SlotLabel>

								<ToggleFixed slotName="RightPanel" />

								<ToggleScrollable slotName="RightPanel" />

							</SlotWrapper>

						</RightPanel>

					)}

				</PageLayout>

			)}

			<ToggleBox>

				<ToggleShown slotName="Banner" />

				<ToggleShown slotName="TopNavigation" />

				<ToggleShown slotName="LeftPanel" />

				<ToggleShown slotName="LeftSidebar" />

				<ToggleShown slotName="Main" />

				<ToggleShown slotName="RightSidebar" />

				<ToggleShown slotName="RightPanel" />

				<ToggleShown slotName="PageLayout" />

			</ToggleBox>

		</Fragment>

	);

};

export default BasicGrid;
```

### Locking the sidebar open

Use the useLeftSidebarFlyoutLock hook to prevent the sidebar flyout from collapsing in some situations, such as when a pop-up menu has been opened inside the sidebar. 

```jsx
/**

 * @jsxRuntime classic

 * @jsx jsx

 */

import { useCallback, useState } from 'react';



// eslint-disable-next-line @atlaskit/ui-styling-standard/use-compiled -- Ignored via go/DSP-18766

import { jsx } from '@emotion/react';



import { IconButton } from '@atlaskit/button/new';

import ShowMoreHorizontalIcon from '@atlaskit/icon/glyph/more';

import { ButtonItem, LinkItem, PopupMenuGroup, Section } from '@atlaskit/menu';

import {

	Content,

	LeftSidebar,

	Main,

	PageLayout,

	RightSidebar,

	useLeftSidebarFlyoutLock,

} from '@atlaskit/page-layout';

import Popup from '@atlaskit/popup';

import {

	Header,

	NavigationHeader,

	NestableNavigationContent,

	SideNavigation,

} from '@atlaskit/side-navigation';



import { SlotLabel } from '../common';



const PopupMenu = ({ closePopupMenu }: { closePopupMenu: () => void }) => {

	useLeftSidebarFlyoutLock();

	return (

		<PopupMenuGroup>

			<Section title="Starred">

				<ButtonItem onClick={closePopupMenu}>Navigation System</ButtonItem>

			</Section>

			<Section hasSeparator>

				<ButtonItem onClick={closePopupMenu}>Create project</ButtonItem>

			</Section>

		</PopupMenuGroup>

	);

};



const Menu = () => {

	const [isOpen, setIsOpen] = useState(false);



	const closePopupMenu = useCallback(() => {

		setIsOpen(false);

	}, [setIsOpen]);



	return (

		<Popup

			shouldRenderToParent

			placement="bottom-start"

			isOpen={isOpen}

			onClose={() => setIsOpen(false)}

			content={() => <PopupMenu closePopupMenu={closePopupMenu} />}

			trigger={(triggerProps) => (

				<IconButton

					{...triggerProps}

					testId="popup-trigger"

					isSelected={isOpen}

					onClick={(e) => {

						e.stopPropagation();

						setIsOpen(!isOpen);

					}}

					icon={ShowMoreHorizontalIcon}

					label="more"

				/>

			)}

		/>

	);

};



const App = () => {

	return (

		<PageLayout>

			<Content>

				<LeftSidebar width={450} testId="left-sidebar">

					<SideNavigation label="Project navigation" testId="side-navigation">

						<NavigationHeader>

							<Header description="Sidebar header description">Sidebar Header</Header>

						</NavigationHeader>

						<NestableNavigationContent initialStack={[]}>

							<Section>

								<LinkItem iconAfter={<Menu />} href="http://www.atlassian.com">

									Atlassian

								</LinkItem>

							</Section>

						</NestableNavigationContent>

					</SideNavigation>

				</LeftSidebar>

				<Main>

					<SlotLabel>Main Content</SlotLabel>

				</Main>

				<RightSidebar testId="right-sidebar">

					<SideNavigation label="Aside">

						<NavigationHeader>

							<Header>Hello world</Header>

						</NavigationHeader>

					</SideNavigation>

				</RightSidebar>

			</Content>

		</PageLayout>

	);

};



export default App;
```

### Left sidebar without resize

If you need a left sidebar slot without any resize functionality, use the lighter-weight LeftSidebarWithoutResize component instead of the LeftSidebar component. 

### Programatically toggling with a keyboard shortcut

A common pattern with our LeftSidebar is to show, hide, and/or toggle the state based on a keyboard shortcut or some external input. For this, we provide utilities that control sidebar state using React Context. These are the supported options exposed via context: The context is only available within the LeftSidebar component, so ensure your logic exists as a child for these to be available, example: 

```jsx
/**

 * @jsxRuntime classic

 * @jsx jsx

 */

import { useEffect } from 'react';



import { bind } from 'bind-event-listener';



import { usePageLayoutResize } from '@atlaskit/page-layout';



export const ExpandLeftSidebarKeyboardShortcut = () => {

	const { toggleLeftSidebar } = usePageLayoutResize();



	useEffect(() => {

		const toggle = (event: KeyboardEvent) => {

			if (event.which === 219) {

				toggleLeftSidebar();

			}

		};



		return bind(document, {

			type: 'keydown',

			listener: toggle,

		});

	}, [toggleLeftSidebar]);



	return null;

};
```

```jsx
/**

 * @jsxRuntime classic

 * @jsx jsx

 */

// eslint-disable-next-line @atlaskit/ui-styling-standard/use-compiled -- Ignored via go/DSP-18766

import { jsx } from '@emotion/react';



import { Content, LeftSidebar, Main, PageLayout } from '@atlaskit/page-layout';

import { Header, NavigationHeader, SideNavigation } from '@atlaskit/side-navigation';



import { ExpandLeftSidebarKeyboardShortcut, SlotLabel } from '../common';



export default () => {

	return (

		<PageLayout>

			<Content>

				<LeftSidebar width={450} testId="left-sidebar">

					<ExpandLeftSidebarKeyboardShortcut />



					<SideNavigation label="Project navigation" testId="side-navigation">

						<NavigationHeader>

							<Header description="Sidebar header description">Sidebar Header</Header>

						</NavigationHeader>

					</SideNavigation>

				</LeftSidebar>



				<Main>

					<SlotLabel>Main Content</SlotLabel>

				</Main>

			</Content>

		</PageLayout>

	);

};
```

## Skip links

Skip links are hidden links that appear on focus and allow people to skip content on the page. We recommend implementing skip links for pages with complex navigation layouts as they allow people navigating by keyboard to skip to different sections of the page. Page layout automatically generates a global skip link menu based on the sections included inside PageLayout. To add a section to the skip link menu, give it an ID to allow focus to be placed on the element, and a skipLinkTitle for the text used to describe the section. Screen readers will read the skipLinkTitle with the text 'skip to' prepended for context. 

### Behavior

The skip links menu: To modify the "Skip to:" text, set the skipLinksLabel prop in PageLayout. On first tab into the example below, you should see the skip link menu appear: 

```jsx
/**

 * @jsxRuntime classic

 * @jsx jsx

 */



// eslint-disable-next-line @atlaskit/ui-styling-standard/use-compiled -- Ignored via go/DSP-18766

import { jsx } from '@emotion/react';



import {

	Banner,

	Content,

	LeftSidebarWithoutResize,

	Main,

	PageLayout,

	RightPanel,

	TopNavigation,

} from '@atlaskit/page-layout';

import { token } from '@atlaskit/tokens';



import { SlotLabel, SlotWrapper } from '../common';



const BasicGrid = () => {

	return (

		<PageLayout>

			{

				<Banner testId="banner" id="banner" skipLinkTitle="Banner" height={60} isFixed={false}>

					<SlotWrapper borderColor={token('color.border.accent.yellow')}>

						<SlotLabel>Banner</SlotLabel>

					</SlotWrapper>

				</Banner>

			}

			{

				<TopNavigation

					testId="topNavigation"

					id="product-navigation"

					skipLinkTitle="Product Navigation"

					height={60}

					isFixed={false}

				>

					<SlotWrapper borderColor={token('color.border.accent.blue')}>

						<SlotLabel>Product Navigation</SlotLabel>

					</SlotWrapper>

				</TopNavigation>

			}

			<Content testId="content">

				{

					<LeftSidebarWithoutResize

						testId="leftSidebar"

						id="space-navigation"

						skipLinkTitle="Project Navigation"

						isFixed={false}

						width={125}

					>

						<SlotWrapper borderColor={token('color.border.accent.green')} hasExtraPadding>

							<SlotLabel isSmall>Space Navigation</SlotLabel>

						</SlotWrapper>

					</LeftSidebarWithoutResize>

				}

				{

					<Main testId="main" id="main" skipLinkTitle="Main Content">

						<SlotWrapper borderColor={token('color.border')} minHeight={400}>

							<SlotLabel isSmall>Main Content</SlotLabel>

							<p>Visit the first focusable element on the page to see the skip links menu</p>

						</SlotWrapper>

					</Main>

				}

			</Content>

			{

				<RightPanel

					testId="rightPanel"

					id="help-panel"

					skipLinkTitle="Help Panel"

					isFixed={false}

					width={125}

				>

					<SlotWrapper borderColor={token('color.border.accent.orange')}>

						<SlotLabel>Help Panel</SlotLabel>

					</SlotWrapper>

				</RightPanel>

			}

		</PageLayout>

	);

};



export default BasicGrid;
```

### Custom skip links

Sometimes it may be necessary to add a skip link to a section of the page which is not one of the slots provided by PageLayout. This is where the useCustomSkipLink hook comes in handy. Here's an example of using the useCustomSkipLink to set up skip links to elements that are not direct children of a PageLayout slot. You can choose the position the link will show up in the menu by using the optional listIndex prop. Positions are zero-indexed. Note: Although useCustomSkipLink can link to DOM elements outside of PageLayout using the HTML id, it needs to be called from within PageLayout, since it relies on the context provider that wraps PageLayout. 

```jsx
/**

 * @jsxRuntime classic

 * @jsx jsx

 */



import { useState } from 'react';



// eslint-disable-next-line @atlaskit/ui-styling-standard/use-compiled -- Ignored via go/DSP-18766

import { jsx } from '@emotion/react';



import {

	Banner,

	Content,

	LeftSidebarWithoutResize,

	Main,

	PageLayout,

	RightPanel,

	TopNavigation,

	useCustomSkipLink,

} from '@atlaskit/page-layout';

import { token } from '@atlaskit/tokens';



import { SlotLabel, SlotWrapper } from '../common';



const baseId = 'list-example';

const ListExample = () => {

	const skipLinkCount = document.querySelectorAll('[data-skip-link-wrapper] a').length;

	const [id, setId] = useState(baseId);

	const [position, setPosition] = useState(2);

	useCustomSkipLink(id, 'List example', position);



	const moveDown = () => {

		setPosition((pos) => Math.min(pos + 1, skipLinkCount));

	};

	const moveUp = () => {

		setPosition((pos) => Math.max(pos - 1, 0));

	};

	const changeId = () => {

		setId(`${baseId}${Date.now()}`);

	};



	return (

		<ol id={id}>

			<li>

				This list is an example of an element that you can skipped to that is <em>nested inside</em>{' '}

				the PageLayout component using the useCustomSkipLink hook.

			</li>

			<li>

				Current position of <i>List example</i> skip link: <b>{position}</b>

				<button onClick={moveUp} type="button">

					Move up

				</button>

				<button onClick={moveDown} type="button">

					Move down

				</button>

			</li>

			<li>

				Current id: <b>{id}</b>

				<button onClick={changeId} type="button">

					Update the id of this section

				</button>

			</li>

		</ol>

	);

};



// Registering custom skip links

// whose targets live outside PageLayout

const RegisterCustomSkipLinks = () => {

	useCustomSkipLink('external-footer', 'External Footer', 7);

	useCustomSkipLink('intro-section', 'Intro section', 0);



	return null;

};



const BasicGrid = () => {

	return (

		<div>

			<section id="intro-section">

				<p>

					This section isn't part of PageLayout, but you can still use skip links to jump to it with

					the `useCustomSkipLink` hook that is exported from PageLayout.

				</p>

			</section>

			<PageLayout>

				<RegisterCustomSkipLinks />

				<Banner testId="banner" id="banner" skipLinkTitle="Banner" height={60} isFixed={false}>

					<SlotWrapper borderColor={token('color.border.accent.yellow')}>

						<SlotLabel>Banner</SlotLabel>

					</SlotWrapper>

				</Banner>

				<TopNavigation

					testId="topNavigation"

					id="product-navigation"

					skipLinkTitle="Product Navigation"

					height={60}

					isFixed={false}

				>

					<SlotWrapper borderColor={token('color.border.accent.blue')}>

						<SlotLabel>Product Navigation</SlotLabel>

					</SlotWrapper>

				</TopNavigation>

				<Content testId="content">

					<LeftSidebarWithoutResize

						testId="leftSidebar"

						id="space-navigation"

						skipLinkTitle="Project Navigation"

						isFixed={false}

						width={125}

					>

						<SlotWrapper borderColor={token('color.border.accent.green')} hasExtraPadding>

							<SlotLabel isSmall>Space Navigation</SlotLabel>

						</SlotWrapper>

					</LeftSidebarWithoutResize>

					<Main testId="main" id="main" skipLinkTitle="Main Content">

						<SlotWrapper borderColor={token('color.border')} minHeight={400}>

							<SlotLabel isSmall>Main Content</SlotLabel>

							<p>Visit the first focusable element on the page to see the skip links menu</p>

							<ListExample />

						</SlotWrapper>

					</Main>

				</Content>

				<RightPanel

					testId="rightPanel"

					id="help-panel"

					skipLinkTitle="Help Panel"

					isFixed={false}

					width={125}

				>

					<SlotWrapper borderColor={token('color.border.accent.orange')}>

						<SlotLabel>Help Panel</SlotLabel>

						<p>It's also possible to</p>

					</SlotWrapper>

				</RightPanel>

			</PageLayout>

			<footer id="external-footer">

				This footer isn't part of PageLayout, but you can still use skip links to jump to it with

				the `useCustomSkipLink` hook that is exported from PageLayout.

			</footer>

		</div>

	);

};



export default BasicGrid;
```

## Server side rendering

Here is an example of a server-rendered page. 

```jsx
/**

 * @jsxRuntime classic

 * @jsx jsx

 */

import { Fragment, useCallback, useState } from 'react';



// eslint-disable-next-line @atlaskit/ui-styling-standard/use-compiled -- Ignored via go/DSP-18766

import { css, jsx } from '@emotion/react';



import {

	Banner,

	BANNER_HEIGHT,

	Content,

	LEFT_PANEL_WIDTH,

	LEFT_SIDEBAR_WIDTH,

	LeftPanel,

	LeftSidebar,

	Main,

	PageLayout,

	RIGHT_PANEL_WIDTH,

	RIGHT_SIDEBAR_WIDTH,

	RightPanel,

	RightSidebar,

	TOP_NAVIGATION_HEIGHT,

	TopNavigation,

} from '@atlaskit/page-layout';

import { token } from '@atlaskit/tokens';



import { ScrollableContent, SlotLabel, SlotWrapper, Toggle, ToggleBox } from '../common';



type SlotName =

	| 'Banner'

	| 'TopNavigation'

	| 'LeftPanel'

	| 'LeftSidebar'

	| 'Main'

	| 'RightSidebar'

	| 'RightPanel';



const serverRenderedStyles = css({

	height: 'auto',

	position: 'absolute',

	backgroundColor: token('color.background.neutral.subtle'),

	insetBlockEnd: 0,

	// eslint-disable-next-line @atlaskit/ui-styling-standard/no-imported-style-values, @atlaskit/ui-styling-standard/no-unsafe-values -- Ignored via go/DSP-18766

	insetBlockStart: `calc(${TOP_NAVIGATION_HEIGHT} + ${BANNER_HEIGHT})`,

	// eslint-disable-next-line @atlaskit/ui-styling-standard/no-imported-style-values, @atlaskit/ui-styling-standard/no-unsafe-values -- Ignored via go/DSP-18766

	insetInlineEnd: `calc(${RIGHT_PANEL_WIDTH} + ${RIGHT_SIDEBAR_WIDTH})`,

	// eslint-disable-next-line @atlaskit/ui-styling-standard/no-imported-style-values, @atlaskit/ui-styling-standard/no-unsafe-values -- Ignored via go/DSP-18766

	insetInlineStart: `calc(${LEFT_PANEL_WIDTH} + ${LEFT_SIDEBAR_WIDTH})`,

	transition: 'left 300ms',

});



const draggingStyles = css({

	// eslint-disable-next-line @atlaskit/design-system/no-nested-styles, @atlaskit/ui-styling-standard/no-nested-selectors, @atlaskit/ui-styling-standard/no-unsafe-values -- Ignored via go/DSP-18766

	[`[data-is-sidebar-dragging] &`]: {

		transition: 'none',

	},

});



const ServerRenderedPage = () => {

	return (

		<SlotWrapper borderColor={token('color.border')} css={[serverRenderedStyles, draggingStyles]}>

			Server rendered page. Added as a sibling to Grid componenet

		</SlotWrapper>

	);

};



const initialState = {

	isBannerShown: true,

	isTopNavigationShown: true,

	isLeftPanelShown: true,

	isLeftSidebarShown: true,

	isRightSidebarShown: true,

	isRightPanelShown: true,

	isBannerFixed: false,

	isTopNavigationFixed: false,

	isLeftPanelFixed: false,

	isLeftPanelScrollable: false,

	isLeftSidebarFixed: false,

	isLeftSidebarScrollable: false,

	isRightSidebarFixed: false,

	isRightSidebarScrollable: false,

	isRightPanelFixed: false,

	isRightPanelScrollable: false,

};



const BasicGrid = () => {

	const [gridState, setGridState] = useState(initialState);



	const ToggleFixed = useCallback(

		({ slotName }: { slotName: SlotName }) => {

			const gridKey = `is${slotName}Fixed` as keyof typeof gridState;

			return (

				<Toggle

					id={`${slotName}--fixed`}

					isChecked={gridState[gridKey]}

					onChange={() => setGridState({ ...gridState, [gridKey]: !gridState[gridKey] })}

				>

					Toggle fixed

				</Toggle>

			);

		},

		[gridState],

	);



	const ToggleScrollable = useCallback(

		({ slotName }: { slotName: SlotName }) => {

			const gridKey = `is${slotName}Scrollable` as keyof typeof gridState;

			return (

				<Fragment>

					<Toggle

						id={`${slotName}--scrollable`}

						isChecked={gridState[gridKey]}

						onChange={() => setGridState({ ...gridState, [gridKey]: !gridState[gridKey] })}

					>

						Toggle scrollable content

					</Toggle>

					{gridState[gridKey] && <ScrollableContent />}

				</Fragment>

			);

		},

		[gridState],

	);



	const ToggleShown = useCallback(

		({ slotName }: { slotName: SlotName }) => {

			const gridKey = `is${slotName}Shown` as keyof typeof gridState;

			return (

				<Toggle

					id={`${slotName}--shown`}

					onChange={() => setGridState({ ...gridState, [gridKey]: !gridState[gridKey] })}

					isChecked={!gridState[gridKey]}

				>{`${gridState[gridKey] ? 'Hide' : 'Show'} ${slotName}`}</Toggle>

			);

		},

		[gridState],

	);



	return (

		<Fragment>

			<PageLayout>

				{gridState.isBannerShown && (

					<Banner isFixed={gridState.isBannerFixed}>

						<SlotWrapper borderColor={token('color.border.accent.yellow')}>

							<SlotLabel>Banner</SlotLabel>

							<ToggleFixed slotName="Banner" />

						</SlotWrapper>

					</Banner>

				)}

				{gridState.isTopNavigationShown && (

					<TopNavigation isFixed={gridState.isTopNavigationFixed}>

						<SlotWrapper borderColor={token('color.border.accent.blue')}>

							<SlotLabel>TopNavigation</SlotLabel>

							<ToggleFixed slotName="TopNavigation" />

						</SlotWrapper>

					</TopNavigation>

				)}

				{gridState.isLeftPanelShown && (

					<LeftPanel isFixed={gridState.isLeftPanelFixed}>

						<SlotWrapper borderColor={token('color.border.accent.orange')}>

							<SlotLabel>LeftPanel</SlotLabel>

							<ToggleFixed slotName="LeftPanel" />

							<ToggleScrollable slotName="LeftPanel" />

						</SlotWrapper>

					</LeftPanel>

				)}

				<Content>

					{gridState.isLeftSidebarShown && (

						<LeftSidebar isFixed={gridState.isLeftSidebarFixed}>

							<SlotWrapper borderColor={token('color.border.accent.green')}>

								<SlotLabel>LeftSidebar</SlotLabel>

								<ToggleFixed slotName="LeftSidebar" />

								<ToggleScrollable slotName="LeftSidebar" />

							</SlotWrapper>

						</LeftSidebar>

					)}

					<Main>{''}</Main>

					{gridState.isRightSidebarShown && (

						<RightSidebar isFixed={gridState.isRightSidebarFixed} width={200}>

							<SlotWrapper borderColor={token('color.border.accent.green')}>

								<SlotLabel>RightSidebar</SlotLabel>

								<ToggleFixed slotName="RightSidebar" />

								<ToggleScrollable slotName="RightSidebar" />

							</SlotWrapper>

						</RightSidebar>

					)}

				</Content>

				{gridState.isRightPanelShown && (

					<RightPanel isFixed={gridState.isRightPanelFixed} width={200}>

						<SlotWrapper borderColor={token('color.border.accent.orange')}>

							<SlotLabel>RightPanel</SlotLabel>

							<ToggleFixed slotName="RightPanel" />

							<ToggleScrollable slotName="RightPanel" />

						</SlotWrapper>

					</RightPanel>

				)}

				<ToggleBox>

					<ToggleShown slotName="Banner" />

					<ToggleShown slotName="TopNavigation" />

					<ToggleShown slotName="LeftPanel" />

					<ToggleShown slotName="LeftSidebar" />

					<ToggleShown slotName="RightSidebar" />

					<ToggleShown slotName="RightPanel" />

				</ToggleBox>

			</PageLayout>

			<ServerRenderedPage />

		</Fragment>

	);

};



export default BasicGrid;
```

## Using CSS variables

@atlaskit/page-layout exports a set of variables that can be used to setup the grid on non-react pages. The following variables are exported: Always use these variables instead of accessing the CSS variable names directly because these variables have sensible fallback values baked into them. Accessing the variables directly runs the risk of setting the intended styles to "unset" which can cause unintended styling issues. See the server rendered example for a more complete example of how to use these variables. 

---

[View Original Documentation](https://atlassian.design/components/page-layout/examples)
