# Inline dialog

An inline dialog is a pop-up container for small amounts of information. It can also contain controls.

---

## Default

Inline dialogs are displayed when triggered by a user action, usually by clicking a button. Hello! 

```jsx
/**

 * @jsxRuntime classic

 * @jsx jsx

 */

import { Component } from 'react';



import Button from '@atlaskit/button/new';

import { cssMap, jsx } from '@atlaskit/css';

import InlineDialog from '@atlaskit/inline-dialog';

import { Box } from '@atlaskit/primitives/compiled';



const styles = cssMap({

	container: {

		minHeight: '120px',

	},

});



interface State {

	dialogOpen: boolean;

}



const content = (

	<Box>

		<p>Hello!</p>

	</Box>

);



export default class InlineDialogDefaultExample extends Component<{}, State> {

	state = {

		dialogOpen: true,

	};



	toggleDialog = () => this.setState({ dialogOpen: !this.state.dialogOpen });



	render() {

		return (

			<Box xcss={styles.container}>

				<InlineDialog

					onClose={() => {

						this.setState({ dialogOpen: false });

					}}

					content={content}

					isOpen={this.state.dialogOpen}

				>

					<Button

						appearance="primary"

						isSelected={this.state.dialogOpen}

						onClick={this.toggleDialog}

					>

						Click me!

					</Button>

				</InlineDialog>

			</Box>

		);

	}

}
```

## Positioning

Inline dialogs can appear at the top, bottom, left or right of the trigger with an additional three positions available for each location. The location of the dialog can be placed in context with the content on the page. Note that auto placements places the inline dialog on the side with the most available space. Current placement: auto-end. 

```jsx
import React, { Component } from 'react';



import Button from '@atlaskit/button/new';

import InlineDialog from '@atlaskit/inline-dialog';

import { token } from '@atlaskit/tokens';



import { Placements } from '../utils';



interface State {

	placementIndex: number;

}



const styles: React.CSSProperties = {

	alignItems: 'center',

	justifyContent: 'center',

	display: 'flex',

	flexDirection: 'column',

	height: '100%',

	width: '100%',

};



export default class InlineDialogPositioningExample extends Component<{}, State> {

	state = {

		placementIndex: 0,

	};



	cyclePlacement = () => {

		const { placementIndex } = this.state;

		if (placementIndex < Placements.length - 1) {

			this.setState({ placementIndex: placementIndex + 1 });

		} else {

			this.setState({ placementIndex: 0 });

		}

	};



	render() {

		return (

			// eslint-disable-next-line @atlaskit/ui-styling-standard/enforce-style-prop -- Ignored via go/DSP-18766

			<div style={styles}>

				<div

					style={{

						// eslint-disable-next-line @atlaskit/ui-styling-standard/enforce-style-prop -- Ignored via go/DSP-18766

						marginTop: token('space.1000'),

						// eslint-disable-next-line @atlaskit/ui-styling-standard/enforce-style-prop -- Ignored via go/DSP-18766

						marginBottom: token('space.1000'),

					}}

				>

					<InlineDialog

						content={

							<div>

								<p>

									Current placement: <strong>{Placements[this.state.placementIndex]}</strong>.

								</p>

							</div>

						}

						isOpen

						placement={Placements[this.state.placementIndex]}

					>

						<Button appearance="primary" onClick={this.cyclePlacement}>

							Cycle the placement

						</Button>

					</InlineDialog>

				</div>

			</div>

		);

	}

}
```

---

[View Original Documentation](https://atlassian.design/components/inline-dialog/examples)
