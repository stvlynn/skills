# Hide

Hide is a responsive primitive that hides children at specified breakpoints

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

### Hide

Using Hide allows you to Hide the children using CSS display: none when the viewport size is above a specified breakpoint. By default, unless the breakpoint is met, contents are hidden. Children that are hidden are still rendered into the DOM, so there so there is typically little performance savings — primarily that they are not painted.

```jsx
import React from 'react';



import Button from '@atlaskit/button/new';

import MaximizeIcon from '@atlaskit/icon/glyph/image-resize';

import { Stack } from '@atlaskit/primitives';

import { Hide } from '@atlaskit/primitives/responsive';



export default function Example() {

	return (

		<Stack alignInline="start" space="space.100">

			Try resizing your browser window

			<Button iconBefore={MaximizeIcon}>

				<Hide below="md">This text is visible only at larger breakpoints</Hide>

			</Button>

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

[View Original Documentation](https://atlassian.design/components/primitives/responsive/hide/examples)
