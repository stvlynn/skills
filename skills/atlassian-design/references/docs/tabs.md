# Tabs

Tabs are used to organize content by grouping similar information on the same page.

---

## Default

The default form of tabs. 

```jsx
/**

 * @jsxRuntime classic

 * @jsx jsx

 */

import { type ReactNode } from 'react';



import { css, jsx } from '@compiled/react';



import Tabs, { Tab, TabList, TabPanel } from '@atlaskit/tabs';

import { token } from '@atlaskit/tokens';



const panelStyles = css({

	display: 'flex',

	alignItems: 'center',

	justifyContent: 'center',

	flexDirection: 'column',

	flexGrow: 1,

	backgroundColor: token('color.background.neutral'),

	borderRadius: '3px',

	color: token('color.text.subtlest'),

	font: token('font.heading.xxlarge'),

	marginBlockEnd: token('space.100'),

	marginBlockStart: token('space.200'),

	paddingBlockEnd: token('space.400'),

	paddingBlockStart: token('space.400'),

	paddingInlineEnd: token('space.400'),

	paddingInlineStart: token('space.400'),

});



export const Panel = ({ children, testId }: { children: ReactNode; testId?: string }) => (

	<div css={panelStyles} data-testid={testId}>

		{children}

	</div>

);



export default function TabsDefaultExample() {

	return (

		<Tabs onChange={(index) => console.log('Selected Tab', index + 1)} id="default">

			<TabList>

				<Tab>Tab 1</Tab>

				<Tab>Tab 2</Tab>

				<Tab>Tab 3</Tab>

			</TabList>

			<TabPanel>

				<Panel>This is the content area of the first tab.</Panel>

			</TabPanel>

			<TabPanel>

				<Panel>This is the content area of the second tab.</Panel>

			</TabPanel>

			<TabPanel>

				<Panel>This is the content area of the third tab.</Panel>

			</TabPanel>

		</Tabs>

	);

}
```

## Controlled

Tabs can be used as a controlled component. 

```jsx
/**

 * @jsxRuntime classic

 * @jsx jsx

 */

import { type ReactNode, useCallback, useState } from 'react';



import { css, jsx } from '@compiled/react';



import Button from '@atlaskit/button/new';

import { Box } from '@atlaskit/primitives/compiled';

import Tabs, { Tab, TabList, TabPanel } from '@atlaskit/tabs';

import { type SelectedType } from '@atlaskit/tabs/types';

import { token } from '@atlaskit/tokens';



const panelStyles = css({

	display: 'flex',

	alignItems: 'center',

	justifyContent: 'center',

	flexDirection: 'column',

	flexGrow: 1,

	backgroundColor: token('color.background.neutral'),

	borderRadius: '3px',

	color: token('color.text.subtlest'),

	font: token('font.heading.xxlarge'),

	marginBlockEnd: token('space.100'),

	marginBlockStart: token('space.200'),

	paddingBlockEnd: token('space.400'),

	paddingBlockStart: token('space.400'),

	paddingInlineEnd: token('space.400'),

	paddingInlineStart: token('space.400'),

});



export const Panel = ({ children, testId }: { children: ReactNode; testId?: string }) => (

	<div css={panelStyles} data-testid={testId}>

		{children}

	</div>

);



export default function TabsControlledExample() {

	const [selected, setSelected] = useState(0);



	const handleUpdate = useCallback((index: SelectedType) => setSelected(index), [setSelected]);



	return (

		<Box>

			<Tabs onChange={handleUpdate} selected={selected} id="controlled">

				<TabList>

					<Tab>Tab 1</Tab>

					<Tab>Tab 2</Tab>

					<Tab>Tab 3</Tab>

				</TabList>

				<TabPanel>

					<Panel>This is the content area of the first tab.</Panel>

				</TabPanel>

				<TabPanel>

					<Panel>This is the content area of the second tab.</Panel>

				</TabPanel>

				<TabPanel>

					<Panel>This is the content area of the third tab.</Panel>

				</TabPanel>

			</Tabs>

			<Button isDisabled={selected === 2} onClick={() => handleUpdate(2)}>

				Select the last tab

			</Button>

		</Box>

	);

}
```

## Customizing tab

### Wrapping tab

You can wrap a tab in other presentational components. In this example we have added a tooltip to each tab. 

```jsx
/**

 * @jsxRuntime classic

 * @jsx jsx

 */

import { type ReactNode } from 'react';



import { css, jsx } from '@compiled/react';



import Tabs, { Tab, TabList, TabPanel } from '@atlaskit/tabs';

import { token } from '@atlaskit/tokens';

import Tooltip from '@atlaskit/tooltip';



const panelStyles = css({

	display: 'flex',

	alignItems: 'center',

	justifyContent: 'center',

	flexDirection: 'column',

	flexGrow: 1,

	backgroundColor: token('color.background.neutral'),

	borderRadius: '3px',

	color: token('color.text.subtlest'),

	font: token('font.heading.xxlarge'),

	marginBlockEnd: token('space.100'),

	marginBlockStart: token('space.200'),

	paddingBlockEnd: token('space.400'),

	paddingBlockStart: token('space.400'),

	paddingInlineEnd: token('space.400'),

	paddingInlineStart: token('space.400'),

});



export const Panel = ({ children }: { children: ReactNode }) => (

	<div css={panelStyles}>{children}</div>

);



const TooltipTab = ({ label, tooltip }: { label: string; tooltip: string }) => (

	<Tooltip content={tooltip}>

		<Tab>{label}</Tab>

	</Tooltip>

);



const TabTooltipExample = () => (

	<Tabs id="tooltip-tabs">

		<TabList>

			<TooltipTab label="Tab 1" tooltip="Tooltip for tab 1" />

			<TooltipTab label="Tab 2" tooltip="Tooltip for tab 2" />

			<TooltipTab label="Tab 3" tooltip="Tooltip for tab 3" />

		</TabList>

		<TabPanel>

			<Panel>This is the content area of the first tab.</Panel>

		</TabPanel>

		<TabPanel>

			<Panel>This is the content area of the second tab.</Panel>

		</TabPanel>

		<TabPanel>

			<Panel>This is the content area of the third tab.</Panel>

		</TabPanel>

	</Tabs>

);



export default TabTooltipExample;
```

