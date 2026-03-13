# Logo

A logo is a visual representation of a brand or product. It can be a word or an image, or a combination of both.

---

## Types

### Icon

An icon is an image or symbol that represents a brand or product. It generally does not contain the name of the brand or product. 

```jsx
import React from 'react';



import { AtlassianIcon } from '@atlaskit/logo';



const Icon = () => {

	return <AtlassianIcon appearance="brand" />;

};



export default Icon;
```

### Lockup

A lockup is the combination of wordmark (the brand or product name) and its icon, generally referred altogether as a logo. 

```jsx
import React from 'react';



import { AtlassianLogo } from '@atlaskit/logo';



const LogoBlue = () => {

	return <AtlassianLogo appearance="brand" />;

};



export default LogoBlue;
```

## Appearance

By default, the lockup and icon inherit their colors from the parent element, however, this can lead to incorrect color combinations. Moving forward, all usages of @atlaskit/logo should use the appearance prop to choose between three brand-approved appearances: brand, neutral, and inverse. 

### Brand

Brand product logos are used in situations that demand a bold brand presence against a neutral background. 

```jsx
import React from 'react';



import { AtlassianLogo } from '@atlaskit/logo';



const LogoBlue = () => {

	return <AtlassianLogo appearance="brand" />;

};



export default LogoBlue;
```

### Neutral

Neutral product logos can be used when the hierarchy calls for the logo to recede, but should always be evaluated for adequate contrast. 

```jsx
import React from 'react';



import { AtlassianLogo } from '@atlaskit/logo';



const LogoNeutral = () => {

	return <AtlassianLogo appearance="neutral" />;

};



export default LogoNeutral;
```

### Inverse

Inverse product logos should be used to contrast against bold backgrounds. 

```jsx
import React from 'react';



import { AtlassianLogo } from '@atlaskit/logo';



const LogoInverse = () => {

	return <AtlassianLogo appearance="inverse" />;

};



export default LogoInverse;
```

## Size

### Small

Use the small logo in areas with minimal space or that contain many logos in close proximity. For example, the icon component, the marketing footer, or the emoji picker. 

```jsx
import React from 'react';



import { AtlassianIcon } from '@atlaskit/logo';



const LogoSmall = () => {

	return <AtlassianIcon size="small" appearance="brand" />;

};



export default LogoSmall;
```

### Medium

The medium size (32px) is the default size. 

```jsx
import React from 'react';



import { AtlassianLogo } from '@atlaskit/logo';



const LogoMedium = () => {

	return <AtlassianLogo size="medium" appearance="brand" />;

};



export default LogoMedium;
```

### Large

The large size (56px) is rarely used. It may be used for a hero piece. For example, Statuspage's login. 

```jsx
import React from 'react';



import { AtlassianLogo } from '@atlaskit/logo';



const LogoLarge = () => {

	return <AtlassianLogo size="large" appearance="brand" />;

};



export default LogoLarge;
```

## Product logos

### Atlassian

```jsx
/**

 * @jsxRuntime classic

 * @jsx jsx

 */



import { css, jsx } from '@compiled/react';



import { AtlassianIcon, AtlassianLogo } from '@atlaskit/logo';



const tableStyle = css({

	width: '415px',

});



const LogoAtlassian = () => {

	return (

		<div>

			<table>

				<thead>

					<tr>

						<th>Logo</th>

						<th>Icon</th>

					</tr>

				</thead>

				<tbody>

					<tr>

						<td css={tableStyle}>

							<AtlassianLogo appearance="brand" />

						</td>

						<td>

							<AtlassianIcon appearance="brand" />

						</td>

					</tr>

				</tbody>

			</table>

		</div>

	);

};



export default LogoAtlassian;
```

### Atlas

