# Flex

A flex implements the CSS flexbox API.

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

The Flex component is a basic mapping to the CSS Flexbox API. It can be used as a less richly-configured Inline or Stack. Like Stack and Inline, Flex exclusively supports token-backed gap properties to ensure layouts using Flex match the Atlassian Design System spacing scale.

```jsx
import React, { useCallback, useState } from 'react';



import Button from '@atlaskit/button/new';

import { Code } from '@atlaskit/code';

import Heading from '@atlaskit/heading';

import { Box, Flex, Stack } from '@atlaskit/primitives';



import ExampleBox from '../shared/example-box';



const alignmentValues = ['start', 'center', 'end'] as const;



export default function Example() {

	const [alignmentIndex, setAlignmentIndex] = useState<0 | 1 | 2>(0);

	const nextIndex = ((alignmentIndex + 1) % alignmentValues.length) as 0 | 1 | 2;

	const changeAlignment = useCallback(() => {

		setAlignmentIndex(nextIndex);

	}, [nextIndex]);

	return (

		<Stack space="space.500">

			<Box>

				<Button onClick={changeAlignment}>

					Change alignment to "{alignmentValues[nextIndex]}"

				</Button>

			</Box>

			<Stack space="space.100">

				<Heading size="xsmall">

					Justify content <Code>{alignmentValues[alignmentIndex]}</Code>

				</Heading>

				<Flex gap="space.100" justifyContent={alignmentValues[alignmentIndex]}>

					<ExampleBox />

					<ExampleBox />

					<ExampleBox />

				</Flex>

			</Stack>

		</Stack>

	);

}
```

## Align items and justify content

Flex applies the alignItems and justifyContent properties to align content along its cross and main axes respectively.

```jsx
import React, { type ReactNode } from 'react';



import { Box, Flex, Stack, xcss } from '@atlaskit/primitives';



import ExampleBox from '../shared/example-box';



const flexContainerStyles = xcss({

	display: 'flex',

	borderRadius: '3px',

	height: 'size.600',

});



export default function Example() {

	return (

		<Flex justifyContent="space-between" wrap="wrap">

			<Stack alignInline="center">

				"start" (default)

				<VisualContainer>

					<Flex gap="space.050" alignItems="start">

						<ExampleBox />

						<ExampleBox />

						<ExampleBox padding="space.300" />

					</Flex>

				</VisualContainer>

			</Stack>

			<Stack alignInline="center">

				"center"

				<VisualContainer>

					<Flex gap="space.050" alignItems="center">

						<ExampleBox />

						<ExampleBox />

						<ExampleBox padding="space.300" />

					</Flex>

				</VisualContainer>

			</Stack>

			<Stack alignInline="center">

				"end"

				<VisualContainer>

					<Flex gap="space.050" alignItems="end">

						<ExampleBox />

						<ExampleBox />

						<ExampleBox padding="space.300" />

					</Flex>

				</VisualContainer>

			</Stack>

			<Stack alignInline="center">

				"baseline"

				<VisualContainer>

					<Flex gap="space.050" alignItems="baseline">

						<ExampleBox />

						<ExampleBox />

						<ExampleBox padding="space.300" />

					</Flex>

				</VisualContainer>

			</Stack>

		</Flex>

	);

}



const VisualContainer = ({ children }: { children: ReactNode }) => (

	<Box backgroundColor="color.background.neutral" padding="space.050" xcss={flexContainerStyles}>

		{children}

	</Box>

);
```

## Wrap

Flex-prefixed properties in CSS do not have this prefix in the component API. For example, flex-wrap is instead applied as the wrap property.

```jsx
import React from 'react';



import { Flex } from '@atlaskit/primitives';



import ExampleBox from '../shared/example-box';



export default function Example() {

	return (

		<Flex gap="space.100" wrap="wrap">

			{[...Array(20).keys()].map((i) => (

				<ExampleBox key={i} />

			))}

		</Flex>

	);

}
```

## Direction

Flex direction is applied via the direction property.

```jsx
import React, { useState } from 'react';



import Button from '@atlaskit/button/new';

import { Code } from '@atlaskit/code';

import Heading from '@atlaskit/heading';

import { Box, Flex, Stack } from '@atlaskit/primitives';



import ExampleBox from '../shared/example-box';



export default function Example() {

	const [direction, setDirection] = useState<'row' | 'column'>('row');



	return (

		<Stack space="space.500">

			<Box>

				<Button

					onClick={() =>

						setDirection((oldDirection) => (oldDirection === 'row' ? 'column' : 'row'))

					}

				>

					Change direction to "{direction === 'row' ? 'column' : 'row'}"

				</Button>

			</Box>

			<Stack space="space.100">

				<Heading size="xsmall">

					Flex direction <Code>{direction}</Code>

				</Heading>

				<Flex gap="space.100" direction={direction}>

					<ExampleBox />

					<ExampleBox />

					<ExampleBox />

				</Flex>

			</Stack>

		</Stack>

	);

}
```

---

[View Original Documentation](https://atlassian.design/components/primitives/flex/examples)
