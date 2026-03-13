# Progress indicator

A progress indicator shows the user where they are along the steps of a journey.

---

## Appearance

### Default

Progress indicators in the default color. 

```jsx
import React, { useState } from 'react';



import Button from '@atlaskit/button/new';

import { Inline } from '@atlaskit/primitives';

import { ProgressIndicator } from '@atlaskit/progress-indicator';



const DefaultExample = () => {

	const [selectedIndex, setSelectedIndex] = useState(0);

	const [values] = useState(['first', 'second', 'third']);



	const handlePrev = () => {

		setSelectedIndex((prevState) => prevState - 1);

	};



	const handleNext = () => {

		setSelectedIndex((prevState) => prevState + 1);

	};



	return (

		<Inline alignBlock="center" spread="space-between">

			<Button isDisabled={selectedIndex === 0} onClick={handlePrev}>

				Previous

			</Button>

			<ProgressIndicator selectedIndex={selectedIndex} values={values} />

			<Button isDisabled={selectedIndex === values.length - 1} onClick={handleNext}>

				Next

			</Button>

		</Inline>

	);

};



export default DefaultExample;
```

### Primary

Progress indicators in the primary color. 

```jsx
import React, { useState } from 'react';



import Button from '@atlaskit/button/new';

import { Inline } from '@atlaskit/primitives';

import { ProgressIndicator } from '@atlaskit/progress-indicator';



const PrimaryExample = () => {

	const [selectedIndex, setSelectedIndex] = useState(0);

	const [values] = useState(['first', 'second', 'third']);



	const handlePrev = () => {

		setSelectedIndex((prevState) => prevState - 1);

	};



	const handleNext = () => {

		setSelectedIndex((prevState) => prevState + 1);

	};



	return (

		<Inline alignBlock="center" spread="space-between">

			<Button isDisabled={selectedIndex === 0} onClick={handlePrev}>

				Previous

			</Button>

			<ProgressIndicator appearance="primary" selectedIndex={selectedIndex} values={values} />

			<Button isDisabled={selectedIndex === values.length - 1} onClick={handleNext}>

				Next

			</Button>

		</Inline>

	);

};



export default PrimaryExample;
```

### Help

Use the help appearance in benefit modals to indicate help. 

```jsx
import React, { useState } from 'react';



import Button from '@atlaskit/button/new';

import { Inline } from '@atlaskit/primitives';

import { ProgressIndicator } from '@atlaskit/progress-indicator';



const HelpExample = () => {

	const [selectedIndex, setSelectedIndex] = useState(0);

	const [values] = useState(['first', 'second', 'third']);



	const handlePrev = () => {

		setSelectedIndex((prevState) => prevState - 1);

	};



	const handleNext = () => {

		setSelectedIndex((prevState) => prevState + 1);

	};



	return (

		<Inline alignBlock="center" spread="space-between">

			<Button isDisabled={selectedIndex === 0} onClick={handlePrev}>

				Previous

			</Button>

			<ProgressIndicator appearance="help" selectedIndex={selectedIndex} values={values} />

			<Button isDisabled={selectedIndex === values.length - 1} onClick={handleNext}>

				Next

			</Button>

		</Inline>

	);

};



export default HelpExample;
```

### Inverted

Use an inverted progress indicator when high contrast against a darker background color is needed. 

```jsx
import React, { useState } from 'react';



import Button from '@atlaskit/button/new';

import { cssMap } from '@atlaskit/css';

import { Inline } from '@atlaskit/primitives/compiled';

import { ProgressIndicator } from '@atlaskit/progress-indicator';

import { token } from '@atlaskit/tokens';



const styles = cssMap({

	container: {

		paddingTop: token('space.200'),

		paddingRight: token('space.200'),

		paddingBottom: token('space.200'),

		paddingLeft: token('space.200'),

		backgroundColor: token('color.background.neutral.bold'),

	},

});



const InvertedExample = () => {

	const [selectedIndex, setSelectedIndex] = useState(0);

	const [values] = useState(['first', 'second', 'third']);



	const handlePrev = () => {

		setSelectedIndex((prevState) => prevState - 1);

	};



	const handleNext = () => {

		setSelectedIndex((prevState) => prevState + 1);

	};



	return (

		<Inline alignBlock="center" spread="space-between" xcss={styles.container}>

			<Button isDisabled={selectedIndex === 0} onClick={handlePrev} appearance="primary">

				Previous

			</Button>

			<ProgressIndicator appearance="inverted" selectedIndex={selectedIndex} values={values} />

			<Button

				isDisabled={selectedIndex === values.length - 1}

				onClick={handleNext}

				appearance="primary"

			>

				Next

			</Button>

		</Inline>

	);

};



export default InvertedExample;
```

