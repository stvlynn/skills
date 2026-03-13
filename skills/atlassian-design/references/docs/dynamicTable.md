# Dynamic table

A dynamic table displays rows of data with built-in pagination, sorting, and re-ordering functionality.

---

## Uncontrolled

Dynamic table manages sorting, pagination, loading, and drag and drop state management by default. If this functionality isn't needed, use the native HTML table element. 

```jsx
import React from 'react';



import DynamicTable from '@atlaskit/dynamic-table';



import { head, rows } from './content/sample-data';



export default function TableUncontrolled() {

	return (

		<DynamicTable

			head={head}

			rows={rows}

			rowsPerPage={5}

			defaultPage={1}

			loadingSpinnerSize="large"

			isRankable

			testId="table"

		/>

	);

}
```

| Name | Party | Term | Comment | Actions |
| --- | --- | --- | --- | --- |
| George WashingtonGeorge Washington | None, Federalist | 1789-1797 | 0 | More |
| John AdamsJohn Adams | Federalist | 1797-1801 | 1 | More |
| Thomas JeffersonThomas Jefferson | Democratic-Republican | 1801-1809 | 2 | More |
| James MadisonJames Madison | Democratic-Republican | 1809-1817 | 3 | More |
| James MonroeJames Monroe | Democratic-Republican | 1817-1825 | 4 | More |

## Controlled

In a controlled dynamic table, you need to manage sorting, drag and drop, and pagination on your own. If you require this functionality, use the stateless dynamic table component. 

```jsx
import React, { useState } from 'react';



import Banner from '@atlaskit/banner';

import ButtonGroup from '@atlaskit/button/button-group';

import Button from '@atlaskit/button/new';

import { DynamicTableStateless } from '@atlaskit/dynamic-table';

import WarningIcon from '@atlaskit/icon/glyph/warning';



import { head, rows } from './content/sample-data';



export default function TableControlled() {

	const [pageNumber, setPageNumber] = useState(3);

	const navigateTo = (pageNumber: number) => {

		setPageNumber(pageNumber);

	};



	return (

		<>

			<Banner appearance="warning" icon={<WarningIcon label="" secondaryColor="inherit" />}>

				This is a stateless table example, which doesn't have pagination support. To navigate pages,

				use the "Previous page" and "Next page" buttons.

			</Banner>



			<ButtonGroup label="Paging navigation">

				<Button isDisabled={pageNumber === 1} onClick={() => navigateTo(pageNumber - 1)}>

					Previous Page

				</Button>

				<Button isDisabled={pageNumber === 5} onClick={() => navigateTo(pageNumber + 1)}>

					Next Page

				</Button>

			</ButtonGroup>

			<DynamicTableStateless

				head={head}

				rows={rows}

				rowsPerPage={5}

				page={pageNumber}

				loadingSpinnerSize="large"

				isLoading={false}

				isFixedSize

				sortKey="term"

				sortOrder="DESC"

				onSort={() => console.log('onSort')}

				onSetPage={() => console.log('onSetPage')}

			/>

		</>

	);

}
```

| Name | Party | Term | Comment | Actions |
| --- | --- | --- | --- | --- |
| Dwight David EisenhowerDwight David Eisenhower | Republican | 1953-1961 | 23 | More |
| Harry S TrumanHarry S Truman | Democrat | 1945-1953 | 22 | More |
| Franklin Delano RooseveltFranklin Delano Roosevelt | Democrat | 1933-1945 | 21 | More |
| Herbert C. HooverHerbert C. Hoover | Republican | 1929-1933 | 20 | More |
| Calvin CoolidgeCalvin Coolidge | Republican | 1923-1929 | 19 | More |

## Sorting

Sorting a dynamic table takes place using the key set on each cell. Note that the type of key will affect the sorted result. For example, numeric and string keys will result in different orderings. Avoid using objects or React nodes as keys. 

```jsx
import React, { type FC } from 'react';



import DynamicTable from '@atlaskit/dynamic-table';



const caption = 'Example issue with DynamicTable';



const head = {

	cells: [

		{

			key: 'number',

			content: 'Number',

			isSortable: true,

		},

		{

			key: 'string',

			content: 'String',

			isSortable: true,

		},

	],

};



const rows = [

	[1, 'd'],

	[2, 'c'],

	[3, 'a'],

	[4, 'b'],

].map(([number, letter]) => ({

	key: number.toString(),

	cells: [

		{

			key: number,

			content: number,

		},

		{

			key: letter,

			content: letter,

		},

	],

}));



const SortingExample: FC = () => (

	// eslint-disable-next-line @atlaskit/ui-styling-standard/enforce-style-prop -- Ignored via go/DSP-18766

	<div style={{ maxWidth: 800 }}>

		<DynamicTable

			caption={caption}

			head={head}

			rows={rows}

			isFixedSize

			defaultSortKey="number"

			defaultSortOrder="ASC"

		/>

	</div>

);



export default SortingExample;
```