```jsx
/**

 * @jsxRuntime classic

 * @jsx jsx

 */



import { css, jsx } from '@compiled/react';



import { AtlasIcon, AtlasLogo } from '@atlaskit/logo';



const tableStyle = css({

	width: '415px',

});



const LogoAtlas = () => {

	return (

		<div>

			<table>

				<thead>

					<tr>

						<th>Logo</th>

						<th>Icon</th>

					</tr>

				</thead>

				<tbody>

					<tr>

						<td css={tableStyle}>

							<AtlasLogo appearance="brand" />

						</td>

						<td>

							<AtlasIcon appearance="brand" />

						</td>

					</tr>

				</tbody>

			</table>

		</div>

	);

};



export default LogoAtlas;
```

### Atlassian Access

```jsx
/**

 * @jsxRuntime classic

 * @jsx jsx

 */



import { css, jsx } from '@compiled/react';



import { AtlassianAccessIcon, AtlassianAccessLogo } from '@atlaskit/logo';



const tableStyle = css({

	width: '415px',

});



const LogoAtlassianAccess = () => {

	return (

		<div>

			<table>

				<thead>

					<tr>

						<th>Logo</th>

						<th>Icon</th>

					</tr>

				</thead>

				<tbody>

					<tr>

						<td css={tableStyle}>

							<AtlassianAccessLogo appearance="brand" />

						</td>

						<td>

							<AtlassianAccessIcon appearance="brand" />

						</td>

					</tr>

				</tbody>

			</table>

		</div>

	);

};



export default LogoAtlassianAccess;
```

### Atlassian Admin

```jsx
/**

 * @jsxRuntime classic

 * @jsx jsx

 */



import { css, jsx } from '@compiled/react';



import { AtlassianAdminIcon, AtlassianAdminLogo } from '@atlaskit/logo';



const tableStyle = css({

	width: '415px',

});



const LogoAtlassianAdmin = () => {

	return (

		<div>

			<table>

				<thead>

					<tr>

						<th>Logo</th>

						<th>Icon</th>

					</tr>

				</thead>

				<tbody>

					<tr>

						<td css={tableStyle}>

							<AtlassianAdminLogo appearance="brand" />

						</td>

						<td>

							<AtlassianAdminIcon appearance="brand" />

						</td>

					</tr>

				</tbody>

			</table>

		</div>

	);

};



export default LogoAtlassianAdmin;
```

### Atlassian Admininstration

```jsx
/**

 * @jsxRuntime classic

 * @jsx jsx

 */



import { css, jsx } from '@compiled/react';



import { AtlassianAdministrationIcon, AtlassianAdministrationLogo } from '@atlaskit/logo';



const tableStyle = css({

	width: '415px',

});



const LogoAtlassianAdministration = () => {

	return (

		<div>

			<table>

				<thead>

					<tr>

						<th>Logo</th>

						<th>Icon</th>

					</tr>

				</thead>

				<tbody>

					<tr>

						<td css={tableStyle}>

							<AtlassianAdministrationLogo appearance="brand" />

						</td>

						<td>

							<AtlassianAdministrationIcon appearance="brand" />

						</td>

					</tr>

				</tbody>

			</table>

		</div>

	);

};



export default LogoAtlassianAdministration;
```

### Atlassian Marketplace

```jsx
/**

 * @jsxRuntime classic

 * @jsx jsx

 */



import { css, jsx } from '@compiled/react';



import { AtlassianMarketplaceIcon, AtlassianMarketplaceLogo } from '@atlaskit/logo';



const tableStyle = css({

	width: '415px',

});



const LogoAtlassianMarketplace = () => {

	return (

		<div>

			<table>

				<thead>

					<tr>

						<th>Logo</th>

						<th>Icon</th>

					</tr>

				</thead>

				<tbody>

					<tr>

						<td css={tableStyle}>

							<AtlassianMarketplaceLogo appearance="brand" />

						</td>

						<td>

							<AtlassianMarketplaceIcon appearance="brand" />

						</td>

					</tr>

				</tbody>

			</table>

		</div>

	);

};



export default LogoAtlassianMarketplace;
```

### Bitbucket

