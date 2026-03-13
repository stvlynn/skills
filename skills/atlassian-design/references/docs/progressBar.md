# Progress bar

A progress bar communicates the status of a system process.

---

## Appearance

### Default

The default appearance of a progress bar. 

```jsx
import React from 'react';



import ProgressBar from '@atlaskit/progress-bar';



const ProgressBarDefaultExample = () => {

	return <ProgressBar ariaLabel="Done: 3 of 10 issues" value={0.3} />;

};



export default ProgressBarDefaultExample;
```

### Inverse

Use the inverse appearance on bold backgrounds to maintain suitable contrast. 

```jsx
import React from 'react';



import ProgressBar from '@atlaskit/progress-bar';



const ProgressBarInverseExample = () => {

	return <ProgressBar appearance="inverse" ariaLabel="Done: 6 of 10 issues" value={0.6} />;

};



export default ProgressBarInverseExample;
```

### Success

The success appearance lets people know that the process is complete. 

```jsx
import React from 'react';



import ProgressBar from '@atlaskit/progress-bar';



const ProgressBarSuccessExample = () => {

	return <ProgressBar appearance="success" ariaLabel="Done: 10 of 10 issues" value={1} />;

};



export default ProgressBarSuccessExample;
```

## Indeterminate

Indeterminate progress bars display movement along the container until the process is finished. Use this when the percentage amount of the progress bar is unknown. 

```jsx
import React from 'react';



import ProgressBar from '@atlaskit/progress-bar';



const ProgressBarIndeterminateExample = () => {

	return <ProgressBar ariaLabel="Loading issues" isIndeterminate />;

};



export default ProgressBarIndeterminateExample;
```

---

[View Original Documentation](https://atlassian.design/components/progress-bar/examples)
