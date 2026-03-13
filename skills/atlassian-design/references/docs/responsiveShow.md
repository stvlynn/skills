# Show

Show is a responsive primitive that displays children at specified breakpoints

---

## Installation

<### Package installation information

#### Install

`yarn add @atlaskit/primitives`

#### Source

[Bitbucket.org﻿, (opens new window)](https://bitbucket.org/atlassian/atlassian-frontend-mirror/src/master/design-system/primitives)

npm

[@atlaskit/primitives﻿, (opens new window)](https://www.npmjs.com/package/@atlaskit/primitives)

Bundle

[unpkg.com﻿, (opens new window)](https://unpkg.com/@atlaskit/primitives/dist/)

### Show

Using Show allows you to show the children using CSS display: … when the viewport size is above a specified breakpoint. By default, unless the breakpoint is met, contents are hidden. Children that are not shown are still rendered into the DOM, so there so there is typically little performance savings — primarily that they are not painted.

```jsx
import React from 'react';



import { Stack } from '@atlaskit/primitives';

import { Show } from '@atlaskit/primitives/responsive';



export default function Example() {

	return (

		<Stack alignInline="start" space="space.100">

			Try resizing your browser window

			<Show above="md">

				<strong>This text is visible only 1024px and above</strong>

			</Show>

		</Stack>

	);

}
```

### Mixing Show and Hide

Prefer using consistent above or below for readability and consistency. Please connect using your desktop or laptop

```jsx
import React from 'react';



import { Hide, Show } from '@atlaskit/primitives/responsive';



export default function Example() {

	return (

		<p>

			Please connect using your{' '}

			<Show below="md" as="span">

				mobile device

			</Show>

			<Hide below="md" as="span">

				desktop or laptop

			</Hide>

		</p>

	);

}
```

---

[View Original Documentation](https://atlassian.design/components/primitives/responsive/show/examples)
