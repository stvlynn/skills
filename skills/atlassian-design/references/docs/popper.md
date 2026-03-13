# Popper

A wrapper for React Popper for situations which require a bespoke popup where other ADS components are deemed unsuitable

---

## Basic positioning

```jsx
/**

 * @jsxRuntime classic

 * @jsx jsx

 */

import { css, jsx } from '@compiled/react';



import Button from '@atlaskit/button/new';

import { Manager, Popper, Reference } from '@atlaskit/popper';

import { token } from '@atlaskit/tokens';



const popupStyles = css({

	maxWidth: '160px',

	backgroundColor: token('elevation.surface.overlay'),

	borderRadius: '3px',

	boxShadow: token('elevation.shadow.raised'),

	paddingBlockEnd: token('space.100'),

	paddingBlockStart: token('space.100'),

	paddingInlineEnd: token('space.100'),

	paddingInlineStart: token('space.100'),

});



const BasicPositioningExample = () => (

	<Manager>

		<Reference>

			{({ ref }) => (

				<Button appearance="primary" ref={ref}>

					Reference element

				</Button>

			)}

		</Reference>

		<Popper placement="right">

			{({ ref, style }) => (

				// eslint-disable-next-line @atlaskit/ui-styling-standard/enforce-style-prop -- Ignored via go/DSP-18766

				<div ref={ref} style={style} css={popupStyles}>

					This text is a popper placed to the right

				</div>

			)}

		</Popper>

	</Manager>

);



export default BasicPositioningExample;
```

## Scroll container

This example uses the isReferenceHidden render prop from the <Popper /> component to conditionally add styles as the reference element enters and leaves the viewport. Sit nulla est ex deserunt exercitation anim occaecat. Nostrud ullamco deserunt aute id consequat veniam incididunt duis in sint irure nisi. Mollit officia cillum Lorem ullamco minim nostrud elit officia tempor esse quis. Sunt ad dolore quis aute consequat. Magna exercitation reprehenderit magna aute tempor cupidatat consequat elit dolor adipisicing. Mollit dolor eiusmod sunt ex incididunt cillum quis. Velit duis sit officia eiusmod Lorem aliqua enim laboris do dolor eiusmod. Et mollit incididunt nisi consectetur esse laborum eiusmod pariatur proident Lorem eiusmod et. Culpa deserunt nostrud ad veniam. Est velit labore esse esse cupidatat. Velit id elit consequat minim. Mollit enim excepteur ea laboris adipisicing aliqua proident occaecat do do adipisicing adipisicing ut fugiat. Consequat pariatur ullamco aute sunt esse. Irure excepteur eu non eiusmod. Commodo commodo et ad ipsum elit esse pariatur sit adipisicing sunt excepteur enim. Incididunt duis commodo mollit esse veniam non exercitation dolore occaecat ea nostrud laboris. Adipisicing occaecat fugiat fugiat irure fugiat in magna non consectetur proident fugiat. Commodo magna et aliqua elit sint cupidatat. Sint aute ullamco enim cillum anim ex. Est eiusmod commodo occaecat consequat laboris est do duis. Enim incididunt non culpa velit quis aute in elit magna ullamco in consequat ex proident. Dolore incididunt mollit fugiat pariatur cupidatat ipsum laborum cillum. Commodo consequat velit cupidatat duis ex nisi non aliquip ad ea pariatur do culpa. Eiusmod proident adipisicing tempor tempor qui pariatur voluptate dolor do ea commodo. Veniam voluptate cupidatat ex nisi do ullamco in quis elit. Cillum proident veniam cupidatat pariatur laborum tempor cupidatat anim eiusmod id nostrud pariatur tempor reprehenderit. Do esse ullamco laboris sunt proident est ea exercitation cupidatat. Do Lorem eiusmod aliqua culpa ullamco consectetur veniam voluptate cillum. Dolor consequat cillum tempor laboris mollit laborum reprehenderit reprehenderit veniam aliqua deserunt cupidatat consequat id. Est id tempor excepteur enim labore sint aliquip consequat duis minim tempor proident. Dolor incididunt aliquip minim elit ea. Exercitation non officia eu id. Ipsum ipsum consequat incididunt do aliquip pariatur nostrud. Qui ut sint culpa labore Lorem. Magna deserunt aliquip aute duis consectetur magna amet anim. Magna fugiat est nostrud veniam. Officia duis ea sunt aliqua. Ipsum minim officia aute anim minim aute aliquip aute non in non. Ipsum aliquip proident ut dolore eiusmod ad fugiat fugiat ut ex. Ea velit Lorem ut et commodo nulla voluptate veniam ea et aliqua esse id. Pariatur dolor et adipisicing ea mollit. Ipsum non irure proident ipsum dolore aliquip adipisicing laborum irure dolor nostrud occaecat exercitation. Culpa qui reprehenderit nostrud aliqua reprehenderit et ullamco proident nisi commodo non ut. Ipsum quis irure nisi sint do qui velit nisi. Sunt voluptate eu reprehenderit tempor consequat eiusmod Lorem irure velit duis Lorem laboris ipsum cupidatat. Pariatur excepteur tempor veniam cillum et nulla ipsum veniam ad ipsum ad aute. Est officia duis pariatur ad eiusmod id voluptate. 