| Number | String |
| --- | --- |
| 1 | d |
| 2 | c |
| 3 | a |
| 4 | b |

## Loading states

Dynamic table uses a spinner to denote loading state. This is toggled by the isLoading prop. Table content is set to 20% opacity in this loading state, using the opacity.loading token. 

```jsx
import React, { useState } from 'react';



import Button from '@atlaskit/button/new';

import { DynamicTableStateless } from '@atlaskit/dynamic-table';



import { head, rows } from './content/sample-data';



const LoadingPartialPageExample = () => {

	const [isLoading, setIsLoading] = useState(false);

	return (

		<div>

			<Button onClick={() => setIsLoading((loading) => !loading)}>Toggle loading</Button>

			<DynamicTableStateless

				head={head}

				rows={rows}

				rowsPerPage={5}

				page={1}

				isLoading={isLoading}

			/>

		</div>

	);

};



export default LoadingPartialPageExample;
```

| Name | Party | Term | Comment | Actions |
| --- | --- | --- | --- | --- |
| George WashingtonGeorge Washington | None, Federalist | 1789-1797 | 0 | More |
| John AdamsJohn Adams | Federalist | 1797-1801 | 1 | More |
| Thomas JeffersonThomas Jefferson | Democratic-Republican | 1801-1809 | 2 | More |
| James MadisonJames Madison | Democratic-Republican | 1809-1817 | 3 | More |
| James MonroeJames Monroe | Democratic-Republican | 1817-1825 | 4 | More |

## Empty state

Use the emptyView prop to show an empty state in the dynamic table. Empty states communicate that the table has no content to show. If there's an action that people must take to create or show table content, add this to the empty state so they know how to proceed. See empty state guidelines for more guidance. 

