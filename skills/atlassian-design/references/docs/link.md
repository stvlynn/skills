# Link

A link takes people to a new location in the product or another website.

---

## Default

The default appearance of a link. 

```jsx
import React from 'react';



import Link from '@atlaskit/link';



export default function Default() {

	return <Link href="https://www.atlassian.com/software/jira">Default link</Link>;

}
```

## Subtle

Use a subtle link if the default link appearance is too prominent. There is no underline in resting state, but one appears on hover. Ensure the surrounding context makes it clear that the link is interactive, such as in navigation or breadcrumbs. Avoid using subtle links in body copy because they're hard to distinguish from the surrounding text. 

```jsx
import React from 'react';



import Link from '@atlaskit/link';



export default function Subtle() {

	return (

		<Link href="https://www.atlassian.com/software/confluence" appearance="subtle">

			Subtle link

		</Link>

	);

}
```

## Inverse

Use an inverse link when displaying it on a bold background. 

```jsx
import React from 'react';



import Link from '@atlaskit/link';



export default function Inverse() {

	return (

		<Link href="https://www.atlassian.com/software/confluence" appearance="inverse">

			Inverse link

		</Link>

	);

}
```

## Visited

Links that have been visited will display in a different color. This is not supported for inverse links due to color contrast limitations. 

```jsx
import React from 'react';



import Link from '@atlaskit/link';



export default function Visited() {

	return <Link href="/components/link/examples">Default link</Link>;

}
```

## Links that open in a new window or tab

It's important to indicate when links open in new windows or tabs. An icon will display next to the link, as well as visually hidden text "(opens new window)" for screen reader users. Opening links in a new window can be disorienting for people, so only do it when necessary. For more information see 'G200: Opening new windows and tabs from a link only when necessary'. 

```jsx
import React from 'react';



import Link from '@atlaskit/link';



export default function NewWindow() {

	return (

		<Link href="https://www.atlassian.com" target="_blank">

			Atlassian home

		</Link>

	);

}
```

## In body text

Links work in body copy, and will wrap onto new lines if necessary. 

```jsx
import React from 'react';



import Link from '@atlaskit/link';

import { Text } from '@atlaskit/primitives/compiled';



export default function BodyCopy() {

	return (

		<Text>

			Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod{' '}

			<Link href="/components/link/usage">tempor incididunt ut labore et dolore magna aliqua.</Link>{' '}

			Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea

			commodo consequat.{' '}

			<Link href="/components/link/usage">Duis aute irure dolor in reprehenderit</Link> in voluptate

			velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non

			proident, sunt in{' '}

			<Link href="/components/link/usage" target="_blank">

				culpa qui officia deserunt mollit anim id est laborum.

			</Link>

		</Text>

	);

}
```

## Inheriting font styles

Links will inherit font styles of surrounding text. 

```jsx
import React from 'react';



import Heading from '@atlaskit/heading';

import Link from '@atlaskit/link';



export default function FontStyleInheritance() {

	return (

		<Heading size="xxlarge">

			The <Link href="/components/link/code">link</Link> inherits font styles

		</Heading>

	);

}
```

## HTML attributes

Link passes through all valid HTML attributes to the underlying <a> element. 

```jsx
import React from 'react';



import Link from '@atlaskit/link';



export default function HtmlAttributes() {

	return (

		<Link href="https://www.loom.com" rel="noopener noreferrer" target="_blank">

			Loom home

		</Link>

	);

}
```

## Router links

Link supports automatic configuration of router link components through the AppProvider. Here's an example of the router link configuration for the anchor primitive. 

## Event tracking

Link has utilities to make tracking events easier. Here's an example of tracking events with the anchor primitive. 

---

[View Original Documentation](https://atlassian.design/components/link/examples)