### 

Sit nulla est ex deserunt exercitation anim occaecat. Nostrud ullamco deserunt aute id consequat veniam incididunt duis in sint irure nisi. Mollit officia cillum Lorem ullamco minim nostrud elit officia tempor esse quis. Sunt ad dolore quis aute consequat. Magna exercitation reprehenderit magna aute tempor cupidatat consequat elit dolor adipisicing. Mollit dolor eiusmod sunt ex incididunt cillum quis. Velit duis sit officia eiusmod Lorem aliqua enim laboris do dolor eiusmod. Et mollit incididunt nisi consectetur esse laborum eiusmod pariatur proident Lorem eiusmod et. Culpa deserunt nostrud ad veniam. Est velit labore esse esse cupidatat. Velit id elit consequat minim. Mollit enim excepteur ea laboris adipisicing aliqua proident occaecat do do adipisicing adipisicing ut fugiat. Consequat pariatur ullamco aute sunt esse. Irure excepteur eu non eiusmod. Commodo commodo et ad ipsum elit esse pariatur sit adipisicing sunt excepteur enim. Incididunt duis commodo mollit esse veniam non exercitation dolore occaecat ea nostrud laboris. Adipisicing occaecat fugiat fugiat irure fugiat in magna non consectetur proident fugiat. Commodo magna et aliqua elit sint cupidatat. Sint aute ullamco enim cillum anim ex. Est eiusmod commodo occaecat consequat laboris est do duis. Enim incididunt non culpa velit quis aute in elit magna ullamco in consequat ex proident. Dolore incididunt mollit fugiat pariatur cupidatat ipsum laborum cillum. Commodo consequat velit cupidatat duis ex nisi non aliquip ad ea pariatur do culpa. Eiusmod proident adipisicing tempor tempor qui pariatur voluptate dolor do ea commodo. Veniam voluptate cupidatat ex nisi do ullamco in quis elit. Cillum proident veniam cupidatat pariatur laborum tempor cupidatat anim eiusmod id nostrud pariatur tempor reprehenderit. Do esse ullamco laboris sunt proident est ea exercitation cupidatat. Do Lorem eiusmod aliqua culpa ullamco consectetur veniam voluptate cillum. Dolor consequat cillum tempor laboris mollit laborum reprehenderit reprehenderit veniam aliqua deserunt cupidatat consequat id. Est id tempor excepteur enim labore sint aliquip consequat duis minim tempor proident. Dolor incididunt aliquip minim elit ea. Exercitation non officia eu id. Ipsum ipsum consequat incididunt do aliquip pariatur nostrud. Qui ut sint culpa labore Lorem. Magna deserunt aliquip aute duis consectetur magna amet anim. Magna fugiat est nostrud veniam. Officia duis ea sunt aliqua. Ipsum minim officia aute anim minim aute aliquip aute non in non. Ipsum aliquip proident ut dolore eiusmod ad fugiat fugiat ut ex. Ea velit Lorem ut et commodo nulla voluptate veniam ea et aliqua esse id. Pariatur dolor et adipisicing ea mollit. Ipsum non irure proident ipsum dolore aliquip adipisicing laborum irure dolor nostrud occaecat exercitation. Culpa qui reprehenderit nostrud aliqua reprehenderit et ullamco proident nisi commodo non ut. Ipsum quis irure nisi sint do qui velit nisi. Sunt voluptate eu reprehenderit tempor consequat eiusmod Lorem irure velit duis Lorem laboris ipsum cupidatat. Pariatur excepteur tempor veniam cillum et nulla ipsum veniam ad ipsum ad aute. Est officia duis pariatur ad eiusmod id voluptate. 

