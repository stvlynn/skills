# Text, Tone, Numbers, and Punctuation Standards

This reference preserves the complete rules and recommendations for headings, paragraphs, sentences, vocabulary, spacing, numbers and quantities, punctuation, and currency symbols.

---

## 1. Heading Standards

### Rules
- **Rule 1**: A heading must accurately summarize the core content of its section.
- **Rule 2**: Keep headings concise, clear, and unambiguous.
- **Rule 3**: Use **noun phrases** for descriptive documents (e.g., "Server Overview").
- **Rule 4**: Use **verb-object structures** for procedural/operational documents (e.g., "Connect to a Database", "Install the Client").
- **Rule 5**: Use **noun phrases** for parameter reference documents (e.g., "Specification Parameters").
- **Rule 6**: Use a consistent grammatical structure for all headings at the same hierarchy level.
- **Rule 7**: Do not simply repeat the parent heading's title in a child heading.
- **Rule 8**: Avoid orphan headings (i.e., having only a single sub-heading under a parent heading). If a section has only one sub-heading, promote or merge it.
- **Rule 9**: Use well-known abbreviations directly in headings without spelling out the full name.
- **Rule 10**: Do not use superscripts or subscripts in headings.
- **Rule 11**: Do not use `&` to indicate coordination in headings; use "and".
- **Rule 12**: Do not use `/` to mean "and" or "or" in headings; write out "and" or "or" explicitly.
- **Rule 13**: Do not use hyphens or en-dashes in headings for supplementary notes; use colons or parentheses instead.
  > **Note**: Never append document lifecycle statuses such as "(Deprecated)", "(Retiring)", or "(Unmaintained)" to headings.

### Recommendations
- **Recommendation 1**: Omit unnecessary words in headings as long as the meaning remains unambiguous.
- **Recommendation 2**: When an operation can be performed in multiple ways or on multiple platforms, use parentheses at the end of the procedural heading to distinguish the method or platform:
  - **Correct**:
    - `Enable Service (Linux)`
    - `Enable Service (Windows)`
- **Recommendation 3**: If identical headings appear under different parent directories, add a distinguishing keyword to improve searchability:
  - **Correct**:
    - `Instance Overview`
    - `Image Overview`
- **Recommendation 4**: Keep headings concise (for CJK text, 15 characters or fewer; for English text, typically 8 words or fewer).

---

## 2. Paragraph Standards

A paragraph is a fundamental unit of thematic information composed of multiple sentences.

### Rules
- **Rule 1**: Each paragraph must focus on a **single topic** or a single central sentence.
- **Rule 2**: Place the **topic sentence at the very beginning** of the paragraph to summarize the main point. Subsequent sentences should elaborate, explain, or provide supporting details for that opening sentence.
- **Rule 3**: A paragraph must **not exceed 7 lines** (the optimal length is **4 lines or fewer**). If a paragraph exceeds 7 lines, split it into multiple paragraphs by sub-topic or convert the details into a list or diagram.
- **Rule 4**: Use a declarative, affirmative tone. Avoid exclamatory sentences (`!`).

### Recommendations
- **Recommendation 1**: Keep the introductory first paragraph of an article brief.
- **Recommendation 2**: For technical descriptions (such as architecture or working principles), follow the **"diagram/table first, text second"** principle rather than relying solely on prose paragraphs.
- **Recommendation 3**: Avoid having **more than 3 consecutive pure-text paragraphs**, and never let continuous text paragraphs span a full page without visual breaks. Use diagrams, tables, or lists to break up dense text.

---

## 3. Sentence Standards

A sentence ends with a period, indicating a complete thought.

### Rules
- **Rule 1**: Each sentence should express only **one main idea** and must be semantically complete.
- **Rule 2**: Avoid overly long sentences. Keep simple sentences under 50 CJK characters (or ~25 English words), and compound/complex sentences under 100 CJK characters (or ~45 English words, no more than 3 lines of body text).
- **Rule 3**: Prefer simple sentences and coordinate clauses; avoid deeply nested complex clauses.
- **Rule 4**: Use direct, affirmative statements. Avoid double negatives and rhetorical questions.
  > **Note**: Write with precision and certainty; avoid vague, hesitant, or ambiguous phrasing.
- **Rule 5**: Avoid stacking multiple nouns or multiple adjectives as modifiers.
  > **Note**: Long noun clusters force readers to untangle modifier relationships, and stacked adjectives obscure the core noun.
  > **Incorrect**: "Configuration management module" (ambiguous stacking of noun modifiers where the relationship between "configuration" and "management" is unclear without context).
- **Rule 6**: Make the grammatical subject of every sentence clear. When omitting the subject, ensure the reader can immediately and unambiguously infer it.
  > **Note**: Imperative sentences may omit the subject (e.g., "Turn off the power switch.").