### Custom tab

To customize a tab, call useTab and spread those attributes onto the custom tab. 

```jsx
/**

 * @jsxRuntime classic

 * @jsx jsx

 */

import { type ReactNode } from 'react';



import { css } from '@compiled/react';



import { cssMap, jsx } from '@atlaskit/css';

import { Box } from '@atlaskit/primitives/compiled';

import Tabs, { TabList, TabPanel, useTab } from '@atlaskit/tabs';

import { token } from '@atlaskit/tokens';



const styles = cssMap({

	customTab: {

		font: token('font.body.small'),

	},

});



const panelStyles = css({

	display: 'flex',

	alignItems: 'center',

	justifyContent: 'center',

	flexDirection: 'column',

	flexGrow: 1,

	backgroundColor: token('color.background.neutral'),

	borderRadius: '3px',

	color: token('color.text.subtlest'),

	font: token('font.heading.xxlarge'),

	marginBlockEnd: token('space.100'),

	marginBlockStart: token('space.200'),

	paddingBlockEnd: token('space.400'),

	paddingBlockStart: token('space.400'),

	paddingInlineEnd: token('space.400'),

	paddingInlineStart: token('space.400'),

});



export const Panel = ({ children }: { children: ReactNode }) => (

	<div css={panelStyles}>{children}</div>

);



const CustomTab = ({ label }: { label: string }) => {

	const tabAttributes = useTab();



	return (

		<Box xcss={styles.customTab} {...tabAttributes}>

			{label}

		</Box>

	);

};



const TabCustomExample = () => (

	<Tabs id="custom-tabs">

		<TabList>

			<CustomTab label="Tab 1" />

			<CustomTab label="Tab 2" />

			<CustomTab label="Tab 3" />

		</TabList>

		<TabPanel>

			<Panel>This is the content area of the first tab.</Panel>

		</TabPanel>

		<TabPanel>

			<Panel>This is the content area of the second tab.</Panel>

		</TabPanel>

		<TabPanel>

			<Panel>This is the content area of the third tab.</Panel>

		</TabPanel>

	</Tabs>

);



export default TabCustomExample;
```

## Customizing tab panel

To customize a tab panel, call useTabPanel and spread those attributes onto the custom tab panel. Body of tab one 

```jsx
/**

 * @jsxRuntime classic

 * @jsx jsx

 */



import { css, jsx } from '@compiled/react';



import { Box } from '@atlaskit/primitives/compiled';

import Tabs, { Tab, TabList, useTabPanel } from '@atlaskit/tabs';

import { token } from '@atlaskit/tokens';



const customPanelStyles = css({

	display: 'flex',

	alignItems: 'center',

	justifyContent: 'center',

	flexDirection: 'column',

	flexGrow: 1,

	backgroundColor: token('color.background.neutral'),

	borderRadius: '3px',

	color: token('color.text.subtlest'),

	font: token('font.heading.xxlarge'),

	marginBlockEnd: token('space.100'),

	marginBlockStart: token('space.200'),

	paddingBlockEnd: token('space.400'),

	paddingBlockStart: token('space.400'),

	paddingInlineEnd: token('space.400'),

	paddingInlineStart: token('space.400'),

	// eslint-disable-next-line @atlaskit/design-system/no-nested-styles, @atlaskit/ui-styling-standard/no-nested-selectors, @atlaskit/ui-styling-standard/no-unsafe-selectors -- Ignored via go/DSP-18766

	'&&': {

		paddingBlockEnd: token('space.400'),

		paddingBlockStart: token('space.400'),

		paddingInlineEnd: token('space.400'),

		paddingInlineStart: token('space.400'),

	},

});



const CustomTabPanel = ({ heading, body }: { heading: string; body: string }) => {

	const tabPanelAttributes = useTabPanel();



	return (

		<div css={customPanelStyles} {...tabPanelAttributes}>

			<Box as="span">{heading}</Box>

			<p>{body}</p>

		</div>

	);

};



const TabPanelCustomExample = () => (

	<Tabs id="custom-panel">

		<TabList>

			<Tab>Tab 1</Tab>

			<Tab>Tab 2</Tab>

			<Tab>Tab 3</Tab>

		</TabList>

		<CustomTabPanel heading="One" body="Body of tab one" />

		<CustomTabPanel heading="Two" body="Body of tab two" />

		<CustomTabPanel heading="Three" body="Body of tab three" />

	</Tabs>

);



export default TabPanelCustomExample;
```

---

[View Original Documentation](https://atlassian.design/components/tabs/examples)
