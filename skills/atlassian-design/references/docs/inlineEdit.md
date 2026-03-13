# Inline edit

An inline edit displays a custom input component that switches between reading and editing on the same page.

---

## Default

Inline edit is a wrapper around a custom input component such as a text field. It starts in a read-only view called readView and people can activate the field to edit it. To prevent an inconsistent transition between read and edit mode, pass in custom readView and editView as props. Not doing this will result in a buggy user experience where the inline edit views do not align. You can use various types of input fields such as text area and select. The appearance of the inline edit will vary depending on the input component it is used with. 

### Text field

If you need a standard editable text field with the views already set up, consider using inline editable textfield. 

```jsx
import React, { useState } from 'react';



import { cssMap } from '@atlaskit/css';

import InlineEdit from '@atlaskit/inline-edit';

import { Box } from '@atlaskit/primitives/compiled';

import Textfield from '@atlaskit/textfield';

import { token } from '@atlaskit/tokens';



/*

  As inline edit allows for a custom input component, styling of `ReadViewContainer` needs to be shipped with the component.

  This keeps `editView` and `readView` components aligned when switching between the two. In this particular case, these

  styles ensure `readView` is in sync with the TextField.

  */

const readViewContainerStyles = cssMap({

	root: {

		font: token('font.body'),

		paddingBlock: token('space.100'),

		paddingInline: token('space.075'),

		wordBreak: 'break-word',

	},

});



const InlineEditDefaultExample = () => {

	const initialValue = 'Default team name value';

	const [editValue, setEditValue] = useState('Pyxis');



	return (

		<Box paddingInlineStart="space.100" paddingInlineEnd="space.600">

			<InlineEdit

				defaultValue={editValue}

				label="Team name"

				editButtonLabel={editValue || initialValue}

				editView={({ errorMessage, ...fieldProps }) => <Textfield {...fieldProps} autoFocus />}

				readView={() => (

					<Box xcss={readViewContainerStyles.root} testId="read-view">

						{editValue || initialValue}

					</Box>

				)}

				onConfirm={(value) => setEditValue(value)}

			/>

		</Box>

	);

};



export default InlineEditDefaultExample;
```

### Text area

The text area example uses keepEditViewOpenOnBlur. When set to true, inline edit stays in editing when blurred (when the user clicks or moves away). This is recommended for larger areas of text to help prevent people from accidentally discarding or saving their unfinished work. 

```jsx
import React, { useState } from 'react';



import { cssMap } from '@atlaskit/css';

import InlineEdit from '@atlaskit/inline-edit';

import { Box } from '@atlaskit/primitives/compiled';

import TextArea from '@atlaskit/textarea';

import { token } from '@atlaskit/tokens';



const containerStyles = cssMap({

	root: {

		paddingBlockStart: token('space.100'),

		paddingInlineEnd: token('space.100'),

		paddingBlockEnd: token('space.600'),

		// eslint-disable-next-line @atlaskit/ui-styling-standard/no-unsafe-values

		width: '70%' as any,

	},

});



const readViewContainerStyles = cssMap({

	root: {

		font: token('font.body'),

		// eslint-disable-next-line @atlaskit/ui-styling-standard/no-unsafe-values

		minHeight: '4em' as any,

		paddingTop: token('space.075'),

		paddingRight: token('space.075'),

		paddingBottom: token('space.075'),

		paddingLeft: token('space.075'),

		wordBreak: 'break-word',

	},

});



const InlineEditCustomTextareaExample = () => {

	const initialValue = 'Tell us about your experience';

	const [editValue, setEditValue] = useState('');

	return (

		<Box xcss={containerStyles.root}>

			<InlineEdit

				defaultValue={editValue}

				label="Send feedback"

				editButtonLabel={editValue || initialValue}

				editView={({ errorMessage, ...fieldProps }, ref) => (

					// @ts-ignore - textarea does not pass through ref as a prop

					<TextArea {...fieldProps} ref={ref} />

				)}

				readView={() => <Box xcss={readViewContainerStyles.root}>{editValue || initialValue}</Box>}

				onConfirm={setEditValue}

				keepEditViewOpenOnBlur

				readViewFitContainerWidth

			/>

		</Box>

	);

};



export default InlineEditCustomTextareaExample;
```

### Select

