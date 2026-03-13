# Benefits modal

A benefits modal explains the benefits of a significant new feature or experience change.

---

## Use with caution

You can use a benefits modal to explain large or impactful updates. All benefits modals should include a heading and actions. Include an illustration with all benefits modals. If you feel that the story isn't strong enough to require one, use a spotlight instead. 

## Using @atlaskit/modal-dialog

```jsx
import React, { useCallback, useState } from 'react';



import ButtonGroup from '@atlaskit/button/button-group';

import Button from '@atlaskit/button/new';

import Image from '@atlaskit/image';

import Modal, { CloseButton, ModalTitle, ModalTransition } from '@atlaskit/modal-dialog';

import { Box, Stack, xcss } from '@atlaskit/primitives';

import { token } from '@atlaskit/tokens';



import welcomeImage from '../assets/this-is-new-jira.png';



const containerStyles = xcss({

	position: 'relative',

});



const closeContainerStyles = xcss({

	position: 'absolute',

	insetBlockStart: 'space.100',

	insetInlineEnd: 'space.100',

	backgroundColor: 'color.background.accent.gray.subtlest',

	borderColor: 'color.border.input',

	borderRadius: token('space.050'),

	borderStyle: 'solid',

	borderWidth: token('space.025'),

});



export default function Example() {

	const [isOpen, setIsOpen] = useState(false);

	const openModal = useCallback(() => setIsOpen(true), []);

	const closeModal = useCallback(() => setIsOpen(false), []);



	return (

		<Box>

			<Button aria-haspopup="dialog" appearance="primary" onClick={openModal}>

				Launch benefits modal

			</Button>



			<ModalTransition>

				{isOpen && (

					<Modal onClose={closeModal}>

						<Box xcss={containerStyles}>

							<Box xcss={closeContainerStyles}>

								<CloseButton onClick={closeModal} />

							</Box>

							<Box>

								<Image src={welcomeImage} alt="Graphic showing users working on a project" />

							</Box>

						</Box>

						<Box padding="space.500">

							<Stack space="space.200" alignInline="center">

								<ModalTitle>Experience your new Jira</ModalTitle>

								<Box as="p">

									Switch context, jump between projects, and get back to work quickly with our new

									look and feel. Take it for a spin and let us know what you think.

								</Box>

							</Stack>

							<Box paddingBlockStart="space.500">

								<Stack alignInline="center">

									<ButtonGroup label="Switch options">

										<Button appearance="subtle" onClick={closeModal}>

											Remind me later

										</Button>

										<Button onClick={closeModal} appearance="discovery">

											Switch to the new Jira

										</Button>

									</ButtonGroup>

								</Stack>

							</Box>

						</Box>

					</Modal>

				)}

			</ModalTransition>

		</Box>

	);

}
```

## Using @atlaskit/onboarding

```jsx
import React, { useState } from 'react';



import Button from '@atlaskit/button/new';

import { Modal, ModalTransition } from '@atlaskit/onboarding';



import welcomeImage from '../assets/this-is-new-jira.png';



const BenefitModalBasicExample = () => {

	const [isActive, setIsActive] = useState(false);



	return (

		<>

			<Button appearance="primary" onClick={() => setIsActive(true)}>

				Launch benefits modal

			</Button>

			<ModalTransition>

				{isActive && (

					<Modal

						actions={[

							{

								onClick: () => setIsActive(false),

								text: 'Get started',

							},

							{ onClick: () => setIsActive(false), text: 'Remind me later' },

						]}

						heading="Experience the new Jira"

						image={welcomeImage}

						key="welcome"

					>

						<p>

							Check out our restructured interface and a bold, colorful design that reflects the

							vibrance of your team. Try it out early and get a chance to influence how we build the

							next generation of Atlassian.

						</p>

					</Modal>

				)}

			</ModalTransition>

		</>

	);

};



export default BenefitModalBasicExample;
```

---

[View Original Documentation](https://atlassian.design/components/onboarding/benefits-modal/examples)
