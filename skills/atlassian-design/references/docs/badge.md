# Badge

A badge is a visual indicator for numeric values such as tallies and scores.

---

## Appearance

### Default

The default form of a badge. 

```jsx
import React from 'react';



import Badge from '@atlaskit/badge';



const BadgeDefaultExample = () => {

	return <Badge>{8}</Badge>;

};



export default BadgeDefaultExample;
```

### Primary

Use a primary badge to help draw attention to new or updated information. 

```jsx
import React from 'react';



import Badge from '@atlaskit/badge';



const BadgePrimaryExample = () => {

	return <Badge appearance="primary">{5}</Badge>;

};



export default BadgePrimaryExample;
```

### Primary inverted

Use a primaryInverted badge when high contrast against a darker background color is needed. 

```jsx
import React from 'react';



import Badge from '@atlaskit/badge';



const BadgePrimaryInvertedExample = () => {

	return <Badge appearance="primaryInverted">{5}</Badge>;

};



export default BadgePrimaryInvertedExample;
```

### Important

Use an important badge to call attention to information that needs to stand out. For example, notifications in Confluence. 

```jsx
import React from 'react';



import Badge from '@atlaskit/badge';



const BadgeImportantExample = () => {

	return <Badge appearance="important">{25}</Badge>;

};



export default BadgeImportantExample;
```

### Added

Use an added appearance to show a plus symbol (+) preceding the number. For example, when characters are added to a line of code in Bitbucket. 

```jsx
import React from 'react';



import Badge from '@atlaskit/badge';



const BadgeAddedExample = () => {

	return <Badge appearance="added">+100</Badge>;

};



export default BadgeAddedExample;
```

### Removed

Use a removed appearance to show a minus symbol (-) preceding the number. For example, when characters are removed from a line of code in Bitbucket. 

```jsx
import React from 'react';



import Badge from '@atlaskit/badge';



const BadgeRemovedExample = () => {

	return <Badge appearance="removed">-100</Badge>;

};



export default BadgeRemovedExample;
```

## Max value

### Capped number values

Use the max prop to cap the value of a badge. When the value to display is greater than the max prop, a + will be appended. The default max value of a badge is 99. 

```jsx
import React from 'react';



import Badge from '@atlaskit/badge';



const BadgeMaxValueExample = () => {

	return (

		<Badge appearance="added" max={500}>

			{1000}

		</Badge>

	);

};



export default BadgeMaxValueExample;
```

### Disabled

If the max prop is set to false then the value will be displayed as it was passed, without a plus symbol (+). 

```jsx
import React from 'react';



import Badge from '@atlaskit/badge';



const BadgeMaxValueDisabledExample = () => {

	return (

		<Badge appearance="added" max={false}>

			{1000}

		</Badge>

	);

};



export default BadgeMaxValueDisabledExample;
```

---

[View Original Documentation](https://atlassian.design/components/badge/examples)
