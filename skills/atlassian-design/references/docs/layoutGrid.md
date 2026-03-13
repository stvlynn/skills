# Layout grid

A responsive layout grid is a component designed to manage the content of a page.

---

## Basic

Grids are composed of a container Grid and child GridItems. These two elements work together to form the grid. 

```jsx
import React from 'react';



import Grid, { GridItem } from '@atlaskit/grid';



import { SkeletonBox } from './shared/skeleton-box';



export default () => (

	<Grid>

		<GridItem span={{ sm: 6, md: 4 }}>

			<SkeletonBox>sm=6 md=4</SkeletonBox>

		</GridItem>

		<GridItem span={{ sm: 6, md: 4 }}>

			<SkeletonBox>sm=6 md=4</SkeletonBox>

		</GridItem>

		<GridItem span={{ md: 4 }}>

			<SkeletonBox>sm=12 md=4</SkeletonBox>

		</GridItem>

		<GridItem span={{ md: 6 }}>

			<SkeletonBox>sm=12 md=6</SkeletonBox>

		</GridItem>

		<GridItem span={{ md: 6 }}>

			<SkeletonBox>sm=12 md=6</SkeletonBox>

		</GridItem>

	</Grid>

);
```

## Grid maxWidth

You can restrict the maxWidth of the Grid to pre-defined sizes. By default, the Grid takes up full space available. 

### narrow

The Grid's maximum width is 744px. On smaller screens it will take up all available width. 

```jsx
import React from 'react';



import Grid, { GridItem } from '@atlaskit/grid';



import { SkeletonBox } from './shared/skeleton-box';



export default () => (

	<Grid maxWidth="narrow">

		<GridItem span={{ sm: 6, md: 4 }}>

			<SkeletonBox>sm=6 md=4</SkeletonBox>

		</GridItem>

		<GridItem span={{ sm: 6, md: 4 }}>

			<SkeletonBox>sm=6 md=4</SkeletonBox>

		</GridItem>

		<GridItem span={{ md: 4 }}>

			<SkeletonBox>sm=12 md=4</SkeletonBox>

		</GridItem>

		<GridItem span={{ md: 6 }}>

			<SkeletonBox>sm=12 md=6</SkeletonBox>

		</GridItem>

		<GridItem span={{ md: 6 }}>

			<SkeletonBox>sm=12 md=6</SkeletonBox>

		</GridItem>

	</Grid>

);
```

### wide

The Grid's maximum width is 1128px. On smaller screens it will take up all available width. 

```jsx
import React from 'react';



import Grid, { GridItem } from '@atlaskit/grid';



import { SkeletonBox } from './shared/skeleton-box';



export default () => (

	<Grid maxWidth="wide">

		<GridItem span={{ sm: 6, md: 4 }}>

			<SkeletonBox>sm=6 md=4</SkeletonBox>

		</GridItem>

		<GridItem span={{ sm: 6, md: 4 }}>

			<SkeletonBox>sm=6 md=4</SkeletonBox>

		</GridItem>

		<GridItem span={{ md: 4 }}>

			<SkeletonBox>sm=12 md=4</SkeletonBox>

		</GridItem>

		<GridItem span={{ md: 6 }}>

			<SkeletonBox>sm=12 md=6</SkeletonBox>

		</GridItem>

		<GridItem span={{ md: 6 }}>

			<SkeletonBox>sm=12 md=6</SkeletonBox>

		</GridItem>

	</Grid>

);
```

## Grid inline padding

By default, the Grid has an inline padding around the outside of the Grid columns. This can be disabled with hasInlinePadding={false} 

```jsx
import React from 'react';



import Grid, { GridItem } from '@atlaskit/grid';



import { SkeletonBox } from './shared/skeleton-box';



export default () => (

	<>

		<Grid maxWidth="wide" hasInlinePadding={true}>

			<GridItem span={12}>

				<SkeletonBox>with padding</SkeletonBox>

			</GridItem>

		</Grid>

		<Grid maxWidth="wide" hasInlinePadding={false}>

			<GridItem span={12}>

				<SkeletonBox>without padding</SkeletonBox>

			</GridItem>

		</Grid>

	</>

);
```

