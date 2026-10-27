# Markdown and HTML Syntax Manual

This reference covers standard Markdown and HTML documentation syntax, including headings, Markdown and HTML tables, code blocks, links, images, callout blocks, lists, and character escaping.

---

## 1. Heading Syntax

Define headings using `#`. The number of `#` characters indicates the heading level.
> **Important: Reserve H1 (`#`) for the top-level document title.** Start all main sections inside the document body with H2 (`##`).

| Heading Level | Markdown Syntax | HTML Output | Usage |
| :--- | :---: | :---: | :---: |
| Heading 2 (H2) | `## Section Title` | `<h2>` | Recommended for top-level body sections |
| Heading 3 (H3) | `### Subsection Title` | `<h3>` | Recommended for subsections |
| Heading 4 (H4) | `#### Sub-subsection Title` | `<h4>` | Use sparingly for deep hierarchy |

Example:
```markdown
## Second-Level Heading (generates <h2>)
Body paragraph content goes here.

### Third-Level Heading (generates <h3>)
Body paragraph content goes here.
```

---

## 2. Table Syntax

### 2.1 Standard Markdown Tables
Use `|` and `-` to define columns and rows:

```markdown
| Month | Revenue | Expense |
| ----- | ------- | ------- |
| 8     | 1000    | 500     |
| 9     | 1200    | 600     |
| 10    | 1400    | 650     |
```

### 2.2 HTML Tables (Custom Column Widths, Row Headers, Diagonal Headers)
Use HTML `<table>` tags when you need custom column widths (`width="20%"`), vertical row headers (`<th>`), multi-line cells (`<br>`), or diagonal split headers.

#### Row-Header & Custom-Width Table
```html
<table>
  <tr>
    <th width="20%">Requirement</th>
    <td width="80%">Description</td>
  </tr>
  <tr>
    <th>Applicable Scenario</th>
    <td>Applies to interactive live streaming and real-time media services.</td>
  </tr>
  <tr>
    <th>Prerequisites</th>
    <td>
      1. Completed account verification.<br>
      2. Obtained the required service license.<br>
      3. Configured network access permissions.
    </td>
  </tr>
</table>
```

#### Diagonal Split Header Table
```html
<table style="width:300px;">
  <tr>
    <th style="width:95px;height:45px;position:relative;font-weight:700;" valign="top">
      <div style="position:absolute;width:1px;height:115px;top:0;left:0;background-color:#d9d9d9;transform:rotate(-60deg);transform-origin:top;"></div>
      &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Header A<br>Header B
    </th>
    <th style="font-weight:700;">Field 1</th>
    <th style="font-weight:700;">Field 2</th>
  </tr>
  <tr>
    <th style="font-weight:700;">Row 1</th>
    <td>Value</td>
    <td>Value</td>
  </tr>
</table>
```

---

## 3. Code Syntax

- **Code blocks**: Wrap standalone code snippets in triple backticks (`` ``` ``) and specify a lowercase language identifier.
- **Inline code**: Wrap parameter names, expressions, file paths, and inline commands in single backticks (`` ` ``).

### 3.1 Syntax Highlighting Languages
Specify the language identifier in **all lowercase** immediately after the opening triple backticks:
- Supported common identifiers: `apache`, `bash`, `c`, `cpp`, `csharp`, `css`, `coffeescript`, `diff`, `go`, `html`, `http`, `ini`, `java`, `javascript`, `json`, `kotlin`, `less`, `lua`, `makefile`, `markdown`, `nginx`, `objectivec`, `perl`, `php`, `properties`, `python`, `ruby`, `rust`, `scss`, `shell`, `sql`, `swift`, `toml`, `typescript`, `xml`, `yaml`.

````markdown
```xml
<configuration>
  <property name="example" value="true" />
</configuration>
```
````

### 3.2 Plaintext Code Blocks (Disable Highlighting)
If a snippet is terminal output, directory trees, or causes rendering anomalies with syntax highlighting, set the language tag to `plaintext`:

````markdown
```plaintext
Plain text or command output without syntax highlighting
```
````

---

## 4. Hyperlink Syntax

Use `[Link Title](URL)` to create hyperlinks:

```markdown
See [Generating Signatures](https://example.com/docs/signature) for details.
```

---

## 5. Image Syntax

### 5.1 Standard Markdown Image
```markdown
![](https://example.com/images/architecture.png)
```

### 5.2 HTML Image (Custom Dimensions)
Markdown image syntax does not support explicit width or height attributes. Use the HTML `<img>` tag to set dimensions:

```html
<img src="https://example.com/images/diagram.png" width="650">
```

---

## 6. Callout Block Syntax

Use Markdown blockquotes (`>`) with bold severity labels (or GitHub-style alerts `> [!NOTE]`, `> [!IMPORTANT]`, `> [!WARNING]`, `> [!CAUTION]`) to distinguish four callout levels:

| Callout Type | Standard Blockquote Syntax | GitHub Alert Syntax | Severity / Purpose |
| - | - | - | - |
| **Note / Tip** | `> **Note:**` | `> [!NOTE]` | Supplementary tips, helpful shortcuts, or additional context |
| **Attention / Caution** | `> **Caution:**` | `> [!IMPORTANT]` | Low-level potential risk or mandatory prerequisite |
| **Warning** | `> **Warning:**` | `> [!WARNING]` | Medium-level risk or high-risk operation (potential data loss/downtime) |
| **Prohibition / Danger** | `> **Danger:**` | `> [!CAUTION]` | High-level critical danger or strictly forbidden operation |

### Examples
```markdown
> **Note:**
> This is a single-line note block.

> **Caution:**
> - First caution item ending with a period.
> - Second caution item ending with a period.
```

> **Formatting Constraints**:
> 1. Always leave a blank line after a callout block, and separate two adjacent callout blocks with body text or a blank line.
> 2. Never indent a callout block or image by 4 or more spaces on a non-code line; indenting by 4 or more spaces causes standard Markdown parsers to misinterpret the block as an indented `<pre><code>` block.

---

## 7. List Syntax

### 7.1 Ordered Lists
Start each line with an Arabic numeral followed by `.` and a space:
```markdown
1. Open the client configuration file.
2. Update the endpoint address.
3. Restart the service.
```

### 7.2 Unordered Lists
Start each line with `-` followed by a space:
```markdown
- First item
- Second item
- Third item
```

### 7.3 Nested Lists
Indent child list items by 2–3 spaces under the parent item (maximum 1 level of nesting):
```markdown
- Parent item
  - Child item 1
  - Child item 2
- Parent item
```

---

## 8. Character Escaping Syntax

Characters such as `>`, `<`, `<>`, and `✓` in `.md` source files outside of backticks may fail to render or be stripped as raw HTML tags. Use HTML entities when writing them in plain prose or tables:

| Character | HTML Entity | Example Source | Rendered Output |
| - | - | - | - |
| `>` | `&gt;` | `2 &gt; 1` | 2 > 1 |
| `<` | `&lt;` | `1 &lt; 2` | 1 < 2 |
| `<>` | `&lt;` `&gt;` | `Value of &lt;content&gt;` | Value of \<content\> |
| `✓` | `&#10003;` | `&#10003;` | ✓ |

> **Note**: When indicating "not supported" or a negative mark in a table cell, use a hyphen (`-`) rather than an `✗` symbol.
