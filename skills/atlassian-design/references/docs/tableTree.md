# Table tree

A table tree is an expandable table for showing nested hierarchies of information.

---

## Basic

The table tree component is a table with expandable nested rows. The basic table tree has configurable props for header titles, columns, column widths, and an array of table items (with child items). You can customise the content of each item, but make sure your data matches the expected schema. 

```jsx
import React from 'react';



import { Box } from '@atlaskit/primitives';

import TableTree from '@atlaskit/table-tree';



type Content = { title: string; description: string };



type Item = {

	id: string;

	content: Content;

	hasChildren: boolean;

	children?: Item[];

};



const items: Item[] = [

	{

		id: 'item1',

		content: {

			title: 'Item 1',

			description: 'First top-level item',

		},

		hasChildren: false,

		children: [],

	},

	{

		id: 'item2',

		content: {

			title: 'Item 2',

			description: 'Second top-level item',

		},

		hasChildren: true,

		children: [

			{

				id: 'child2.1',

				content: {

					title: 'Child item',

					description: 'A child item',

				},

				hasChildren: false,

			},

		],

	},

];



const Title = (props: Content) => <Box as="span">{props.title}</Box>;

const Description = (props: Content) => <Box as="span">{props.description}</Box>;



export default () => (

	<TableTree

		columns={[Title, Description]}

		headers={['Title', 'Description']}

		columnWidths={['120px', '300px']}

		items={items}

		label="Basic"

	/>

);
```

## Advanced

For advanced usage, you can compose Cell, Header, Headers, Row, and Rows components. This approach lets you customize the structure of your data. 

```jsx
import React from 'react';



import TableTree, { Cell, Header, Headers, Row, Rows } from '@atlaskit/table-tree';



type Item = {

	id: string;

	title: string;

	description: string;

	children?: Item[];

};



const items = [

	{

		id: 'item1',

		title: 'Item 1',

		description: 'First top-level item',

	},

	{

		id: 'item2',

		title: 'Item 2',

		description: 'Second top-level item',

		children: [

			{

				id: 'child2.1',

				title: 'Child item',

				description: 'A child item',

			},

		],

	},

];



export default () => (

	<TableTree label="Advanced usage">

		<Headers>

			<Header width={120}>Title</Header>

			<Header width={300}>Description</Header>

		</Headers>

		<Rows

			items={items}

			render={({ id, title, description, children = [] }: Item) => (

				<Row itemId={id} items={children} hasChildren={children.length > 0}>

					<Cell>{title}</Cell>

					<Cell>{description}</Cell>

				</Row>

			)}

		/>

	</TableTree>

);
```

## Uncontrolled

In an uncontrolled table, expanding and collapsing each row is handled automatically. Use the isDefaultExpanded prop to change whether a row is expanded by default. 

```jsx
import React from 'react';



import TableTree, { Cell, Header, Headers, Row, Rows } from '@atlaskit/table-tree';



import items from './data';



type Item = {

	title: string;

	numbering: string;

	page: number;

	children?: Item[];

	id: string;

};



export default () => (

	<TableTree label="Automatically controlled row expansion">

		<Headers>

			<Header width={200}>Chapter title</Header>

			<Header width={120}>Numbering</Header>

			<Header width={100}>Page</Header>

		</Headers>

		<Rows

			items={items}

			render={({ title, numbering, page, children = [] }: Item) => (

				<Row

					itemId={numbering}

					items={children}

					hasChildren={children.length > 0}

					isDefaultExpanded

				>

					<Cell singleLine>{title}</Cell>

					<Cell>{numbering}</Cell>

					<Cell>{page}</Cell>

				</Row>

			)}

		/>

	</TableTree>

);
```

## Controlled

Use the isExpanded prop to manually control whether a row is expanded or not. Respond to user interaction by providing callbacks to the onExpand and onCollapse props. 

```jsx
import React, { useState } from 'react';



import TableTree, { Cell, Header, Headers, Row, Rows } from '@atlaskit/table-tree';



import items from './data';



type Item = {

	title: string;

	numbering: string;

	page: number;

	children?: Item[];

	id: string;

};



const defaultExpansionMap: Record<string, boolean> = { '2': true };



export default () => {

	const [expansionMap, setExpansionMap] = useState(defaultExpansionMap);

	return (

		<TableTree label="Manually controlled row expansion">

			<Headers>

				<Header width={200}>Chapter title</Header>

				<Header width={120}>Numbering</Header>

				<Header width={100}>Page</Header>

			</Headers>

			<Rows

				items={items}

				render={({ title, numbering, page, children = [] }: Item) => (

					<Row

						itemId={numbering}

						items={children}

						hasChildren={children.length > 0}

						isExpanded={Boolean(expansionMap[numbering])}

						onExpand={() => setExpansionMap({ ...expansionMap, [numbering]: true })}

						onCollapse={() => setExpansionMap({ ...expansionMap, [numbering]: false })}

					>

						<Cell singleLine>{title}</Cell>

						<Cell>{numbering}</Cell>

						<Cell>{page}</Cell>

					</Row>

				)}

			/>

		</TableTree>

	);

};
```

