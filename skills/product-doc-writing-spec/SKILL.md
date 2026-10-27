---
name: product-doc-writing-spec
description: Comprehensive technical and product documentation writing, formatting, and style standards (covering headings, paragraphs, sentences, vocabulary, CJK-Latin spacing, punctuation, numbers and currencies, hyperlinks, cross-references, examples, procedural steps, lists, code blocks, tables, UI controls, callout boxes, screenshots and diagrams, Markdown syntax, document genre templates, internationalization and English capitalization, and advertising/superlative compliance). Use whenever the user asks to write, edit, format, review, or audit product documentation, operation guides, API/SDK references, troubleshooting guides, parameter references, FAQs, or glossaries.
---

# Product Documentation Writing & Formatting Specification

This skill provides a complete, vendor-neutral specification for authoring, formatting, localizing, and reviewing technical and product documentation.

---

## 1. High-Frequency Formatting Rules (16 Core Checkpoints)

Always verify these 16 high-frequency rules when writing or reviewing documentation:

1. **Never Use H1 in the Document Body**: Reserve H1 (`#`) for the top-level document or page title. Start all main sections inside the document body at **H2 (`##`)**.
2. **Indent Step Screenshots**: Indent screenshots under ordered steps or list items so they align vertically with the parent step's text.
3. **Remove Redundant Blank Lines/Spaces**: Delete extra blank lines and leading/trailing spaces between paragraphs.
4. **Space Around Hyperlinks**: In mixed CJK/Latin text, add a space before and after a hyperlink, **except** when the link is immediately followed by punctuation (`For details, see [CLI Tool](https://example.com).`).
5. **Space Between CJK and Latin Words**: Insert a half-width space between CJK characters and Latin words (omit before punctuation; **do not add spaces between numbers and CJK characters, numbers and units, or CJK characters and units**, e.g., `3s`, `5KB`, `10Mbps`).
6. **Standardize Cross-Reference Phrasing**: Use a single standardized cross-reference phrase across the documentation set, such as **"see [Title](url)"** or **"refer to [Title](url)"**, rather than mixing inconsistent synonyms.
7. **Keep Terminal Punctuation Consistent in Lists and Tables**:
   - End list items with a period if they are full sentences (or a mix of sentences and phrases); omit periods if all items are short phrases/words.
   - Keep terminal punctuation uniform within each table column (all sentences end with periods; all short phrases omit periods).
8. **Embed Links in Anchor Text**: Never paste raw URLs in prose; attach links to descriptive noun phrases (`[KV Storage](https://example.com)`).
9. **Bold UI Controls Without Quotes or the Word "Button"**:
   - Format UI labels in **bold** without quotation marks.
   - Never append the word "button" after a bolded button name.
   - **Correct**: In the **Virtual Server** tab, click **Create**.
   - **Incorrect**: In the "Virtual Server" tab, click the **Create** button.
   - Format menu paths as `Select **Menu 1 > Menu 2 > Menu 3**` with spaces around `>`.
10. **Attach Links to Console References**: Link the console name on first mention in procedural steps (`Log in to the [Management Console](https://example.com)`).
11. **Format Lists and Nested Blocks Properly**: Use `-` for unordered lists and `1.` for ordered lists; nest lists **at most 1 level deep** (`≤ 1`), and align nested code blocks/tabs vertically with the list item text.
12. **Distinguish Punctuation by Language**: Never mix full-width CJK and half-width Latin punctuation in the same document; ensure paired marks (quotes, parentheses, colons) match on both sides; always use a half-width colon in time expressions (`18:00`).
13. **Include Table Headers and Fill Empty Cells**: Every table (`≥ 2×2`) must have a header row. Fill empty cells with `None` or `-`; never leave cells blank or write "Same as above".
14. **Match Screenshot UI Language to Document Language**: Ensure the UI language in console screenshots matches the language of the document.
15. **Clean Up Pasted Markdown Artifacts**: Check for unrendered Markdown syntax (`**`, `-`) or 4-space indentation that accidentally turns callouts or text into code blocks.
16. **Never Link to Empty Directory Pages**: Always link to concrete content pages, never to empty category nodes that only list child links.

---

## 2. Quick Reference Summary by Dimension

