# Modal dialog

A modal dialog displays content that requires user interaction, in a layer above the page.

---

## Default

The default form of a modal dialog. 

```jsx
import React, { Fragment, useCallback, useState } from 'react';



import Button from '@atlaskit/button/new';

import Modal, {

	ModalBody,

	ModalFooter,

	ModalHeader,

	ModalTitle,

	ModalTransition,

} from '@atlaskit/modal-dialog';

import { Text } from '@atlaskit/primitives/compiled';



export default function Example() {

	const [isOpen, setIsOpen] = useState(false);

	const openModal = useCallback(() => setIsOpen(true), []);

	const closeModal = useCallback(() => setIsOpen(false), []);



	return (

		<Fragment>

			<Button aria-haspopup="dialog" appearance="primary" onClick={openModal}>

				Open modal

			</Button>



			<ModalTransition>

				{isOpen && (

					<Modal onClose={closeModal}>

						<ModalHeader hasCloseButton>

							<ModalTitle>Duplicate this page</ModalTitle>

						</ModalHeader>

						<ModalBody>

							Duplicating this page will make it a child page of{' '}

							<Text weight="bold">Search - user exploration</Text>, in the{' '}

							<Text weight="bold">Search & Smarts</Text> space.

						</ModalBody>

						<ModalFooter>

							<Button appearance="subtle" onClick={closeModal}>

								Cancel

							</Button>

							<Button appearance="primary" onClick={closeModal}>

								Duplicate

							</Button>

						</ModalFooter>

					</Modal>

				)}

			</ModalTransition>

		</Fragment>

	);

}
```

## Appearance

You can give the modal warning or danger styling to indicate the severity of the action or message. The appearance needs to be set on both the modal title and the primary button. 

### Warning

Use a warning modal to help inform people of a significant change. If the warning comes before an action, clearly communicate what will happen if they proceed and provide an alternative or opt-out where possible. 

```jsx
import React, { useCallback, useState } from 'react';



import Button from '@atlaskit/button/new';

import Modal, {

	ModalBody,

	ModalFooter,

	ModalHeader,

	ModalTitle,

	ModalTransition,

} from '@atlaskit/modal-dialog';



export default function Example() {

	const [isOpen, setIsOpen] = useState(false);

	const openModal = useCallback(() => setIsOpen(true), []);

	const closeModal = useCallback(() => setIsOpen(false), []);



	return (

		<>

			<Button aria-haspopup="dialog" appearance="primary" onClick={openModal}>

				Open modal

			</Button>



			<ModalTransition>

				{isOpen && (

					<Modal onClose={closeModal}>

						<ModalHeader hasCloseButton>

							<ModalTitle appearance="warning">Move your page to the Design team space</ModalTitle>

						</ModalHeader>

						<ModalBody>

							If you move this page to the Design system space, your access permissions will change

							to view only. You'll need to ask the space admin for edit access.

						</ModalBody>

						<ModalFooter>

							<Button appearance="subtle">Cancel</Button>

							<Button appearance="warning" onClick={closeModal}>

								Move page

							</Button>

						</ModalFooter>

					</Modal>

				)}

			</ModalTransition>

		</>

	);

}
```

### Danger

Use danger modals to alert people when something potentially destructive or irreversible will happen if they continue. Explain the problem and provide a next step or an alternative. 

