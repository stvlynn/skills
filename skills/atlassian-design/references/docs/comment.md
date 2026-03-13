# Comment

A comment displays discussions and user feedback.

---

## Default

The simplest form of a comment contains an avatar and text. Our mission is to unleash the potential of every team. 

```jsx
import React from 'react';



import Avatar from '@atlaskit/avatar';

import Comment from '@atlaskit/comment';



import sampleAvatar from '../images/avatar_400x400.jpg';



const CommentDefaultExample = () => {

	return (

		<Comment

			avatar={<Avatar name="Scott Farquhar" src={sampleAvatar} />}

			content={<p>Our mission is to unleash the potential of every team.</p>}

		/>

	);

};



export default CommentDefaultExample;
```

## Full

Many features are available to customize the display of the comment. The package exports a wrapper component, as well as smaller components which can be passed through to display a richer comment. 

### Scott Farquhar
AUTHOR
Mar 14, 2024
Edited
•
Restricted to Admins Only

During COVID we took a big bet on remote work. It made sense, as we already had employees in 10+ countries. Today, the majority of hires live over 2hrs from an office and these amazing, talented people couldn't work for us otherwise. Proud to be recognized as a great place to work. 

```jsx
import React from 'react';



import Avatar from '@atlaskit/avatar';

import Comment, {

	CommentAction,

	CommentAuthor,

	CommentEdited,

	CommentTime,

} from '@atlaskit/comment';



import sampleAvatar from '../images/avatar_400x400.jpg';



const CommentFullExample = () => {

	return (

		<Comment

			avatar={<Avatar name="Scott Farquhar" src={sampleAvatar} />}

			author={<CommentAuthor>Scott Farquhar</CommentAuthor>}

			type="author"

			edited={<CommentEdited>Edited</CommentEdited>}

			restrictedTo="Restricted to Admins Only"

			time={<CommentTime>Mar 14, 2024</CommentTime>}

			content={

				<p>

					During COVID we took a big bet on remote work. It made sense, as we already had employees

					in 10+ countries. Today, the majority of hires live over 2hrs from an office and these

					amazing, talented people couldn't work for us otherwise. Proud to be recognized as a great

					place to work.

				</p>

			}

			actions={[

				<CommentAction>Reply</CommentAction>,

				<CommentAction>Edit</CommentAction>,

				<CommentAction>Like</CommentAction>,

			]}

		/>

	);

};



export default CommentFullExample;
```

## Nested

Comments can be nested inside of each other by passing comments as children. 

### Scott Farquhar
AUTHOR
Jun 3, 2022

Hard to believe it’s been 20 years since we started Atlassian, but we’re just getting started! 

### John Smith
Jun 3, 2022

Congratulations! 

### Sabina Vu
Jun 4, 2022

I wonder what Atlassian will be like 20 years from now? 

```jsx
import React from 'react';



import Avatar from '@atlaskit/avatar';

import Comment, { CommentAction, CommentAuthor, CommentTime } from '@atlaskit/comment';



import sampleAvatar from '../images/avatar_400x400.jpg';



const CommentNestedExample = () => {

	return (

		<Comment

			avatar={<Avatar name="Scott Farquhar" src={sampleAvatar} />}

			author={<CommentAuthor>Scott Farquhar</CommentAuthor>}

			type="author"

			time={<CommentTime>Jun 3, 2022</CommentTime>}

			content={

				<p>

					Hard to believe it’s been 20 years since we started Atlassian, but we’re just getting

					started!

				</p>

			}

			actions={[

				<CommentAction>Reply</CommentAction>,

				<CommentAction>Edit</CommentAction>,

				<CommentAction>Like</CommentAction>,

			]}

		>

			<Comment

				avatar={<Avatar name="John Smith" />}

				author={<CommentAuthor>John Smith</CommentAuthor>}

				time={<CommentTime>Jun 3, 2022</CommentTime>}

				content={<p>Congratulations!</p>}

				actions={[<CommentAction>Reply</CommentAction>, <CommentAction>Like</CommentAction>]}

			>

				<Comment

					avatar={<Avatar name="Sabina Vu" />}

					author={<CommentAuthor>Sabina Vu</CommentAuthor>}

					time={<CommentTime>Jun 4, 2022</CommentTime>}

					content={<p>I wonder what Atlassian will be like 20 years from now?</p>}

					actions={[<CommentAction>Reply</CommentAction>, <CommentAction>Like</CommentAction>]}

				/>

			</Comment>

		</Comment>

	);

};



export default CommentNestedExample;
```

## Saving

An "optimistic saving" mode can be enabled using isSaving, which hides actions and lets people know the comment is saving, by showing text from the savingText prop. Using the optimistic UI technique means that people receive a fast, responsive experience even on limited connections. 

### Scott Farquhar
Saving...

Building “soft skills,” like effective communication and collaboration, are vital to a team’s success. 

