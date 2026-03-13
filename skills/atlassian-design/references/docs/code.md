# Code

Code highlights short strings of code snippets inline with body text.

---

## Inline code

Formatted code can appear in a variety of contexts, increasing the legibility and contrasting it against default paragraph text. Use inline code when you wish to highlight a short code snippet from the surrounding default text, such as when referencing variable names. To start creating a changeset, run yarn changeset. Then you'll be prompted to select packages for release. 

```jsx
import React from 'react';



import { Code } from '@atlaskit/code';

import { Text } from '@atlaskit/primitives/compiled';



const CodeDefaultExample = () => {

	return (

		<Text as="p">

			To start creating a changeset, run <Code>yarn changeset</Code>. Then you'll be prompted to

			select packages for release.

		</Text>

	);

};



export default CodeDefaultExample;
```

---

[View Original Documentation](https://atlassian.design/components/code/examples)