```jsx
/**

 * @jsxRuntime classic

 * @jsx jsx

 */

import { css, jsx } from '@compiled/react';

import Lorem from 'react-lorem-component';



import Button from '@atlaskit/button/new';

import { Manager, Popper, Reference } from '@atlaskit/popper';

import { token } from '@atlaskit/tokens';



const popupStyles = css({

	maxWidth: '160px',

	backgroundColor: token('elevation.surface.overlay'),

	borderRadius: '3px',

	boxShadow: token('elevation.shadow.raised'),

	paddingBlockEnd: token('space.100'),

	paddingBlockStart: token('space.100'),

	paddingInlineEnd: token('space.100'),

	paddingInlineStart: token('space.100'),

});



const popupHiddenStyles = css({

	pointerEvents: 'none',

	visibility: 'hidden',

});



const BasicPopper = () => (

	<Manager>

		<Reference>

			{({ ref }) => (

				<Button appearance="primary" ref={ref}>

					Reference element

				</Button>

			)}

		</Reference>

		<Popper>

			{({ ref, placement, isReferenceHidden, style }) => (

				<div

					ref={ref}

					data-placement={placement}

					// eslint-disable-next-line @atlaskit/ui-styling-standard/enforce-style-prop -- Ignored via go/DSP-18766

					style={style}

					css={[popupStyles, isReferenceHidden && popupHiddenStyles]}

				>

					<h3>New Popper</h3>

					<Lorem count={1} />

				</div>

			)}

		</Popper>

	</Manager>

);



const containerStyles = css({

	maxWidth: '800px',

	maxHeight: '400px',

	borderColor: 'black',

	borderStyle: 'solid',

	borderWidth: '1px',

	marginBlockStart: token('space.250'),

	overflow: 'auto',

});



const innerStyles = css({

	boxSizing: 'border-box',

	width: '300%',

	height: '250%',

	backgroundColor: token('elevation.surface'),

	paddingBlockEnd: token('space.200'),

	paddingBlockStart: token('space.200'),

	paddingInlineEnd: token('space.200'),

	paddingInlineStart: token('space.200'),

});



const popperWrapperStyles = css({

	display: 'flex',

	justifyContent: 'center',

});



const instructionStyles = css({

	display: 'block',

	marginBlockEnd: token('space.400'),

});



const ScrollContainerExample = () => (

	<div css={containerStyles}>

		<div css={innerStyles}>

			<b css={instructionStyles}>

				Scroll to the middle of this container to see the popper <span>↘</span>

			</b>

			<Lorem count={10} />

			<div css={popperWrapperStyles}>

				<BasicPopper />

			</div>

			<Lorem count={10} />

		</div>

	</div>

);



export default ScrollContainerExample;
```

---

[View Original Documentation](https://atlassian.design/components/popper/examples)
