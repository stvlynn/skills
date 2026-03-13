# Success progress bar

A success progress bar indicates the completion of a process.

---

## Complete

A success progress bar turns green when value is 1. 

```jsx
import React from 'react';



import { SuccessProgressBar } from '@atlaskit/progress-bar';



const SuccessProgressBarCompleteExample = () => {

	return <SuccessProgressBar ariaLabel="Done: 10 of 10 issues" value={1} />;

};



export default SuccessProgressBarCompleteExample;
```

## Incomplete

When a success progress bar is incomplete (any value below 1) it looks and behaves exactly like a standard progress bar. 

```jsx
import React from 'react';



import { SuccessProgressBar } from '@atlaskit/progress-bar';



const SuccessProgressBarIncompleteExample = () => {

	return <SuccessProgressBar ariaLabel="Done: 8 of 10 issues" value={0.8} />;

};



export default SuccessProgressBarIncompleteExample;
```

## Indeterminate

A success progress bar can be indeterminate, just like a standard progress bar. 

```jsx
import React from 'react';



import { SuccessProgressBar } from '@atlaskit/progress-bar';



const SuccessProgressBarIndeterminateExample = () => {

	return <SuccessProgressBar ariaLabel="Loading issues" isIndeterminate />;

};



export default SuccessProgressBarIndeterminateExample;
```

---

[View Original Documentation](https://atlassian.design/components/progress-bar/success-progress-bar/examples)
