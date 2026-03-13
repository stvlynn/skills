# Blanket

A blanket covers the underlying UI for a layered component, such as a modal dialog or a tooltip.

---

## Default

A blanket overlays the rest of the page with a transparent grey when used with a modal or popup. An onBlanketClicked prop is provided to catch clicks elsewhere on the page other than the modal or popup. Blanket doesn't have its' own show/hide functionality, it should be controlled with its' parent element. 

```jsx
/**

 * @jsxRuntime classic

 * @jsx jsx

 */

import { useCallback, useState } from 'react';



import Blanket from '@atlaskit/blanket';

import Button from '@atlaskit/button/new';

import { jsx } from '@atlaskit/css';

import { Box } from '@atlaskit/primitives/compiled';



const BlanketBasicExample = () => {

	const [isBlanketVisible, setIsBlanketVisible] = useState(false);

	const [shouldAllowClickThrough, setShouldAllowClickThrough] = useState(true);



	const showBlanketClick = useCallback(() => {

		setIsBlanketVisible(true);

		setShouldAllowClickThrough(false);

	}, []);



	const onBlanketClicked = useCallback(() => {

		setIsBlanketVisible(false);

		setShouldAllowClickThrough(true);

	}, []);



	return (

		<Box>

			<Button appearance="default" onClick={showBlanketClick} testId="show-button">

				Show blanket

			</Button>

			<Blanket

				onBlanketClicked={onBlanketClicked}

				isTinted={isBlanketVisible}

				shouldAllowClickThrough={shouldAllowClickThrough}

				testId="basic-blanket"

			/>

		</Box>

	);

};



export default BlanketBasicExample;
```

## Clickthrough

If you enable the shouldAllowClickThrough prop, onBlanketClicked doesn't get called and the elements underneath the blanket can be interacted with directly. 

```jsx
import React, { useCallback, useState } from 'react';



import Blanket from '@atlaskit/blanket';

import Button from '@atlaskit/button/new';

import { Box } from '@atlaskit/primitives/compiled';



const BlanketClickthroughExample = () => {

	const [isBlanketVisible, setIsBlanketVisible] = useState(false);

	const showBlanketClick = useCallback(() => {

		setIsBlanketVisible((isBlanketVisible) => !isBlanketVisible);

	}, [setIsBlanketVisible]);

	return (

		<Box>

			<Button appearance="default" onClick={showBlanketClick}>

				{!isBlanketVisible ? 'Show blanket' : 'Hide blanket'}

			</Button>



			<Blanket isTinted={isBlanketVisible} shouldAllowClickThrough />

		</Box>

	);

};



export default BlanketClickthroughExample;
```

## Children

A blanket with children will exclude the children from being tinted by the blanket. Open this example in CodeSandbox for a full-page experience. 

```jsx
/**

 * @jsxRuntime classic

 * @jsx jsx

 */

import { useCallback, useState } from 'react';



import Blanket from '@atlaskit/blanket';

import Button from '@atlaskit/button/new';

import { cssMap, jsx } from '@atlaskit/css';

import { Box } from '@atlaskit/primitives/compiled';

import { token } from '@atlaskit/tokens';



const blanketChildStyles = cssMap({

	root: {

		// eslint-disable-next-line @atlaskit/ui-styling-standard/no-unsafe-values

		width: '50%' as any,

		marginTop: token('space.600'),

		marginRight: token('space.600'),

		marginBottom: token('space.600'),

		marginLeft: token('space.600'),

		paddingBlock: token('space.300'),

		backgroundColor: token('elevation.surface'),

	},

});



const BlanketWithChildrenExample = () => {

	const [isBlanketVisible, setIsBlanketVisible] = useState(false);

	const [shouldAllowClickThrough, setShouldAllowClickThrough] = useState(true);



	const showBlanketClick = useCallback(() => {

		setIsBlanketVisible(true);

		setShouldAllowClickThrough(false);

	}, []);



	const onBlanketClicked = useCallback(() => {

		setIsBlanketVisible(false);

		setShouldAllowClickThrough(true);

	}, []);



	return (

		<Box>

			<Button appearance="default" onClick={showBlanketClick} testId="show-button">

				Show blanket

			</Button>



			<Blanket

				onBlanketClicked={onBlanketClicked}

				isTinted={isBlanketVisible}

				shouldAllowClickThrough={shouldAllowClickThrough}

				testId="blanket-with-children"

			>

				<Box xcss={blanketChildStyles.root}>

					Click "Show blanket" button to open the blanket & click the blanket to dismiss it.

				</Box>

			</Blanket>

		</Box>

	);

};



export default BlanketWithChildrenExample;
```

---

[View Original Documentation](https://atlassian.design/components/blanket/examples)