<table class="_1bsb1osq _yq5hus1c _btyzidpf _ect41gqc" style="--local-dynamic-table-hover-bg: var(--ds-background-neutral-subtle-hovered, #FAFBFC); --local-dynamic-table-highlighted-bg: var(--ds-background-selected, #DEEBFF); --local-dynamic-table-hover-highlighted-bg: var(--ds-background-selected-hovered, #B3D4FF); --local-dynamic-table-row-focus-outline: var(--ds-border-focused, #4C9AFF);"><thead class="_179rglyw"><tr><th class="_izbqglyw _h7alglyw _85i51b66 _1q511b66 _y4tiu2gc _bozgu2gc _y3gn1e5h _1s37ze3t _uupyze3t _11c8dcr7 _179r1on0 _mqm2glyw _t51zglyw _191wglyw _vchhusvi _kqswh2mm _syaz34id _k48pmoej _s7n4jp4b _1ygbvd8c _1bsb8a2a _173zglyw _pw6dglyw _1xgk1j28 _1wfn1j28 _y9yonqa1 _997wnqa1 _sklb1l7b _1j091l7b _19w61ule _1w611ule _1hvvidpf _n56nidpf _wyc4idpf _1d4oidpf _no7mstnw _qh32stnw _4b5mb3bt _hn3bb3bt _14gsx0bf _cigmx0bf _c77kvia6 _qzvtu2gc _f473via6 _1fpyidpf _a04fh2mm _xv14glyw _58ej1kw7 _1ay31kw7 _mdbq1kw7 _10pp1kw7 _1yw3ze3t _n2fdze3t _8607ze3t _szhwze3t _1g2wwc43 _ze9fwc43 _1lcgnqa1 _at5qnqa1 _o4d71l7b _npl51l7b _1rp11onz _1iornqa1 _oi051l7b _1ehx1onz _19t8nqa1 _1bog1l7b" style="--local-dynamic-table-width: 25%; --local-dynamic-table-text-color: var(--ds-text-subtlest, #5E6C84);"><div class="_19itglyw _vchhusvi _r06hglyw _1e0c1txw _4cvr1h6o"><div role="presentation"><button aria-roledescription="Sort button" type="button" class="_mizu194a _1ah31bk5 _ra3xnqa1 _128m1bk5 _1cvmnqa1 _4davt94y _19itglyw _vchhusvi _r06hglyw _80omtlke _1e0c1txw _bfhk1j28 _4cvr1h6o _ca0qze3t _u5f3ze3t _n3tdze3t _19bvze3t _d0altlke"><div class="_1e0c1txw _vchhusvi _tzy4kb7n _u5f31b66"><span class="_19pkidpf _2hwxidpf _otyridpf _18u0idpf _1i4qfg65 _11c81o8v _syaz1gjq _1reo15vq _18m915vq _1e0ccj1k _sudp1e54 _1nmz9jpi _k48pmoej" style="-webkit-line-clamp: 1;">Name</span></div><div class="_1e0c1txw _vchhusvi _tzy4idpf _bfhk1j28 _ca0q1b66 _u5f31b66 _n3td1b66 _19bv1b66 _1h7hkb7n"><span aria-hidden="true" class="_1e0c1o8l _vchhusvi _1o9zidpf _vwz4kb7n _y4ti1igz _bozg1mb9 _12va1onz _jcxd1r8n" style="color: var(--ds-text-subtle, #44546F);"><svg fill="none" viewBox="0 0 16 16" role="presentation" class="_1reo15vq _18m915vq _syaz1r31 _lcxvglyw _s7n4yfq0 _vc881r31 _1bsbpxbi _4t3ipxbi"><path fill="currentcolor" fill-rule="evenodd" d="M8.75 1v11.44l3.72-3.72 1.06 1.06-5 5a.75.75 0 0 1-1.06 0l-5-5 1.06-1.06 3.72 3.72V1z" clip-rule="evenodd"></path></svg></span></div></button></div></div></th><th class="_izbqglyw _h7alglyw _85i51b66 _1q511b66 _y4tiu2gc _bozgu2gc _y3gn1e5h _1s37ze3t _uupyze3t _11c8dcr7 _179r1on0 _mqm2glyw _t51zglyw _191wglyw _vchhusvi _kqswh2mm _syaz34id _k48pmoej _s7n4jp4b _1ygbvd8c _1bsb8a2a _173zglyw _pw6dglyw _1xgk1j28 _1wfn1j28 _y9yonqa1 _997wnqa1 _sklb1l7b _1j091l7b _19w61ule _1w611ule _1hvvidpf _n56nidpf _wyc4idpf _1d4oidpf _no7mstnw _qh32stnw _4b5mb3bt _hn3bb3bt _14gsx0bf _cigmx0bf _c77kvia6 _qzvtu2gc _f473via6 _1fpyidpf _a04fh2mm _xv14glyw _58ej1kw7 _1ay31kw7 _mdbq1kw7 _10pp1kw7 _1yw3ze3t _n2fdze3t _8607ze3t _szhwze3t _1g2wwc43 _ze9fwc43 _1lcgnqa1 _at5qnqa1 _o4d71l7b _npl51l7b _1rp11onz _1iornqa1 _oi051l7b _1ehx1onz _19t8nqa1 _1bog1l7b" style="--local-dynamic-table-width: 15%; --local-dynamic-table-text-color: var(--ds-text-subtlest, #5E6C84);"><div class="_19itglyw _vchhusvi _r06hglyw _1e0c1txw _4cvr1h6o"><div role="presentation"><button aria-roledescription="Sort button" type="button" class="_mizu194a _1ah31bk5 _ra3xnqa1 _128m1bk5 _1cvmnqa1 _4davt94y _19itglyw _vchhusvi _r06hglyw _80omtlke _1e0c1txw _bfhk1j28 _4cvr1h6o _ca0qze3t _u5f3ze3t _n3tdze3t _19bvze3t _d0altlke"><div class="_1e0c1txw _vchhusvi _tzy4kb7n _u5f31b66"><span class="_19pkidpf _2hwxidpf _otyridpf _18u0idpf _1i4qfg65 _11c81o8v _syaz1gjq _1reo15vq _18m915vq _1e0ccj1k _sudp1e54 _1nmz9jpi _k48pmoej" style="-webkit-line-clamp: 1;">Party</span></div><div class="_1e0c1txw _vchhusvi _tzy4idpf _bfhk1j28 _ca0q1b66 _u5f31b66 _n3td1b66 _19bv1b66 _1h7hkb7n"><span aria-hidden="true" class="_1e0c1o8l _vchhusvi _1o9zidpf _vwz4kb7n _y4ti1igz _bozg1mb9 _12va1onz _jcxd1r8n" style="color: var(--ds-text-subtle, #44546F);"><svg fill="none" viewBox="0 0 16 16" role="presentation" class="_1reo15vq _18m915vq _syaz1r31 _lcxvglyw _s7n4yfq0 _vc881r31 _1bsbpxbi _4t3ipxbi"><path fill="currentcolor" fill-rule="evenodd" d="M8.75 1v11.44l3.72-3.72 1.06 1.06-5 5a.75.75 0 0 1-1.06 0l-5-5 1.06-1.06 3.72 3.72V1z" clip-rule="evenodd"></path></svg></span></div></button></div></div></th><th class="_izbqglyw _h7alglyw _85i51b66 _1q511b66 _y4tiu2gc _bozgu2gc _y3gn1e5h _1s37ze3t _uupyze3t _11c8dcr7 _179r1on0 _mqm2glyw _t51zglyw _191wglyw _vchhusvi _kqswh2mm _syaz34id _k48pmoej _s7n4jp4b _1ygbvd8c _1bsb8a2a _173zglyw _pw6dglyw _1xgk1j28 _1wfn1j28 _y9yonqa1 _997wnqa1 _sklb1l7b _1j091l7b _19w61ule _1w611ule _1hvvidpf _n56nidpf _wyc4idpf _1d4oidpf _no7mstnw _qh32stnw _4b5mb3bt _hn3bb3bt _14gsx0bf _cigmx0bf _c77kvia6 _qzvtu2gc _f473via6 _1fpyidpf _a04fh2mm _xv14glyw _58ej1kw7 _1ay31kw7 _mdbq1kw7 _10pp1kw7 _1yw3ze3t _n2fdze3t _8607ze3t _szhwze3t _1g2wwc43 _ze9fwc43 _1lcgnqa1 _at5qnqa1 _o4d71l7b _npl51l7b _1rp11onz _1iornqa1 _oi051l7b _1ehx1onz _19t8nqa1 _1bog1l7b" style="--local-dynamic-table-width: 10%; --local-dynamic-table-text-color: var(--ds-text-subtlest, #5E6C84);"><div class="_19itglyw _vchhusvi _r06hglyw _1e0c1txw _4cvr1h6o"><div role="presentation"><button aria-roledescription="Sort button" type="button" class="_mizu194a _1ah31bk5 _ra3xnqa1 _128m1bk5 _1cvmnqa1 _4davt94y _19itglyw _vchhusvi _r06hglyw _80omtlke _1e0c1txw _bfhk1j28 _4cvr1h6o _ca0qze3t _u5f3ze3t _n3tdze3t _19bvze3t _d0altlke"><div class="_1e0c1txw _vchhusvi _tzy4kb7n _u5f31b66"><span class="_19pkidpf _2hwxidpf _otyridpf _18u0idpf _1i4qfg65 _11c81o8v _syaz1gjq _1reo15vq _18m915vq _1e0ccj1k _sudp1e54 _1nmz9jpi _k48pmoej" style="-webkit-line-clamp: 1;">Term</span></div><div class="_1e0c1txw _vchhusvi _tzy4idpf _bfhk1j28 _ca0q1b66 _u5f31b66 _n3td1b66 _19bv1b66 _1h7hkb7n"><span aria-hidden="true" class="_1e0c1o8l _vchhusvi _1o9zidpf _vwz4kb7n _y4ti1igz _bozg1mb9 _12va1onz _jcxd1r8n" style="color: var(--ds-text-subtle, #44546F);"><svg fill="none" viewBox="0 0 16 16" role="presentation" class="_1reo15vq _18m915vq _syaz1r31 _lcxvglyw _s7n4yfq0 _vc881r31 _1bsbpxbi _4t3ipxbi"><path fill="currentcolor" fill-rule="evenodd" d="M8.75 1v11.44l3.72-3.72 1.06 1.06-5 5a.75.75 0 0 1-1.06 0l-5-5 1.06-1.06 3.72 3.72V1z" clip-rule="evenodd"></path></svg></span></div></button></div></div></th><th class="_izbqglyw _h7alglyw _85i51b66 _1q511b66 _y4tiu2gc _bozgu2gc _y3gn1e5h _1s37ze3t _uupyze3t _11c8dcr7 _179r1on0 _mqm2glyw _t51zglyw _191wglyw _vchhusvi _kqswh2mm _syaz34id _k48pmoej _s7n4jp4b _1ygbvd8c _1bsb8a2a" style="--local-dynamic-table-text-color: var(--ds-text-subtlest, #5E6C84);">Comment</th><th class="_izbqglyw _h7alglyw _85i51b66 _1q511b66 _y4tiu2gc _bozgu2gc _y3gn1e5h _1s37ze3t _uupyze3t _11c8dcr7 _179r1on0 _mqm2glyw _t51zglyw _191wglyw _vchhusvi _kqswh2mm _syaz34id _k48pmoej _s7n4jp4b _1ygbvd8c _1bsb8a2a" style="--local-dynamic-table-text-color: var(--ds-text-subtlest, #5E6C84);">Actions</th></tr></thead></table>

