# CSS

Style components backed by Atlassian Design System design tokens powered by Compiled CSS-in-JS.

---

## Migration from Emotion to Compiled

The Atlassian Design System is migrating from Emotion to Compiled CSS-in-JS. This transition aims to improve performance and align with modern React features. Read our RFC to learn more. @atlaskit/css is the replacement for @atlaskit/primitives.xcss. It serves as a bounded styling library for use with native HTML elements and the Atlassian Design System, including primitive components. Built on Compiled CSS-in-JS, it provides a performant, static styling solution with some syntax changes. Notably, dynamic styles and certain imports/exports may not work as before. For configuration details, see our Get Started guide. 

## Usage

@atlaskit/css closely resembles the behavior of @compiled/react and other CSS-in-JS libraries' css() functions. However, we encourage using cssMap to create style maps, as the common practice at Atlassian. This is a strictly bounded variant designed to align the use of Design System tokens and properties. You cannot use arbitrary values, such as color: 'rgba(123, 45, 67)' nor padding: 8. Typically, only tokenized values are allowed. Additionally, there are some restrictions, such as zIndex, which only supports a limited set of numeric values. 

### cssMap()

We recommend using cssMap to create style maps. These maps can be applied and reused on both native elements and React components using props.css and props.xcss respectively. Make sure to define the styles before using them in your components, i.e. at the top of the file. 

```jsx
/**

 * @jsxRuntime classic

 * @jsx jsx

 */

import { useState } from 'react';



import Button from '@atlaskit/button/new';

import { cssMap, jsx } from '@atlaskit/css';

import { Stack } from '@atlaskit/primitives/compiled';

import { token } from '@atlaskit/tokens';



const styles = cssMap({

	root: {

		paddingTop: token('space.200'),

		paddingRight: token('space.200'),

		paddingBottom: token('space.200'),

		paddingLeft: token('space.200'),

	},

	primary: {

		backgroundColor: token('color.background.brand.bold'),

		color: token('color.text.inverse'),

	},

	discovery: {

		backgroundColor: token('color.background.discovery.bold'),

		color: token('color.text.inverse'),

	},

	success: {

		backgroundColor: token('color.background.success.bold'),

		color: token('color.text.inverse'),

	},

	disabled: { opacity: 0, cursor: 'not-allowed' },

	button: { marginTop: token('space.200') },

});



const appearances = ['primary', 'discovery', 'success'] as const;



export default ({

	appearance,

	isDisabled,

}: {

	appearance: 'primary' | 'discovery' | 'success';

	isDisabled?: boolean;

}) => {

	const [appearanceIndex, setAppearanceIndex] = useState(0);



	const cycleAppearance = () => {

		setAppearanceIndex((prev) => (prev + 1) % appearances.length);

	};



	return (

		<Stack space="space.200" alignInline="start">

			<Button onClick={cycleAppearance}>Change appearance</Button>

			<div css={[styles.root, styles[appearances[appearanceIndex]], isDisabled && styles.disabled]}>

				{appearances[appearanceIndex]}

			</div>

		</Stack>

	);

};
```

### css()

The css() function is a lower-level API that creates a single style object. Unlike cssMap(), it's best suited for one-off styles. Use it with elements that accept a css prop. While css() is simpler to use, we recommend cssMap() for most cases because it provides better reusability and type safety. When using @atlaskit/css, it's important to note that it's not compatible with the Emotion variant of Primitives. Instead, use the Compiled variant of Primitives, available at @atlaskit/primitives/compiled. The Compiled variant is a drop-in replacement that provides the same components and APIs you're familiar with. 

```jsx
const styles = css({
    padding: token('space.100'),
    color: token('color.text'),
});

<div css={styles}>Hello world!</div>;
```

```jsx
const styles = css({
    padding: token('space.100'),
    color: token('color.text'),
});

<div css={styles}>Hello world!</div>;
```

### cx

Use the cx function when combining styles in an xcss prop to maintain correct typing. This is not required for native elements, but still works with or without. 

### JSX pragma

You must have a JSX pragma in scope in order to use this, depending on your setup this may be automatic, require React imported, or require jsx imported. 