```jsx
import React, { useCallback, useState } from 'react';



import Button from '@atlaskit/button/new';

import Modal, {

	ModalBody,

	ModalFooter,

	ModalHeader,

	ModalTitle,

	ModalTransition,

} from '@atlaskit/modal-dialog';



export default function Example() {

	const [isOpen, setIsOpen] = useState(false);

	const openModal = useCallback(() => setIsOpen(true), []);

	const closeModal = useCallback(() => setIsOpen(false), []);



	return (

		<>

			<Button aria-haspopup="dialog" appearance="primary" onClick={openModal}>

				Open modal

			</Button>



			<ModalTransition>

				{isOpen && (

					<Modal onClose={closeModal}>

						<ModalHeader hasCloseButton>

							<ModalTitle appearance="danger">You’re about to delete this page</ModalTitle>

						</ModalHeader>

						<ModalBody>

							<p>Before you delete it permanently, there’s some things you should know:</p>

							<ul>

								<li>4 pages have links to this page that will break</li>

								<li>2 child pages will be left behind in the page tree</li>

							</ul>

						</ModalBody>

						<ModalFooter>

							<Button appearance="subtle">Cancel</Button>

							<Button appearance="danger" onClick={closeModal}>

								Delete

							</Button>

						</ModalFooter>

					</Modal>

				)}

			</ModalTransition>

		</>

	);

}
```

## Width

There are multiple ways to specify the width of a modal. We recommend using named size options to specify modal width. 

```jsx
import React, { useCallback, useState } from 'react';



import ButtonGroup from '@atlaskit/button/button-group';

import Button from '@atlaskit/button/new';

import Modal, {

	ModalBody,

	ModalFooter,

	ModalHeader,

	ModalTitle,

	ModalTransition,

} from '@atlaskit/modal-dialog';



export default function Example() {

	const [isOpen, setIsOpen] = useState(false);

	const [width, setWidth] = useState('medium');



	const closeModal = useCallback(() => setIsOpen(false), [setIsOpen]);

	const setWidthAndOpen = useCallback(

		(newWidth: string) => {

			setWidth(newWidth);

			requestAnimationFrame(() => setIsOpen(true));

		},

		[setWidth, setIsOpen],

	);



	return (

		<>

			<ButtonGroup label="Choose modal width">

				<Button

					aria-haspopup="dialog"

					appearance="primary"

					onClick={() => setWidthAndOpen('small')}

				>

					small

				</Button>

				<Button

					aria-haspopup="dialog"

					appearance="primary"

					onClick={() => setWidthAndOpen('medium')}

				>

					medium

				</Button>

				<Button

					aria-haspopup="dialog"

					appearance="primary"

					onClick={() => setWidthAndOpen('large')}

				>

					large

				</Button>

				<Button

					aria-haspopup="dialog"

					appearance="primary"

					onClick={() => setWidthAndOpen('x-large')}

				>

					x-large

				</Button>

			</ButtonGroup>



			<ModalTransition>

				{isOpen && (

					<Modal onClose={closeModal} width={width}>

						<ModalHeader hasCloseButton>

							<ModalTitle>Set up your own projects</ModalTitle>

						</ModalHeader>

						<ModalBody>

							We simplified the way you set up issue types, workflows, fields, and screens. Check

							out the new, independent project experience to see it in action.

						</ModalBody>

						<ModalFooter>

							<Button appearance="subtle">Skip</Button>

							<Button appearance="primary" onClick={closeModal}>

								Get started

							</Button>

						</ModalFooter>

					</Modal>

				)}

			</ModalTransition>

		</>

	);

}
```

## Focus management

Once open, focus immediately moves to the container (modal window) when rendered so a user is aware they are inside a modal. View focus order. Pass the autoFocus prop an element ref to focus on a specific element. 