## The table is empty and this is the empty view

```jsx
import React from 'react';



import { DynamicTableStateless } from '@atlaskit/dynamic-table';



import { head } from './content/sample-data';



const EmptyViewExample = () => (

	<DynamicTableStateless

		head={head}

		emptyView={<h2>The table is empty and this is the empty view</h2>}

	/>

);



export default EmptyViewExample;
```

## Pagination

You can enable or disable pagination with the rowsPerPage prop. If the rowsPerPage prop is set and the number of rows exceed one page, the pagination component will show below the table. 

```jsx
import React from 'react';



import DynamicTable from '@atlaskit/dynamic-table';



import { head, rows } from './content/sample-data';



export default () => {

	return (

		<DynamicTable

			caption="List of US Presidents"

			head={head}

			rows={rows}

			rowsPerPage={5}

			defaultPage={1}

			isFixedSize

			defaultSortKey="term"

			defaultSortOrder="ASC"

			onSort={() => console.log('onSort')}

			onSetPage={() => console.log('onSetPage')}

		/>

	);

};
```

| Name | Party | Term | Comment | Actions |
| --- | --- | --- | --- | --- |
| George WashingtonGeorge Washington | None, Federalist | 1789-1797 | 0 | More |
| John AdamsJohn Adams | Federalist | 1797-1801 | 1 | More |
| Thomas JeffersonThomas Jefferson | Democratic-Republican | 1801-1809 | 2 | More |
| James MadisonJames Madison | Democratic-Republican | 1809-1817 | 3 | More |
| James MonroeJames Monroe | Democratic-Republican | 1817-1825 | 4 | More |