```jsx
/**

 * @jsxRuntime classic

 * @jsx jsx

 */



import { css, jsx } from '@compiled/react';



import { BitbucketIcon, BitbucketLogo } from '@atlaskit/logo';



const tableStyle = css({

	width: '415px',

});



const LogoBitbucket = () => {

	return (

		<div>

			<table>

				<thead>

					<tr>

						<th>Logo</th>

						<th>Icon</th>

					</tr>

				</thead>

				<tbody>

					<tr>

						<td css={tableStyle}>

							<BitbucketLogo appearance="brand" />

						</td>

						<td>

							<BitbucketIcon appearance="brand" />

						</td>

					</tr>

				</tbody>

			</table>

		</div>

	);

};



export default LogoBitbucket;
```

### Compass

```jsx
/**

 * @jsxRuntime classic

 * @jsx jsx

 */



import { css, jsx } from '@compiled/react';



import { CompassIcon, CompassLogo } from '@atlaskit/logo';



const tableStyle = css({

	width: '415px',

});



const LogoCompass = () => {

	return (

		<div>

			<table>

				<thead>

					<tr>

						<th>Logo</th>

						<th>Icon</th>

					</tr>

				</thead>

				<tbody>

					<tr>

						<td css={tableStyle}>

							<CompassLogo appearance="brand" />

						</td>

						<td>

							<CompassIcon appearance="brand" />

						</td>

					</tr>

				</tbody>

			</table>

		</div>

	);

};



export default LogoCompass;
```

### Confluence

```jsx
/**

 * @jsxRuntime classic

 * @jsx jsx

 */



import { css, jsx } from '@compiled/react';



import { ConfluenceIcon, ConfluenceLogo } from '@atlaskit/logo';



const tableStyle = css({

	width: '415px',

});



const LogoConfluence = () => {

	return (

		<div>

			<table>

				<thead>

					<tr>

						<th>Logo</th>

						<th>Icon</th>

					</tr>

				</thead>

				<tbody>

					<tr>

						<td css={tableStyle}>

							<ConfluenceLogo appearance="brand" />

						</td>

						<td>

							<ConfluenceIcon appearance="brand" />

						</td>

					</tr>

				</tbody>

			</table>

		</div>

	);

};



export default LogoConfluence;
```

### Focus

```jsx
/**

 * @jsxRuntime classic

 * @jsx jsx

 */



import { css, jsx } from '@compiled/react';



import { FocusIcon, FocusLogo } from '@atlaskit/logo';



const tableStyle = css({

	width: '415px',

});



const LogoFocus = () => {

	return (

		<div>

			<table>

				<thead>

					<tr>

						<th>Logo</th>

						<th>Icon</th>

					</tr>

				</thead>

				<tbody>

					<tr>

						<td css={tableStyle}>

							<FocusLogo appearance="brand" />

						</td>

						<td>

							<FocusIcon appearance="brand" />

						</td>

					</tr>

				</tbody>

			</table>

		</div>

	);

};



export default LogoFocus;
```

### Guard

```jsx
/**

 * @jsxRuntime classic

 * @jsx jsx

 */



import { css, jsx } from '@compiled/react';



import { GuardIcon, GuardLogo } from '@atlaskit/logo';



const tableStyle = css({

	width: '415px',

});



const LogoGuard = () => {

	return (

		<div>

			<table>

				<thead>

					<tr>

						<th>Logo</th>

						<th>Icon</th>

					</tr>

				</thead>

				<tbody>

					<tr>

						<td css={tableStyle}>

							<GuardLogo appearance="brand" />

						</td>

						<td>

							<GuardIcon appearance="brand" />

						</td>

					</tr>

				</tbody>

			</table>

		</div>

	);

};



export default LogoGuard;
```

### Jira

```jsx
/**

 * @jsxRuntime classic

 * @jsx jsx

 */



import { css, jsx } from '@compiled/react';



import { JiraIcon, JiraLogo } from '@atlaskit/logo';



const tableStyle = css({

	width: '415px',

});



const LogoJira = () => {

	return (

		<div>

			<table>

				<thead>

					<tr>

						<th>Logo</th>

						<th>Icon</th>

					</tr>

				</thead>

				<tbody>

					<tr>

						<td css={tableStyle}>

							<JiraLogo appearance="brand" />

						</td>

						<td>

							<JiraIcon appearance="brand" />

						</td>

					</tr>

				</tbody>

			</table>

		</div>

	);

};



export default LogoJira;
```