```jsx
import React, { useCallback, useRef, useState } from 'react';



import Breadcrumbs, { BreadcrumbsItem } from '@atlaskit/breadcrumbs';

import Button from '@atlaskit/button/new';

import { cssMap } from '@atlaskit/css';

import { Field } from '@atlaskit/form';

import Modal, {

	CloseButton,

	ModalBody,

	ModalFooter,

	ModalHeader,

	ModalTitle,

	ModalTransition,

} from '@atlaskit/modal-dialog';

import { Flex } from '@atlaskit/primitives/compiled';

import Textfield from '@atlaskit/textfield';



const styles = cssMap({

	header: {

		flexDirection: 'row-reverse',

		width: '100%',

	},

	headerEnd: {

		flexDirection: 'row-reverse',

	},

});



export default function Example() {

	const [isOpen, setIsOpen] = useState(false);

	const openModal = useCallback(() => setIsOpen(true), []);

	const closeModal = useCallback(() => setIsOpen(false), []);

	const focusRef = useRef<HTMLSpanElement>(null);



	return (

		<>

			<Button aria-haspopup="dialog" appearance="primary" onClick={openModal}>

				Open modal

			</Button>



			<ModalTransition>

				{isOpen && (

					<Modal autoFocus={focusRef} onClose={closeModal}>

						<ModalHeader hasCloseButton={false}>

							<Flex alignItems="center" justifyContent="space-between" xcss={styles.header}>

								<Flex alignItems="center" gap="space.200" xcss={styles.headerEnd}>

									{/* We have the close button first in the DOM and then are

									reversing it using the flex styles to ensure that it is

									focused as the first interactive element in the modal,

									*before* any other relevant content inside the modal. This

									ensures users of assistive technology get all relevant

									content. */}

									<CloseButton onClick={closeModal} />

									<Breadcrumbs>

										<BreadcrumbsItem href="https://atlassian.design/" text="Projects" />

										<BreadcrumbsItem href="https://atlassian.design/" text="Design System Team" />

									</Breadcrumbs>

								</Flex>

								<ModalTitle>

									<span tabIndex={-1} ref={focusRef}>

										Sign up

									</span>

								</ModalTitle>

							</Flex>

						</ModalHeader>

						<ModalBody>

							<Field label="Email" name="my-email" defaultValue="">

								{({ fieldProps }) => <Textfield autoComplete="off" {...fieldProps} />}

							</Field>

						</ModalBody>

						<ModalFooter>

							<Button appearance="subtle">Account settings</Button>

							<Button appearance="primary" onClick={closeModal}>

								Sign up

							</Button>

						</ModalFooter>

					</Modal>

				)}

			</ModalTransition>

		</>

	);

}
```

## Scrolling behavior

While you can set the width of the modal, the content determines the height of the modal. Once it reaches a certain threshold, the body content will scroll while the header and footer remain fixed until the user reaches the bottom of the modal dialog. You can configure the scroll behavior of modals so that scrolling happens inside the modal body or outside the modal, within the viewport. In either case, modals prevent the window from being scrolled both natively and programatically. This will prevent browser issues such as scrollIntoView scrolling the window instead of only the closest scroll parent. 

