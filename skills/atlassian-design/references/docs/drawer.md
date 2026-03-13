# Drawer

A drawer is a panel that slides in from the left side of the screen.

---

## Default

The default form of a drawer. Use either the label or titleId prop to announce the accessible name of the drawer to users of assistive technology. 

```jsx
import React, { useState } from 'react';



import Lorem from 'react-lorem-component';



import Button from '@atlaskit/button/new';

import { Drawer, DrawerCloseButton, DrawerContent, DrawerSidebar } from '@atlaskit/drawer/compiled';



const DrawerDefaultExample = () => {

	const [open, setOpen] = useState<boolean>(false);



	return (

		<>

			<Drawer label="Default drawer" onClose={() => setOpen(false)} isOpen={open}>

				<DrawerSidebar>

					<DrawerCloseButton />

				</DrawerSidebar>

				<DrawerContent>

					<Lorem count={10} />

				</DrawerContent>

			</Drawer>

			<Button appearance="primary" onClick={() => setOpen(true)}>

				Open drawer

			</Button>

		</>

	);

};



export default DrawerDefaultExample;
```

## Width

You can set the drawer's width to one of the predefined sizes. Use medium or wide for most applications. Use extended and full with caution, because there isn’t enough visual affordance that this is a drawer and not a new page. 

```jsx
import React, { useState } from 'react';



import Button from '@atlaskit/button/new';

import {

	Drawer,

	DrawerCloseButton,

	DrawerContent,

	DrawerSidebar,

	type DrawerWidth,

} from '@atlaskit/drawer/compiled';

import { widths } from '@atlaskit/drawer/constants';



const DrawerWidths = () => {

	const [open, setOpen] = useState<boolean>(false);

	const [drawerWidth, setDrawerWidth] = useState<DrawerWidth>('wide');



	return (

		<>

			<Drawer

				testId="drawer"

				width={drawerWidth}

				onClose={() => setOpen(false)}

				isOpen={open}

				label={`Drawer ${drawerWidth}`}

			>

				<DrawerSidebar>

					<DrawerCloseButton />

				</DrawerSidebar>

				<DrawerContent>

					{widths.map((width) => (

						<p>

							<Button isSelected={width === drawerWidth} onClick={() => setDrawerWidth(width)}>

								{width.charAt(0).toUpperCase()}

								{width.substring(1).toLowerCase()}

							</Button>

						</p>

					))}

				</DrawerContent>

			</Drawer>

			<Button appearance="primary" onClick={() => setOpen(true)}>

				See drawer widths

			</Button>

		</>

	);

};



export default DrawerWidths;
```

## Customization

### XCSS

You can customize the DrawerContent and DrawerSidebar components using the xcss prop. This prop allows you to apply a subset of styles that are consistent with the Design System. 

```jsx
/**

 * @jsxRuntime classic

 * @jsx jsx

 * @jsxFrag

 */



import React, { useState } from 'react';



import Lorem from 'react-lorem-component';



import Button from '@atlaskit/button/new';

import { cssMap, jsx } from '@atlaskit/css';

import { Drawer, DrawerCloseButton, DrawerContent, DrawerSidebar } from '@atlaskit/drawer/compiled';

import { token } from '@atlaskit/tokens';



const styles = cssMap({

	sidebar: {

		backgroundColor: token('color.background.accent.gray.subtlest'),

	},

	content: {

		marginTop: token('space.0'),

		paddingLeft: token('space.300'),

		paddingRight: token('space.300'),

		paddingTop: token('space.300'),

		paddingBottom: token('space.300'),

	},

});



export default function DrawerExample() {

	const [isDrawerOpen, setIsDrawerOpen] = useState(false);



	return (

		<>

			<Drawer isOpen={isDrawerOpen} label="Drawer with xcss" onClose={() => setIsDrawerOpen(false)}>

				<DrawerSidebar xcss={styles.sidebar}>

					<DrawerCloseButton />

				</DrawerSidebar>

				<DrawerContent xcss={styles.content}>

					<Lorem count={10} />

				</DrawerContent>

			</Drawer>

			<Button appearance="primary" onClick={() => setIsDrawerOpen(true)}>

				Open drawer

			</Button>

		</>

	);

}
```

### Composition