- **Rule 7**: Maintain parallel sentence structures, especially across coordinate clauses.

### Recommendations
- **Recommendation 1**: Break complex sentences into bulleted lists or shorter simple sentences.
- **Recommendation 2**: Use **imperative sentences** for commands and user actions:
  - **Correct**: Start the process.
  - **Incorrect**: The process should be started.
- **Recommendation 3**: Use the **active voice** and avoid the passive voice whenever possible.
  > **Note**: Passive constructions are wordier, rely on abstract nouns, and often obscure who performs the action.

---

## 4. Vocabulary Standards

### Rules
- **Rule 1**: Never use typos, misspellings, or internet slang/puns.
- **Rule 2**: Avoid colloquialisms, spoken filler words, and informal phrasing.
- **Rule 3**: Avoid subjective degree modifiers, intensifiers, and empty transitional fillers:
  > **Avoid**:
  > - Subjective degree words: *quite a few*, *fairly good*, *completely*, *basically*, *decisive*, *ultimate*, *merely*, *in fact*, *noteworthy*.
  > - Conversational transitions: *of course*, *needless to say*.
  > - Vague quantifiers: *some*, *very*, *massive*, *a few*, *a little*.
- **Rule 4**: Avoid words with negative or hostile emotional connotations toward the user (such as "kill" or "kick out" in user-facing messages).
  > **Incorrect**: "The process was killed", "You have been kicked out."
  > **Correct**: "The process was terminated", "You have been removed from the session."
- **Rule 5**: Keep terminology strictly consistent throughout the document. Never use different words to refer to the same entity or action.
  > **Correct**: If you use "local PC" early in the document, do not switch to "workstation" or "computer" later.
- **Rule 6**: Keep adjacent phrases parallel in part of speech and grammatical structure.
  > **Correct**: The system provides database management, permission management, and data import. (All noun phrases)
  > **Incorrect**: The system provides database management, permission management, and importing data. (Mixing noun phrases with a gerund phrase)
- **Rule 7**: Avoid words prohibited by advertising or compliance laws (such as unverified absolute superlatives).

### Recommendations
- **Recommendation 1**: Introduce examples consistently (e.g., using "for example" or "such as"). When "for example" introduces a complete clause, follow it with a comma; when introducing a short inline phrase in CJK text, omit the comma.
- **Recommendation 2**: Ensure modifiers (adjectives vs. adverbs) match the grammatical role of the word they modify.
- **Recommendation 3**: For the first-person plural pronoun, use **"we"** (or the official organization role), never informal self-references like "the author" or "the editor".
- **Recommendation 4**: Address the reader respectfully as **"you"** or **"the user"** consistently.
- **Recommendation 5**: Distinguish between **login account IDs** and **financial/billing accounts** consistently.

---

## 5. Spacing Standards

### Rules
- **Rule 1**: English words must be separated by spaces.
  > **Note**: Code identifiers and parameter names are exempt from this rule.
- **Rule 2**: In mixed CJK/Latin text, insert a single half-width space between CJK characters and Latin words.
  > **Exception**: **Measurement units are exempt when following numbers or CJK characters** (see Rules 4 and 5).
- **Rule 3**: In CJK text, do **not** add a space between Arabic numerals and CJK characters.
- **Rule 4**: Do **not** add a space between a number and its measurement unit (e.g., `3s`, `5KB`, `10Mbps`).
- **Rule 5**: In CJK text, do **not** add a space between CJK characters and measurement units.
- **Rule 6**: Do **not** add spaces before or after unary mathematical sign/property symbols (`+`, `-`, `±`, `| |`).
  > **Example**: `–48±20%`
- **Rule 7**: **Add spaces before and after** binary mathematical operators and relational symbols, and always use half-width Latin symbols:
  - **Mathematical operators**: `+`, `-`, `×` (or `·`), `÷` (or `/`), `∪`, `∩`, `√`, `log`, `lg`, `ln`, `:`, `dx`, `∫`, `∮`.
  - **Relational symbols**: `=`, `≈`, `≠`, `>`, `<`, `≥`, `≤`.
  > **Example**: `A > B > C`
- **Rule 8**: Do **not** add spaces around `+` in keyboard shortcuts.
  > **Example**: `Ctrl+C`
- **Rule 9**: In mixed CJK/Latin text, add a space between a hyperlink and adjacent CJK characters, but do **not** add a space between a hyperlink and adjacent punctuation marks.
- **Rule 10**: Express numeric ranges using a half-width hyphen (`-`) with a space on both sides.
  > **Example**: `10Mbps - 100Mbps`
- **Rule 11**: Do **not** add a space between a currency symbol and the numeric amount.
  > **Example**: `¥1,234.56`