```jsx
/**

 * @jsxRuntime classic

 * @jsx jsx

 */
import { cssMap, cx, jsx } from '@atlaskit/css';
import { Box } from '@atlaskit/primitives/compiled';
import { token } from '@atlaskit/tokens';

const styles = cssMap({
    root: {
        padding: token('space.100'),
        color: token('color.text'),
    },
    compact: { padding: token('space.050') },
});

export default ({ spacing = 'default' }: { spacing: 'compact' | 'default' }) => {
    return (
        <Box xcss={cx(styles.root, spacing === 'compact' && styles.compact)}>
            <p css={[styles.compact]}>Hello world!</p>
        </Box>
    );
};
```

```jsx
/**

 * @jsxRuntime classic

 * @jsx jsx

 */
import { cssMap, cx, jsx } from '@atlaskit/css';
import { Box } from '@atlaskit/primitives/compiled';
import { token } from '@atlaskit/tokens';

const styles = cssMap({
    root: {
        padding: token('space.100'),
        color: token('color.text'),
    },
    compact: { padding: token('space.050') },
});

export default ({ spacing = 'default' }: { spacing: 'compact' | 'default' }) => {
    return (
        <Box xcss={cx(styles.root, spacing === 'compact' && styles.compact)}>
            <p css={[styles.compact]}>Hello world!</p>
        </Box>
    );
};
```

## Building reusable components

With the introduction of @atlaskit/css, and leveraging the underlying createStrictAPI from Compiled, we've established a strictly bounded API for our components. This approach ensures consistency and alignment with our Design System, and it might be an API pattern you find beneficial to adopt in your own projects. For instance, if you want to create a component that allows you to extend and pass-through styles, you can do so: You can then build a component using this Card component and override its properties as needed: However, if you're extending a component that uses props.xcss under the hood, for example a Primitive, the first Card component would look a bit different, brief example: 

```jsx
/**

 * @jsxRuntime classic

 * @jsx jsx

 */
import { cssMap, jsx, type StrictXCSSProp } from '@atlaskit/css';
import { token } from '@atlaskit/tokens';

const styles = cssMap({
    button: { padding: token('space.100'), borderRadius: token('border.radius.100') },
    dense: { padding: token('space.050'), borderRadius: token('border.radius.050') },
});

export function Card({
    children,
    xcss,
    isDense,
}: {
    children: React.ReactNode;
    isDense?: boolean;
    xcss?: StrictXCSSProp<
        'padding' | 'borderRadius' | 'backgroundColor' | 'color',
        '&:hover' | '&:focus'
    >;
}) {
    return (
        <div css={[styles.button, isDense && styles.dense]} className={xcss}>
            {children}
        </div>
    );
}
```

```jsx
/**

 * @jsxRuntime classic

 * @jsx jsx

 */
import { cssMap, jsx, type StrictXCSSProp } from '@atlaskit/css';
import { token } from '@atlaskit/tokens';

const styles = cssMap({
    button: { padding: token('space.100'), borderRadius: token('border.radius.100') },
    dense: { padding: token('space.050'), borderRadius: token('border.radius.050') },
});

export function Card({
    children,
    xcss,
    isDense,
}: {
    children: React.ReactNode;
    isDense?: boolean;
    xcss?: StrictXCSSProp<
        'padding' | 'borderRadius' | 'backgroundColor' | 'color',
        '&:hover' | '&:focus'
    >;
}) {
    return (
        <div css={[styles.button, isDense && styles.dense]} className={xcss}>
            {children}
        </div>
    );
}
```

```jsx
/**

 * @jsxRuntime classic

 * @jsx jsx

 */
import { cssMap, cx, jsx, type StrictXCSSProp } from '@atlaskit/css';
import { token } from '@atlaskit/tokens';
import { Card } from './Card';

const styles = cssMap({
    root: { padding: token('space.200'), borderRadius: token('border.radius.200') },
    inverse: {
        backgroundColor: token('color.background.discovery'),
        color: token('color.text.inverse'),
    },
});

export const LargeCard = ({
    children,
    isInverse,
}: {
    children: React.ReactNode;
    isInverse?: boolean;
}) => {
    return <Card xcss={cx(styles.root, isInverse && styles.inverse)}>{children}</Card>;
};
```

