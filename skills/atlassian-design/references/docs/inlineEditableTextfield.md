# Inline editable textfield

An inline editable textfield displays a textfield that switches between reading and editing on the same page.

---

## Default

The default form of the inline editable text field allows for easy switching between read-only text and editable text on the same page. Most inline edit use cases use a standard text field. This component includes our recommended defaults for this use case. Use an inline edit if you require more customisation and need to pass in your own custom input components. 

```jsx
import React, { useState } from 'react';



import { InlineEditableTextfield } from '@atlaskit/inline-edit';

import { Box } from '@atlaskit/primitives/compiled';



const InlineEditableTextfieldDefault = () => {

	const placeholderLabel = 'Initial description value';

	const [editValue, setEditValue] = useState('Default description value');



	const validate = (value: string) => {

		if (value.length <= 6) {

			return 'Please enter a description longer than 6 characters';

		}

		return undefined;

	};



	return (

		<Box paddingInline="space.100" paddingBlockStart="space.100" paddingBlockEnd="space.600">

			<InlineEditableTextfield

				defaultValue={editValue}

				label="Description"

				editButtonLabel={editValue || placeholderLabel}

				onConfirm={(value) => setEditValue(value)}

				placeholder={placeholderLabel}

				validate={validate}

			/>

		</Box>

	);

};

export default InlineEditableTextfieldDefault;
```

## Compact

The height of the inline edit can be decreased through isCompact. The top and bottom padding decreases. 

```jsx
import React, { useState } from 'react';



import { InlineEditableTextfield } from '@atlaskit/inline-edit';

import { Box } from '@atlaskit/primitives/compiled';



const InlineEditableTextfieldCompactExample = () => {

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

				isCompact

			/>

		</Box>

	);

};

export default InlineEditableTextfieldCompactExample;
```

---

[View Original Documentation](https://atlassian.design/components/inline-edit/inline-editable-textfield/examples)