```jsx
import React, { useCallback, useState } from 'react';



import ButtonGroup from '@atlaskit/button/button-group';

import Button from '@atlaskit/button/new';

import Heading from '@atlaskit/heading';

import Modal, {

	ModalBody,

	ModalFooter,

	ModalHeader,

	ModalTitle,

	ModalTransition,

} from '@atlaskit/modal-dialog';



export default function Example() {

	const [shouldScrollInViewport, setShouldScrollInViewport] = useState(false);

	const [isOpen, setIsOpen] = useState(false);



	const closeModal = useCallback(() => setIsOpen(false), [setIsOpen]);

	const setShouldScrollInViewportAndOpen = useCallback(

		(shouldScrollInViewport: boolean) => {

			setShouldScrollInViewport(shouldScrollInViewport);

			requestAnimationFrame(() => setIsOpen(true));

		},

		[setShouldScrollInViewport],

	);



	return (

		<>

			<ButtonGroup label="Choose scroll option">

				<Button

					aria-haspopup="dialog"

					appearance="primary"

					onClick={() => setShouldScrollInViewportAndOpen(false)}

				>

					Scroll inside body

				</Button>

				<Button aria-haspopup="dialog" onClick={() => setShouldScrollInViewportAndOpen(true)}>

					Scroll inside viewport

				</Button>

			</ButtonGroup>



			<ModalTransition>

				{isOpen && (

					<Modal onClose={closeModal} shouldScrollInViewport={shouldScrollInViewport} height={600}>

						<ModalHeader hasCloseButton>

							<ModalTitle>Our voice and tone</ModalTitle>

						</ModalHeader>

						<ModalBody>

							<Heading as="h3" size="medium">

								Be bold

							</Heading>

							<p>

								Motivate teams to do their best work. Offer best practices to get users going in the

								right direction. Be bold and offer just enough help to get the work started, and

								then get out of the way. Give accurate information so users can make educated

								decisions. Know your user's struggles and desired outcomes and give just enough

								information to let them get where they need to go.

							</p>



							<Heading as="h3" size="medium">

								Be optimistic

							</Heading>



							<p>

								Focusing on the details gives people confidence in our products. Weave a consistent

								story across our fabric and be diligent about vocabulary across all messaging by

								being brand conscious across products to create a seamless flow across all the

								things. Let people know that they can jump in and start working expecting to find a

								dependable experience across all the things. Keep teams in the loop about what is

								happening by informing them of relevant features, products and opportunities for

								success. Be on the journey with them and highlight the key points that will help

								them the most - right now. Be in the moment by focusing attention on the important

								bits first.

							</p>



							<Heading as="h3" size="medium">

								Be practical, with a wink

							</Heading>



							<p>

								Keep our own story short and give teams just enough to get moving. Get to the point

								and be direct. Be concise - we tell the story of how we can help, but we do it

								directly and with purpose. Be on the lookout for opportunities and be quick to offer

								a helping hand. At the same time realize that nobody likes a nosy neighbor. Give the

								user just enough to know that something awesome is around the corner and then get

								out of the way. Write clear, accurate, and concise text that makes interfaces more

								usable and consistent - and builds trust. We strive to write text that is

								understandable by anyone, anywhere, regardless of their culture or language so that

								everyone feels they are part of the team.

							</p>

						</ModalBody>

						<ModalFooter>

							<Button appearance="primary" onClick={closeModal}>

								Close

							</Button>

						</ModalFooter>

					</Modal>

				)}

			</ModalTransition>

		</>

	);

}
```

## Form

These internal components can be wrapped in a form element to support having buttons of type submit in the footer. 

```jsx
import React, { Fragment, useCallback, useState } from 'react';



import Button from '@atlaskit/button/new';

import Form, { Field, HelperMessage } from '@atlaskit/form';

import Modal, {

	ModalBody,

	ModalFooter,

	ModalHeader,

	ModalTitle,

	ModalTransition,

} from '@atlaskit/modal-dialog';

import Textfield from '@atlaskit/textfield';



export default function Example() {

	const [isOpen, setIsOpen] = useState(false);

	const [name, setName] = useState('');



	const openModal = useCallback(() => setIsOpen(true), []);

	const closeModal = useCallback(() => setIsOpen(false), []);



	const onSubmit = useCallback(

		(data: Record<string, any>) => {

			console.log(data);

			setName(data.name);

		},

		[setName],

	);



	return (

		<>

			<Button aria-haspopup="dialog" appearance="primary" onClick={openModal}>

				Open modal

			</Button>



			<ModalTransition>

				{isOpen && (

					<Modal onClose={closeModal}>

						<Form onSubmit={onSubmit}>

							{({ formProps }) => (

								<form {...formProps} id="modal-form">

									<ModalHeader hasCloseButton>

										<ModalTitle>Create a user</ModalTitle>

									</ModalHeader>

									<ModalBody>

										<Field

											id="name"

											name="name"

											label="Type your name to continue"

											defaultValue="Ian Atlas"

										>

											{({ fieldProps }) => (

												<Fragment>

													<Textfield {...fieldProps} />

													<HelperMessage>{name ? `Hello, ${name}` : ''}</HelperMessage>

												</Fragment>

											)}

										</Field>

									</ModalBody>

									<ModalFooter>

										<Button appearance="subtle" onClick={closeModal}>

											Close

										</Button>

										<Button appearance="primary" type="submit">

											Create

										</Button>

									</ModalFooter>

								</form>

							)}

						</Form>

					</Modal>

				)}

			</ModalTransition>

		</>

	);

}
```

