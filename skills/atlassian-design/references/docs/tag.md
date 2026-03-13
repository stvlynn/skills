# Tag

A tag labels UI objects for quick recognition and navigation.

---

## Default

The default form of a tag, where text is required. Tags with static text can be used as a flag or as a reference to an object or attribute. 

```jsx
import React from 'react';



import { SimpleTag as Tag } from '@atlaskit/tag';



export default () => <Tag text="Tag" />;
```

## Tag link

A tag with an href can link to more information on the tagged item. 

```jsx
import React from 'react';



import { SimpleTag as Tag } from '@atlaskit/tag';



export default () => <Tag text="Tag link" href="/components/tag" />;
```

## Removable

Once a tag has been removed, it cannot be re-rendered. Removable tags are visible in "edit" mode or in multi-select controls. 

```jsx
import React from 'react';



import Tag from '@atlaskit/tag';



export default () => <Tag text="Removable tag" removeButtonLabel="Remove" />;
```

## Removable link

A removable tag with an href can link to more information. 

```jsx
import React from 'react';



import Tag from '@atlaskit/tag';



export default () => (

	<Tag text="Removable tag link" removeButtonLabel="Remove" href="/components/tag" />

);
```

## Rounded

Use rounded tags with an avatar to add or remove people in multi-select controls. 

```jsx
import React from 'react';



import Avatar from '@atlaskit/avatar';

import Tag from '@atlaskit/tag';



export default () => (

	<Tag

		appearance="rounded"

		removeButtonLabel="Remove"

		text="Round removable tag"

		elemBefore={<Avatar borderColor="transparent" size="xsmall" />}

	/>

);
```

## Rounded link

A rounded tag with an avatar can link to more information. 

```jsx
import React from 'react';



import Avatar from '@atlaskit/avatar';

import Tag from '@atlaskit/tag';



export default () => (

	<Tag

		appearance="rounded"

		removeButtonLabel="Remove"

		text="Round removable link"

		href="/components/tag"

		elemBefore={<Avatar borderColor="transparent" size="xsmall" />}

	/>

);
```

## Color

The color theme for background and text. 

```jsx
import React from 'react';



import { SimpleTag as Tag } from '@atlaskit/tag';

import TagGroup from '@atlaskit/tag-group';



export default () => (

	<TagGroup label="Colored tags">

		<Tag text="standard Tag" color="standard" />

		<Tag text="blue Tag" color="blue" />

		<Tag text="green Tag" color="green" />

		<Tag text="teal Tag" color="teal" />

		<Tag text="purple Tag" color="purple" />

		<Tag text="red Tag" color="red" />

		<Tag text="yellow Tag" color="yellow" />

		<Tag text="orange Tag" color="orange" />

		<Tag text="magenta Tag" color="magenta" />

		<Tag text="lime Tag" color="lime" />

		<Tag text="grey Tag" color="grey" />

		<Tag text="greenLight Tag" color="greenLight" />

		<Tag text="tealLight Tag" color="tealLight" />

		<Tag text="blueLight Tag" color="blueLight" />

		<Tag text="purpleLight Tag" color="purpleLight" />

		<Tag text="redLight Tag" color="redLight" />

		<Tag text="yellowLight Tag" color="yellowLight" />

		<Tag text="orangeLight Tag" color="orangeLight" />

		<Tag text="magentaLight Tag" color="magentaLight" />

		<Tag text="limeLight Tag" color="limeLight" />

		<Tag text="greyLight Tag" color="greyLight" />

	</TagGroup>

);
```

## Text max length

Once the text reaches 180px, it is truncated with an ellipsis. Avoid truncation wherever possible by using short text in tags. 

```jsx
import React from 'react';



import { SimpleTag as Tag } from '@atlaskit/tag';



const cupcakeipsum = 'Croissant tiramisu gummi bears.';



export default () => <Tag text={cupcakeipsum} />;
```

---

[View Original Documentation](https://atlassian.design/components/tag/examples)