You can compose the DrawerContent, DrawerSidebar, and DrawerCloseButton components together as needed to create a custom drawer. Refer to the composing code guide for more information on effective composition with the Atlassian Design System. 

```jsx
/**

 * @jsxRuntime classic

 * @jsx jsx

 * @jsxFrag

 */



import React, { useState } from 'react';



import Lorem from 'react-lorem-component';



import Button from '@atlaskit/button/new';

import { cssMap, jsx } from '@atlaskit/css';

import { Drawer, DrawerCloseButton, DrawerContent } from '@atlaskit/drawer/compiled';

import { Stack, Text } from '@atlaskit/primitives';

import { token } from '@atlaskit/tokens';



const styles = cssMap({

	buttonLayout: {

		position: 'absolute',

		insetBlockStart: token('space.200'),

		insetInlineStart: token('space.200'),

	},

	content: {

		marginTop: token('space.0'),

		paddingLeft: token('space.300'),

		paddingRight: token('space.300'),

	},

	contentLayout: {

		height: '100%',

		display: 'flex',

		alignItems: 'center',

		textAlign: 'center',

	},

});



export default function DrawerExample() {

	const [isDrawerOpen, setIsDrawerOpen] = useState(false);



	return (

		<>

			<Drawer

				isOpen={isDrawerOpen}

				label="Drawer with customized composition"

				onClose={() => setIsDrawerOpen(false)}

			>

				<div css={styles.buttonLayout}>

					<DrawerCloseButton />

				</div>

				<DrawerContent xcss={styles.content}>

					<div css={styles.contentLayout}>

						<Stack space="space.200" alignInline="center">

							<Text size="large" weight="bold">

								Centered content

							</Text>

							<Lorem count={1} />

							<Button onClick={() => setIsDrawerOpen(false)}>Close</Button>

						</Stack>

					</div>

				</DrawerContent>

			</Drawer>

			<Button appearance="primary" onClick={() => setIsDrawerOpen(true)}>

				Open drawer

			</Button>

		</>

	);

}
```

## Surface detection

The current surface CSS variable is set to the surface color of the drawer. You can use the utility.elevation.surface.current design token to style children with the current surface color. 

```jsx
/**

 * @jsxRuntime classic

 * @jsx jsx

 */

import { Fragment, useState } from 'react';



import Lorem from 'react-lorem-component';



import Button from '@atlaskit/button/new';

import { cssMap, jsx } from '@atlaskit/css';

import { Drawer, DrawerCloseButton, DrawerContent, DrawerSidebar } from '@atlaskit/drawer/compiled';

import { token } from '@atlaskit/tokens';



const styles = cssMap({

	content: {

		position: 'relative',

		paddingTop: token('space.100'),

		paddingRight: token('space.100'),

		paddingBottom: token('space.100'),

		paddingLeft: token('space.100'),

	},

	header: {

		paddingTop: token('space.100'),

		paddingRight: token('space.100'),

		paddingBottom: token('space.100'),

		paddingLeft: token('space.100'),

		position: 'absolute',

		backgroundColor: token('utility.elevation.surface.current'),

		borderBlockEndColor: token('color.border'),

		borderBlockEndStyle: 'solid',

		borderBlockEndWidth: token('border.width'),

		boxShadow: token('elevation.shadow.overflow'),

		insetBlockStart: token('space.0'),

		insetInlineEnd: token('space.0'),

		insetInlineStart: token('space.0'),

	},

});



const DrawerSurfaceDetectionExample = () => {

	const [open, setOpen] = useState(false);



	return (

		<Fragment>

			<Drawer onClose={() => setOpen(false)} isOpen={open} label="Surface detection">

				<DrawerSidebar>

					<DrawerCloseButton />

				</DrawerSidebar>

				<DrawerContent>

					<div css={styles.content}>

						<div css={styles.header}>

							<h2>Header overlay</h2>

						</div>

						<Lorem count={2} />

					</div>

				</DrawerContent>

			</Drawer>

			<Button appearance="primary" onClick={() => setOpen(true)}>

				Open drawer

			</Button>

		</Fragment>

	);

};



export default DrawerSurfaceDetectionExample;
```

---

[View Original Documentation](https://atlassian.design/components/drawer/examples)
