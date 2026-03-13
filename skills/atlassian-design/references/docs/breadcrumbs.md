# Breadcrumbs

Breadcrumbs are a navigation system used to show a user's location in a site or app.

---

## Default

The default form of breadcrumbs. 

```jsx
import React from 'react';



import Breadcrumbs, { BreadcrumbsItem } from '@atlaskit/breadcrumbs';



const BreadcrumbsDefaultExample = () => {

	return (

		<Breadcrumbs>

			<BreadcrumbsItem href="/item" text="Item 1" />

			<BreadcrumbsItem href="/item" text="Item 2" />

			<BreadcrumbsItem href="/item" text="Item 3" />

			<BreadcrumbsItem href="/item" text="Item 4" />

			<BreadcrumbsItem href="/item" text="Item 5" />

			<BreadcrumbsItem href="/item" text="Item 6" />

			<BreadcrumbsItem href="/item" text="Item 7" />

			<BreadcrumbsItem href="/item" text="Item 8" />

		</Breadcrumbs>

	);

};



export default BreadcrumbsDefaultExample;
```

## Long breadcrumbs

When a breadcrumb contains more than eight items, the breadcrumb auto-collapses and uses ellipses to indicate more information. The first and last items are shown by default. Users expand the breadcrumb by selecting the ellipsis. 

```jsx
import React from 'react';



import Breadcrumbs, { BreadcrumbsItem } from '@atlaskit/breadcrumbs';



const BreadcrumbsLongExample = () => {

	return (

		<Breadcrumbs>

			<BreadcrumbsItem href="/item" text="Item 1" />

			<BreadcrumbsItem href="/item" text="Item 2" />

			<BreadcrumbsItem href="/item" text="Item 3" />

			<BreadcrumbsItem href="/item" text="Item 4" />

			<BreadcrumbsItem href="/item" text="Item 5" />

			<BreadcrumbsItem href="/item" text="Item 6" />

			<BreadcrumbsItem href="/item" text="Item 7" />

			<BreadcrumbsItem href="/item" text="Item 8" />

			<BreadcrumbsItem href="/item" text="Item 9" />

			<BreadcrumbsItem href="/item" text="Item 10" />

		</Breadcrumbs>

	);

};



export default BreadcrumbsLongExample;
```

## Max items

You can customise the maximum number of breadcrumbs using the maxItems prop. When there are more than the maximum number of nested links, the breadcrumb auto-collapses with an ellipses in between the items. Select the ellipses to reveal the hidden items. 

```jsx
import React from 'react';



import Breadcrumbs, { BreadcrumbsItem } from '@atlaskit/breadcrumbs';



const BreadcrumbsMaxItemsExample = () => {

	return (

		<Breadcrumbs maxItems={3}>

			<BreadcrumbsItem href="/item" text="Item 1" />

			<BreadcrumbsItem href="/item" text="Item 2" />

			<BreadcrumbsItem href="/item" text="Item 3" />

			<BreadcrumbsItem href="/item" text="Item 4" />

			<BreadcrumbsItem href="/item" text="Item 5" />

			<BreadcrumbsItem href="/item" text="Item 6" />

		</Breadcrumbs>

	);

};



export default BreadcrumbsMaxItemsExample;
```

## Expanded overflow

When expanded, breadcrumbs that exceed the page width will overflow to the next line. 

```jsx
import React from 'react';



import Breadcrumbs, { BreadcrumbsItem } from '@atlaskit/breadcrumbs';



const BreadcrumbsExpandedExample = () => {

	return (

		<div

			style={{

				// eslint-disable-next-line @atlaskit/ui-styling-standard/enforce-style-prop -- Ignored via go/DSP-18766

				maxWidth: '500px',

			}}

		>

			<Breadcrumbs maxItems={5}>

				<BreadcrumbsItem href="/item" text="Item" />

				<BreadcrumbsItem href="/item" text="Another item" />

				<BreadcrumbsItem href="/item" text="A third item" />

				<BreadcrumbsItem href="/item" text="A fourth item with a very long name" />

				<BreadcrumbsItem href="/item" text="Item 5" />

				<BreadcrumbsItem href="/item" text="A sixth item" />

			</Breadcrumbs>

		</div>

	);

};



export default BreadcrumbsExpandedExample;
```

## Items before or after collapse

The number of items shown before or after auto-collapse can be customized. This is useful when people need more information on the breadcrumb hierarchy to be aware of their location within the product. To reduce screen clutter, it's recommended to only display the first and last items when collapsing. 