### Select

The usage of the select component within the modal dialog requires the menuPosition value set to fixed. Without this, it will not show up on top of the modal dialog, and instead will remain within it's boundaries. In some cases, this causes the select to visually seem like it is not opening whatsoever when being interacted with. No country has been selected yet. 

```jsx
import React, { useCallback, useState } from 'react';



import Button from '@atlaskit/button/new';

import { Code } from '@atlaskit/code';

import Form, { Field } from '@atlaskit/form';

import ModalDialog, {

	ModalBody,

	ModalFooter,

	ModalHeader,

	ModalTitle,

	ModalTransition,

} from '@atlaskit/modal-dialog';

import Select, { OptionType as Option, ValueType as Value } from '@atlaskit/select';



export default function ModalDialogSelect() {

	const [isOpen, setIsOpen] = useState(false);

	const [country, setCountry] = useState<Option>();



	const openModal = useCallback(() => setIsOpen(true), []);

	const closeModal = useCallback(() => setIsOpen(false), []);



	const onSubmit = useCallback(

		(data: Record<string, any>) => {

			console.log(data);

			setCountry(data.country);

			closeModal();

		},

		[closeModal, setCountry],

	);



	return (

		<>

			<Button

				aria-haspopup="dialog"

				appearance="primary"

				onClick={openModal}

				testId="modal-trigger"

			>

				Open Modal

			</Button>

			<p>

				{country

					? `The country selected is '${country.label}'.`

					: 'No country has been selected yet.'}

			</p>



			<ModalTransition>

				{isOpen && (

					<ModalDialog onClose={closeModal} testId="modal">

						<ModalHeader hasCloseButton>

							<ModalTitle>Using select in a modal dialog</ModalTitle>

						</ModalHeader>

						<ModalBody>

							<p>

								This select should open and be visible on top of the modal dialog. This is because

								of the usage of <Code>menuPosition="fixed"</Code> on <Code>@atlaskit/select</Code>.

							</p>

							<Form onSubmit={onSubmit}>

								{({ formProps }) => (

									<form {...formProps} id="modal-form">

										<Field<Value<Option, true>> name="country" label="Country of residence">

											{({ fieldProps }) => (

												<Select<Option, true>

													{...fieldProps}

													menuPosition="fixed"

													options={[

														{ label: 'Adelaide', value: 'adelaide' },

														{ label: 'Brisbane', value: 'brisbane' },

														{ label: 'Canberra', value: 'canberra' },

														{ label: 'Darwin', value: 'darwin' },

														{ label: 'Hobart', value: 'hobart' },

														{ label: 'Melbourne', value: 'melbourne' },

														{ label: 'Perth', value: 'perth' },

														{ label: 'Sydney', value: 'sydney' },

													]}

												/>

											)}

										</Field>

									</form>

								)}

							</Form>

						</ModalBody>

						<ModalFooter>

							<Button appearance="subtle" onClick={closeModal}>

								Close

							</Button>

							<Button appearance="primary" type="submit" form="modal-form">

								Submit

							</Button>

						</ModalFooter>

					</ModalDialog>

				)}

			</ModalTransition>

		</>

	);

}
```

## Modal header