## Drag and drop

Drag and drop functionality is built into the dynamic table. You can enable it using the isRankable prop. This lets people drag rows and rank them in different orders. 

```jsx
import React, { useCallback, useState } from 'react';



import DynamicTable from '@atlaskit/dynamic-table';

import Toggle from '@atlaskit/toggle';



import { createHead, rows } from './content/sample-data';



export default function DynamicTableRankableExample() {

	const [isFixedSize, setIsFixedSize] = useState(false);

	const [isLoading, setIsLoading] = useState(false);



	const onToggleFixedChange = useCallback(() => {

		setIsFixedSize((isFixedSize) => !isFixedSize);

	}, [setIsFixedSize]);



	const onLoadingChange = useCallback(() => {

		setIsLoading((isLoading) => !isLoading);

	}, [setIsLoading]);



	return (

		<div>

			<div>

				<Toggle label="Fixed size" onChange={onToggleFixedChange} isChecked={isFixedSize} />

				Fixed size

			</div>

			<div>

				<Toggle label="Loading" onChange={onLoadingChange} isChecked={isLoading} />

				Loading

			</div>

			<DynamicTable

				caption="List of US Presidents"

				head={createHead(isFixedSize)}

				rows={rows}

				rowsPerPage={5}

				defaultPage={1}

				isRankable

				isLoading={isLoading}

				onRankStart={(params) => console.log('onRankStart', params)}

				onRankEnd={(params) => console.log('onRankEnd', params)}

				onSort={() => console.log('onSort')}

				onSetPage={() => console.log('onSetPage')}

				testId="my-table"

			/>

		</div>

	);

}
```

| Name | Party | Term | Comment | Actions |
| --- | --- | --- | --- | --- |
| George WashingtonGeorge Washington | None, Federalist | 1789-1797 | 0 | More |
| John AdamsJohn Adams | Federalist | 1797-1801 | 1 | More |
| Thomas JeffersonThomas Jefferson | Democratic-Republican | 1801-1809 | 2 | More |
| James MadisonJames Madison | Democratic-Republican | 1809-1817 | 3 | More |
| James MonroeJames Monroe | Democratic-Republican | 1817-1825 | 4 | More |

## Overflow

Larger tables or tables that cannot be constrained easily can use horizontal scroll. This isn't supported directly by dynamic table, but the component can be easily extended to support this. Be mindful that horizontally scrolling tables can cause accessibility issues if there isn't enough visual affordance to indicate that the table has a scroll. For this reason, we recommend finding ways to simplify the table before opting for a horizontal scroll solution. 

```jsx
/**

 * @jsxRuntime classic

 * @jsx jsx

 */

import { css, jsx } from '@compiled/react';



import DynamicTable from '@atlaskit/dynamic-table';



import { head, rows } from './content/sample-data';



const wrapperStyles = css({

	overflowX: 'auto',

});



const overflowStyles = css({

	width: 1000,

});



const HeadlessExample = () => (

	<div css={wrapperStyles}>

		<div css={overflowStyles}>

			<DynamicTable head={head} rows={rows.slice(0, 10)} />

		</div>

	</div>

);



export default HeadlessExample;
```