```jsx
/**

 * @jsxRuntime classic

 * @jsx jsx

 */

import { useState } from 'react';



import { cssMap, jsx } from '@atlaskit/css';

import InlineEdit from '@atlaskit/inline-edit';

import { Box } from '@atlaskit/primitives/compiled';

import Select, { type OptionType, type ValueType } from '@atlaskit/select';

import Tag from '@atlaskit/tag';

import Group from '@atlaskit/tag-group';

import { token } from '@atlaskit/tokens';



const containerStyles = cssMap({

	root: {

		paddingBlockStart: token('space.100'),

		paddingInlineEnd: token('space.100'),

		paddingBlockEnd: token('space.600'),

	},

});



const readViewContainerStyles = cssMap({

	root: {

		font: token('font.body'),

		paddingBlock: token('space.100'),

		paddingInline: token('space.075'),

	},

});



const editViewContainerStyles = cssMap({

	root: {

		position: 'relative',

		// eslint-disable-next-line @atlaskit/ui-styling-standard/no-unsafe-values

		zIndex: 'dialog' as any,

	},

});



const tagGroupContainerStyles = cssMap({

	root: {

		paddingTop: token('space.050'),

		paddingRight: token('space.050'),

		paddingBottom: token('space.050'),

		paddingLeft: token('space.050'),

	},

});

const selectOptions = [

	{ label: 'CSS', value: 'CSS' },

	{ label: 'Design', value: 'Design' },

	{ label: 'HTML', value: 'HTML' },

	{ label: 'Javascript', value: 'Javascript' },

	{ label: 'User experience', value: 'User experience' },

	{ label: 'User research', value: 'User research' },

];



const InlineEditCustomSelectExample = () => {

	const [editValue, setEditValue] = useState<ValueType<OptionType, true>>([]);

	const inlineEditLabel = 'Skills required';

	const selectLabel = 'Select skills';



	const onConfirm = (value: ValueType<OptionType, true>) => {

		if (!value) {

			return;

		}



		setEditValue(value);

	};



	return (

		<Box xcss={containerStyles.root}>

			<InlineEdit<ValueType<OptionType, true>>

				defaultValue={editValue}

				label={inlineEditLabel}

				editButtonLabel={editValue.length > 0 ? inlineEditLabel : selectLabel}

				editView={(fieldProps) => (

					<Box xcss={editViewContainerStyles.root}>

						<Select {...fieldProps} options={selectOptions} isMulti autoFocus openMenuOnFocus />

					</Box>

				)}

				readView={() =>

					editValue && editValue.length === 0 ? (

						<Box xcss={readViewContainerStyles.root}>{selectLabel}</Box>

					) : (

						<Box xcss={tagGroupContainerStyles.root}>

							<Group label="Selected skills">

								{editValue &&

									editValue.map((option: OptionType) => (

										<Tag text={option.label} key={option.label} />

									))}

							</Group>

						</Box>

					)

				}

				onConfirm={onConfirm}

			/>

		</Box>

	);

};



export default InlineEditCustomSelectExample;
```

## Custom text

When using a text field, the font size can be made larger. You can also change the line height. 

```jsx
/**

 * @jsxRuntime classic

 * @jsx jsx

 */

import { useState } from 'react';



import { css, cssMap, jsx } from '@compiled/react';



import InlineEdit from '@atlaskit/inline-edit';

import { Box } from '@atlaskit/primitives/compiled';

import Textfield from '@atlaskit/textfield';

import { token } from '@atlaskit/tokens';



const readViewContainerStyles = cssMap({

	root: {

		font: token('font.heading.large'),

		paddingBlock: token('space.100'),

		paddingInline: token('space.075'),

		wordBreak: 'break-word',

	},

});



const textFieldStyles = css({

	// eslint-disable-next-line @atlaskit/design-system/no-nested-styles, @atlaskit/ui-styling-standard/no-nested-selectors -- Ignored via go/DSP-18766

	'& > [data-ds--text-field--input]': {

		font: token('font.heading.large'),

	},

});



const InlineEditExample = () => {

	const initialValue = 'Enter text';

	const [editValue, setEditValue] = useState('Default value');



	return (

		<Box padding="space.100">

			<InlineEdit

				defaultValue={editValue}

				editButtonLabel={editValue || initialValue}

				editView={({ errorMessage, ...fieldProps }) => (

					// eslint-disable-next-line @atlaskit/design-system/no-unsafe-style-overrides

					<Textfield {...fieldProps} autoFocus css={textFieldStyles} />

				)}

				readView={() => (

					<Box xcss={readViewContainerStyles.root} testId="read-view">

						{editValue || initialValue}

					</Box>

				)}

				onConfirm={(value) => {

					setEditValue(value);

				}}

			/>

		</Box>

	);

};



export default InlineEditExample;
```