```jsx
import React, { Fragment, useCallback, useState } from 'react';



import Button from '@atlaskit/button/new';

import Modal, {

	ModalBody,

	ModalFooter,

	ModalHeader,

	ModalTitle,

	ModalTransition,

} from '@atlaskit/modal-dialog';



export default function Example() {

	const [isOpen, setIsOpen] = useState(false);

	const openModal = useCallback(() => setIsOpen(true), []);

	const closeModal = useCallback(() => setIsOpen(false), []);



	return (

		<Fragment>

			<Button aria-haspopup="dialog" appearance="primary" onClick={openModal}>

				Open modal

			</Button>



			<ModalTransition>

				{isOpen && (

					<Modal onClose={closeModal}>

						<ModalHeader hasCloseButton>

							<ModalTitle>Default modal header</ModalTitle>

						</ModalHeader>

						<ModalBody>

							<p>

								If you wish to customise a modal dialog, it accepts any valid React element as

								children.

							</p>



							<p>

								Modal header accepts any valid React element as children, so you can use modal title

								in conjunction with other elements like an exit button in the top right.

							</p>



							<p>

								Modal footer accepts any valid React element as children. For example, you can add

								an avatar in the footer. For very custom use cases, you can achieve the same thing

								without modal footer.

							</p>

						</ModalBody>

						<ModalFooter>

							<Button appearance="subtle">About modals</Button>

							<Button appearance="primary" onClick={closeModal}>

								Close

							</Button>

						</ModalFooter>

					</Modal>

				)}

			</ModalTransition>

		</Fragment>

	);

}
```

### Custom modal header

For very custom use cases, you can achieve the same thing without the modal header. A title is required, however, so use either a titleId if there's a visible title or a label if there isn’t a title. To make sure the modal is accessible, call useModal and set titleId as the id on the heading. 

```jsx
import React, { Fragment, useCallback, useState } from 'react';



import Button from '@atlaskit/button/new';

import { cssMap } from '@atlaskit/css';

import Heading from '@atlaskit/heading';

import Modal, {

	CloseButton,

	ModalBody,

	ModalFooter,

	ModalTransition,

	useModal,

} from '@atlaskit/modal-dialog';

import { Box } from '@atlaskit/primitives/compiled';



const styles = cssMap({

	header: {

		display: 'flex',

		alignItems: 'center',

		justifyContent: 'space-between',

		flexDirection: 'row-reverse',

	},

});



const CustomHeader = () => {

	const { onClose, titleId } = useModal();

	return (

		<Box xcss={styles.header} padding="space.300">

			{/* We have the close button first in the DOM and then are reversing it

			using the flex styles to ensure that it is focused as the first

			interactive element in the modal, *before* any other relevant content

			inside the modal. This ensures users of assistive technology get all

			relevant content. */}

			<CloseButton onClick={onClose} />

			<Heading as="h1" size="medium" id={titleId}>

				Custom modal header

			</Heading>

		</Box>

	);

};



export default function Example() {

	const [isOpen, setIsOpen] = useState(false);

	const openModal = useCallback(() => setIsOpen(true), []);

	const closeModal = useCallback(() => setIsOpen(false), []);



	return (

		<Fragment>

			<Button aria-haspopup="dialog" appearance="primary" onClick={openModal}>

				Open modal

			</Button>



			<ModalTransition>

				{isOpen && (

					// This is fixed in the custom header

					// eslint-disable-next-line @atlaskit/design-system/use-modal-dialog-close-button

					<Modal onClose={closeModal}>

						<CustomHeader />

						<ModalBody>

							<p>

								If you wish to customise a modal dialog, it accepts any valid React element as

								children.

							</p>



							<p>

								Modal header accepts any valid React element as children, so you can use modal title

								in conjunction with other elements like an exit button in the top right.

							</p>



							<p>

								Modal footer accepts any valid React element as children. For example, you can add

								an avatar in the footer. For very custom use cases, you can achieve the same thing

								without modal footer.

							</p>

						</ModalBody>

						<ModalFooter>

							<Button appearance="subtle">About modals</Button>

							<Button appearance="primary" onClick={closeModal}>

								Close

							</Button>

						</ModalFooter>

					</Modal>

				)}

			</ModalTransition>

		</Fragment>

	);

}
```

## Modal footer

The modal footer accepts any valid React element as children. For example, you can add an avatar in the footer. 