| Name | Party | Term | Comment | Actions |
| --- | --- | --- | --- | --- |
| George WashingtonGeorge Washington | None, Federalist | 1789-1797 | 0 | More |
| John AdamsJohn Adams | Federalist | 1797-1801 | 1 | More |
| Thomas JeffersonThomas Jefferson | Democratic-Republican | 1801-1809 | 2 | More |
| James MadisonJames Madison | Democratic-Republican | 1809-1817 | 3 | More |
| James MonroeJames Monroe | Democratic-Republican | 1817-1825 | 4 | More |
| John Quincy AdamsJohn Quincy Adams | Democratic-Republican | 1825-1829 | 5 | More |
| Andrew JacksonAndrew Jackson | Democrat | 1829-1837 | 6 | More |
| Martin van BurenMartin van Buren | Democrat | 1837-1841 | 7 | More |
| William H. HarrisonWilliam H. Harrison | Whig | 1841 | 8 | More |
| John TylerJohn Tyler | Whig | 1841-1845 | 9 | More |

## Custom column span

Individual cells can use colSpan to make cells span across more than one column. 

```jsx
import React from 'react';



import DynamicTable from '@atlaskit/dynamic-table';



const days = ['Time', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday'];



const head = {

	cells: days.map((day) => ({

		key: day,

		content: day,

	})),

};



const rows = [

	{

		key: `morning-row`,

		cells: ['9:00', 'Math', 'History', 'Science', 'Computing', 'Math'].map((content, index) => ({

			key: index,

			content,

		})),

	},

	{

		key: 'midday-row',

		cells: [

			{

				key: 0,

				content: '12:00',

			},

			{

				key: 1,

				content: 'LUNCH',

				colSpan: 5,

			},

		],

	},

	{

		key: 'afternoon-row',

		cells: ['13:00', 'Science', 'History', 'Psychology', 'Computing', 'Business'].map(

			(content, index) => ({

				key: index,

				content,

			}),

		),

	},

];



const CustomColSpanExample = () => (

	<DynamicTable

		caption="Class timetable"

		head={head}

		rows={rows}

		loadingSpinnerSize="large"

		isLoading={false}

		isFixedSize

	/>

);



export default CustomColSpanExample;
```