## Custom children

You can use other components as children instead of additional rows and items. For example, use an empty state when table children don’t exist. We're having trouble connecting to our database. Please check your internet connection and try again. 

```jsx
import React from 'react';



import Button from '@atlaskit/button/new';

import EmptyState from '@atlaskit/empty-state';

import TableTree, { Cell, Header, Headers, Row, Rows } from '@atlaskit/table-tree';



import items from './data';



type Item = {

	title: string;

	numbering: string;

	page: number;

	children?: Item[];

	id: string;

};



export default () => (

	<TableTree label="Custom child component">

		<Headers>

			<Header width={200}>Chapter title</Header>

			<Header width={120}>Numbering</Header>

			<Header width={100}>Page</Header>

		</Headers>

		<Rows

			items={items}

			render={({ title, numbering, page, children = [] }: Item) =>

				numbering === '2.1' ? (

					<EmptyState

						header="Cannot load data"

						description="We're having trouble connecting to our database. Please check your internet connection and try again."

						primaryAction={<Button appearance="primary">Retry</Button>}

					/>

				) : (

					<Row

						itemId={numbering}

						items={children}

						hasChildren={children.length > 0}

						isDefaultExpanded

					>

						<Cell singleLine>{title}</Cell>

						<Cell singleLine>{numbering}</Cell>

						<Cell singleLine>{page}</Cell>

					</Row>

				)

			}

		/>

	</TableTree>

);
```

## Loading states

Each nesting level can be displayed in a loading state. Use this when loading data asynchronously. 

### Root

To display the root level in a loading state, ensure that the items value provided to Rows is undefined. 

```jsx
import React from 'react';



import TableTree, { Header, Headers, Rows } from '@atlaskit/table-tree';



export default () => (

	<TableTree label="Root loading state">

		<Headers>

			<Header width={200}>Chapter title</Header>

			<Header width={120}>Numbering</Header>

			<Header width={100}>Page</Header>

		</Headers>

		<Rows items={undefined} render={() => null} />

	</TableTree>

);
```

### Nested

To display a nested level in a loading state, ensure that the items value provided to the corresponding Row is undefined. 

```jsx
import React from 'react';



import TableTree, { Cell, Header, Headers, Row, Rows } from '@atlaskit/table-tree';



import items from './data';



type Item = {

	title: string;

	numbering: string;

	page: number;

	children?: Item[];

};



export default () => (

	<TableTree label="Nested loading state">

		<Headers>

			<Header width={200}>Chapter title</Header>

			<Header width={120}>Numbering</Header>

			<Header width={100}>Page</Header>

		</Headers>

		<Rows

			items={items}

			render={({ title, numbering, page, children = [] }: Item) => (

				<Row

					itemId={numbering}

					items={undefined}

					hasChildren={children.length > 0}

					isDefaultExpanded

				>

					<Cell singleLine>{title}</Cell>

					<Cell>{numbering}</Cell>

					<Cell>{page}</Cell>

				</Row>

			)}

		/>

	</TableTree>

);
```

## Managing data

You can use the TableTreeDataHelper class to handle the manipulation of table items, like when loading data asynchronously. 

### Append items

The appendItems method will add to the existing items. 

```jsx
import React, { useCallback, useState } from 'react';



import Button from '@atlaskit/button/new';

import { Box } from '@atlaskit/primitives';

import TableTree, {

	Cell,

	Header,

	Headers,

	Row,

	Rows,

	TableTreeDataHelper,

} from '@atlaskit/table-tree';



import { fetchNewItems, getDefaultItems } from './data';



type Item = {

	title: string;

	numbering: string;

	page: number;

	children?: Item[];

	id: string;

};



const tableTreeHelper = new TableTreeDataHelper<Item>({ key: 'numbering' });



const getInitialItems = () => {

	return tableTreeHelper.updateItems(getDefaultItems());

};



export default () => {

	const [items, setItems] = useState<Item[]>(getInitialItems);



	const loadMore = useCallback(() => {

		fetchNewItems().then((newItems) => {

			setItems((items) => tableTreeHelper.appendItems(newItems, items, items[items.length - 1]));

		});

	}, []);



	return (

		<Box>

			<Button onClick={loadMore}>Load more</Button>

			<TableTree label="Appended data">

				<Headers>

					<Header width={200}>Chapter title</Header>

					<Header width={120}>Numbering</Header>

					<Header width={100}>Page</Header>

				</Headers>

				<Rows

					items={items}

					render={({ title, numbering, page, children = [] }) => (

						<Row

							itemId={numbering}

							items={children}

							hasChildren={children.length > 0}

							isDefaultExpanded

						>

							<Cell>{title}</Cell>

							<Cell>{numbering}</Cell>

							<Cell>{page}</Cell>

						</Row>

					)}

				/>

			</TableTree>

		</Box>

	);

};
```