## Size

The size of progress indicators can be medium (default), or large depending on how subtle or prominent the indicator should be. 

### Medium (default)

Default sized progress indicators. 

```jsx
import React, { useState } from 'react';



import Button from '@atlaskit/button/new';

import { Inline } from '@atlaskit/primitives';

import { ProgressIndicator } from '@atlaskit/progress-indicator';



const MediumExample = () => {

	const [selectedIndex, setSelectedIndex] = useState(0);

	const [values] = useState(['first', 'second', 'third']);



	const handlePrev = () => {

		setSelectedIndex((prevState) => prevState - 1);

	};



	const handleNext = () => {

		setSelectedIndex((prevState) => prevState + 1);

	};



	return (

		<Inline alignBlock="center" spread="space-between">

			<Button isDisabled={selectedIndex === 0} onClick={handlePrev}>

				Previous

			</Button>

			<ProgressIndicator selectedIndex={selectedIndex} values={values} />

			<Button isDisabled={selectedIndex === values.length - 1} onClick={handleNext}>

				Next

			</Button>

		</Inline>

	);

};



export default MediumExample;
```

### Large

Large sized progress indicators. 

```jsx
import React, { useState } from 'react';



import Button from '@atlaskit/button/new';

import { Inline } from '@atlaskit/primitives';

import { ProgressIndicator } from '@atlaskit/progress-indicator';



const LargeExample = () => {

	const [selectedIndex, setSelectedIndex] = useState(0);

	const [values] = useState(['first', 'second', 'third']);



	const handlePrev = () => {

		setSelectedIndex((prevState) => prevState - 1);

	};



	const handleNext = () => {

		setSelectedIndex((prevState) => prevState + 1);

	};



	return (

		<Inline alignBlock="center" spread="space-between">

			<Button isDisabled={selectedIndex === 0} onClick={handlePrev}>

				Previous

			</Button>

			<ProgressIndicator selectedIndex={selectedIndex} values={values} size="large" />

			<Button isDisabled={selectedIndex === values.length - 1} onClick={handleNext}>

				Next

			</Button>

		</Inline>

	);

};



export default LargeExample;
```

## Spacing

You can set the spacing to comfortable, cozy, or compact depending on the availability of space on the page. 

### Comfortable

Progress indicators with the default comfortable spacing. 

```jsx
import React, { useState } from 'react';



import Button from '@atlaskit/button/new';

import { Inline } from '@atlaskit/primitives';

import { ProgressIndicator } from '@atlaskit/progress-indicator';



const ComfortableExample = () => {

	const [selectedIndex, setSelectedIndex] = useState(0);

	const [values] = useState(['first', 'second', 'third']);



	const handlePrev = () => {

		setSelectedIndex((prevState) => prevState - 1);

	};



	const handleNext = () => {

		setSelectedIndex((prevState) => prevState + 1);

	};



	return (

		<Inline alignBlock="center" spread="space-between">

			<Button isDisabled={selectedIndex === 0} onClick={handlePrev}>

				Previous

			</Button>

			<ProgressIndicator spacing="comfortable" selectedIndex={selectedIndex} values={values} />

			<Button isDisabled={selectedIndex === values.length - 1} onClick={handleNext}>

				Next

			</Button>

		</Inline>

	);

};



export default ComfortableExample;
```

### Cozy

Progress indicators with cozy spacing. 

```jsx
import React, { useState } from 'react';



import Button from '@atlaskit/button/new';

import { Inline } from '@atlaskit/primitives';

import { ProgressIndicator } from '@atlaskit/progress-indicator';



const CozyExample = () => {

	const [selectedIndex, setSelectedIndex] = useState(0);

	const [values] = useState(['first', 'second', 'third']);



	const handlePrev = () => {

		setSelectedIndex((prevState) => prevState - 1);

	};



	const handleNext = () => {

		setSelectedIndex((prevState) => prevState + 1);

	};



	return (

		<Inline alignBlock="center" spread="space-between">

			<Button isDisabled={selectedIndex === 0} onClick={handlePrev}>

				Previous

			</Button>

			<ProgressIndicator spacing="cozy" selectedIndex={selectedIndex} values={values} />

			<Button isDisabled={selectedIndex === values.length - 1} onClick={handleNext}>

				Next

			</Button>

		</Inline>

	);

};



export default CozyExample;
```