```jsx
import React from 'react';



import Breadcrumbs, { BreadcrumbsItem } from '@atlaskit/breadcrumbs';

import { Box } from '@atlaskit/primitives';



const BreadcrumbsBeforeAfterCollapseExample = () => {

	return (

		<Box>

			<Breadcrumbs itemsBeforeCollapse={3} itemsAfterCollapse={2}>

				<BreadcrumbsItem href="/item" text="Item 1" />

				<BreadcrumbsItem href="/item" text="Item 2" />

				<BreadcrumbsItem href="/item" text="Item 3" />

				<BreadcrumbsItem href="/item" text="Item 4" />

				<BreadcrumbsItem href="/item" text="Item 5" />

				<BreadcrumbsItem href="/item" text="Item 6" />

				<BreadcrumbsItem href="/item" text="Item 7" />

				<BreadcrumbsItem href="/item" text="Item 8" />

				<BreadcrumbsItem href="/item" text="Item 9" />

				<BreadcrumbsItem href="/item" text="Item 10" />

			</Breadcrumbs>

		</Box>

	);

};



export default BreadcrumbsBeforeAfterCollapseExample;
```

## Controlled

Set isExpanded to true to expand the breadcrumbs. Use the onExpand prop to expand the breadcrumbs, when a user interacts with the ellipsis button. 

```jsx
import React, { useState } from 'react';



import Breadcrumbs, { BreadcrumbsItem } from '@atlaskit/breadcrumbs';

import Button from '@atlaskit/button/new';

import { Box } from '@atlaskit/primitives';



const BreadcrumbsControlledExample = () => {

	const [isExpanded, setExpanse] = useState(false);

	return (

		<Box>

			<Breadcrumbs isExpanded={isExpanded} onExpand={() => setExpanse(!isExpanded)}>

				<BreadcrumbsItem href="/item" text="Item 1" />

				<BreadcrumbsItem href="/item" text="Item 2" />

				<BreadcrumbsItem href="/item" text="Item 3" />

				<BreadcrumbsItem href="/item" text="Item 4" />

				<BreadcrumbsItem href="/item" text="Item 5" />

				<BreadcrumbsItem href="/item" text="Item 6" />

				<BreadcrumbsItem href="/item" text="Item 7" />

				<BreadcrumbsItem href="/item" text="Item 8" />

				<BreadcrumbsItem href="/item" text="Item 9" />

				<BreadcrumbsItem href="/item" text="Item 10" />

			</Breadcrumbs>

			<Button appearance="primary" onClick={() => setExpanse(!isExpanded)}>

				Toggle

			</Button>

		</Box>

	);

};



export default BreadcrumbsControlledExample;
```

## Breadcrumbs with icon

### Icon before

Use iconBefore to display an icon before the breadcrumb. 

```jsx
import React from 'react';



import Breadcrumbs, { BreadcrumbsItem } from '@atlaskit/breadcrumbs';

import { AtlassianIcon } from '@atlaskit/logo';



const TestIcon = <AtlassianIcon label="Test icon" size="small" />;



const BreadcrumbsItemIconBeforeExample = () => {

	return (

		<Breadcrumbs>

			<BreadcrumbsItem iconBefore={TestIcon} text="Atlassian" />

		</Breadcrumbs>

	);

};



export default BreadcrumbsItemIconBeforeExample;
```

### Icon after

Use iconAfter to display an icon after the breadcrumb. 

```jsx
import React from 'react';



import Breadcrumbs, { BreadcrumbsItem } from '@atlaskit/breadcrumbs';

import { AtlassianIcon } from '@atlaskit/logo';



const TestIcon = <AtlassianIcon label="Test icon" size="small" />;



const BreadcrumbsItemIconAfterExample = () => {

	return (

		<Breadcrumbs>

			<BreadcrumbsItem iconAfter={TestIcon} text="Atlassian" />

		</Breadcrumbs>

	);

};



export default BreadcrumbsItemIconAfterExample;
```

## Truncation width

When a truncationWidth is specified, long item names will truncate and a tooltip containing the full item name will appear on hover. If unspecified, truncation only happens when an item cannot fit alone on a line. 

```jsx
import React from 'react';



import Breadcrumbs, { BreadcrumbsItem } from '@atlaskit/breadcrumbs';



const BreadcrumbsItemTruncationExample = () => {

	return (

		<Breadcrumbs>

			<BreadcrumbsItem text="Confluence" />

			<BreadcrumbsItem

				truncationWidth={100}

				text="The new Confluence experience will soon be on for everyone"

			/>

		</Breadcrumbs>

	);

};



export default BreadcrumbsItemTruncationExample;
```

---

[View Original Documentation](https://atlassian.design/components/breadcrumbs/examples)