<table class="_1bsb1osq _yq5hus1c _btyzidpf _ect41gqc _1kqm1n9t _179r1on0" style="--local-dynamic-table-hover-bg: var(--ds-background-neutral-subtle-hovered, #FAFBFC); --local-dynamic-table-highlighted-bg: var(--ds-background-selected, #DEEBFF); --local-dynamic-table-hover-highlighted-bg: var(--ds-background-selected-hovered, #B3D4FF); --local-dynamic-table-row-focus-outline: var(--ds-border-focused, #4C9AFF);"><caption class="_11c8lodh _6rthu2gc _1pfh1ejb _m6k41e03">Class timetable</caption><thead class="_179rglyw"><tr><th class="_izbqglyw _h7alglyw _85i51b66 _1q511b66 _y4tiu2gc _bozgu2gc _y3gn1e5h _1s37ze3t _uupyze3t _11c8dcr7 _179r1on0 _mqm2glyw _t51zglyw _191wglyw _vchhusvi _kqswh2mm _syaz34id _k48pmoej _s7n4jp4b _1ygbvd8c _1bsb8a2a" style="--local-dynamic-table-text-color: var(--ds-text-subtlest, #5E6C84);">Time</th><th class="_izbqglyw _h7alglyw _85i51b66 _1q511b66 _y4tiu2gc _bozgu2gc _y3gn1e5h _1s37ze3t _uupyze3t _11c8dcr7 _179r1on0 _mqm2glyw _t51zglyw _191wglyw _vchhusvi _kqswh2mm _syaz34id _k48pmoej _s7n4jp4b _1ygbvd8c _1bsb8a2a" style="--local-dynamic-table-text-color: var(--ds-text-subtlest, #5E6C84);">Monday</th><th class="_izbqglyw _h7alglyw _85i51b66 _1q511b66 _y4tiu2gc _bozgu2gc _y3gn1e5h _1s37ze3t _uupyze3t _11c8dcr7 _179r1on0 _mqm2glyw _t51zglyw _191wglyw _vchhusvi _kqswh2mm _syaz34id _k48pmoej _s7n4jp4b _1ygbvd8c _1bsb8a2a" style="--local-dynamic-table-text-color: var(--ds-text-subtlest, #5E6C84);">Tuesday</th><th class="_izbqglyw _h7alglyw _85i51b66 _1q511b66 _y4tiu2gc _bozgu2gc _y3gn1e5h _1s37ze3t _uupyze3t _11c8dcr7 _179r1on0 _mqm2glyw _t51zglyw _191wglyw _vchhusvi _kqswh2mm _syaz34id _k48pmoej _s7n4jp4b _1ygbvd8c _1bsb8a2a" style="--local-dynamic-table-text-color: var(--ds-text-subtlest, #5E6C84);">Wednesday</th><th class="_izbqglyw _h7alglyw _85i51b66 _1q511b66 _y4tiu2gc _bozgu2gc _y3gn1e5h _1s37ze3t _uupyze3t _11c8dcr7 _179r1on0 _mqm2glyw _t51zglyw _191wglyw _vchhusvi _kqswh2mm _syaz34id _k48pmoej _s7n4jp4b _1ygbvd8c _1bsb8a2a" style="--local-dynamic-table-text-color: var(--ds-text-subtlest, #5E6C84);">Thursday</th><th class="_izbqglyw _h7alglyw _85i51b66 _1q511b66 _y4tiu2gc _bozgu2gc _y3gn1e5h _1s37ze3t _uupyze3t _11c8dcr7 _179r1on0 _mqm2glyw _t51zglyw _191wglyw _vchhusvi _kqswh2mm _syaz34id _k48pmoej _s7n4jp4b _1ygbvd8c _1bsb8a2a" style="--local-dynamic-table-text-color: var(--ds-text-subtlest, #5E6C84);">Friday</th></tr></thead><tbody><tr class="_bfhkqtfy _1ygbi9un _1ah312gs _irr3s8ts"><td class="_1bsb8a2a _1reo15vq _18m915vq _19itglyw _85i51b66 _1q511b66 _y4tiu2gc _bozgu2gc _y3gn1e5h _1s37ze3t _uupyze3t">9:00</td><td class="_1bsb8a2a _1reo15vq _18m915vq _19itglyw _85i51b66 _1q511b66 _y4tiu2gc _bozgu2gc _y3gn1e5h _1s37ze3t _uupyze3t">Math</td><td class="_1bsb8a2a _1reo15vq _18m915vq _19itglyw _85i51b66 _1q511b66 _y4tiu2gc _bozgu2gc _y3gn1e5h _1s37ze3t _uupyze3t">History</td><td class="_1bsb8a2a _1reo15vq _18m915vq _19itglyw _85i51b66 _1q511b66 _y4tiu2gc _bozgu2gc _y3gn1e5h _1s37ze3t _uupyze3t">Science</td><td class="_1bsb8a2a _1reo15vq _18m915vq _19itglyw _85i51b66 _1q511b66 _y4tiu2gc _bozgu2gc _y3gn1e5h _1s37ze3t _uupyze3t">Computing</td><td class="_1bsb8a2a _1reo15vq _18m915vq _19itglyw _85i51b66 _1q511b66 _y4tiu2gc _bozgu2gc _y3gn1e5h _1s37ze3t _uupyze3t">Math</td></tr><tr class="_bfhkqtfy _1ygbi9un _1ah312gs _irr3s8ts"><td class="_1bsb8a2a _1reo15vq _18m915vq _19itglyw _85i51b66 _1q511b66 _y4tiu2gc _bozgu2gc _y3gn1e5h _1s37ze3t _uupyze3t">12:00</td><td class="_1bsb8a2a _1reo15vq _18m915vq _19itglyw _85i51b66 _1q511b66 _y4tiu2gc _bozgu2gc _y3gn1e5h _1s37ze3t _uupyze3t" colspan="5">LUNCH</td></tr><tr class="_bfhkqtfy _1ygbi9un _1ah312gs _irr3s8ts"><td class="_1bsb8a2a _1reo15vq _18m915vq _19itglyw _85i51b66 _1q511b66 _y4tiu2gc _bozgu2gc _y3gn1e5h _1s37ze3t _uupyze3t">13:00</td><td class="_1bsb8a2a _1reo15vq _18m915vq _19itglyw _85i51b66 _1q511b66 _y4tiu2gc _bozgu2gc _y3gn1e5h _1s37ze3t _uupyze3t">Science</td><td class="_1bsb8a2a _1reo15vq _18m915vq _19itglyw _85i51b66 _1q511b66 _y4tiu2gc _bozgu2gc _y3gn1e5h _1s37ze3t _uupyze3t">History</td><td class="_1bsb8a2a _1reo15vq _18m915vq _19itglyw _85i51b66 _1q511b66 _y4tiu2gc _bozgu2gc _y3gn1e5h _1s37ze3t _uupyze3t">Psychology</td><td class="_1bsb8a2a _1reo15vq _18m915vq _19itglyw _85i51b66 _1q511b66 _y4tiu2gc _bozgu2gc _y3gn1e5h _1s37ze3t _uupyze3t">Computing</td><td class="_1bsb8a2a _1reo15vq _18m915vq _19itglyw _85i51b66 _1q511b66 _y4tiu2gc _bozgu2gc _y3gn1e5h _1s37ze3t _uupyze3t">Business</td></tr></tbody></table>

