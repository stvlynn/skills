# Grid

Grid controls layout and spacing on a page and serves as a wrapper for Grid columns.

---

## Layout

Grids can have either a fixed or fluid layout, which determines its width. 

### Fixed layout (default)

A fixed layout will occupy a maximum of 80px for each column space, plus a fixed amount based on the chosen spacing. 

### Comfortable spacing

### Cosy spacing (default)

### Compact spacing

```jsx
import React from 'react';



import Page, { Grid, GridColumn } from '@atlaskit/page';

import { Dummy } from '../common/dummy';

import VerticalSpace from '../common/vertical-space';



const columns = 6;

const GridFixedLayoutExample = () => {

	return (

		<Page>

			<Grid spacing="comfortable" columns={columns}>

				<GridColumn medium={columns}>

					<h3>Comfortable spacing</h3>

				</GridColumn>

				<GridColumn medium={3}>

					<Dummy hasMargin>3 col</Dummy>

				</GridColumn>

				<GridColumn medium={2}>

					<Dummy hasMargin>2 col</Dummy>

				</GridColumn>

				<GridColumn medium={1}>

					<Dummy hasMargin>1 col</Dummy>

				</GridColumn>

				<GridColumn>

					<Dummy hasMargin>Unspecified</Dummy>

				</GridColumn>

			</Grid>



			<VerticalSpace />



			<Grid spacing="cosy" columns={columns}>

				<GridColumn medium={columns}>

					<h3>Cosy spacing (default)</h3>

				</GridColumn>

				<GridColumn medium={3}>

					<Dummy hasMargin>3 col</Dummy>

				</GridColumn>

				<GridColumn medium={2}>

					<Dummy hasMargin>2 col</Dummy>

				</GridColumn>

				<GridColumn medium={1}>

					<Dummy hasMargin>1 col</Dummy>

				</GridColumn>

				<GridColumn>

					<Dummy hasMargin>Unspecified</Dummy>

				</GridColumn>

			</Grid>



			<VerticalSpace />



			<Grid spacing="compact" columns={columns}>

				<GridColumn medium={columns}>

					<h3>Compact spacing</h3>

				</GridColumn>

				<GridColumn medium={3}>

					<Dummy hasMargin>3 col</Dummy>

				</GridColumn>

				<GridColumn medium={2}>

					<Dummy hasMargin>2 col</Dummy>

				</GridColumn>

				<GridColumn medium={1}>

					<Dummy hasMargin>1 col</Dummy>

				</GridColumn>

				<GridColumn>

					<Dummy hasMargin>Unspecified</Dummy>

				</GridColumn>

			</Grid>

		</Page>

	);

};

export default GridFixedLayoutExample;
```

### Fluid layout (custom width)

Custom width pages are supported by setting layout="fluid" on the Grid. This will make the grid expand to fill its container. 

### Comfortable spacing

### Cosy spacing (default)

### Compact spacing

```jsx
import React from 'react';



import Page, { Grid, GridColumn } from '@atlaskit/page';

import { Dummy } from '../common/dummy';

import VerticalSpace from '../common/vertical-space';



const columns = 6;

const GridFluidLayoutExample = () => {

	return (

		<Page>

			<Grid layout="fluid" spacing="comfortable" columns={columns}>

				<GridColumn medium={columns}>

					<h3>Comfortable spacing</h3>

				</GridColumn>

				<GridColumn medium={3}>

					<Dummy hasMargin>3 col</Dummy>

				</GridColumn>

				<GridColumn medium={2}>

					<Dummy hasMargin>2 col</Dummy>

				</GridColumn>

				<GridColumn medium={1}>

					<Dummy hasMargin>1 col</Dummy>

				</GridColumn>

				<GridColumn>

					<Dummy hasMargin>Unspecified</Dummy>

				</GridColumn>

			</Grid>



			<VerticalSpace />



			<Grid layout="fluid" spacing="cosy" columns={columns}>

				<GridColumn medium={columns}>

					<h3>Cosy spacing (default)</h3>

				</GridColumn>

				<GridColumn medium={3}>

					<Dummy hasMargin>3 col</Dummy>

				</GridColumn>

				<GridColumn medium={2}>

					<Dummy hasMargin>2 col</Dummy>

				</GridColumn>

				<GridColumn medium={1}>

					<Dummy hasMargin>1 col</Dummy>

				</GridColumn>

				<GridColumn>

					<Dummy hasMargin>Unspecified</Dummy>

				</GridColumn>

			</Grid>



			<VerticalSpace />



			<Grid layout="fluid" spacing="compact" columns={columns}>

				<GridColumn medium={columns}>

					<h3>Compact spacing</h3>

				</GridColumn>

				<GridColumn medium={3}>

					<Dummy hasMargin>3 col</Dummy>

				</GridColumn>

				<GridColumn medium={2}>

					<Dummy hasMargin>2 col</Dummy>

				</GridColumn>

				<GridColumn medium={1}>

					<Dummy hasMargin>1 col</Dummy>

				</GridColumn>

				<GridColumn>

					<Dummy hasMargin>Unspecified</Dummy>

				</GridColumn>

			</Grid>

		</Page>

	);

};

export default GridFluidLayoutExample;
```

