# Document Elements and Visual Formatting Standards

This reference preserves the complete rules and recommendations for hyperlinks, cross-references, examples, procedural steps, lists, code, tables, UI controls, callout boxes, graphics/screenshots, and videos.

---

## 1. Hyperlink Standards

### Precautions
- All hyperlinks must be reachable. Verify every link before and after publishing to prevent 404 errors.
- External links must use **absolute URLs** (`https://...`), never relative paths.
- Never point a hyperlink to an empty directory/category node that only lists child pages.

### Writing Requirements
- Every hyperlink must have descriptive anchor text (`[Title](URL)`). Never paste a raw URL directly into body text.
- Embed hyperlinks naturally inside the sentence on the relevant noun phrase or document title.
- Keep link anchor text concise and accurate.
- In mixed CJK/Latin text, add a space before and after a hyperlink, except when the link is immediately followed by a punctuation mark.

---

## 2. Cross-Reference Standards

### Rules
- **Rule 1**: Use standardized phrasing to introduce cross-references: **"see"** or **"refer to"** in English, and a single standardized phrase in local languages (never mix multiple synonyms).
- **Rule 2**: Always attach a hyperlink to the referenced target so users can navigate directly:
  > **Example**: For details on signature generation, see [Generating a Signature](https://example.com).
- **Rule 3**: If the referenced target has a heading, use that exact heading as the link anchor text; if it does not have a heading, summarize the target with a concise noun phrase as the anchor text.
- **Rule 4**: Use cross-references when a list of items cannot be exhaustively enumerated inline:
  > **Example**: For more instance specifications, see the [Specification Query Page](https://example.com).

### Recommendations
- **Recommendation 1**: If the referenced content is **short (fewer than 50 CJK characters or ~30 English words)** and essential to the current task, state it directly inline instead of sending the user to another page.
- **Recommendation 2**: If the referenced content is lengthy and would disrupt the flow if repeated, use a cross-reference link.
- **Recommendation 3**: If the referenced content is in the **same document and located nearby**, do not add a hyperlink.

---

## 3. Example Standards

### Rules
- **Rule 1**: Place all inline examples after **"for example"**:
  - **Correct**: Enter a custom server name (for example, `web-app-01`), and click **OK**.
  - **Incorrect**: Change it to `web-app-01` (customizable), and click **OK**.
- **Rule 2**: Examples must reflect realistic user scenarios and conventions.

### Recommendations
- **Recommendation 1**: Provide concrete example values when describing parameters to reduce cognitive load.
- **Recommendation 2**: Introduce examples consistently with "for example" or "such as".
- **Recommendation 3**: Use **reserved private IP addresses** in examples. Never use real production public IP addresses to prevent information leakage:
  - **RFC 1918 IPv4 private ranges**:
    - Class A: `10.0.0.0` – `10.255.255.255` (`10.0.0.0/8`)
    - Class B: `172.16.0.0` – `172.31.255.255` (`172.16.0.0/12`)
    - Class C: `192.168.0.0` – `192.168.255.255` (`192.168.0.0/16`)
  - **RFC 4193 IPv6 private range**: `FEC0:0000:0000:0000:0000:0000:0000:0000/10` (or RFC 5737 documentation blocks `192.0.2.0/24`, `198.51.100.0/24`, `203.0.113.0/24`).
- **Recommendation 4**: Use **`example.com`** (or `example.org` / `example.net` per RFC 2606 Section 3) for domain name examples. Never use registered third-party domains.

---

## 4. Procedural Step Standards

### Rules
- **Rule 1**: Every procedure must be tested and verified to be executable.
- **Rule 2**: Steps must be specific and clearly state **who** performs the action and **where** (which console, terminal, or directory) it is performed.
- **Rule 3**: Separate the **user action** from lengthy **descriptions or results**. Put supplementary descriptions and command outputs on a new line/paragraph under the step.
- **Rule 4**: Provide the **expected result** after an action (for example, show the expected terminal output after running a command).
- **Rule 5**: Include an indented screenshot below any step that involves complex UI interactions or hard-to-find controls. The screenshot must match the step text.
- **Rule 6**: When a step requires a third-party or official tool, provide the official download link right at that step.
- **Rule 7**: Do not clutter the middle of a step sequence with side notes. Place supplementary notes at the end of the step or procedure using a callout box (`Note` / `Warning`).
- **Rule 8**: Every procedure must end with a **verification method** so the user can confirm whether the operation succeeded (e.g., a UI success message or verification command).

### Recommendations
- **Recommendation 1**: State the estimated time required to complete a long procedure.
- **Recommendation 2**: Keep a single procedure to **9 steps or fewer**. If it has more than 9 steps, group them into logical sub-tasks/phases.
- **Recommendation 3**: If a step is optional or skippable, state the condition clearly and indicate which step to jump to next.
- **Recommendation 4**: If a sub-step is already covered in detail by another document, link to that document instead of duplicating the full sub-procedure.
- **Recommendation 5**: When using steps as section headings, format them as **`Step N: Action Description`** (e.g., `Step 1: Configure the Device Object`).

---

## 5. List Standards

Lists include ordered lists (`1.`) and unordered lists (`-`).

### Rules
- **Rule 1**: When all list items are **words or short phrases**, do **not** add terminal punctuation.
- **Rule 2**: When list items are **complete sentences**, end every item with a **period**.
- **Rule 3**: Indent any explanatory paragraph or code block that belongs to a specific list item.
- **Rule 4**: A list must contain **at least 2 items** (`≥ 2`). Never create a single-item list.
- **Rule 5**: Nest lists to **at most 1 sub-level** (`≤ 1` level of nesting).

**Correct (1 level of nesting)**:
```markdown
1. Top-level item
   - Sub-item
   - Sub-item
2. Top-level item
```

**Incorrect (2 levels of nesting)**:
```markdown
1. Top-level item
   - Sub-item
     1. Deeply nested item
     2. Deeply nested item
   - Sub-item
2. Top-level item
```

### Recommendations
- **Recommendation 1**: Use parallel grammatical structures for all items in a list (either all phrases or all sentences).
- **Recommendation 2**: If a list unavoidably mixes phrases and full sentences, end **every item with a period**.
- **Recommendation 3**: Keep a single list to **9 items or fewer** (`≤ 9`).
- **Recommendation 4**: Maintain a consistent voice and mood across all items (e.g., all imperative verb-object phrases, or all declarative statements; never mix questions and statements in the same list).

---

## 6. Code Standards

Documentation includes two types of code:
- **Code blocks**: Multi-line or standalone code snippets wrapped in triple backticks (`` ``` ``).
- **Inline code**: Parameters, expressions, filenames, or short commands embedded in prose wrapped in single backticks (`` ` ``).

### Rules
- **Rule 1**: All code blocks and inline code must match the actual product implementation.
- **Rule 2**: Code blocks must use clean, consistent indentation.
- **Rule 3**: Explain key parameters in code blocks using inline code comments or a parameter table immediately below the block.
- **Rule 4**: Highlight key lines or placeholders when appropriate.
- **Rule 5**: Always wrap parameter names, expressions, paths, and inline commands in prose with single backticks (`` ` ``).
- **Rule 6**: Place standalone code snippets in fenced code blocks separated from body paragraphs.
- **Rule 7**: **Never include real secrets, credentials, private keys, or sensitive internal addresses in code blocks or inline code.** Always scan code examples for sensitive data before publishing.

### Recommendations
- **Recommendation 1**: Full code examples should be directly executable.
- **Recommendation 2**: Include concise comments in code blocks.
- **Recommendation 3**: Place comments immediately above or alongside the code lines they describe.

---

## 7. Table Standards

### Rules
- **Rule 1**: A table must have **at least 2 rows and 2 columns**.

**Correct**:
| **Header 1** | **Header 2** |
| - | - |
| Value 1 | Value 2 |

- **Rule 2**: Keep table layouts clean and use a consistent structure for tables of the same type.
- **Rule 3**: Every table must have a **header row** (except standalone 2-column glossary layouts where specified).
- **Rule 4**: Keep column header names concise and consistent across the entire document (for example, do not alternate between "Description", "Meaning", and "Explanation" across parameter tables in the same guide).
- **Rule 5**: Never insert a second header row in the middle of a single table.
- **Rule 6**: Keep phrasing and **terminal punctuation consistent within each column**:
  - If a column contains full sentences (or a mix of sentences and phrases), end **every cell in that column with a period**.
  - If a column contains only single words or short phrases, **omit periods** throughout that column.

**Correct**:
| **Error Code** | **Description** |
| - | - |
| 6016 | Registration timed out. Please try again. |
| 6017 | Invalid API parameter. Check whether the parameter meets the requirements. |

**Incorrect (inconsistent periods)**:
| **Error Code** | **Description** |
| - | - |
| 6016 | Registration timed out. Please try again |
| 6017 | Invalid API parameter. Check whether the parameter meets the requirements. |

- **Rule 7**: **Never leave a table cell blank.** Fill empty cells with `None` or a hyphen (`-`). If a special symbol is used, explain its meaning in a note.
- **Rule 8**: If multiple rows share the same value, repeat the value or merge the cells. **Never write "Same as above" or "Same as below".**
- **Rule 9**: Keep a numeric value and its measurement unit on the same line within a cell; do not wrap between the number and unit.

### Recommendations
- **Recommendation 1**: Prefer tables with **9 rows or fewer** and **4 columns or fewer** (2–3 columns is ideal).
- **Recommendation 2**: Introduce each table with a brief lead-in sentence or caption that does not exceed the width of the table.

---

## 8. UI Control Standards

### Rules
- **Rule 1**: Format UI control names (buttons, tabs, menu items, dialog titles) in **bold** so they stand out. Do not wrap UI labels in quotation marks.
  > **Example**: In the **Instances** tab, click **Create**.
- **Rule 2**: Do **not** add the word "button" after a bolded button label:
  - **Correct**: Click **Create**.
  - **Incorrect**: Click the **Create** button.
- **Rule 3**: Express sequential menu navigation using **`Select Menu 1 > Menu 2 > Menu 3`**, with a single space before and after each `>`:
  > **Example**: Log in to the management console, select **Security > Unblock**, locate the target IP, and click **Unblock** in the **Actions** column.
- **Rule 4**: When a screen contains many controls, state the **spatial location** (e.g., top-left, top-right, center, bottom-left, bottom-right) to help users locate the control quickly.
- **Rule 5**: Omit mnemonic access keys in parentheses when naming buttons or menus:
  - **Correct**: Click **New**
  - **Incorrect**: Click **New (N)**
- **Rule 6**: Write keyboard key names exactly as printed on the physical keycap (e.g., `Press Enter`).
- **Rule 7**: For unlabeled icon buttons, embed a `20×20px` inline icon screenshot: `Click ![Edit Icon](url)`.
- **Rule 8**: Ensure all UI labels in the text match the actual product interface verbatim.

---

## 9. Callout Box Standards: Note, Attention, Warning, Prohibition

### Four Callout Severity Levels
1. **Note / Tip**:
   - **Purpose**: Supplementary information, helpful tips, or brief examples that add convenience or clarify a concept without implying operational risk.
2. **Attention / Caution**:
   - **Purpose**: Low-level potential risk or mandatory prerequisite information. Ignoring this information may cause an operation to fail or lead to minor inconvenience that is tedious to fix.
3. **Warning**:
   - **Purpose**: Medium-level risk or high-risk operation. Ignoring this warning may result in equipment damage, data loss, performance degradation, or unpredictable system behavior.
4. **Prohibition / Danger**:
   - **Purpose**: High-level critical danger or strictly forbidden operation. Violating this rule will cause system crashes, unrecoverable data loss, or severe security incidents.

### Recommendations
- **Recommendation 1**: Include **no more than 3 callout boxes** in a single document. If you have more than 3 items to call out, create a dedicated H2 section titled **`Precautions`** and list them as bullet points.
- **Recommendation 2**: Never stack two callout boxes directly against each other; separate multiple callout boxes with body text or tables.
- **Recommendation 3**: Keep each callout box concise (**6 lines or fewer**).

---

## 10. Graphic and Screenshot Standards

### Precautions
- **Never use an image to display a table.** Always use Markdown or HTML tables.
- Do not use bitmap icons with transparent backgrounds where rendering artifacts may occur; keep icon styles consistent within any diagram.
- Never include screenshots of unauthorized or unlicensed third-party software.
- Do not capture OS **Start > Programs** menus (due to third-party trademark/IP risks); describe the launch path in text instead.
- **Mask all sensitive information** in screenshots, including personal usernames, real names, real `SecretId` / `SecretKey` credentials, instance IDs, node names, and real IP addresses.
  > **Masking Tip**: Mask the middle or trailing portion of the field rather than obscuring the entire UI control.
- Match the UI language of screenshots to the language of the document.

### General Requirements
- Keep text and graphics strictly consistent.
- Crop screenshots to show only the relevant area (for example, omit the left navigation sidebar unless the step is specifically about navigation).
- Ensure the captured window is active and **hide the mouse cursor or blinking text caret** unless essential to the instruction.
- Avoid putting long paragraphs of text inside diagrams; replace long labels with numbered callouts and explain them in the body text below the image.
- Spell out or explain any abbreviations used inside a diagram in the surrounding text.
- Use licensed fonts for all text inside diagrams, and ensure text never overlaps lines or borders.
- Keep multi-digit Arabic numbers on a single line inside diagrams.
- **Standard image width**: **`978px`**; **inline icon size**: **`20×20px`**.
- Keep aspect ratios consistent across images in the same document, and do not add outer borders to images.
- Separate multiple images with explanatory body text rather than stacking images back-to-back.

### Detailed Design Specifications by Graphic Type
1. **UI Screenshots**:
   - **Width & Alignment**: Target **`978px`** width (height flexible, except mobile viewports). If an image is narrower than `978px`, its width must be **at least `460px`** (`258px` minimum for mobile/scenario captures) and **left-aligned** with the body text. Use `.jpg` or `.png`.
   - **Highlight Boxes**: Highlight key fields and buttons using a **red rectangle (`#FB5555`, `2px` stroke)**.
   - **Step Number Markers**: Use **`16px` diameter circles** filled with **orange (`#FF7200`)**, drop shadow `#C2C5CA` (`X: 0, Y: 1, Blur: 4`), and bold white (`#FFFFFF`) sans-serif numerals (`1, 2, 3...`).
2. **Topology Diagrams**:
   - **Canvas & Padding**: Canvas width **`976px`**, top/bottom padding **`20px`**, left/right padding **`≥ 10px`**.
   - **Color Palette**: Brand Blue `#00A4FF`, Primary Text `#333333`, Area Blue `#D9EEFF`, Area Gray `#EAEBEC`, Line Gray `#D7D7D7`, Secondary Text `#999999`.
   - **Typography**: Keep node labels concise (**10 characters/words or fewer**); secondary annotations use `14px` in `#999999`.
3. **Flowcharts and Architecture Diagrams**:
   - **Canvas & Padding**: Horizontal flowchart width **`978px`** (vertical flowcharts: `578px`; architecture/org charts: `630px`, `820px`, or `1160px`), top/bottom padding **`30px`**, left/right padding **`≥ 10px`**, spacing between blocks **`15px`**.
   - **Color Palette**: Primary Blue `#1D94FF`, Secondary Blue `#126EFF`, Teal `#01C3DC`, Accent Orange `#FF7200`, Primary Text `#333333`, Secondary Text `#888888`, Border Gray `#E2E3E7`.
   - **Standard Shapes**:
     - **Rounded Rectangle (Oval)**: Start / End
     - **Rectangle**: Process / Operation step
     - **Diamond**: Decision / Branch condition
     - **Wavy-base Document**: Document input/output
     - **Double-bordered Rectangle**: Sub-process
     - **Cloud**: External system or cloud interface
     - **Cylinder**: Database or storage
     - **Solid Arrow**: Primary flow; **Dashed Arrow**: Secondary/feedback flow.
4. **Multi-Grid Palettes & Map Annotations**:
   - Limit diagrams to **at most 3 primary colors**, using standard blue (`#006EFF` base) and cyan (`#1FC0CC` base) gradients.
   - For point markers on visual overlays, avoid large opaque circles that obscure underlying details; use **`12px` circles at `50%` opacity** filled with `#29CC85` (green) or `#00A4FF` (blue).

---

## 11. Video Standards

### Rules
- **Rule 1**: Only embed videos that directly match the topic of the document.
- **Rule 2**: Video content must be technically accurate, logically structured, and free of exaggerated claims.
- **Rule 3**: Never include sensitive topics, religious content, or mentions of competitors.
- **Rule 4**: Videos must be free of typos, sensitive terms, and prohibited advertising words.
- **Rule 5**: Videos must be complete and free of third-party watermarks.
- **Rule 6**: Video playback must be sharp, smooth, and synchronized with the audio track.
- **Rule 7**: All visual and audio assets (images, logos, fonts, music) must be properly licensed.
- **Rule 8**: Blur or mask all sensitive information (credentials, personal data, real IPs) appearing in the video.
- **Rule 9**: Keep the recording environment clean (hide browser bookmark bars, unrelated tabs, personal search history, third-party extensions, and ads).
- **Rule 10**: Eliminate background noise (phone rings, traffic, loud keyboard/mouse clicks).
- **Rule 11**: Record voiceovers in clear, standard pronunciation without heavy regional accents.
- **Rule 12**: Maintain balanced audio levels without clipping, plosives, static hum, or microphone hiss.

### Recommendations
- **Recommendation 1**: Record in full screen to avoid black letterbox bars.
- **Recommendation 2**: Use a video bitrate of at least `1800 kbps` (`2400 kbps` recommended), audio bitrate of at least `192 kbps` (`320 kbps` recommended), and frame rate of `30 fps` or higher.
- **Recommendation 3**: Export in standard **MP4 format (`H.264` video + `AAC` audio)**.
- **Recommendation 4**: Maintain a moderate speaking pace (~130–160 English words per minute, or 180–250 CJK characters per minute).
- **Recommendation 5**: Avoid repetitive verbal fillers (`uh`, `um`, `then`, `so`).
- **Recommendation 6**: Edit out long pauses, slips of the tongue, and redundant repetitions.
