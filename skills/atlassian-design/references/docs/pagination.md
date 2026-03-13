# Pagination

Pagination allows you to divide large amounts of content into smaller chunks across multiple pages.

---

## Default

The default form of pagination. 

```jsx
import React from 'react';



import Pagination from '@atlaskit/pagination';



export default function PaginationDefaultExample() {

	return (

		<Pagination

			nextLabel="Next"

			label="Page"

			pageLabel="Page"

			pages={[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]}

			previousLabel="Previous"

		/>

	);

}
```

## Truncation

When the number of pages exceeds the maximum display limit, an ellipsis is used to truncate the remaining pages. When the current page is separated by more than five pages from both the first and last page, we use double truncation. 

```jsx
import React from 'react';



import Pagination from '@atlaskit/pagination';



export default function PaginationTruncationExample() {

	return (

		<Pagination

			nextLabel="Next"

			label="Page"

			pageLabel="Page"

			pages={[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]}

			previousLabel="Previous"

		/>

	);

}
```

## Default selected index

You can specify index of the page to be selected by default. 

```jsx
import React from 'react';



import Pagination from '@atlaskit/pagination';



export default function PaginationDefaultSelectedIndexExample() {

	return (

		<Pagination

			defaultSelectedIndex={5}

			pages={[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]}

			nextLabel="Next"

			label="Page"

			pageLabel="Page"

			previousLabel="Previous"

		/>

	);

}
```

---

[View Original Documentation](https://atlassian.design/components/pagination/examples)