```jsx
/**

 * @jsxRuntime classic

 * @jsx jsx

 */

import { Fragment, useCallback, useState } from 'react';



import Avatar from '@atlaskit/avatar';

import Button from '@atlaskit/button/new';

import { cssMap, jsx } from '@atlaskit/css';

import Modal, {

	ModalBody,

	ModalFooter,

	ModalHeader,

	ModalTitle,

	ModalTransition,

} from '@atlaskit/modal-dialog';

import { Flex, Text } from '@atlaskit/primitives/compiled';



const styles = cssMap({

	footer: { flex: '1' },

});



export default function Example() {

	const [isOpen, setIsOpen] = useState(false);



	const openModal = useCallback(() => setIsOpen(true), []);

	const closeModal = useCallback(() => setIsOpen(false), []);



	return (

		<Fragment>

			<Button aria-haspopup="dialog" appearance="primary" onClick={openModal}>

				Open modal

			</Button>



			<ModalTransition>

				{isOpen && (

					<Modal onClose={closeModal}>

						<ModalHeader hasCloseButton>

							<ModalTitle>Default modal footer</ModalTitle>

						</ModalHeader>

						<ModalBody>

							<p>

								If you wish to customise a modal dialog, it accepts any valid React element as

								children.

							</p>



							<p>

								Modal header accepts any valid React element as children, so you can use modal title

								in conjunction with other elements like an exit button in the top right.

							</p>



							<p>

								Modal footer accepts any valid React element as children. For example, you can add

								an avatar in the footer. For very custom use cases, you can achieve the same thing

								without modal footer.

							</p>

						</ModalBody>

						<ModalFooter>

							<Flex xcss={styles.footer} justifyContent="space-between">

								<Flex alignItems="center" gap="space.100">

									<Avatar

										size="small"

										src="https://pbs.twimg.com/profile_images/803832195970433027/aaoG6PJI_400x400.jpg"

									/>

									<Text>Hey there!</Text>

								</Flex>

								<Button appearance="primary" onClick={closeModal}>

									Close

								</Button>

							</Flex>

						</ModalFooter>

					</Modal>

				)}

			</ModalTransition>

		</Fragment>

	);

}
```

### Custom modal footer

For very custom use cases, you can achieve the same thing without the modal footer. 

```jsx
/**

 * @jsxRuntime classic

 * @jsx jsx

 */

import { Fragment, useCallback, useState } from 'react';



import { jsx } from '@compiled/react';



import Avatar from '@atlaskit/avatar';

import Button from '@atlaskit/button/new';

import { cssMap } from '@atlaskit/css';

import Modal, {

	ModalBody,

	ModalHeader,

	ModalTitle,

	ModalTransition,

	useModal,

} from '@atlaskit/modal-dialog';

import { Box, Flex, Text } from '@atlaskit/primitives/compiled';



const styles = cssMap({

	footer: { display: 'flex', alignItems: 'center', justifyContent: 'space-between' },

});



const CustomFooter = () => {

	const { onClose } = useModal();



	return (

		<Box xcss={styles.footer} padding="space.300">

			<Flex alignItems="center" gap="space.100">

				<Avatar

					size="small"

					src="https://pbs.twimg.com/profile_images/803832195970433027/aaoG6PJI_400x400.jpg"

				/>

				<Text>Hey there!</Text>

			</Flex>

			<Button appearance="primary" onClick={onClose}>

				Close

			</Button>

		</Box>

	);

};



export default function Example() {

	const [isOpen, setIsOpen] = useState(false);

	const openModal = useCallback(() => setIsOpen(true), []);

	const closeModal = useCallback(() => setIsOpen(false), []);



	return (

		<Fragment>

			<Button aria-haspopup="dialog" appearance="primary" onClick={openModal}>

				Open modal

			</Button>



			<ModalTransition>

				{isOpen && (

					<Modal onClose={closeModal}>

						<ModalHeader hasCloseButton>

							<ModalTitle>Custom modal footer</ModalTitle>

						</ModalHeader>

						<ModalBody>

							<p>

								If you wish to customise a modal dialog, it accepts any valid React element as

								children.

							</p>



							<p>

								Modal header accepts any valid React element as children, so you can use modal title

								in conjunction with other elements like an exit button in the top right.

							</p>



							<p>

								Modal footer accepts any valid React element as children. For example, you can add

								an avatar in the footer. For very custom use cases, you can achieve the same thing

								without modal footer.

							</p>

						</ModalBody>

						<CustomFooter />

					</Modal>

				)}

			</ModalTransition>

		</Fragment>

	);

}
```