## No action buttons

Action buttons include a confirm (checkmark) and a cancel (cross) button. These indicate the completion of editing and the cancellation of editing respectively. Use hideActionButtons to remove the buttons and leave the field by itself. Use this when the action buttons obstruct other contents below. For example, on mobile devices. If there's no obstruction, keep action buttons for accessibility purposes. The contents in the field are saved when the user navigates away from the element, but this isn't immediately obvious on its' own. 

```jsx
import React, { useState } from 'react';



import { InlineEditableTextfield } from '@atlaskit/inline-edit';

import { Box } from '@atlaskit/primitives/compiled';



const InlineEditNoActionsExample = () => {

	const placeholderLabel = 'Initial postcode value';

	const [editValue, setEditValue] = useState('94538');



	return (

		<Box paddingInline="space.100" paddingBlockStart="space.100" paddingBlockEnd="space.600">

			<InlineEditableTextfield

				testId="editable-text-field"

				defaultValue={editValue}

				label="Postcode"

				editButtonLabel={editValue || placeholderLabel}

				onConfirm={(value) => setEditValue(value)}

				placeholder={placeholderLabel}

				hideActionButtons

			/>

		</Box>

	);

};

export default InlineEditNoActionsExample;
```

## Start with edit view

Inline edit starts in readView by default. You must click into the field to start editing. Use startWithEditViewOpen to set it to start in editView instead. 

```jsx
import React, { useState } from 'react';



import { InlineEditableTextfield } from '@atlaskit/inline-edit';

import { Box } from '@atlaskit/primitives/compiled';



const InlineEditStartEditExample = () => {

	const placeholderLabel = 'Initial Team name value';

	const [editValue, setEditValue] = useState('Pyxis');



	return (

		<Box paddingInline="space.100" paddingBlockStart="space.100" paddingBlockEnd="space.600">

			<InlineEditableTextfield

				testId="editable-text-field"

				defaultValue={editValue}

				label="Team name"

				editButtonLabel={editValue || placeholderLabel}

				onConfirm={(value) => setEditValue(value)}

				placeholder={placeholderLabel}

				startWithEditViewOpen

			/>

		</Box>

	);

};

export default InlineEditStartEditExample;
```

## Validation

Validation displays an error message related to the restrictions of the inline edit. These error and warning messages disappear when the criteria is met. Try to keep the helper text as short as possible. For complex information, provide a link to more information in a new browser tab (see messaging guidelines for more information). 

```jsx
import React, { useEffect, useState } from 'react';



import Button from '@atlaskit/button/new';

import { cssMap } from '@atlaskit/css';

import ErrorIcon from '@atlaskit/icon/glyph/error';

import InlineDialog from '@atlaskit/inline-dialog';

import InlineEdit from '@atlaskit/inline-edit';

import { Box } from '@atlaskit/primitives/compiled';

import TextField from '@atlaskit/textfield';

import { token } from '@atlaskit/tokens';



const containerStyles = cssMap({

	root: {

		paddingBlockStart: token('space.100'),

		paddingInlineEnd: token('space.100'),

		paddingBlockEnd: token('space.600'),

		// eslint-disable-next-line @atlaskit/ui-styling-standard/no-unsafe-values

		width: '50%' as any,

	},

});



const errorIconContainerStyles = cssMap({

	root: {

		paddingInlineEnd: token('space.075'),

		// eslint-disable-next-line @atlaskit/ui-styling-standard/no-unsafe-values

		lineHeight: '100%' as any,

	},

});



const readViewContainerStyles = cssMap({

	root: {

		display: 'flex',

		font: token('font.body'),

		maxWidth: '100%',

		paddingBlock: token('space.100'),

		paddingInline: token('space.075'),

		wordBreak: `break-word`,

	},

});



const InlineEditValidationExample = () => {

	const initialValue = 'Initial description value';

	const [editValue, setEditValue] = useState('Default description value');



	let validateValue = '';

	let validateTimeoutId: number | undefined;



	useEffect(() => {

		return () => {

			if (validateTimeoutId) {

				window.clearTimeout(validateTimeoutId);

			}

		};

	});



	const validate = (value: string) => {

		validateValue = value;

		return new Promise<{ value: string; error: string } | undefined>((resolve) => {

			validateTimeoutId = window.setTimeout(() => {

				if (value.length <= 6) {

					resolve({

						value,

						error: 'Enter a description greater than 6 characters',

					});

				}

				resolve(undefined);

			}, 100);

		}).then((validateObject) => {

			if (validateObject && validateObject.value === validateValue) {

				return validateObject.error;

			}

			return undefined;

		});

	};



	const clearInlineEditContent = () => {

		setEditValue('');

	};



	return (

		<Box xcss={containerStyles.root}>

			<Button testId="clear-button" onClick={clearInlineEditContent}>

				Clear field

			</Button>

			<InlineEdit

				defaultValue={editValue}

				label="Description"

				editButtonLabel={editValue || initialValue}

				editView={({ errorMessage, ...fieldProps }) => (

					<InlineDialog

						isOpen={fieldProps.isInvalid}

						content={<Box id="error-message">{errorMessage}</Box>}

						placement="right"

					>

						<TextField

							testId="edit-view"

							{...fieldProps}

							elemAfterInput={

								fieldProps.isInvalid && (

									<Box xcss={errorIconContainerStyles.root}>

										<ErrorIcon

											label="error"

											primaryColor={token('color.icon.danger')}

										/>

									</Box>

								)

							}

							autoFocus

						/>

					</InlineDialog>

				)}

				readView={() => (

					<Box xcss={readViewContainerStyles.root} testId="read-view">

						{editValue}

					</Box>

				)}

				onConfirm={(value) => setEditValue(value)}

				validate={validate}

			/>

		</Box>

	);

};



export default InlineEditValidationExample;
```

