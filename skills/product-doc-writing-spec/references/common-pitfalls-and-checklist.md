# Common Pitfalls and Quality Checklist

This reference provides high-frequency writing and formatting rules and a 30-category documentation quality inspection checklist.

---

## 1. High-Frequency Formatting Pitfalls

1. **Use H2 Instead of H1 in the Document Body**
   - Reserve H1 (`#`) for the document or page title.
   - Start all top-level sections inside the document body at **H2 (`##`)**.

2. **Indent Screenshots Under Steps and Lists**
   - Screenshots accompanying a numbered step or bulleted list item must be indented so their left edge aligns with the text of the parent step or list item.

3. **Remove Extra Blank Spaces and Lines Between Paragraphs**
   - Delete redundant blank lines or leading/trailing spaces between paragraphs to maintain standard paragraph spacing.

4. **Add Spaces Around Hyperlinks in Mixed CJK/Latin Text (Except Before Punctuation)**
   - In mixed CJK/Latin text, add a space before and after a hyperlink.
   - If the hyperlink is immediately followed by a period or other punctuation mark, do **not** add a space after the link.
   - **Correct**: `For installation and usage details, see [CLI Tool](https://example.com).`

5. **Add Spaces Around Latin Words in CJK Text**
   - Insert a space between CJK characters and Latin words (omit the trailing space when immediately followed by punctuation).

6. **Standardize Cross-Reference Phrasing**
   - Always use a single standardized cross-reference phrase across the documentation set, such as **"see [Title](url)"** or **"refer to [Title](url)"**, rather than mixing multiple inconsistent introductory phrases.

7. **Maintain Consistent Terminal Punctuation (Especially in Lists and Tables)**
   - Every sentence in a callout box (`Note` / `Warning`) or list must end with a period.
   - Within any table column, keep terminal punctuation consistent: if entries are full sentences (or a mix of sentences and phrases), end every entry with a period; if all entries are short phrases or single words, omit periods throughout the column.

8. **Embed Links in Anchor Text**
   - Never paste raw URLs directly in the body text or leave URLs outside the sentence. Embed hyperlinks directly into descriptive noun phrases (e.g., `For details on key-value storage, see [KV Storage](https://example.com).`).

9. **Format UI Controls in Bold Without Quotes or the Word "Button"**
   - Format UI control names in **bold**. Never wrap UI labels in quotation marks.
   - When instructing users to click a button, bold the button label and **do not append the word "button"**.
     - **Correct**: Click **Create**.
     - **Incorrect**: Click the **Create** button.
   - **Example**: In the **Virtual Server** tab, click **Create**.

10. **Attach Links to Console References**
    - When an operating step instructs the user to log in to or open the management console, attach a direct hyperlink to the console text.

11. **Format Unordered and Ordered Lists Properly**
    - Use solid round bullets (`-` / `•`) for unordered lists and `1.` for ordered lists.
    - Ensure nested elements under ordered list items (such as code blocks, tabs, or sub-headings) are vertically aligned with the step text rather than flush with the left margin.

12. **Distinguish Punctuation by Document Language**
    - Never mix full-width (CJK) and half-width (Latin) punctuation within the same language version.
    - Pay special attention to paired symbols (colons, quotation marks, parentheses) to ensure opening and closing marks belong to the same character set.

13. **Include Table Headers**
    - Every table must have a header row (except standalone 2-column glossary layouts where specified).

14. **Match Console Screenshots to the Document Language**
    - Ensure the UI language in screenshots matches the language of the document.

15. **Inspect Content Pasted from Markdown Editors**
    - Carefully check pasted Markdown content to ensure no unrendered Markdown syntax (such as raw `- **key**:`) or unintended code blocks caused by excessive indentation remain.

16. **Never Link to Empty Directory/Category Pages**
    - Hyperlinks must point to concrete content pages, never to directory index pages that only list child links.

---

## 2. Documentation Quality Inspection Checklist (30 Categories)

