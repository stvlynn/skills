# Code block

A code block highlights an entire block of code and keeps the formatting.

---

## Default

A code block highlights an entire block of code and keeps the formatting. 

```jsx
import { Box } from '@atlaskit/primitives/compiled'

class HelloMessage extends React.Component {
  render() {
    return (
      <Box>
        Hello {this.props.name}
      </Box>
    );
  }
}

ReactDOM.render(
  <HelloMessage name="Taylor" />,
  mountNode
);
```

```jsx
import React from 'react';



import { CodeBlock } from '@atlaskit/code';



const exampleCodeBlock = `import { Box } from '@atlaskit/primitives/compiled'



class HelloMessage extends React.Component {

  render() {

    return (

      <Box>

        Hello {this.props.name}

      </Box>

    );

  }

}



ReactDOM.render(

  <HelloMessage name="Taylor" />,

  mountNode

);`;



const CodeBlockDefaultExample = () => {

	return <CodeBlock language="jsx" showLineNumbers={false} text={exampleCodeBlock} />;

};



export default CodeBlockDefaultExample;
```

## Line numbers

You can display a code block with or without line numbers. Line numbers are included by default. You can also adjust the starting line of a code block. This can be useful when referencing specific lines from an existing codebase. 

```jsx
import { Box } from '@atlaskit/primitives/compiled'



class HelloMessage extends React.Component {

  render() {

    return (

      <Box>

        Hello {this.props.name}

      </Box>

    );

  }

}



ReactDOM.render(

  <HelloMessage name="Taylor" />,

  mountNode

);
```

```jsx
import React from 'react';



import { CodeBlock } from '@atlaskit/code';



const exampleCodeBlock = `import { Box } from '@atlaskit/primitives/compiled'



class HelloMessage extends React.Component {

  render() {

    return (

      <Box>

        Hello {this.props.name}

      </Box>

    );

  }

}



ReactDOM.render(

  <HelloMessage name="Taylor" />,

  mountNode

);`;



const CodeBlockLineNumbersExample = () => {

	return <CodeBlock language="jsx" text={exampleCodeBlock} />;

};



export default CodeBlockLineNumbersExample;
```

```jsx
import React from 'react';



import { CodeBlock } from '@atlaskit/code';



const exampleCodeBlock = `	<Box>

		Hello {this.props.name} // <- Bug on this line

	</Box>`;



const CodeBlockLineNumbersExample = () => {

	return <CodeBlock language="jsx" firstLineNumber={139} text={exampleCodeBlock} />;

};



export default CodeBlockLineNumbersExample;
```

## Line highlighting

You can highlight lines in a code block. 

```jsx
class HelloMessage extends React.Component {

  import { Box } from '@atlaskit/primitives/compiled'

  render() {

    return (

      <Box>

        Hello {this.props.name}

      </Box>

    );

  }

}

ReactDOM.render(

  <HelloMessage name="Taylor" />,

  mountNode

);
```

```jsx
import React from 'react';



import { CodeBlock } from '@atlaskit/code';



const exampleCodeBlock = `class HelloMessage extends React.Component {

  import { Box } from '@atlaskit/primitives/compiled'



  render() {

    return (

      <Box>

        Hello {this.props.name}

      </Box>

    );

  }

}



ReactDOM.render(

  <HelloMessage name="Taylor" />,

  mountNode

);`;



const CodeBlockLineHighlightExample = () => {

	return <CodeBlock language="jsx" text={exampleCodeBlock} highlight="2,5-7" />;

};



export default CodeBlockLineHighlightExample;
```

## Wrapping long lines

By default, long lines will result in a horizontal-scrolling code block. You can use the shouldWrapLongLines prop to make the long lines wrap instead. 

```jsx
import Message from '../../../src/packages/components/example-of-a-really-long-import-path/message'

// This is an example of a comment that is going to create a long line of code, where you may want to use the `shouldWrapLongLines` prop. When this prop is set to false, the CodeBlock container will scroll horizontally. When it is set to true, the CodeBlock content will wrap to the next line. As you can see from this line, the 'highlight' and 'shouldWrapLongLines' props work well in tandem.

class ExtremelyLongComponentNameThatMightNormallyForceCodeBlockToScrollHorizontally extends React.Component {

  render() {

    return (

      <Message>

        Hello world

      </Message>

    );

  }

}

ReactDOM.render(

  <ExtremelyLongComponentNameThatMightNormallyForceCodeBlockToScrollHorizontally />,

  mountNode

);
```

```jsx
import React, { useState } from 'react';



import { CodeBlock } from '@atlaskit/code';

import { Label } from '@atlaskit/form';

import Toggle from '@atlaskit/toggle';

import { token } from '@atlaskit/tokens';



const exampleCodeBlock = `import Message from '../../../src/packages/components/example-of-a-really-long-import-path/message'



// This is an example of a comment that is going to create a long line of code, where you may want to use the \`shouldWrapLongLines\` prop. When this prop is set to false, the CodeBlock container will scroll horizontally. When it is set to true, the CodeBlock content will wrap to the next line. As you can see from this line, the 'highlight' and 'shouldWrapLongLines' props work well in tandem.



class ExtremelyLongComponentNameThatMightNormallyForceCodeBlockToScrollHorizontally extends React.Component {

  render() {

    return (

      <Message>

        Hello world

      </Message>

    );

  }

}



ReactDOM.render(

  <ExtremelyLongComponentNameThatMightNormallyForceCodeBlockToScrollHorizontally />,

  mountNode

);`;



const CodeBlockShouldWrapLongLinesExample = () => {

	const [lineWrapState, setLineWrapState] = useState(true);

	return (

		<>

			<div

				style={{

					// eslint-disable-next-line @atlaskit/ui-styling-standard/enforce-style-prop -- Ignored via go/DSP-18766

					paddingBottom: token('space.300'),

					// eslint-disable-next-line @atlaskit/ui-styling-standard/enforce-style-prop -- Ignored via go/DSP-18766

					display: 'flex',

					// eslint-disable-next-line @atlaskit/ui-styling-standard/enforce-style-prop -- Ignored via go/DSP-18766

					flexDirection: 'column',

				}}

			>

				<Label htmlFor="toggle">Wrap long lines</Label>

				<Toggle

					isChecked={lineWrapState}

					onChange={() => setLineWrapState(!lineWrapState)}

					size="large"

					id="toggle"

				/>

			</div>

			<CodeBlock

				language="jsx"

				text={exampleCodeBlock}

				shouldWrapLongLines={lineWrapState}

				highlight="3"

			/>

		</>

	);

};



export default CodeBlockShouldWrapLongLinesExample;
```

---

[View Original Documentation](https://atlassian.design/components/code/code-block/examples)