## Surface detection

The current surface CSS variable is set to the surface color of the modal. You can use the utility.elevation.surface.current design token to style children with the current surface color. 

```jsx
import React, { Fragment, useCallback, useState } from 'react';



import Button from '@atlaskit/button/new';

import { cssMap } from '@atlaskit/css';

import Heading from '@atlaskit/heading';

import Modal, {

	ModalBody,

	ModalFooter,

	ModalHeader,

	ModalTitle,

	ModalTransition,

} from '@atlaskit/modal-dialog';

import { Box } from '@atlaskit/primitives/compiled';



const styles = cssMap({

	container: {

		position: 'relative',

	},

	sticky: {

		position: 'sticky',

	},

});



function SurfaceAwareBox() {

	return (

		<Box padding="space.250" backgroundColor="utility.elevation.surface.current">

			A surface aware box. The background color depends on the surface it's placed on.

		</Box>

	);

}



export default function Example() {

	const [isOpen, setIsOpen] = useState(false);

	const closeModal = useCallback(() => setIsOpen(false), [setIsOpen]);



	return (

		<Fragment>

			<Button aria-haspopup="dialog" appearance="primary" onClick={() => setIsOpen(true)}>

				Open modal

			</Button>

			<SurfaceAwareBox />

			<ModalTransition>

				{isOpen && (

					<Modal onClose={closeModal} height={600}>

						<ModalHeader hasCloseButton>

							<ModalTitle>Our voice and tone</ModalTitle>

						</ModalHeader>

						<ModalBody>

							<Box xcss={styles.container}>

								<Box xcss={styles.sticky} paddingBlockStart="space.0" paddingBlockEnd="space.0">

									<SurfaceAwareBox />

								</Box>

								<Heading as="h3" size="medium">

									Be bold

								</Heading>

								<p>

									Motivate teams to do their best work. Offer best practices to get users going in

									the right direction. Be bold and offer just enough help to get the work started,

									and then get out of the way. Give accurate information so users can make educated

									decisions. Know your user's struggles and desired outcomes and give just enough

									information to let them get where they need to go.

								</p>



								<Heading as="h3" size="medium">

									Be optimistic

								</Heading>



								<p>

									Focusing on the details gives people confidence in our products. Weave a

									consistent story across our fabric and be diligent about vocabulary across all

									messaging by being brand conscious across products to create a seamless flow

									across all the things. Let people know that they can jump in and start working

									expecting to find a dependable experience across all the things. Keep teams in the

									loop about what is happening by informing them of relevant features, products and

									opportunities for success. Be on the journey with them and highlight the key

									points that will help them the most - right now. Be in the moment by focusing

									attention on the important bits first.

								</p>



								<Heading as="h3" size="medium">

									Be practical, with a wink

								</Heading>



								<p>

									Keep our own story short and give teams just enough to get moving. Get to the

									point and be direct. Be concise - we tell the story of how we can help, but we do

									it directly and with purpose. Be on the lookout for opportunities and be quick to

									offer a helping hand. At the same time realize that nobody likes a nosy neighbor.

									Give the user just enough to know that something awesome is around the corner and

									then get out of the way. Write clear, accurate, and concise text that makes

									interfaces more usable and consistent - and builds trust. We strive to write text

									that is understandable by anyone, anywhere, regardless of their culture or

									language so that everyone feels they are part of the team.

								</p>

							</Box>

						</ModalBody>

						<ModalFooter>

							<Button appearance="primary" onClick={closeModal}>

								Close

							</Button>

						</ModalFooter>

					</Modal>

				)}

			</ModalTransition>

		</Fragment>

	);

}
```

---

[View Original Documentation](https://atlassian.design/components/modal-dialog/examples)