## Highlighted row

You can highlight rows with highlightedRowIndex. Highlights provide additional visual prominence to a row. For example, you could use highlighted rows to show new rows that are added to a table. Keep in mind that people with visual disabilities may not notice when rows are highlighted, so don’t rely on highlights alone to convey information. Never use highlighted rows to indicate that a person has selected or focused on the row. 

```jsx
import React from 'react';



import DynamicTable from '@atlaskit/dynamic-table';



import { head, rows } from './content/sample-data';



const rowsWithHighlightedRow = [...rows];

rowsWithHighlightedRow[6].isHighlighted = true;



export default () => (

	<DynamicTable

		head={head}

		rows={rowsWithHighlightedRow}

		rowsPerPage={10}

		page={1}

		testId="the-table"

	/>

);
```

| Name | Party | Term | Comment | Actions |
| --- | --- | --- | --- | --- |
| George WashingtonGeorge Washington | None, Federalist | 1789-1797 | 0 | More |
| John AdamsJohn Adams | Federalist | 1797-1801 | 1 | More |
| Thomas JeffersonThomas Jefferson | Democratic-Republican | 1801-1809 | 2 | More |
| James MadisonJames Madison | Democratic-Republican | 1809-1817 | 3 | More |
| James MonroeJames Monroe | Democratic-Republican | 1817-1825 | 4 | More |
| John Quincy AdamsJohn Quincy Adams | Democratic-Republican | 1825-1829 | 5 | More |
| Andrew JacksonAndrew Jackson | Democrat | 1829-1837 | 6 | More |
| Martin van BurenMartin van Buren | Democrat | 1837-1841 | 7 | More |
| William H. HarrisonWilliam H. Harrison | Whig | 1841 | 8 | More |
| John TylerJohn Tyler | Whig | 1841-1845 | 9 | More |

## Interactive row

Rows can be interactive if you provide an onClick or onKeydown handler to the row. 

```jsx
import React from 'react';



import { DynamicTableStateless } from '@atlaskit/dynamic-table';

import type { RowType } from '@atlaskit/dynamic-table/types';



import { rows as allRows, head } from './content/sample-data';



const rows = allRows.slice(0, 10);



const extendRows = (

	rows: Array<RowType>,

	onClick: (e: React.MouseEvent, rowIndex: number) => void,

) => {

	return rows.map((row, index) => ({

		...row,

		onClick: (e: React.MouseEvent) => onClick(e, index),

	}));

};



interface StatelessState {

	highlightedRowIndex?: number[];

}



class RegularStatelessExample extends React.Component<{}, StatelessState> {

	state = {

		highlightedRowIndex: [],

	};



	onRowClick = (e: React.MouseEvent, rowIndex: number) => {

		this.setState(({ highlightedRowIndex }) => {

			const newHighlightedRowIndex = [...(highlightedRowIndex || [])];

			const existingIndex = newHighlightedRowIndex.indexOf(rowIndex);

			if (existingIndex > -1) {

				newHighlightedRowIndex.splice(existingIndex, 1);

			} else {

				newHighlightedRowIndex.push(rowIndex);

			}

			return { highlightedRowIndex: newHighlightedRowIndex };

		});

	};



	render() {

		return (

			<DynamicTableStateless

				head={head}

				highlightedRowIndex={this.state.highlightedRowIndex}

				rows={extendRows(rows, this.onRowClick)}

			/>

		);

	}

}



export default () => {

	return (

		<>

			<h4>Click in a row to highlight it</h4>

			<RegularStatelessExample />

		</>

	);

};
```

| Name | Party | Term | Comment | Actions |
| --- | --- | --- | --- | --- |
| George WashingtonGeorge Washington | None, Federalist | 1789-1797 | 0 | More |
| John AdamsJohn Adams | Federalist | 1797-1801 | 1 | More |
| Thomas JeffersonThomas Jefferson | Democratic-Republican | 1801-1809 | 2 | More |
| James MadisonJames Madison | Democratic-Republican | 1809-1817 | 3 | More |
| James MonroeJames Monroe | Democratic-Republican | 1817-1825 | 4 | More |
| John Quincy AdamsJohn Quincy Adams | Democratic-Republican | 1825-1829 | 5 | More |
| Andrew JacksonAndrew Jackson | Democrat | 1829-1837 | 6 | More |
| Martin van BurenMartin van Buren | Democrat | 1837-1841 | 7 | More |
| William H. HarrisonWilliam H. Harrison | Whig | 1841 | 8 | More |
| John TylerJohn Tyler | Whig | 1841-1845 | 9 | More |

---

[View Original Documentation](https://atlassian.design/components/dynamic-table/examples)