### Jira Product Discovery

```jsx
/**

 * @jsxRuntime classic

 * @jsx jsx

 */



import { css, jsx } from '@compiled/react';



import { JiraProductDiscoveryIcon, JiraProductDiscoveryLogo } from '@atlaskit/logo';



const tableStyle = css({

	width: '415px',

});



const LogoJiraProductDiscovery = () => {

	return (

		<div>

			<table>

				<thead>

					<tr>

						<th>Logo</th>

						<th>Icon</th>

					</tr>

				</thead>

				<tbody>

					<tr>

						<td css={tableStyle}>

							<JiraProductDiscoveryLogo appearance="brand" />

						</td>

						<td>

							<JiraProductDiscoveryIcon appearance="brand" />

						</td>

					</tr>

				</tbody>

			</table>

		</div>

	);

};



export default LogoJiraProductDiscovery;
```

### Jira Service Management

```jsx
/**

 * @jsxRuntime classic

 * @jsx jsx

 */



import { css, jsx } from '@compiled/react';



import { JiraServiceManagementIcon, JiraServiceManagementLogo } from '@atlaskit/logo';



const tableStyle = css({

	width: '415px',

});



const LogoJiraServiceManagement = () => {

	return (

		<div>

			<table>

				<thead>

					<tr>

						<th>Logo</th>

						<th>Icon</th>

					</tr>

				</thead>

				<tbody>

					<tr>

						<td css={tableStyle}>

							<JiraServiceManagementLogo appearance="brand" />

						</td>

						<td>

							<JiraServiceManagementIcon appearance="brand" />

						</td>

					</tr>

				</tbody>

			</table>

		</div>

	);

};



export default LogoJiraServiceManagement;
```

### Jira Software

```jsx
/**

 * @jsxRuntime classic

 * @jsx jsx

 */



import { css, jsx } from '@compiled/react';



import { JiraSoftwareIcon, JiraSoftwareLogo } from '@atlaskit/logo';



const tableStyle = css({

	width: '415px',

});



const LogoJiraSoftware = () => {

	return (

		<div>

			<table>

				<thead>

					<tr>

						<th>Logo</th>

						<th>Icon</th>

					</tr>

				</thead>

				<tbody>

					<tr>

						<td css={tableStyle}>

							<JiraSoftwareLogo appearance="brand" />

						</td>

						<td>

							<JiraSoftwareIcon appearance="brand" />

						</td>

					</tr>

				</tbody>

			</table>

		</div>

	);

};



export default LogoJiraSoftware;
```

### Jira Work Management

```jsx
/**

 * @jsxRuntime classic

 * @jsx jsx

 */



import { css, jsx } from '@compiled/react';



import { JiraWorkManagementIcon, JiraWorkManagementLogo } from '@atlaskit/logo';



const tableStyle = css({

	width: '415px',

});



const LogoJiraWorkManagement = () => {

	return (

		<div>

			<table>

				<thead>

					<tr>

						<th>Logo</th>

						<th>Icon</th>

					</tr>

				</thead>

				<tbody>

					<tr>

						<td css={tableStyle}>

							<JiraWorkManagementLogo appearance="brand" />

						</td>

						<td>

							<JiraWorkManagementIcon appearance="brand" />

						</td>

					</tr>

				</tbody>

			</table>

		</div>

	);

};



export default LogoJiraWorkManagement;
```

### Loom

```jsx
/**

 * @jsxRuntime classic

 * @jsx jsx

 */



import { css, jsx } from '@compiled/react';



import { LoomIcon, LoomLogo } from '@atlaskit/logo';



const tableStyle = css({

	width: '415px',

});



const LogoLoom = () => {

	return (

		<div>

			<table>

				<thead>

					<tr>

						<th>Logo</th>

						<th>Icon</th>

					</tr>

				</thead>

				<tbody>

					<tr>

						<td css={tableStyle}>

							<LoomLogo appearance="brand" />

						</td>

						<td>

							<LoomIcon appearance="brand" />

						</td>

					</tr>

				</tbody>

			</table>

		</div>

	);

};



export default LogoLoom;
```

