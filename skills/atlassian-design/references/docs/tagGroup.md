# Tag group

A tag group controls the layout and alignment for a collection of tags.

---

## Default

By default, a tag group lays out a collection of tags from left to right. It handles overflow by wrapping to the next line. Tags inside of a tag group should be of the same type to provide a consistent user experience. 

```jsx
/**

 * @jsxRuntime classic

 * @jsx jsx

 */

import { css, jsx } from '@compiled/react';



import Tag, { SimpleTag } from '@atlaskit/tag';

import TagGroup from '@atlaskit/tag-group';

import { token } from '@atlaskit/tokens';



const layoutStyles = css({

	display: 'flex',

	gap: token('space.300'),

	flexDirection: 'column',

	paddingBlockEnd: token('space.300'),

	paddingBlockStart: token('space.300'),

	paddingInlineEnd: 0,

	paddingInlineStart: 0,

});



export default () => (

	<div css={layoutStyles}>

		<TagGroup label="Simple tags">

			<SimpleTag text="Tag" />

			<SimpleTag text="Tag" />

			<SimpleTag text="Tag" />

			<SimpleTag text="Tag" />

		</TagGroup>

		<TagGroup label="Link tags">

			<SimpleTag text="Tag link" href="/components/tag-group" />

			<SimpleTag text="Tag link" href="/components/tag-group" />

			<SimpleTag text="Tag link" href="/components/tag-group" />

			<SimpleTag text="Tag link" href="/components/tag-group" />

		</TagGroup>

		<TagGroup label="Rounded tags">

			<SimpleTag text="Rounded tag" appearance="rounded" />

			<SimpleTag text="Rounded tag" appearance="rounded" />

			<SimpleTag text="Rounded tag" appearance="rounded" />

			<SimpleTag text="Rounded tag" appearance="rounded" />

		</TagGroup>

		<TagGroup label="Removable tags">

			<Tag text="Removable tag" />

			<Tag text="Removable tag" />

			<Tag text="Removable tag" />

			<Tag text="Removable tag" />

		</TagGroup>

	</div>

);
```

## Alignment

The alignment direction can be set to either the start or end of the tag group container using the alignment prop. This will also impact the direction of the exiting animation when a removable tag is removed. 

### Start

Set the alignment prop to "start" to align the tags to the start of the tag group container. Tags will animate out to the left when removed. 

```jsx
import React from 'react';



import Tag from '@atlaskit/tag';

import TagGroup from '@atlaskit/tag-group';



export default () => (

	<TagGroup label="Atlassian products" alignment="start">

		<Tag text="Bitbucket" />

		<Tag text="Compass" />

		<Tag text="Confluence" />

		<Tag text="Jira" />

		<Tag text="Jira Service Management" />

		<Tag text="Jira Software" />

		<Tag text="Jira Work Management" />

		<Tag text="Opsgenie" />

		<Tag text="Statuspage" />

		<Tag text="Trello" />

	</TagGroup>

);
```

### End

Set the alignment prop to "end" to align the tags to the end of the group. Tags will animate out to the right when removed. 

```jsx
import React from 'react';



import Tag from '@atlaskit/tag';

import TagGroup from '@atlaskit/tag-group';



export default () => (

	<TagGroup label="Atlassian products" alignment="end">

		<Tag text="Bitbucket" />

		<Tag text="Compass" />

		<Tag text="Confluence" />

		<Tag text="Jira" />

		<Tag text="Jira Service Management" />

		<Tag text="Jira Software" />

		<Tag text="Jira Work Management" />

		<Tag text="Opsgenie" />

		<Tag text="Statuspage" />

		<Tag text="Trello" />

	</TagGroup>

);
```

---

[View Original Documentation](https://atlassian.design/components/tag-group/examples)