## Required field

Set isRequired when an inline edit field needs to be filled out to continue. 

```jsx
import React, { useState } from 'react';



import { InlineEditableTextfield } from '@atlaskit/inline-edit';

import { Box } from '@atlaskit/primitives/compiled';



const InlineEditRequiredFieldExample = () => {

	const placeholderLabel = 'Initial description value';

	const [editValue, setEditValue] = useState('Default description value');



	return (

		<Box paddingInline="space.100" paddingBlockStart="space.100" paddingBlockEnd="space.600">

			<InlineEditableTextfield

				testId="editable-text-field"

				defaultValue={editValue}

				label="Description"

				editButtonLabel={editValue || placeholderLabel}

				onConfirm={(value) => setEditValue(value)}

				placeholder={placeholderLabel}

				isRequired

			/>

		</Box>

	);

};

export default InlineEditRequiredFieldExample;
```

## Stateless

In a stateless inline edit, you can manage the checked state of the input by using the isEditing prop. This requires the setEditing handler to control the state value that you pass into the isEditing prop. 

```jsx
import React, { useState } from 'react';



import { cssMap } from '@atlaskit/css';

import InlineEdit from '@atlaskit/inline-edit';

import { Box } from '@atlaskit/primitives/compiled';

import Textfield from '@atlaskit/textfield';

import { token } from '@atlaskit/tokens';



const containerStyles = cssMap({

	root: {

		paddingBlockStart: token('space.100'),

		paddingInlineEnd: token('space.100'),

		paddingBlockEnd: token('space.600'),

	},

});



const readViewContainerStyles = cssMap({

	root: {

		display: 'flex',

		font: token('font.body'),

		maxWidth: '100%',

		paddingBlock: token('space.100'),

		paddingInline: token('space.075'),

		wordBreak: 'break-word',

	},

});



const InlineEditStatelessExample = () => {

	const initialValue = 'Initial description value';

	const [editValue, setEditValue] = useState('Default description value');

	const [isEditing, setEditing] = useState(true);



	return (

		<Box xcss={containerStyles.root}>

			<InlineEdit

				defaultValue={editValue}

				label="Description"

				editButtonLabel={editValue || initialValue}

				isEditing={isEditing}

				editView={({ errorMessage, ...fieldProps }) => <Textfield {...fieldProps} autoFocus />}

				readView={() => (

					<Box xcss={readViewContainerStyles.root} testId="read-view">

						{editValue}

					</Box>

				)}

				onCancel={() => setEditing(false)}

				onConfirm={(value: string) => {

					setEditValue(value);

					setEditing(false);

				}}

				onEdit={() => setEditing(true)}

			/>

		</Box>

	);

};



export default InlineEditStatelessExample;
```

---

[View Original Documentation](https://atlassian.design/components/inline-edit/examples)