### Compact

Progress indicators with compact spacing. 

```jsx
import React, { useState } from 'react';



import Button from '@atlaskit/button/new';

import { Inline } from '@atlaskit/primitives';

import { ProgressIndicator } from '@atlaskit/progress-indicator';



const CompactExample = () => {

	const [selectedIndex, setSelectedIndex] = useState(0);

	const [values] = useState(['first', 'second', 'third']);



	const handlePrev = () => {

		setSelectedIndex((prevState) => prevState - 1);

	};



	const handleNext = () => {

		setSelectedIndex((prevState) => prevState + 1);

	};



	return (

		<Inline alignBlock="center" spread="space-between">

			<Button isDisabled={selectedIndex === 0} onClick={handlePrev}>

				Previous

			</Button>

			<ProgressIndicator spacing="compact" selectedIndex={selectedIndex} values={values} />

			<Button isDisabled={selectedIndex === values.length - 1} onClick={handleNext}>

				Next

			</Button>

		</Inline>

	);

};



export default CompactExample;
```

## Interaction

If interaction is enabled, people can navigate to the selected step by selecting the corresponding dot indicator. Once the dots are in focus, people can also navigate using the keyboard arrow keys. Sit nulla est ex deserunt exercitation anim occaecat. Nostrud ullamco deserunt aute id consequat veniam incididunt duis in sint irure nisi. Mollit officia cillum Lorem ullamco minim nostrud elit officia tempor esse quis. Sit nulla est ex deserunt exercitation anim occaecat. Nostrud ullamco deserunt aute id consequat veniam incididunt duis in sint irure nisi. Mollit officia cillum Lorem ullamco minim nostrud elit officia tempor esse quis. Sit nulla est ex deserunt exercitation anim occaecat. Nostrud ullamco deserunt aute id consequat veniam incididunt duis in sint irure nisi. Mollit officia cillum Lorem ullamco minim nostrud elit officia tempor esse quis. 

```jsx
import React, { type ReactNode, useState } from 'react';



import Lorem from 'react-lorem-component';



import Button from '@atlaskit/button/new';

import { cssMap, cx } from '@atlaskit/css';

import { Box, Inline, Stack, Text } from '@atlaskit/primitives/compiled';

import { ProgressIndicator } from '@atlaskit/progress-indicator';



const styles = cssMap({

	displayBlock: { display: 'block' },

	displayNone: { display: 'none' },



	page: {

		maxWidth: '840px',

		marginInline: 'auto',

	},

});



const SpreadInlineLayout = ({ children }: { children: ReactNode }) => {

	return (

		<Inline space="space.100" spread="space-between" alignBlock="center">

			{children}

		</Inline>

	);

};



const Example = () => {

	const [selectedIndex, setSelectedIndex] = useState(0);

	const values = ['first', 'second', 'third'];



	const handlePrev = () => {

		setSelectedIndex((prevState) => prevState - 1);

	};



	const handleNext = () => {

		setSelectedIndex((prevState) => prevState + 1);

	};



	const handleSelect = ({

		event,

		index: selectedIndex,

	}: {

		event: React.MouseEvent<HTMLButtonElement>;

		index: number;

	}): void => {

		setSelectedIndex(selectedIndex);

	};



	return (

		<Box xcss={styles.page}>

			<Box paddingBlock="space.400">

				{values.map((v, i) => {

					const selected = i === selectedIndex;

					const panelId = `custom-panel${i}`;



					return (

						<Box

							aria-hidden={!selected}

							aria-labelledby={`tab${i}`}

							key={v}

							id={panelId}

							role="tabpanel"

						>

							<Stack

								space="space.100"

								xcss={cx(styles.displayBlock, !selected && styles.displayNone)}

							>

								<Text as="strong">Panel {i + 1}</Text>

								<Lorem count={1} />

							</Stack>

						</Box>

					);

				})}

			</Box>

			<SpreadInlineLayout>

				<Button isDisabled={selectedIndex === 0} onClick={handlePrev}>

					Previous

				</Button>

				<ProgressIndicator

					onSelect={handleSelect}

					ariaControls="custom-panel"

					selectedIndex={selectedIndex}

					values={values}

				/>

				<Button isDisabled={selectedIndex === values.length - 1} onClick={handleNext}>

					Next

				</Button>

			</SpreadInlineLayout>

		</Box>

	);

};



export default Example;
```

---

[View Original Documentation](https://atlassian.design/components/progress-indicator/examples)
