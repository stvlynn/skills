# Drawer (legacy)

Edit in code sandbox
(opens in a new window)

---

## Default

The default form of a drawer. Use either the label or titleId prop to announce the accessible name of the drawer to users of assistive technology. 

```jsx
import React, { useState } from 'react';



import Lorem from 'react-lorem-component';



import Button from '@atlaskit/button/new';

import Drawer from '@atlaskit/drawer';



const DrawerDefaultExample = () => {

	const [open, setOpen] = useState<boolean>(false);



	return (

		<>

			<Drawer label="Default drawer" onClose={() => setOpen(false)} isOpen={open}>

				<Lorem count={10} />

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

import Drawer, { type DrawerWidth } from '@atlaskit/drawer';

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

				{widths.map((width) => (

					<p>

						<Button isSelected={width === drawerWidth} onClick={() => setDrawerWidth(width)}>

							{width.charAt(0).toUpperCase()}

							{width.substring(1).toLowerCase()}

						</Button>

					</p>

				))}

			</Drawer>

			<Button appearance="primary" onClick={() => setOpen(true)}>

				See drawer widths

			</Button>

		</>

	);

};



export default DrawerWidths;
```

## Surface detection

The current surface CSS variable is set to the surface color of the drawer. You can use the utility.elevation.surface.current design token to style children with the current surface color. 

```jsx
/**

 * @jsxRuntime classic

 * @jsx jsx

 */

import { Fragment, useState } from 'react';



// eslint-disable-next-line @atlaskit/ui-styling-standard/use-compiled -- Ignored via go/DSP-18766

import { css, jsx } from '@emotion/react';

import Lorem from 'react-lorem-component';



import Button from '@atlaskit/button/new';

import Drawer from '@atlaskit/drawer';

import { token } from '@atlaskit/tokens';



const wrapperStyles = css({

	position: 'relative',

});



const contentStyles = css({

	padding: token('space.100'),

});



const headerStyles = css({

	padding: token('space.100'),

	position: 'sticky',

	backgroundColor: token('utility.elevation.surface.current'),

	borderBlockEnd: `1px solid ${token('color.border')}`,

	boxShadow: token('elevation.shadow.overflow'),

	insetBlockStart: 0,

	insetInlineEnd: 0,

	insetInlineStart: 0,

});



const DrawerSurfaceDetectionExample = () => {

	const [open, setOpen] = useState<boolean>(false);



	return (

		<Fragment>

			<Drawer onClose={() => setOpen(false)} isOpen={open} titleId="drawerTitle">

				<div css={wrapperStyles}>

					<div css={headerStyles}>

						<h1 id="drawerTitle">Header overlay</h1>

					</div>

					<div css={contentStyles}>

						<Lorem count={10} />

					</div>

				</div>

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

[View Original Documentation](https://atlassian.design/components/drawer/drawer-legacy/examples)