## Spacing

The spacing between a grid's columns is configurable. There are three options available: 

## Cosy spacing (default)

## Compact spacing

## Comfortable spacing

```jsx
import React from 'react';



import Page, { Grid, GridColumn } from '@atlaskit/page';

import { Dummy } from '../common/dummy';

import VerticalSpace from '../common/vertical-space';



const GridSpacingExample = () => {

	return (

		<Page>

			<Grid>

				<GridColumn medium={12}>

					<h2>Cosy spacing (default)</h2>

				</GridColumn>

				<GridColumn medium={2}>

					<Dummy>2 col</Dummy>

				</GridColumn>

				<GridColumn medium={2}>

					<Dummy>2 col</Dummy>

				</GridColumn>

				<GridColumn medium={2}>

					<Dummy>2 col</Dummy>

				</GridColumn>

				<GridColumn medium={2}>

					<Dummy>2 col</Dummy>

				</GridColumn>

				<GridColumn medium={2}>

					<Dummy>2 col</Dummy>

				</GridColumn>

				<GridColumn medium={2}>

					<Dummy>2 col</Dummy>

				</GridColumn>

			</Grid>



			<VerticalSpace />



			<Grid spacing="compact">

				<GridColumn medium={12}>

					<h2>Compact spacing</h2>

				</GridColumn>

				<GridColumn medium={2}>

					<Dummy>2 col</Dummy>

				</GridColumn>

				<GridColumn medium={2}>

					<Dummy>2 col</Dummy>

				</GridColumn>

				<GridColumn medium={2}>

					<Dummy>2 col</Dummy>

				</GridColumn>

				<GridColumn medium={2}>

					<Dummy>2 col</Dummy>

				</GridColumn>

				<GridColumn medium={2}>

					<Dummy>2 col</Dummy>

				</GridColumn>

				<GridColumn medium={2}>

					<Dummy>2 col</Dummy>

				</GridColumn>

			</Grid>



			<VerticalSpace />



			<Grid spacing="comfortable">

				<GridColumn medium={12}>

					<h2>Comfortable spacing</h2>

				</GridColumn>

				<GridColumn medium={2}>

					<Dummy>2 col</Dummy>

				</GridColumn>

				<GridColumn medium={2}>

					<Dummy>2 col</Dummy>

				</GridColumn>

				<GridColumn medium={2}>

					<Dummy>2 col</Dummy>

				</GridColumn>

				<GridColumn medium={2}>

					<Dummy>2 col</Dummy>

				</GridColumn>

				<GridColumn medium={2}>

					<Dummy>2 col</Dummy>

				</GridColumn>

				<GridColumn medium={2}>

					<Dummy>2 col</Dummy>

				</GridColumn>

			</Grid>

		</Page>

	);

};

export default GridSpacingExample;
```

## Nesting

Grids can be nested inside of each other to form complex layouts. If a nested Grid is inside of a GridColumn with a provided value for medium, then the nested Grid will use that medium value as its default number of columns. 

## Nested Grid

```jsx
import React from 'react';



import Page, { Grid, GridColumn } from '@atlaskit/page';

import { Dummy, DummyNested } from '../common/dummy';



const NestedGridExample = () => {

	return (

		<Page testId="page">

			<Grid spacing="cosy" testId="outer-grid">

				<GridColumn medium={12}>

					<h2>Nested Grid</h2>

				</GridColumn>

				<GridColumn medium={8}>

					<Dummy>

						This content sits inside a column of width 8. The text is before the nested grid.

						<Grid testId="inner-grid">

							<GridColumn medium={4}>

								<DummyNested>4 col</DummyNested>

							</GridColumn>

							<GridColumn medium={4}>

								<DummyNested>4 col</DummyNested>

							</GridColumn>

						</Grid>

						This content sits after the nested grid. Notice how the grid pulls itself out into the

						margins of the column its in.

					</Dummy>

				</GridColumn>



				<GridColumn medium={4}>

					<Dummy>4 col</Dummy>

				</GridColumn>

			</Grid>

		</Page>

	);

};

export default NestedGridExample;
```

---

[View Original Documentation](https://atlassian.design/components/page/grid/examples)