## Item span

Define how many columns an item will span. This is a 1-indexed range 1-12. By default, span is 12 and will span the entire row. We enable a shorthand here, using span={6} is the same as span={{ xxs: 6 }}. The shorthand will override the default full-width functionality across all breakpoints. See usage to understand our how responsive object syntax works. 

```jsx
import React from 'react';



import Grid, { GridItem } from '@atlaskit/grid';



import { SkeletonBox } from './shared/skeleton-box';



export default () => (

	<Grid>

		<GridItem span={6}>

			<SkeletonBox>half-width</SkeletonBox>

		</GridItem>



		<GridItem span={{ xxs: 12 }}>

			<SkeletonBox>full-width</SkeletonBox>

		</GridItem>



		<GridItem>

			<SkeletonBox>full-width (default)</SkeletonBox>

		</GridItem>

	</Grid>

);
```

### Hide an item entirely

In the case that you do not want a GridItem rendered at all, use span="none" or span={{ xxs: 'none', md: 6 }} (etc). This is useful because if you wanted to hide the inner contents of the GridItem, the GridItem would still take up the space it's alloted. 

```jsx
import React, { Fragment, useState } from 'react';



import Grid, { GridItem } from '@atlaskit/grid';



import { SkeletonBox } from './shared/skeleton-box';



export default () => {

	const [visible, setVisible] = useState(false);



	return (

		<Fragment>

			<Grid>

				<GridItem>

					<button type="button" onClick={() => setVisible((v) => !v)}>

						toggle visibility to {visible ? 'hidden' : 'visible'}

					</button>

				</GridItem>



				<GridItem span={6}>

					<SkeletonBox>always visible</SkeletonBox>

				</GridItem>



				<GridItem span={{ xxs: 'none', md: 6 }}>

					<SkeletonBox>hidden below md</SkeletonBox>

				</GridItem>



				<GridItem span={{ xxs: 6, lg: 'none' }}>

					<SkeletonBox>hidden above lg</SkeletonBox>

				</GridItem>



				<GridItem span={visible ? 6 : 'none'}>

					<SkeletonBox>only visible when toggled</SkeletonBox>

				</GridItem>



				<GridItem span={6}>

					<SkeletonBox>always visible</SkeletonBox>

				</GridItem>

			</Grid>

		</Fragment>

	);

};
```

## Item start column

Define the column at which your item will start. This is a 1-indexed range 1-12. By default, start is 'auto' and will fill the next available column in the row, as space is available. We enable a shorthand here, using start={1} is the same as start={{ xxs: 1 }}. The shorthand will override the default 'auto' functionality across all breakpoints. See usage to understand our how responsive object syntax works. 

```jsx
import React from 'react';



import Grid, { GridItem } from '@atlaskit/grid';



import { SkeletonBox } from './shared/skeleton-box';



export default () => (

	<Grid>

		<GridItem span={8} start={3}>

			<SkeletonBox>centered</SkeletonBox>

		</GridItem>



		<GridItem span={8} start={{ lg: 3 }}>

			<SkeletonBox>centered on desktop</SkeletonBox>

		</GridItem>



		<GridItem span={{ xxs: 6 }} start={7}>

			<SkeletonBox>forced right</SkeletonBox>

		</GridItem>

	</Grid>

);
```

### Auto positioning

'auto' is the default which will fill the next available column in the row, as space is available. This may be required though to reset the functionality back to default when using the responsive object syntax due to the cascading nature. 

```jsx
import React from 'react';



import Grid, { GridItem } from '@atlaskit/grid';



import { SkeletonBox } from './shared/skeleton-box';



export default () => (

	<Grid>

		<GridItem span={4} start={{ xxs: 5, md: 'auto' }}>

			<SkeletonBox>

				centered xs+

				<br />

				auto md+

			</SkeletonBox>

		</GridItem>

	</Grid>

);
```