| Dimension | Category | Subcategory | Description | Example |
| - | - | - | - | - |
| **Completeness** | Completeness Issues | Missing Document | Mandatory documents are missing from the documentation set, leaving key user scenarios uncovered. | A software documentation package lacks acceptance test cases, preventing users from verifying basic functionality after deployment. |
| **Completeness** | Completeness Issues | Missing Module | Required sections are absent from a document's structure (e.g., missing troubleshooting or feature overview sections). | A device user manual lacks an FAQ or troubleshooting section, leaving users unable to resolve common issues. |
| **Completeness** | Completeness Issues | Missing Step | Operating procedures omit a critical step (e.g., missing a key configuration step during installation or a check step during maintenance). | A driver installation guide omits the required system reboot step after installation, causing the device to fail to work. |
| **Completeness** | Completeness Issues | Missing Information | Essential context is missing, such as prerequisites (required OS configuration), risk warnings (consequences of deleting data), verification methods (how to confirm an operation succeeded), or rollback instructions (how to restore state after an upgrade). | A database upgrade manual fails to mention the risk of data loss during upgrade and omits instructions on verifying the database version afterward. |
| **Completeness** | Completeness Issues | Missing Example | Complex operations lack concrete input/output examples. | A data analytics guide explains data cleansing without providing sample input data and before/after output comparisons. |
| **Accuracy** | Accuracy Issues | Incorrect Step | Documented steps do not match the actual product behavior (wrong sequence or wrong action label, such as writing "Save" when the UI button is "Save As"). | A drawing software tutorial instructs users to "click the Circle tool and adjust parameters to draw a square" instead of "click the Rectangle tool and set equal side lengths." |
| **Accuracy** | Accuracy Issues | Incorrect Terminology | Technical terms or concepts are explained or used inaccurately (e.g., confusing network "bandwidth" with actual "transfer speed"). | A networking manual defines "bandwidth" as the actual speed of data transfer rather than the maximum transmission capacity of the link. |
| **Accuracy** | Accuracy Issues | Incorrect Data | Data, parameters, or configuration values are wrong (e.g., wrong default port number or hardware power rating). | A server installation guide lists the default port as `8081` instead of `8080`, preventing users from accessing the application. |
| **Accuracy** | Accuracy Issues | Incorrect Screenshot | UI screenshots do not match the actual software interface (different element positions, changed icons, mismatched versions, or callout boxes pointing to the wrong control). | An office software guide shows a legacy UI screenshot where button icons and positions differ from the current release, and the red box highlights "Print" instead of "Save." |
| **Accuracy** | Accuracy Issues | Broken Link | External hyperlinks return 404 or are inaccessible due to permissions, or internal anchor links fail to jump to the target section. | A hyperlink in an operation guide points to an external URL that returns "Page Not Found." |
| **Accuracy** | Accuracy Issues | Punctuation Error | Punctuation marks are misused, missing, or redundant. | A feature list uses bullet points where most items end with a period, but several items have no terminal punctuation. |
| **Accuracy** | Timeliness Issues | Outdated Content | Documentation fails to keep pace with product version updates and workflow changes. | A video editing application has added new features across multiple releases, but the manual still reflects an older version. |
| **Accuracy** | Timeliness Issues | Missing Update Guidance | When documentation is updated, there is no changelog or migration guidance to help users transition from the old workflow to the new one. | After a major client update, the manual provides no release notes or transition guide for the redesigned workflow. |
| **Accuracy** | Timeliness Issues | Outdated Screenshot | Screenshots show an older UI version after the layout has significantly changed. | A manual displays legacy screenshots after a major UI redesign, making it impossible for users to locate buttons. |
| **Accuracy** | Timeliness Issues | Text-Image Mismatch | The text description contradicts the accompanying image (e.g., text says "click the bottom-right button" while the arrow in the image points to the bottom-left). | A navigation application guide instructs users to click "Route Plan" in the bottom-right corner, but the arrow points to "Search" in the bottom-left. |
| **Business Risk** | Access Permission Issues | Improper Access Scope | Document visibility does not follow the principle of least privilege (e.g., internal architecture diagrams exposed to public/guest users). | An internal architecture design document containing proprietary diagrams is configured as publicly visible to anonymous visitors. |
| **Business Risk** | Security Issues | Insufficient Risk Assessment | Operations with security implications lack risk warnings (e.g., network exposure without data leak warnings, or credential input without security reminders). | A remote-work application guide fails to warn users about credential theft risks when logging in over public Wi-Fi. |
| **Business Risk** | Security Issues | Missing Permission Guidance | Operations that modify system or file permissions fail to explain the permission scope, security impact, and least-privilege recommendations. | A file permission manual does not warn that overly permissive settings allow unauthorized tampering, nor does it recommend safe permission values. |
| **Business Risk** | Legal & Compliance Issues | Data Privacy Non-Compliance | Operations involving user data collection, storage, or transmission fail to state the purpose, storage location, or user deletion rights required by privacy regulations. | A health monitoring application guide does not explain where collected health data is stored or how users can delete their data. |
| **Business Risk** | Performance Impact Issues | Unstated Resource Consumption | Resource-intensive operations (large installations, heavy data processing) do not state CPU, memory, or disk I/O requirements. | A 3D modeling software installation guide omits high CPU and RAM requirements, leading to system freezes after installation. |
| **Business Risk** | Performance Impact Issues | Unstated Performance Impact | Operations that affect long-term system performance (installing plugins, changing kernel parameters) do not explain positive/negative impacts or optimization tips. | A mobile utility application guide fails to mention that continuous background scanning reduces battery life. |
| **Usability** | Consistency Issues | Inconsistent Terminology | Multiple terms are used to refer to the same concept or action across the document (e.g., switching between "user interface" and "operation interface"). | A project management guide refers to task assignment as "assign tasks to members" in one section and "delegate work items" in another. |
| **Usability** | Consistency Issues | Inconsistent Logic | Workflows or repeated procedures contradict each other across different sections. | A finance software manual states "approve vouchers before closing accounts" in Chapter 2, but "close accounts before approving vouchers" in Chapter 5. |
| **Usability** | Consistency Issues | Inconsistent Formatting | Fonts, font sizes, paragraph indentation, heading numbering, or figure/table numbering are inconsistent across the deliverable. | A hardware maintenance manual uses inconsistent heading font sizes and jumps from Figure 1-1 directly to Figure 1-3. |
| **Usability** | Usability Issues | Overly Complex Language | Sentences are overly long, convoluted, or filled with unexplained jargon inappropriate for the target audience. | A consumer smart speaker manual explains wireless pairing as "establishing a data link layer connection via the protocol stack." |
| **Usability** | Usability Issues | Disorganized Structure | Information lacks logical order, operating steps are scattered, or the table of contents does not match the actual content. | An e-commerce seller guide has a table of contents that does not match the section headings, preventing users from finding product listing instructions. |
| **Usability** | Usability Issues | Missing User Guidance | Steps lack clear purpose statements, necessary notes/warnings, or error-handling tips when an operation fails. | A kitchen appliance manual explains the defrost button without specifying defrost times or precautions for different food types. |
| **Usability** | Compatibility Issues | Cross-Platform Incompatibility | Multi-platform documentation (desktop OS, mobile OS, tablet) only provides instructions for a single platform without noting differences. | An office suite guide only describes desktop mouse operations and omits keyboard shortcuts and tablet touch gestures. |
| **Usability** | Compatibility Issues | Browser Incompatibility | Web application instructions fail to account for rendering or behavior differences across major web browsers. | A web console guide describes steps that work in one browser engine but fail in another due to UI rendering differences. |
| **Usability** | Maintainability & Extensibility | Inflexible Structure | The document uses a monolithic, non-modular structure where adding a new feature or step requires rewriting and reformatting the entire document. | A hardware manual is written as a single linear narrative; adding a new module breaks numbering and flow across the entire file. |