### Update items

The updateItems method will replace the existing items. 

```jsx
import React, { useCallback, useState } from 'react';



import Button from '@atlaskit/button/new';

import { Box } from '@atlaskit/primitives';

import TableTree, {

	Cell,

	Header,

	Headers,

	Row,

	Rows,

	TableTreeDataHelper,

} from '@atlaskit/table-tree';



import { fetchItems, getDefaultItems } from './data';



type Item = {

	title: string;

	numbering: string;

	page: number;

	children?: Item[];

	id: string;

};



const tableTreeHelper = new TableTreeDataHelper<Item>({ key: 'numbering' });



const getInitialItems = () => {

	return tableTreeHelper.updateItems(getDefaultItems());

};



export default () => {

	const [items, setItems] = useState<Item[]>(getInitialItems);

	const [isLoading, setIsLoading] = useState(false);



	const reloadItems = useCallback(() => {

		setIsLoading(true);

		fetchItems().then((newItems) => {

			setItems((items) => tableTreeHelper.updateItems(newItems, items, items[items.length - 1]));

			setIsLoading(false);

		});

	}, []);



	return (

		<Box>

			<Button onClick={reloadItems}>Reload items</Button>

			<TableTree label="Updated data">

				<Headers>

					<Header width={200}>Chapter title</Header>

					<Header width={120}>Numbering</Header>

					<Header width={100}>Page</Header>

				</Headers>

				<Rows

					items={items}

					render={({ title, numbering, page, children = [] }) => (

						<Row

							itemId={numbering}

							items={isLoading ? undefined : children}

							hasChildren={children.length > 0}

							isDefaultExpanded

						>

							<Cell>{title}</Cell>

							<Cell>{numbering}</Cell>

							<Cell>{page}</Cell>

						</Row>

					)}

				/>

			</TableTree>

		</Box>

	);

};
```

## Expand and collapse on row click

Use the shouldExpandOnClick prop to change whether a row with children expands when clicked anywhere on a row instead of only via the chevron. Don’t use this prop if interactive elements like a button or dropdown menu exist within your row. Clicking on those elements will trigger the row to unexpectedly expand or collapse, along with the default behavior of the interactive element. 

```jsx
import React from 'react';



import TableTree, { Cell, Header, Headers, Row, Rows } from '@atlaskit/table-tree';



import items from './data';



type Item = {

	title: string;

	numbering: string;

	page: number;

	children?: Item[];

	id: string;

};



export default () => (

	<TableTree label="Expand on row click">

		<Headers>

			<Header width={200}>Chapter title</Header>

			<Header width={120}>Numbering</Header>

			<Header width={100}>Page</Header>

		</Headers>

		<Rows

			items={items}

			render={({ title, numbering, page, children = [] }: Item) => (

				<Row

					itemId={numbering}

					items={children}

					hasChildren={children.length > 0}

					shouldExpandOnClick

				>

					<Cell singleLine>{title}</Cell>

					<Cell>{numbering}</Cell>

					<Cell>{page}</Cell>

				</Row>

			)}

		/>

	</TableTree>

);
```

## Accessibility

### Adding an accessible name

Use either the label or referencedLabel prop to provide an accessible name for the table. 

### Using an explicit label

### Using a reference to an element

```jsx
import React from 'react';



import { Box } from '@atlaskit/primitives';

import TableTree from '@atlaskit/table-tree';



type Content = { title: string; description: string };



type Item = {

	id: string;

	content: Content;

	hasChildren: boolean;

	children?: Item[];

};



const items: Item[] = [

	{

		id: 'item1',

		content: {

			title: 'Item 1',

			description: 'First top-level item',

		},

		hasChildren: false,

		children: [],

	},

	{

		id: 'item2',

		content: {

			title: 'Item 2',

			description: 'Second top-level item',

		},

		hasChildren: true,

		children: [

			{

				id: 'child2.1',

				content: {

					title: 'Child item',

					description: 'A child item',

				},

				hasChildren: false,

			},

		],

	},

];



const Title = (props: Content) => <Box as="span">{props.title}</Box>;

const Description = (props: Content) => <Box as="span">{props.description}</Box>;



export default () => (

	<div>

		<h3>Using an explicit label</h3>

		<TableTree

			columns={[Title, Description]}

			headers={['Title', 'Description']}

			columnWidths={['120px', '300px']}

			items={items}

			label="Explicit labelling example"

		/>

		<h3 id="referenced-label">Using a reference to an element</h3>

		<TableTree

			columns={[Title, Description]}

			headers={['Title', 'Description']}

			columnWidths={['120px', '300px']}

			items={items}

			referencedLabel="referenced-label"

		/>

	</div>

);
```