```jsx
/**

 * @jsxRuntime classic

 * @jsx jsx

 */
import { cssMap, cx, jsx, type StrictXCSSProp } from '@atlaskit/css';
import { token } from '@atlaskit/tokens';
import { Card } from './Card';

const styles = cssMap({
    root: { padding: token('space.200'), borderRadius: token('border.radius.200') },
    inverse: {
        backgroundColor: token('color.background.discovery'),
        color: token('color.text.inverse'),
    },
});

export const LargeCard = ({
    children,
    isInverse,
}: {
    children: React.ReactNode;
    isInverse?: boolean;
}) => {
    return <Card xcss={cx(styles.root, isInverse && styles.inverse)}>{children}</Card>;
};
```

```jsx
/**

 * @jsxRuntime classic

 * @jsx jsx

 */
import { cssMap, jsx, type StrictXCSSProp } from '@atlaskit/css';
import { token } from '@atlaskit/tokens';

const styles = cssMap({
    button: { padding: token('space.100'), borderRadius: token('border.radius.100') },
    dense: { padding: token('space.050'), borderRadius: token('border.radius.050') },
});

export function Card({
    children,
    xcss,
    isDense,
}: {
    children: React.ReactNode;
    isDense?: boolean;
    xcss?: StrictXCSSProp<'padding' | 'borderRadius', never>;
}) {
    return (
        // eslint-disable-next-line @atlaskit/ui-styling-standard/no-classname-prop -- required with `xcss`
        <div css={[styles.button, isDense && styles.dense]} className={xcss}>
            {children}
        </div>
    );
}
```

```jsx
/**

 * @jsxRuntime classic

 * @jsx jsx

 */
import { cssMap, jsx, type StrictXCSSProp } from '@atlaskit/css';
import { token } from '@atlaskit/tokens';

const styles = cssMap({
    button: { padding: token('space.100'), borderRadius: token('border.radius.100') },
    dense: { padding: token('space.050'), borderRadius: token('border.radius.050') },
});

export function Card({
    children,
    xcss,
    isDense,
}: {
    children: React.ReactNode;
    isDense?: boolean;
    xcss?: StrictXCSSProp<'padding' | 'borderRadius', never>;
}) {
    return (
        // eslint-disable-next-line @atlaskit/ui-styling-standard/no-classname-prop -- required with `xcss`
        <div css={[styles.button, isDense && styles.dense]} className={xcss}>
            {children}
        </div>
    );
}
```

### Unbounded styles

If you need to apply styles that aren't tokenized, or styles that aren't within the @atlaskit/css API, you can use the cssMap() function from @compiled/react directly on native HTML elements. Note that this won't work on primitive components. While it's best to stick to the Design System guidelines, this option can be useful for handling specific edge cases. Please note this isn't recommended for general use. 

```jsx
/**

 * @jsxRuntime classic

 * @jsx jsx

 */

import { cssMap } from '@compiled/react';



import { jsx } from '@atlaskit/css';

import { token } from '@atlaskit/tokens';



type ContainerProps = {

	children: React.ReactNode;

	testId?: string;

};



const unboundedStyles = cssMap({

	container: {

		padding: '21px',

		// eslint-disable-next-line @atlaskit/ui-styling-standard/no-unsafe-selectors

		'&:first-child': {

			paddingBlockEnd: token('space.150'),

			backgroundColor: 'powderblue',

		},

		'@media (min-width: 48rem)': {

			// eslint-disable-next-line @atlaskit/ui-styling-standard/no-unsafe-selectors

			'&:first-child': {

				paddingBlockStart: token('space.400'),

			},

		},

		'&:hover': {

			backgroundColor: 'royalblue',

			color: 'white',

		},

	},

});



export default ({ children, testId }: ContainerProps) => (

	<div css={unboundedStyles.container} data-testid={testId}>

		Hover over me

		{children}

	</div>

);
```

## Configuration required

In order to use any Atlassian Design System packages that distribute Compiled CSS-in-JS, you must configure your project, please refer to our Get started guide. 

---

[View Original Documentation](https://atlassian.design/components/css/examples)