```jsx
import React, { useState } from 'react';



import Avatar from '@atlaskit/avatar';

import { Checkbox } from '@atlaskit/checkbox';

import Comment, { CommentAction, CommentAuthor, CommentTime } from '@atlaskit/comment';

import { Box } from '@atlaskit/primitives/compiled';



import sampleAvatar from '../images/avatar_400x400.jpg';



const CommentDefaultExample = () => {

	const [saving, setSaving] = useState(true);



	return (

		<>

			<Box>

				<Checkbox

					label="Enable saving mode"

					isChecked={saving}

					onChange={(e) => setSaving(e.currentTarget.checked)}

				/>

			</Box>

			<Comment

				isSaving={saving}

				savingText="Saving..."

				avatar={<Avatar name="Scott Farquhar" src={sampleAvatar} />}

				author={<CommentAuthor>Scott Farquhar</CommentAuthor>}

				time={<CommentTime>Mar 14, 2024</CommentTime>}

				content={

					<p>

						Building “soft skills,” like effective communication and collaboration, are vital to a

						team’s success.

					</p>

				}

				actions={[

					<CommentAction>Reply</CommentAction>,

					<CommentAction>Edit</CommentAction>,

					<CommentAction>Like</CommentAction>,

				]}

			/>

		</>

	);

};



export default CommentDefaultExample;
```

## Edited

Mark a comment as edited by passing a CommentEdited component to the the edited prop. 

### Scott Farquhar
Jul 3, 2020
Edited

I'm super proud that 69% of our almost 5,000 Atlassian employees donated their time for volunteering in the last year. Thanks team! 

```jsx
import React from 'react';



import Avatar from '@atlaskit/avatar';

import Comment, { CommentAuthor, CommentEdited, CommentTime } from '@atlaskit/comment';



import sampleAvatar from '../images/avatar_400x400.jpg';



const CommentEditedExample = () => {

	return (

		<Comment

			edited={<CommentEdited>Edited</CommentEdited>}

			avatar={<Avatar name="Scott Farquhar" src={sampleAvatar} />}

			author={<CommentAuthor>Scott Farquhar</CommentAuthor>}

			time={<CommentTime>Jul 3, 2020</CommentTime>}

			content={

				<p>

					I'm super proud that 69% of our almost 5,000 Atlassian employees donated their time for

					volunteering in the last year. Thanks team!

				</p>

			}

		/>

	);

};



export default CommentEditedExample;
```

## Restricted

Display a message in the comment header by using the restrictedTo prop. 

### Scott Farquhar
•
Restricted to Admins

I’ve seen first-hand how making it easy for employees to volunteer builds a stronger culture. It’s a great way to invest in your company and your community at the same time. 

```jsx
import React from 'react';



import Avatar from '@atlaskit/avatar';

import Comment, { CommentAuthor } from '@atlaskit/comment';



import sampleAvatar from '../images/avatar_400x400.jpg';



const CommentDefaultExample = () => {

	return (

		<Comment

			restrictedTo="Restricted to Admins"

			avatar={<Avatar name="Scott Farquhar" src={sampleAvatar} />}

			author={<CommentAuthor>Scott Farquhar</CommentAuthor>}

			content={

				<p>

					I’ve seen first-hand how making it easy for employees to volunteer builds a stronger

					culture. It’s a great way to invest in your company and your community at the same time.

				</p>

			}

		/>

	);

};



export default CommentDefaultExample;
```

## Highlighted

Highlight a comment using the highlighted prop. 

### Scott Farquhar
Mar 14, 2024

Atlassian employees choose everyday where and how they want to work - we call it Team Anywhere. This has been key for our continued growth. 

```jsx
import React from 'react';



import Avatar from '@atlaskit/avatar';

import Comment, { CommentAuthor, CommentTime } from '@atlaskit/comment';



import sampleAvatar from '../images/avatar_400x400.jpg';



const CommentHighlightedExample = () => {

	return (

		<Comment

			highlighted

			avatar={<Avatar name="Scott Farquhar" src={sampleAvatar} />}

			author={<CommentAuthor>Scott Farquhar</CommentAuthor>}

			time={<CommentTime>Mar 14, 2024</CommentTime>}

			content={

				<p>

					Atlassian employees choose everyday where and how they want to work - we call it Team

					Anywhere. This has been key for our continued growth.

				</p>

			}

		/>

	);

};



export default CommentHighlightedExample;
```

## Custom heading level

Change the heading level using the headingLevel prop. The default heading has an h3 tag. Make sure that headings are in the correct order and don’t skip levels. For example, an h3 should follow an h2 or lower, never an h1. I’m passionate about our mission to unleash the potential of every team. Teams are so much more productive than a single person. If we can increase team bandwidth we can truly improve the world. 

```jsx
import React from 'react';



import Avatar from '@atlaskit/avatar';

import Comment, { CommentAuthor, CommentTime } from '@atlaskit/comment';



import sampleAvatar from '../images/avatar_400x400.jpg';



const CommentCustomHeadingLevelExample = () => {

	return (

		<Comment

			headingLevel="5"

			avatar={<Avatar name="Scott Farquhar" src={sampleAvatar} />}

			author={<CommentAuthor>Scott Farquhar</CommentAuthor>}

			time={<CommentTime>Mar 14, 2024</CommentTime>}

			content={

				<p>

					I’m passionate about our mission to unleash the potential of every team. Teams are so much

					more productive than a single person. If we can increase team bandwidth we can truly

					improve the world.

				</p>

			}

		/>

	);

};



export default CommentCustomHeadingLevelExample;
```

---

[View Original Documentation](https://atlassian.design/components/comment/examples)