### Extended accessible label for expand and collapse button

Use the mainColumnForExpandCollapseLabel prop to add detail to the expand and collapse button’s aria-label announcement. The prop accepts a column's component name and adds the text from that column's cell to the row's expand button. For example, the first expand button below would read "Expand chapter 1: clean code row". 

```jsx
import React from 'react';



import { Box } from '@atlaskit/primitives';

import TableTree from '@atlaskit/table-tree';



type Content = { title: string; numbering: string; page: number };



type Item = {

	id: string;

	content: Content;

	hasChildren: boolean;

	children?: Item[];

};



const items: Item[] = [

	{

		id: 'item1',

		content: {

			title: 'Chapter 1: Clean code',

			numbering: '1',

			page: 1,

		},

		hasChildren: true,

		children: [

			{

				id: 'child1.1',

				content: {

					title: 'There will be code',

					numbering: '1.1',

					page: 2,

				},

				hasChildren: false,

			},

			{

				id: 'child1.2',

				content: {

					title: 'Bad code',

					numbering: '1.2',

					page: 3,

				},

				hasChildren: false,

			},

			{

				id: 'child1.3',

				content: {

					title: 'The cost of owning a mess',

					numbering: '1.3',

					page: 4,

				},

				hasChildren: true,

				children: [

					{

						id: 'child1.3.1',

						content: {

							title: 'Redesigning your code',

							numbering: '1.3.1',

							page: 5,

						},

						hasChildren: false,

					},

					{

						id: 'child1.3.2',

						content: {

							title: 'Accessibility considerations',

							numbering: '1.3.2',

							page: 5,

						},

						hasChildren: false,

					},

					{

						id: 'child1.3.3',

						content: {

							title: 'Planning for clean code',

							numbering: '1.3.3',

							page: 6,

						},

						hasChildren: false,

					},

					{

						id: 'child1.3.4',

						content: {

							title: 'The art of clean code',

							numbering: '1.3.4',

							page: 6,

						},

						hasChildren: false,

					},

					{

						id: 'child1.3.5',

						content: {

							title: 'What is clean code',

							numbering: '1.3.5',

							page: 7,

						},

						hasChildren: false,

					},

				],

			},

		],

	},

	{

		id: 'item2',

		content: {

			title: 'Chapter 2: Meaningful names',

			numbering: '2',

			page: 17,

		},

		hasChildren: false,

	},

	{

		id: 'item3',

		content: {

			title: 'Chapter 3: Functions',

			numbering: '3',

			page: 17,

		},

		hasChildren: true,

		children: [

			{

				id: 'child3.1',

				content: {

					title: 'Small!',

					numbering: '3.1',

					page: 34,

				},

				hasChildren: false,

			},

			{

				id: 'child3.2',

				content: {

					title: 'Do one thing',

					numbering: '3.2',

					page: 35,

				},

				hasChildren: false,

			},

			{

				id: 'child3.3',

				content: {

					title: 'One level of abstraction per function',

					numbering: '3.3',

					page: 36,

				},

				hasChildren: false,

			},

			{

				id: 'child3.4',

				content: {

					title: 'Switch statements',

					numbering: '3.4',

					page: 37,

				},

				hasChildren: false,

			},

			{

				id: 'child3.5',

				content: {

					title: 'Use descriptive names',

					numbering: '3.5',

					page: 39,

				},

				hasChildren: false,

			},

		],

	},

];



const Title = (props: Content) => <Box as="span">{props.title}</Box>;

const Numbering = (props: Content) => <Box as="span">{props.numbering}</Box>;

const Page = (props: Content) => <Box as="span">{props.page}</Box>;



export default () => (

	<TableTree

		columns={[Title, Numbering, Page]}

		headers={['Chapter Title', 'Numbering', 'Page']}

		mainColumnForExpandCollapseLabel="title"

		columnWidths={['200px', '100px', '100px']}

		items={items}

		label="Aria labelled expand and collapse button example"

	/>

);
```

---

[View Original Documentation](https://atlassian.design/components/table-tree/examples)