| Dimension | Core Rules |
| - | - |
| **Headings** | Use **noun phrases** for descriptive and parameter docs (`Instance Overview`, `Specification Parameters`); use **verb-object phrases** for procedural docs (`Connect to a Database`); state the **exact symptom** in troubleshooting titles (`Unable to Log In to Server`, omitting redundant words like "Troubleshooting"). Keep headings concise (`≤ 15` CJK characters or `≤ 8` English words); never use `&` (use `and`), `/` (use `and` / `or`), or hyphens for notes (use parentheses, e.g., `Enable Service (Linux)`); avoid single-child orphan headings. |
| **Paragraphs & Sentences** | One topic per paragraph with the topic sentence first; paragraph length `≤ 7` lines (`≤ 4` optimal); no more than 3 consecutive pure-text paragraphs (use diagrams/tables first for technical concepts). Keep simple sentences concise (`≤ 50` CJK chars / `~25` English words), compound sentences `≤ 100` CJK chars (`~45` English words); use active voice and declarative/imperative mood; avoid passive voice, double negatives, and rhetorical questions. |
| **Vocabulary & Tone** | Use first-person plural `we` (never informal self-references like "the author/editor") and second-person `you` / `the user`. Introduce examples consistently with `for example`. Avoid slang, vague intensifiers (`very`, `basically`), and hostile terms (`kill` / `kick out`). |
| **Numbers & Ranges** | Write ranges with a spaced half-width hyphen and repeat the unit on both bounds (`10Mbps - 100Mbps`, never `10 - 100Mbps`). Distinguish increments (`increased by`) from totals (`increased to`). **Never express a decrease as "reduced by N times"** — always use percentages (`reduced by 80%`). Format timestamps as `YYYY-MM-DD hh:mm:ss`. |
| **Currency** | Prefer `Number + Currency Code/Name` (`10 USD`). When using a symbol, place it immediately before the number with no space and no trailing unit word (`¥1,234.56`, `CNY¥100`). Standardize international docs to `USD`. |
| **Safe Examples** | Use RFC 1918 private IPv4 ranges (`10.0.0.0/8`, `172.16.0.0/12`, `192.168.0.0/16`) and `example.com` (RFC 2606). Never include real credentials (`SecretId`/`SecretKey`) or production IPs in code or screenshots. |
| **Callout Boxes** | Four severity levels: **Note** (tips/context), **Caution / Important** (low risk/prerequisites), **Warning** (medium risk/potential data loss), **Danger** (critical danger/prohibited action). Keep to `≤ 3` callouts per page, `≤ 6` lines each, separated by body text. |

---

## 3. Detailed Reference Files (Load on Demand)

Read the corresponding reference file under `references/` when working on specific documentation tasks:

1. **[references/common-pitfalls-and-checklist.md](references/common-pitfalls-and-checklist.md)**
   - High-frequency writing/formatting rules and the 30-category documentation quality inspection checklist (Completeness, Accuracy, Timeliness, Business Risk, Usability).
2. **[references/text-and-punctuation.md](references/text-and-punctuation.md)**
   - Complete rules and positive/negative examples for Headings, Paragraphs, Sentences, Vocabulary, Spacing, Numbers & Quantities, Punctuation, and Currency Symbols.
3. **[references/elements-and-formatting.md](references/elements-and-formatting.md)**
   - Complete rules for Hyperlinks, Cross-References, Examples, Procedural Steps, Lists, Code, Tables, UI Controls, Callout Boxes, Graphics/Screenshots (`978px` width, `#FB5555` red highlight boxes, `#FF7200` step markers, topology & flowchart specs), and Videos.
4. **[references/markdown-syntax.md](references/markdown-syntax.md)**
   - Complete Markdown and HTML syntax manual: Headings, Markdown & HTML Tables (row headers, diagonal headers), Code Highlighting & `plaintext`, Links, Images, Callout Blocks, Lists, and HTML Character Escaping (`&gt;`, `&lt;`, `&#10003;`).
5. **[references/doc-types-and-templates.md](references/doc-types-and-templates.md)**
   - Documentation Tree Frameworks (Cloud/SaaS & On-Premises) and genre-specific standards & Markdown templates:
   - Descriptive Docs, Procedural Guides (5W2H1E template), Parameter References, Troubleshooting Guides (3W symptom template), FAQs, Glossaries, High-Risk Operation Warnings, Feature Lifecycle Stages (Beta/Allowlist/Deprecation), Release Notes, and API Reference Templates & Checklists.
6. **[references/i18n-and-english-style.md](references/i18n-and-english-style.md)**
   - Internationalization Writing Standards, Pre-Translation Source Checklist, English Capitalization Rules (**Title Caps** vs. **Sentence caps**), UI String Translation Matrix, Terminology vs. Preferred Expressions, and the 15-Point Multilingual Quality Review Checklist.
7. **[references/compliance-and-sensitive-words.md](references/compliance-and-sensitive-words.md)**
   - Advertising Law & Superlative Compliance (prohibited absolute claims, 5 permitted exceptions, data citation rules, and objective product descriptions).
