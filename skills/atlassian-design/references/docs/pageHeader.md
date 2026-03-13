# Page header

A page header defines the top of a page. It contains a title and can be optionally combined with breadcrumbs buttons, search, and filters.

---

## Default

Use a default page header for a title underneath breadcrumbs. The header automatically wraps if the text is too long. 

```jsx
import React from 'react';



import Breadcrumbs, { BreadcrumbsItem } from '@atlaskit/breadcrumbs';

import __noop from '@atlaskit/ds-lib/noop';

import PageHeader from '@atlaskit/page-header';



const breadcrumbs = (

	<Breadcrumbs onExpand={__noop}>

		<BreadcrumbsItem text="Projects" key="Projects" />

		<BreadcrumbsItem text="Design System" key="Design System" />

	</Breadcrumbs>

);



const PageHeaderDefaultExample = () => {

	return <PageHeader breadcrumbs={breadcrumbs}>How to use the page header component</PageHeader>;

};



export default PageHeaderDefaultExample;
```

## Complex

Page headers can include breadcrumbs, which appear above the header. You can also pass buttons into actions. The action buttons appear at the end of the header. To help people refine the page content on a more granular level, a filter bar and search dropdown component can be added to the bottomBar below the header title. 

```jsx
/**

 * @jsxRuntime classic

 * @jsx jsx

 */

import Breadcrumbs, { BreadcrumbsItem } from '@atlaskit/breadcrumbs';

import ButtonGroup from '@atlaskit/button/button-group';

import Button from '@atlaskit/button/new';

import { cssMap, jsx } from '@atlaskit/css';

import __noop from '@atlaskit/ds-lib/noop';

import PageHeader from '@atlaskit/page-header';

import { Box, Inline } from '@atlaskit/primitives/compiled';

import Select from '@atlaskit/select';

import TextField from '@atlaskit/textfield';

import { token } from '@atlaskit/tokens';



const styles = cssMap({

	selectContainer: {

		flex: '0 0 200px',

		marginInlineStart: token('space.100'),

	},



	flexBox: {

		flex: '0 0 200px',

	},

});



const breadcrumbs = (

	<Breadcrumbs onExpand={__noop}>

		<BreadcrumbsItem text="Teams" key="Teams" />

		<BreadcrumbsItem text="Design System Team" key="Design System Team" />

	</Breadcrumbs>

);

const actionsContent = (

	<ButtonGroup label="Content actions">

		<Button appearance="primary">Edit page</Button>

		<Button>Share</Button>

		<Button>...</Button>

	</ButtonGroup>

);

const barContent = (

	<Inline>

		<Box xcss={styles.flexBox}>

			<TextField isCompact placeholder="Filter" aria-label="Filter" />

		</Box>

		<Box xcss={styles.selectContainer}>

			<Select spacing="compact" placeholder="Choose an option" label="Choose an option" />

		</Box>

	</Inline>

);



const PageHeaderComplexExample = () => {

	return (

		<PageHeader breadcrumbs={breadcrumbs} actions={actionsContent} bottomBar={barContent}>

			Introducing the Design System Team

		</PageHeader>

	);

};



export default PageHeaderComplexExample;
```

## Custom title component

Use custom components for titles where necessary. For example, an inline edit lets people edit the title on the page. 

```jsx
/**

 * @jsxRuntime classic

 * @jsx jsx

 */



import { css, jsx } from '@compiled/react';



import __noop from '@atlaskit/ds-lib/noop';

import InlineEdit from '@atlaskit/inline-edit';

import PageHeader from '@atlaskit/page-header';

import { token } from '@atlaskit/tokens';



const readViewStyles = css({

	display: 'flex',

	maxWidth: '100%',

	font: token('font.heading.large'),

	overflow: 'hidden',

	paddingBlockEnd: token('space.100'),

	paddingBlockStart: token('space.100'),

	paddingInlineEnd: token('space.075'),

	paddingInlineStart: token('space.075'),

});



const editViewStyles = css({

	boxSizing: 'border-box',

	width: '100%',

	border: `2px solid ${token('color.border')}`,

	borderRadius: '3px',

	cursor: 'inherit',

	font: token('font.heading.large'),

	outline: 'none',

	paddingBlockEnd: token('space.075'),

	paddingBlockStart: token('space.075'),

	paddingInlineEnd: token('space.075'),

	paddingInlineStart: token('space.075'),

	'&:focus': {

		border: `2px solid ${token('color.border.focused')}`,

	},

});



const CustomTitleComponent = () => {

	return (

		<InlineEdit

			readView={() => <div css={readViewStyles}>Editable title</div>}

			editView={(props, ref) => <input css={editViewStyles} {...props} ref={ref} />}

			defaultValue="Editable title"

			onConfirm={__noop}

		/>

	);

};



const PageHeaderCustomTitleExample = () => {

	return (

		<PageHeader disableTitleStyles>

			<CustomTitleComponent />

		</PageHeader>

	);

};



export default PageHeaderCustomTitleExample;
```

## Focus heading

You can set the focus back to the title for accessibility purposes. 

```jsx
import React, { useState } from 'react';



import Breadcrumbs, { BreadcrumbsItem } from '@atlaskit/breadcrumbs';

import Button from '@atlaskit/button/new';

import __noop from '@atlaskit/ds-lib/noop';

import PageHeader from '@atlaskit/page-header';

import { Box } from '@atlaskit/primitives/compiled';



const breadcrumbs = (

	<Breadcrumbs onExpand={__noop}>

		<BreadcrumbsItem text="Project" key="Project" />

		<BreadcrumbsItem text="Design System" key="Design System" />

	</Breadcrumbs>

);



const PageHeaderFocusHeadingExample = () => {

	const [ref, setRef] = useState<HTMLElement>();



	const onClick = () => {

		if (ref) {

			ref.focus();

		}

	};



	const innerRef = (element: HTMLElement) => {

		setRef(element);

	};



	return (

		<Box>

			<Button onClick={onClick}>Focus on the heading</Button>

			<PageHeader breadcrumbs={breadcrumbs} innerRef={innerRef}>

				Task: Improve accessibility for the page header

			</PageHeader>

		</Box>

	);

};



export default PageHeaderFocusHeadingExample;
```

---

[View Original Documentation](https://atlassian.design/components/page-header/examples)
