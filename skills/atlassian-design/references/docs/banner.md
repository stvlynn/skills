# Banner

A banner displays a prominent message at the top of the screen.

---

## Appearance

### Warning

The default form of a banner. Use warning banners when you want the user to take a specific action or to warn them that something is about to go wrong. 

```jsx
import React from 'react';



import Banner from '@atlaskit/banner';

import WarningIcon from '@atlaskit/icon/glyph/warning';

import Link from '@atlaskit/link';



const BannerWarningExample = () => {

	return (

		<Banner

			appearance="warning"

			icon={<WarningIcon label="Warning" secondaryColor="inherit" />}

		>

			Payment details needed. To stay on your current plan, add payment details by June 30, 2020.{' '}

			<Link href="/components/banner/examples">Add payment details</Link>

		</Banner>

	);

};



export default BannerWarningExample;
```

### Error

Use error banners to inform users something critical has happened and requires immediate attention. 

```jsx
import React from 'react';



import Banner from '@atlaskit/banner';

import ErrorIcon from '@atlaskit/icon/glyph/error';

import Link from '@atlaskit/link';



const BannerErrorExample = () => {

	return (

		<Banner appearance="error" icon={<ErrorIcon label="Error" secondaryColor="inherit" />}>

			Bitbucket is experiencing an incident. Check our status page for more details.{' '}

			<Link href="http://www.bitbucket.com">Status page</Link>

		</Banner>

	);

};



export default BannerErrorExample;
```

### Announcement

Announcement banners are used by admins who want to make a general announcement about the product. These banners do not contain an icon. 

```jsx
import React from 'react';



import Banner from '@atlaskit/banner';

import Link from '@atlaskit/link';



const BannerAnnouncementExample = () => {

	return (

		<Banner appearance="announcement">

			We’re making changes to our server and Data Center products, including the end of sale for new

			server licenses on February 2, 2021 and the end of support for server on February 2, 2024.{' '}

			<Link href="/components/banner/examples">Upcoming product changes</Link>

		</Banner>

	);

};



export default BannerAnnouncementExample;
```

## Truncation

Banner width can change based on the size of the browser. Lengthy text will be truncated with an ellipses. For longer content that wraps, compose your banner with design token primitives instead. 

```jsx
import React from 'react';



import Banner from '@atlaskit/banner';

import WarningIcon from '@atlaskit/icon/glyph/warning';

import { Box, xcss } from '@atlaskit/primitives';



const containerStyles = xcss({

	maxWidth: '400px',

	margin: 'auto',

});



const message =

	'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vestibulum lobortis, odio egestas pulvinar sodales, neque justo tempor tellus, eget venenatis arcu ante non purus. Pellentesque tellus eros, rutrum vel enim non, tempor faucibus felis. Nullam pharetra erat sed magna porttitor, eget tincidunt odio finibus';



const BannerOverflowExample = () => {

	return (

		<Box xcss={containerStyles}>

			<Banner icon={<WarningIcon label="Warning" secondaryColor="inherit" />}>

				{message}

			</Banner>

		</Box>

	);

};



export default BannerOverflowExample;
```

---

[View Original Documentation](https://atlassian.design/components/banner/examples)