### Loom Attribution

```jsx
/**

 * @jsxRuntime classic

 * @jsx jsx

 */



import { css, jsx } from '@compiled/react';



import { LoomAttributionIcon, LoomAttributionLogo } from '@atlaskit/logo';



const tableStyle = css({

	width: '415px',

});



const LogoLoom = () => {

	return (

		<div>

			<table>

				<thead>

					<tr>

						<th>Logo</th>

						<th>Icon</th>

					</tr>

				</thead>

				<tbody>

					<tr>

						<td css={tableStyle}>

							<LoomAttributionLogo appearance="brand" />

						</td>

						<td>

							<LoomAttributionIcon appearance="brand" />

						</td>

					</tr>

				</tbody>

			</table>

		</div>

	);

};



export default LogoLoom;
```

### Opsgenie

```jsx
/**

 * @jsxRuntime classic

 * @jsx jsx

 */



import { css, jsx } from '@compiled/react';



import { OpsgenieIcon, OpsgenieLogo } from '@atlaskit/logo';



const tableStyle = css({

	width: '415px',

});



const LogoOpsgenie = () => {

	return (

		<div>

			<table>

				<thead>

					<tr>

						<th>Logo</th>

						<th>Icon</th>

					</tr>

				</thead>

				<tbody>

					<tr>

						<td css={tableStyle}>

							<OpsgenieLogo appearance="brand" />

						</td>

						<td>

							<OpsgenieIcon appearance="brand" />

						</td>

					</tr>

				</tbody>

			</table>

		</div>

	);

};



export default LogoOpsgenie;
```

### Rovo

```jsx
/**

 * @jsxRuntime classic

 * @jsx jsx

 */



import { css, jsx } from '@compiled/react';



import { RovoIcon, RovoLogo } from '@atlaskit/logo';



const tableStyle = css({

	width: '415px',

});



const LogoRovo = () => {

	return (

		<div>

			<table>

				<thead>

					<tr>

						<th>Logo</th>

						<th>Icon</th>

					</tr>

				</thead>

				<tbody>

					<tr>

						<td css={tableStyle}>

							<RovoLogo appearance="brand" />

						</td>

						<td>

							<RovoIcon appearance="brand" />

						</td>

					</tr>

				</tbody>

			</table>

		</div>

	);

};



export default LogoRovo;
```

### Statuspage

```jsx
/**

 * @jsxRuntime classic

 * @jsx jsx

 */



import { css, jsx } from '@compiled/react';



import { StatuspageIcon, StatuspageLogo } from '@atlaskit/logo';



const tableStyle = css({

	width: '415px',

});



const LogoStatusPage = () => {

	return (

		<div>

			<table>

				<thead>

					<tr>

						<th>Logo</th>

						<th>Icon</th>

					</tr>

				</thead>

				<tbody>

					<tr>

						<td css={tableStyle}>

							<StatuspageLogo appearance="brand" />

						</td>

						<td>

							<StatuspageIcon appearance="brand" />

						</td>

					</tr>

				</tbody>

			</table>

		</div>

	);

};



export default LogoStatusPage;
```

### Trello

```jsx
/**

 * @jsxRuntime classic

 * @jsx jsx

 */



import { css, jsx } from '@compiled/react';



import { TrelloIcon, TrelloLogo } from '@atlaskit/logo';



const tableStyle = css({

	width: '415px',

});



const LogoTrello = () => {

	return (

		<div>

			<table>

				<thead>

					<tr>

						<th>Logo</th>

						<th>Icon</th>

					</tr>

				</thead>

				<tbody>

					<tr>

						<td css={tableStyle}>

							<TrelloLogo appearance="brand" />

						</td>

						<td>

							<TrelloIcon appearance="brand" />

						</td>

					</tr>

				</tbody>

			</table>

		</div>

	);

};



export default LogoTrello;
```

---

[View Original Documentation](https://atlassian.design/components/logo/examples)
