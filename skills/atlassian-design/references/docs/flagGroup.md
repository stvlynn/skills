# Flag group

A flag group is used to group a set of related flags, with entry and exit animations.

---

## Default

Use FlagGroup to group a set of related flags, with entry and exit animation. 

```jsx
import React, { type ReactElement, type ReactNode, useCallback, useState } from 'react';



import Button from '@atlaskit/button/new';

import noop from '@atlaskit/ds-lib/noop';

import Flag, { FlagGroup } from '@atlaskit/flag';

import ErrorIcon from '@atlaskit/icon/glyph/error';

import InformationIcon from '@atlaskit/icon/glyph/info';

import SuccessIcon from '@atlaskit/icon/glyph/check-circle';

import WarningIcon from '@atlaskit/icon/glyph/warning';

import { Box } from '@atlaskit/primitives/compiled';

import { token } from '@atlaskit/tokens';



type flagData = {

	created: number;

	description: string;

	icon: ReactNode;

	id: number;

	key: number;

	title: string;

};



const getRandomIcon = (): ReactNode => {

	const icons = iconMap() as { [key: string]: ReactNode };

	const iconArray = Object.keys(icons).map((i) => icons[i]);

	return iconArray[Math.floor(Math.random() * iconArray.length)];

};



const iconMap = (key?: string) => {

	const icons: { [key: string]: ReactElement } = {

		info: (

			<InformationIcon

				label="Info"

				primaryColor={token('color.icon.information')}

			/>

		),

		success: (

			<SuccessIcon

				label="Success"

				primaryColor={token('color.icon.success')}

			/>

		),

		warning: (

			<WarningIcon

				label="Warning"

				primaryColor={token('color.icon.warning')}

			/>

		),

		error: (

			<ErrorIcon

				label="Error"

				primaryColor={token('color.icon.danger')}

			/>

		),

	};



	return key ? icons[key] : icons;

};



const getRandomDescription = () => {

	const descriptions = [

		'Marzipan croissant pie. Jelly beans gingerbread caramels brownie icing.',

		'Fruitcake topping wafer pie candy dragée sesame snaps cake. Cake cake cheesecake. Pie tiramisu carrot cake tart tart dessert cookie. Lemon drops cookie tootsie roll marzipan liquorice cotton candy brownie halvah.',

	];



	return descriptions[Math.floor(Math.random() * descriptions.length)];

};



const getFlagData = (index: number): flagData => {

	return {

		created: Date.now(),

		description: getRandomDescription(),

		icon: getRandomIcon(),

		id: index,

		key: index,

		title: `${index + 1}: Whoa a new flag!`,

	};

};



const FlagGroupExample = () => {

	const [flags, setFlags] = useState<Array<flagData>>([]);



	const addFlag = () => {

		setFlags((current) => [getFlagData(flags.length), ...current]);

	};



	const dismissFlag = useCallback(

		(id: string | number) => {

			setFlags((current) => current.filter((flag) => flag.id !== id));

		},

		[setFlags],

	);



	return (

		<Box>

			<Button appearance="primary" onClick={addFlag}>

				Add Flag

			</Button>

			<FlagGroup onDismissed={dismissFlag}>

				{flags.map((flag) => (

					<Flag

						actions={[

							{

								content: 'Nice one!',

								onClick: noop,

							},

							{

								content: 'Not right now thanks',

								onClick: () => dismissFlag(flag.id),

							},

						]}

						{...flag}

					/>

				))}

			</FlagGroup>

		</Box>

	);

};



export default FlagGroupExample;
```

## Using in modal components

By default, the flag group is rendered inside React.Portal. Use shouldRenderToParent prop to render the group in its direct parent instead of React.Portal. 

```jsx
import React, { useState } from 'react';



import Button from '@atlaskit/button/new';

import { Drawer, DrawerCloseButton, DrawerContent, DrawerSidebar } from '@atlaskit/drawer/compiled';

import Flag, { FlagGroup } from '@atlaskit/flag';

import InformationIcon from '@atlaskit/icon/glyph/info';

import { Box } from '@atlaskit/primitives/compiled';

import { token } from '@atlaskit/tokens';



const FlagsInDrawerExample = () => {

	const [open, setOpen] = useState<boolean>(false);

	const [flags, setFlags] = useState<Array<number>>([]);



	const addFlag = () => {

		const newFlagId = flags.length + 1;

		const newFlags = flags.slice();

		newFlags.splice(0, 0, newFlagId);



		setFlags(newFlags);

	};



	const handleDismiss = () => {

		setFlags(flags.slice(1));

	};



	return (

		<Box>

			<Drawer

				label="Default drawer"

				onClose={() => {

					setOpen(false);

					setFlags([]);

				}}

				isOpen={open}

			>

				<DrawerSidebar>

					<DrawerCloseButton />

				</DrawerSidebar>

				<DrawerContent>

					<Button onClick={addFlag}>Add flag</Button>

					<FlagGroup onDismissed={handleDismiss} shouldRenderToParent>

						{flags.map((flagId) => {

							return (

								<Flag

									id={flagId}

									icon={

										<InformationIcon

											label="Info"

											primaryColor={token('color.icon.information')}

										/>

									}

									key={flagId}

									title={`Flag #${flagId}`}

									description="Example flag description"

								/>

							);

						})}

					</FlagGroup>

				</DrawerContent>

			</Drawer>

			<Button appearance="primary" onClick={() => setOpen(true)}>

				Open drawer

			</Button>

		</Box>

	);

};



export default FlagsInDrawerExample;
```

---

[View Original Documentation](https://atlassian.design/components/flag/flag-group/examples)