### Position with an offset

If there's room to fill a column, using start will stay on the same row, where possible. 

```jsx
import React from 'react';



import Grid, { GridItem } from '@atlaskit/grid';



import { SkeletonBox } from './shared/skeleton-box';



export default () => (

	<Grid>

		<GridItem span={4}>

			<SkeletonBox>(left)</SkeletonBox>

		</GridItem>



		<GridItem span={4} start={9}>

			<SkeletonBox>(right)</SkeletonBox>

		</GridItem>

	</Grid>

);
```

### Forced to a new row

With start, you can force a GridItem to a new row by setting start={1}. This is because whenever a column is unavailable on the same row subsequently from the previous item, it will always start on the next row at that column instead. 

```jsx
import React from 'react';



import Grid, { GridItem } from '@atlaskit/grid';



import { SkeletonBox } from './shared/skeleton-box';



export default () => (

	<Grid>

		<GridItem span={4}>

			<SkeletonBox>Line 1</SkeletonBox>

		</GridItem>



		<GridItem span={4} start={1}>

			<SkeletonBox>Forced to Line 2</SkeletonBox>

		</GridItem>

	</Grid>

);
```

## Nested grids

We do not support nested Grids at this stage; doing so will throw an error. Further guidance may be provided in the future. 

## Grid container

GridContainer allows the stacking of independent grids on top of each other. Functionaly, it is a grid that has a single fluid column with the same responsive gutter as Grid. This allows the stacking of multiple independent grids whilst keeping the vertical rhythm enforced by Grid's responsive gap values. When within GridContainer all Grid instances are configured to fill their GridContainer's width, whilst also disabling inline padding. In that case, the hasInlinePadding and maxWidth props should be set in the GridContainer instead, ignoring them in Grid. 

```jsx
import React from 'react';



import Grid, { GridContainer, GridItem } from '@atlaskit/grid';



import { SkeletonBox } from './shared/skeleton-box';



export default () => {

	return (

		<GridContainer hasInlinePadding={true}>

			<Grid>

				<GridItem span={{ md: 6 }}>

					<SkeletonBox>md=6</SkeletonBox>

				</GridItem>

				<GridItem span={{ md: 6 }}>

					<SkeletonBox>md=6</SkeletonBox>

				</GridItem>

				<GridItem span={{ md: 6 }}>

					<SkeletonBox>md=6</SkeletonBox>

				</GridItem>

				<GridItem span={{ md: 6 }}>

					<SkeletonBox>md=6</SkeletonBox>

				</GridItem>

			</Grid>

			<Grid>

				<GridItem span={{ md: 4 }}>

					<SkeletonBox>md=4</SkeletonBox>

				</GridItem>

				<GridItem span={{ md: 8 }}>

					<SkeletonBox>md=8</SkeletonBox>

				</GridItem>

				<GridItem span={{ md: 4 }}>

					<SkeletonBox>md=4</SkeletonBox>

				</GridItem>

				<GridItem span={{ md: 8 }}>

					<SkeletonBox>md=8</SkeletonBox>

				</GridItem>

			</Grid>

			<Grid>

				<GridItem span={{ md: 4 }}>

					<SkeletonBox>md=4</SkeletonBox>

				</GridItem>

				<GridItem span={{ md: 8 }}>

					<SkeletonBox>md=8</SkeletonBox>

				</GridItem>

				<GridItem span={{ md: 4 }}>

					<SkeletonBox>md=4</SkeletonBox>

				</GridItem>

				<GridItem span={{ md: 8 }}>

					<SkeletonBox>md=8</SkeletonBox>

				</GridItem>

			</Grid>

		</GridContainer>

	);

};
```

---

[View Original Documentation](https://atlassian.design/components/grid/examples)
