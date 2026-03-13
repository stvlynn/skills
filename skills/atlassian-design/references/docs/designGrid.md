# Grid

A grid uses the CSS grid API to create consistent layouts.

---

## Installation

### Package installation information

#### Install

`yarn add @atlaskit/primitives`

#### Source

[Bitbucket.org﻿, (opens new window)](https://bitbucket.org/atlassian/atlassian-frontend-mirror/src/master/design-system/primitives)

npm

[@atlaskit/primitives﻿, (opens new window)](https://www.npmjs.com/package/@atlaskit/primitives)

Bundle

[unpkg.com﻿, (opens new window)](https://unpkg.com/@atlaskit/primitives/dist/)

## Basic

The Grid component is designed as a very basic mapping to the CSS Grid API. It can be used as an alternative to Flex, Inline or Stack.

```jsx
import React from 'react';



import { Grid } from '@atlaskit/primitives';



import ExampleBox from '../shared/example-box';



export default function Basic() {

	return (

		<Grid gap="space.200" alignItems="center">

			<ExampleBox />

			<ExampleBox />

			<ExampleBox />

		</Grid>

	);

}
```

## Gap properties

Gap properties rowGap, columnGap and gap only allow token-backed values. This is to aid ergonomics and keep the whitespace of the grid harmonious with the spacing system.

```jsx
import React from 'react';



import { Grid } from '@atlaskit/primitives';



import ExampleBox from '../shared/example-box';



export default function Basic() {

	return (

		<Grid gap="space.200" alignItems="center">

			<Grid templateColumns="1fr 1fr" testId="grid-basic" gap="space.100">

				<ExampleBox />

				<ExampleBox />

				<ExampleBox />

				<ExampleBox />

			</Grid>

			<Grid templateColumns="1fr 1fr" testId="grid-basic" gap="space.200">

				<ExampleBox />

				<ExampleBox />

				<ExampleBox />

				<ExampleBox />

			</Grid>

			<Grid templateColumns="1fr 1fr" testId="grid-basic" gap="space.400">

				<ExampleBox />

				<ExampleBox />

				<ExampleBox />

				<ExampleBox />

			</Grid>

		</Grid>

	);

}
```

## Template syntax

Grid-prefixed template properties in CSS do not have this prefix in the component API. For example grid-template-* are instead applied as templateColumns, templateRows and templateArea properties.

### Template columns

Template columns enables grid to declare the way columns are applied in the template.

```jsx
import React from 'react';



import { Grid } from '@atlaskit/primitives';



import ExampleBox from '../shared/example-box';



export default function Basic() {

	return (

		<Grid

			testId="grid-basic"

			rowGap="space.200"

			columnGap="space.400"

			templateColumns="1fr 100px 1fr"

		>

			<ExampleBox />

			<ExampleBox />

			<ExampleBox />

			<ExampleBox />

			<ExampleBox />

			<ExampleBox />

		</Grid>

	);

}
```

### Template rows

Template rows enables grid to declare the way row are applied in the template.

```jsx
import React from 'react';



import { Grid } from '@atlaskit/primitives';



import ExampleBox from '../shared/example-box';



export default function Basic() {

	return (

		<Grid testId="grid-basic" rowGap="space.200" columnGap="space.400" templateRows="3rem 2rem">

			<ExampleBox />

			<ExampleBox />

		</Grid>

	);

}
```

### Template areas

Template areas enables grid to declare the grid areas are applied in the template.

```jsx
import React from 'react';



import { Grid } from '@atlaskit/primitives';



import ExampleBox from '../shared/example-box';



export default function Basic() {

	return (

		<Grid

			testId="grid-basic"

			gap="space.200"

			templateAreas={[

				'navigation navigation navigation',

				'sidenav content content',

				'footer footer footer',

			]}

		>

			{/* eslint-disable-next-line @atlaskit/ui-styling-standard/enforce-style-prop -- Ignored via go/DSP-18766 */}

			<ExampleBox style={{ gridArea: 'navigation' }} />

			{/* eslint-disable-next-line @atlaskit/ui-styling-standard/enforce-style-prop -- Ignored via go/DSP-18766 */}

			<ExampleBox style={{ gridArea: 'sidenav' }} />

			{/* eslint-disable-next-line @atlaskit/ui-styling-standard/enforce-style-prop -- Ignored via go/DSP-18766 */}

			<ExampleBox style={{ gridArea: 'content' }} />

			{/* eslint-disable-next-line @atlaskit/ui-styling-standard/enforce-style-prop -- Ignored via go/DSP-18766 */}

			<ExampleBox style={{ gridArea: 'footer' }} />

		</Grid>

	);

}
```

## Autoflow syntax

Grid-prefixed properties in CSS do not have this prefix in the component API. grid-auto-flow is instead applied via autoFlow.

```jsx
import React from 'react';



import { Grid } from '@atlaskit/primitives';



import ExampleBox from '../shared/example-box';



export default function Basic() {

	return (

		<Grid autoFlow="column" gap="space.200">

			<ExampleBox />

			<ExampleBox />

			<ExampleBox />

		</Grid>

	);

}
```

## Responsive grid

Here, we construct a grid layout that adapts from a single column to a four-column layout depending on the viewport size. You may also be looking for:

```jsx
import React from 'react';



import { Grid, xcss } from '@atlaskit/primitives';

import { media } from '@atlaskit/primitives/responsive';



import ExampleBox from '../shared/example-box';



const responsiveStyles = xcss({

	[media.above.xxs]: { gridTemplateColumns: 'repeat(1, 1fr)' },

	[media.above.xs]: {

		gridTemplateColumns: 'repeat(2, 1fr)',

	},

	[media.above.sm]: {

		gridTemplateColumns: 'repeat(3, 1fr)',

	},

	[media.above.lg]: {

		gridTemplateColumns: 'repeat(4, 1fr)',

	},

});



const ResponsiveGrid = () => {

	return (

		<Grid xcss={responsiveStyles} gap="space.200" alignItems="center">

			<ExampleBox />

			<ExampleBox />

			<ExampleBox />

			<ExampleBox />

		</Grid>

	);

};



export default ResponsiveGrid;
```

---

[View Original Documentation](https://atlassian.design/components/primitives/grid/examples)
