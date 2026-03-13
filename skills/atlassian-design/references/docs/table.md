# Table

A table is used to display data.

---

## Basic

A table is composed of simple composable elements. In its base form these UI elements are purely presentational. 

```jsx
import React from 'react';



import Table, { Cell, HeadCell, Row, TBody, THead } from '@atlaskit/table';



import { presidents } from './content/presidents';



/**

 * Primary UI component for user interaction

 */

const CompositionExample = () => {

	return (

		<Table>

			<THead>

				<HeadCell>Name</HeadCell>

				<HeadCell>Party</HeadCell>

				<HeadCell>Year</HeadCell>

			</THead>

			<TBody>

				{presidents.map((row) => (

					<Row key={row.id}>

						<Cell>{row.name}</Cell>

						<Cell>{row.party}</Cell>

						<Cell>{row.term}</Cell>

					</Row>

				))}

			</TBody>

		</Table>

	);

};



export default CompositionExample;
```

| Name | Party | Year |
| --- | --- | --- |
| George Washington | None, Federalist | 1789-1797 |
| John Adams | Federalist | 1797-1801 |
| Thomas Jefferson | Democratic-Republican | 1801-1809 |
| James Madison | Democratic-Republican | 1809-1817 |
| James Monroe | Democratic-Republican | 1817-1825 |
| John Quincy Adams | Democratic-Republican | 1825-1829 |
| Andrew Jackson | Democrat | 1829-1837 |
| Martin van Buren | Democrat | 1837-1841 |
| William H. Harrison | Whig | 1841 |
| John Tyler | Whig | 1841-1845 |

## Basic data table

A data table is used to display dynamic data. 

```jsx
import React, { useCallback, useRef } from 'react';



import Button from '@atlaskit/button/new';

import { Box, Stack, xcss } from '@atlaskit/primitives';



import { triggerPostMoveFlash } from '@atlaskit/table/trigger-post-move-flash';



const cardStyles = xcss({

	width: '100%',

	height: '100px',

	backgroundColor: 'elevation.surface.raised',

	boxShadow: 'elevation.shadow.raised',

	borderRadius: 'border.radius.100',

});



export default function BasicExample() {

	const ref = useRef<HTMLElement>(null);



	const runAnimation = useCallback(() => {

		const element = ref.current;

		if (!element) {

			return;

		}

		triggerPostMoveFlash(element);

	}, []);



	return (

		<Stack space="space.200" alignInline="center">

			<Box ref={ref} xcss={cardStyles} />

			<Button onClick={runAnimation}>Run animation</Button>

		</Stack>

	);

}
```

| Select all rows | Name | Party | Year |
| --- | --- | --- | --- |
| Select row 1 | George Washington | None, Federalist | 1789-1797 |
| Select row 2 | John Adams | Federalist | 1797-1801 |
| Select row 3 | Thomas Jefferson | Democratic-Republican | 1801-1809 |
| Select row 4 | James Madison | Democratic-Republican | 1809-1817 |
| Select row 5 | James Monroe | Democratic-Republican | 1817-1825 |
| Select row 6 | John Quincy Adams | Democratic-Republican | 1825-1829 |
| Select row 7 | Andrew Jackson | Democrat | 1829-1837 |
| Select row 8 | Martin van Buren | Democrat | 1837-1841 |
| Select row 9 | William H. Harrison | Whig | 1841 |
| Select row 10 | John Tyler | Whig | 1841-1845 |

## Expandable

Expanding row functionality can be added using composable elements. 

```jsx
import React from 'react';



import { Date as AKDate } from '@atlaskit/date';

import SectionMessage from '@atlaskit/section-message';

import VisuallyHidden from '@atlaskit/visually-hidden';



import Table, {

	Cell,

	ExpandableCell,

	ExpandableRow,

	ExpandableRowContent,

	HeadCell,

	Row,

	TBody,

	THead,

} from '@atlaskit/table';



export default function Expandable() {

	return (

		<Table testId="expandable-table">

			<THead>

				<HeadCell>

					{/* A hidden label can be used to title the column for accessibility */}

					<VisuallyHidden>Expand row</VisuallyHidden>

				</HeadCell>

				<HeadCell>Item</HeadCell>

				<HeadCell>Category</HeadCell>

				<HeadCell align="number">Quantity</HeadCell>

				<HeadCell align="number">Cost</HeadCell>

				<HeadCell>Date</HeadCell>

			</THead>

			<TBody>

				<ExpandableRow isDefaultExpanded>

					<Row>

						<ExpandableCell />

						<Cell>Banana</Cell>

						<Cell>Groceries</Cell>

						<Cell align="number">5</Cell>

						<Cell align="number">$5.62</Cell>

						<Cell>

							<AKDate value={Number(new Date('01/11/2023'))} />

						</Cell>

					</Row>

					<ExpandableRowContent>

						<Row>

							<Cell />

							<Cell />

							<Cell />

							<Cell align="number">2</Cell>

							<Cell align="number">$2.03</Cell>

							<Cell>

								<AKDate value={Number(new Date('01/21/2023'))} />

							</Cell>

						</Row>

						<Row>

							<Cell />

							<Cell />

							<Cell />

							<Cell align="number">3</Cell>

							<Cell align="number">$3.59</Cell>

							<Cell>

								<AKDate value={Number(new Date('01/29/2023'))} />

							</Cell>

						</Row>

					</ExpandableRowContent>

				</ExpandableRow>

				<ExpandableRow>

					<Row>

						<ExpandableCell />

						<Cell>Chair</Cell>

						<Cell>Homeware</Cell>

						<Cell align="number">1</Cell>

						<Cell align="number">$74.87</Cell>

						<Cell>

							<AKDate value={Number(new Date('02/03/2023'))} />

						</Cell>

					</Row>

					<ExpandableRowContent>

						<Row>

							<Cell />

							<Cell colSpan={5}>

								<SectionMessage appearance="discovery">

									<p>This is a full-width expanded row.</p>

								</SectionMessage>

							</Cell>

						</Row>

					</ExpandableRowContent>

				</ExpandableRow>

				{/* Non-expanding row */}

				<Row>

					<Cell />

					<Cell>Shirt</Cell>

					<Cell>Clothing</Cell>

					<Cell align="number">2</Cell>

					<Cell align="number">$89.62</Cell>

					<Cell>

						<AKDate value={Number(new Date('02/19/2023'))} />

					</Cell>

				</Row>

			</TBody>

		</Table>

	);

}
```

| Expand row | Item | Category | Quantity | Cost | Date |
| --- | --- | --- | --- | --- | --- |
| Expand row | Banana | Groceries | 5 | $5.62 | 11/01/2023 |
|  |  |  | 2 | $2.03 | 21/01/2023 |
|  |  |  | 3 | $3.59 | 29/01/2023 |
| Expand row | Chair | Homeware | 1 | $74.87 | 03/02/2023 |
|  | Shirt | Clothing | 2 | $89.62 | 19/02/2023 |

---

[View Original Documentation](https://atlassian.design/components/table/examples)