---

## 6. Numbers and Quantities Standards

Documents use two forms of numerals: word numerals (one, two, three...) and Arabic numerals (`0, 1, 2...`).

### Rules
- **Rule 1**: Always use **Arabic numerals** for numeric values in tables and technical metrics, including positive/negative integers, decimals, percentages, fractions, and ratios.
- **Rule 2**: Use **word numerals** in fixed idioms, set phrases, and approximate modifiers (e.g., "hundreds of thousands", "first-tier").
- **Rule 3**: Keep special formal numbering consistent throughout the document.
- **Rule 4**: When documenting parameter values of 4 or more digits, match the actual system format regarding thousands separators (commas): if the system uses commas, include them; if the system does not use commas (or does not specify), omit commas in parameter values.
- **Rule 5**: Use a spaced half-width hyphen (` - `) for numeric ranges. When numbers carry SI units or quantifiers, **attach the unit or quantifier to both the lower and upper bounds**:
  - **Correct**: `10Mbps - 100Mbps`
  - **Incorrect**: `10 - 100Mbps`
- **Rule 6**: Write percentages as `Arabic numeral + %` with **no space** between the number and the `%` sign (e.g., `1%`).
- **Rule 7**: Never break an Arabic numeral across a line wrap.
- **Rule 8**: Clearly distinguish incremental increases from target totals:
  - Use **"increased by"** for the delta/increment, and **"increased to"** for the final total.
    - "Increased to 2× the previous value": `1 → 2`.
    - "Increased by 2×": `1 → 3`.
- **Rule 9**: Clearly distinguish incremental decreases from target totals, and **never express a decrease as "reduced by N times"**:
  - Always express decreases using **percentages**: **"reduced by X%"** or **"reduced to X%"**.
    - "Reduced to 80%": `100 → 80`.
    - "Reduced by 80%": `100 → 20`.
- **Rule 10**: Use Arabic numerals for dates and times:
  - **Date**: In tables, indexes, and timelines, use `YYYY-MM-DD` with zero-padded two-digit months and days (e.g., `2026-12-24`).
  - **Time**: Follow ISO 8601 extended format `hh:mm:ss` (e.g., `08:13:12`).
  - **Combined Date and Time**: Use `YYYY-MM-DD hh:mm:ss` (e.g., `2026-12-24 21:18:35`).
- **Rule 11**: Always use Arabic numerals with standard legal/SI measurement units for physical quantities.
- **Rule 12**: Follow applicable format conventions for document serial numbers and identification numbers.

### Recommendations
- **Recommendation 1**: Use one numeral style consistently within the same paragraph rather than mixing word numerals and Arabic numerals for comparable quantities.
- **Recommendation 2**: For readability in general prose, separate integers of 1,000 or more into 3-digit groups from right to left using half-width commas (e.g., `33,987`). If a number contains a decimal point, **do not add commas to the integer part or fractional part** (e.g., `33987.1314`).
  > **Note**: Always prioritize actual code/parameter syntax requirements (see Rule 4).
- **Recommendation 3**: Prefer Arabic numerals (`1, 2, 3, 4`) over Roman numerals (`I, II, III, IV`) for list and section numbering.

---

## 7. Punctuation Standards

### Rules
- **Rule 1**: Follow standard technical punctuation conventions.
- **Rule 2**: Always use a **half-width colon (`:`)** in time expressions, never a full-width colon:
  - **Correct**: `18:00`
- **Rule 3**: Never mix half-width and full-width punctuation within the same language document. Always verify that paired punctuation marks (colons, quotation marks, parentheses) use matching characters on both sides.

---

## 8. Currency Symbol Standards

### Rules
- **Rule 1**: Prefer writing **`Number + Currency Name/Code`** rather than `Currency Symbol + Number` to avoid ambiguity (since symbols like `$` can represent USD, CAD, AUD, or NZD):
  - **Correct**: `10 USD`
  - **Incorrect**: `$10`
- **Rule 2**: Comply with applicable financial and legal regulations when displaying currency symbols.
- **Rule 3**: When a currency symbol is used, place it **immediately before the amount with no space in between**, and **do not append a currency unit word after the amount** (because the symbol itself already represents the unit):
  - **Correct**: `¥1,234.56`
  - **Incorrect**: `¥ 1,234.56`
- **Rule 4**: Avoid repeating currency symbols multiple times within the same sentence or paragraph.

### Recommendations
- **Recommendation 1**: Avoid using currency symbols in headings to preserve visual clarity and readability.
- **Recommendation 2**: When using a currency symbol, prefix it with the ISO 4217 currency code to prevent ambiguity (e.g., `CNY¥100`, `USD$100`).
