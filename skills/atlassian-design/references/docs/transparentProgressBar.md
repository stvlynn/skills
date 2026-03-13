# Transparent progress bar

A transparent progress bar is used on bold backgrounds to maintain suitable contrast.

---

## Default

```jsx
import React from 'react';



import { TransparentProgressBar } from '@atlaskit/progress-bar';



const TransparentProgressBarExample = () => {

	return <TransparentProgressBar ariaLabel="Done: 4 of 10 issues" value={0.4} />;

};



export default TransparentProgressBarExample;
```

## Indeterminate

A transparent progress bar can be indeterminate, just like a standard progress bar. 

```jsx
import React from 'react';



import { TransparentProgressBar } from '@atlaskit/progress-bar';



const TransparentProgressBarIndeterminateExample = () => {

	return <TransparentProgressBar ariaLabel="Loading issues" isIndeterminate />;

};



export default TransparentProgressBarIndeterminateExample;
```

---

[View Original Documentation](https://atlassian.design/components/progress-bar/transparent-progress-bar/examples)
