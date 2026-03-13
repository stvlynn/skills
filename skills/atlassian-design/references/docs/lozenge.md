# Lozenge

A lozenge is a visual indicator used to highlight an item's status for quick recognition.

---

## Appearance

Lozenges are either subtle or bold and use color to indicate meanings that people can learn and recognize across products. Change the lozenge's appearance to bold by setting isBold. 

### Default

Use default lozenges for a general status. For example: "to do", "unavailable", "minor", or "not started". 

```jsx
import React from 'react';



import Lozenge from '@atlaskit/lozenge';



export default () => (

	<>

		<div>

			<Lozenge>Default</Lozenge>

		</div>

		<div>

			<Lozenge isBold>Default bold</Lozenge>

		</div>

	</>

);
```

### Success

Use success lozenges to represent a constructive status. For example: "available", "completed", "approved", "resolved", or "added". 

```jsx
import React from 'react';



import Lozenge from '@atlaskit/lozenge';



export default () => (

	<>

		<div>

			<Lozenge appearance="success">Success</Lozenge>

		</div>

		<div>

			<Lozenge appearance="success" isBold>

				Success bold

			</Lozenge>

		</div>

	</>

);
```

### Removed

Use removed lozenges to represent a critical or problematic status. For example: "error", "declined", "deleted", or "failed". 

```jsx
import React from 'react';



import Lozenge from '@atlaskit/lozenge';



export default () => (

	<>

		<div>

			<Lozenge appearance="removed">Removed</Lozenge>

		</div>

		<div>

			<Lozenge appearance="removed" isBold>

				Removed bold

			</Lozenge>

		</div>

	</>

);
```

### In progress

Use inprogress lozenges to represent an in progress or current status. For example: "in progress", "open", or "modified". 

```jsx
import React from 'react';



import Lozenge from '@atlaskit/lozenge';



export default () => (

	<>

		<div>

			<Lozenge appearance="inprogress">In progress</Lozenge>

		</div>

		<div>

			<Lozenge appearance="inprogress" isBold>

				In progress bold

			</Lozenge>

		</div>

	</>

);
```

### New

Use new lozenges to represent a new status. For example: "new", "created", or "help". 

```jsx
import React from 'react';



import Lozenge from '@atlaskit/lozenge';



export default () => (

	<>

		<div>

			<Lozenge appearance="new">New</Lozenge>

		</div>

		<div>

			<Lozenge appearance="new" isBold>

				New bold

			</Lozenge>

		</div>

	</>

);
```

### Moved

Use moved lozenges to represent a status for items that have changed and require attention. For example: "busy", "blocked", "missing", or "warning". 

```jsx
import React from 'react';



import Lozenge from '@atlaskit/lozenge';



export default () => (

	<>

		<div>

			<Lozenge appearance="moved">Moved</Lozenge>

		</div>

		<div>

			<Lozenge appearance="moved" isBold>

				Moved bold

			</Lozenge>

		</div>

	</>

);
```

## Max width

When the text in the lozenge exceeds the maximum width, it will be truncated with an ellipsis. By default, the maximum width of a lozenge is 200px. You can use the maxWidth prop to customize the width of the lozenge. Avoid truncation wherever possible by using shorter text in lozenges. The truncated text is not focusable or accessible. DEFAULT MAX WIDTH WITH LONG TEXT WHICH TRUNCATES CUSTOM MAX WIDTH WITH LONG TEXT WHICH TRUNCATES 

```jsx
import React from 'react';



import Lozenge from '@atlaskit/lozenge';



export default () => (

	<div>

		<p>

			<Lozenge appearance="success">default max width with long text which truncates</Lozenge>

		</p>

		<p>

			<Lozenge appearance="success" maxWidth={100}>

				custom max width with long text which truncates

			</Lozenge>

		</p>

	</div>

);
```

---

[View Original Documentation](https://atlassian.design/components/lozenge/examples)
