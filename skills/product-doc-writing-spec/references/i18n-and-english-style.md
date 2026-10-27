# Internationalization (i18n) and English Style Guide

This reference preserves the complete rules and checklists for internationalized documentation, source-text optimization before translation, English capitalization (Title Caps vs. Sentence caps), UI string translation styles, terminology vs. preferred expressions, and multilingual quality review criteria.

---

## 1. Internationalization Writing Standards

### Rules
- **Rule 1**: Use accurate, industry-standard technical terminology.
- **Rule 2**: Keep terminology strictly consistent throughout the document; never use different terms to describe the same entity or action.
- **Rule 3**: Use common, simple, and neutral words.
- **Rule 4**: Use appropriate verb tenses consistently (prefer the simple present tense for general behaviors and instructions).
- **Rule 5**: Prefer the **active voice** over the passive voice.
- **Rule 6**: **Avoid idioms, slang, colloquialisms, and culture-specific metaphors**, as they translate poorly across languages.
- **Rule 7**: Localize all screenshots, diagrams, and hyperlinks for the target audience.
- **Rule 8**: Localize all examples and code samples (e.g., names, addresses, time zones, endpoints).
- **Rule 9**: **Use `USD` / US dollars uniformly in international documentation** unless specifically documenting a local currency billing rule.
- **Rule 10**: Provide globally accessible contact and support channels.

### Recommendations
- **Recommendation 1**: Account for text expansion across languages when designing UI labels, table columns, and diagram nodes (English text is typically longer than CJK text).
- **Recommendation 2**: Express times in **24-hour format** using Arabic numerals and explicitly state the **time zone and UTC offset** (e.g., `2026-03-15 14:00:00 (UTC+0)`).

---

## 2. Pre-Translation Source Text Checklist

Before submitting source documentation for translation (or when writing source text intended for localization), verify the following items:

| Dimension | Check Item | Guidance / Notes |
| - | - | - |
| **Linguistic Accuracy** | Is a unified glossary established? | Define bilingual mappings for core concepts, technical terms, and abbreviations; spell out abbreviations on first occurrence. |
| **Linguistic Accuracy** | Is terminology consistent throughout? | Never use multiple synonyms for the same concept or action. |
| **Linguistic Accuracy** | Are sentences short and concise? | Split long compound sentences into shorter sentences to reduce ambiguity and translation complexity. |
| **Linguistic Accuracy** | Is the active voice prioritized? | Active voice makes the actor and action explicit. |
| **Linguistic Accuracy** | Are subjects, objects, and logical connectors explicit? | - **Supply omitted subjects/objects**: Source languages often omit subjects or objects; supply them explicitly so translated sentences are complete.<br/>- **Clarify pronoun references**: Replace vague pronouns with explicit nouns and add clear logical conjunctions.<br/>- **Avoid long noun stacks**: Unpack dense clusters of consecutive nouns. |
| **Cultural Adaptability** | Are idioms, slang, and jargon removed? | Replace culture-specific idioms with plain, literal statements. |
| **Cultural Adaptability** | Is space reserved for text expansion? | Reserve sufficient width in headings, tables, and UI containers for longer translated strings. |
| **Global Conventions** | Is currency standardized to `USD`? | Use `USD` uniformly in international docs. |
| **Global Conventions** | Are number, phone, date, and time formats standardized? | Follow international ISO/industry standards for numbers, phone numbers, dates, and times. |
| **Global Conventions** | Are standard SI/international measurement units used? | Use international units (`GB`, `MB`, `ms`, `kbps`) rather than local traditional units. |
| **Inclusive Wording** | Are discriminatory or culturally sensitive terms avoided? | Use inclusive, neutral technical terminology:<br/>- Use **`blocklist` / `allowlist`** instead of `blacklist` / `whitelist`.<br/>- Use **`primary` / `secondary`** (or `main` / `replica`) instead of `master` / `slave`. |

---

## 3. English Capitalization Style Guide

| Category | Specification |
| - | - |
| **General Principles** | Two capitalization styles are used:<br/>1. **Sentence caps**: Only the first letter of the first word in the sentence is capitalized; all other words are lowercase (except proper nouns and acronyms, which follow their own standard capitalization).<br/>2. **Title Caps**: Every lexical/content word in the heading or label has its initial letter capitalized. |
| **Title Caps Rules** | Follow these 9 rules when applying **Title Caps**:<br/>1. **Capitalize** the first letter of all **nouns, verbs, adverbs, adjectives, and pronouns**.<br/>2. **Capitalize the first word and the last word** of the heading regardless of part of speech (unless it is a proper noun with a fixed lowercase initial, such as `iOS Configuration`). Example: `Changed By`.<br/>3. **Capitalize prepositions that belong to a phrasal verb**. Example: `Log In Now`, `Set Up an Instance`.<br/>4. For ordinary prepositions (not part of a phrasal verb): **lowercase prepositions of 4 letters or fewer** (`in`, `on`, `of`, `to`, `for`, `with`, `from`, `into`, `over`); **capitalize prepositions of 5 letters or more** (`Without`, `Between`, `Through`, `During`).<br/>5. **Lowercase articles** (`a`, `an`, `the`). Note: Avoid starting headings with an article in technical documentation.<br/>6. **Lowercase coordinating conjunctions** (`and`, `or`, `but`, `for`, `nor`); capitalize subordinating conjunctions.<br/>7. In **hyphenated compounds**: capitalize the word after the hyphen if it is a noun or has equal status with the first word (`High-Speed Link`, `Client-Server Architecture`); lowercase the word after the hyphen if it merely modifies the first word (`IP-based Configuration`).<br/>8. In **prefixed words**, capitalize only the initial letter of the prefix unless the root word is a proper noun (`Pre-upgrade`, `Multi-region`, `Non-root`).<br/>9. Lowercase `that` when it introduces an appositive clause in a heading (`Message Indicating that...`). |
| **Supplementary Rules** | 1. **Proper nouns & industry terms**: Follow official industry casing (`SaaS`, `HTTPS`, `OAuth 2.0`, `gRPC`).<br/>2. **Captions vs. Table Headers**: Image titles, table titles, figure captions, and table notes use **Sentence caps**. Table headers (both column headers and row headers) use **Title Caps**.<br/>3. **Formulas**: Each independent expression separated by mathematical operators uses **Sentence caps**. Example: `Registration rate = (Number of users registered / Number of users who receive the registration email) × 100%`.<br/>4. **Legal documents**: Key emphasis clauses in SLAs, contracts, or terms of service may use **ALL CAPS**. |

---

## 4. UI String Translation Style Guide

| UI Element Type | Capitalization | Grammatical Structure | English Examples | Notes |
| - | - | - | - | - |
| **Menu** | Title Caps | Noun phrase | `Products` | If a menu item directly triggers an action, treat it like a button (`Verb` or `Verb + Object`). |
| **Navigation Tree** | Title Caps | Noun phrase | `Storage` | — |
| **Page Title** | Title Caps | Noun phrase | `User Management` | — |
| **Tab Title** | Title Caps | Noun phrase | `Servers` | — |
| **Panel / Section Title** | Title Caps | Noun phrase | `Application Management` | — |
| **Modal / Dialog Title** | Title Caps | Noun phrase<br/>Base verb<br/>Base verb + Object | `Warning`<br/>`Disable SSL` | When a dialog opens directly from clicking a button and shares the button's source label, keep the dialog title identical to the button label (`Disable SSL`). |
| **Button** | Title Caps | Base verb<br/>Base verb + Object | `OK`<br/>`Cancel`<br/>`Submit Ticket`<br/>`Add Remarks`<br/>`View Logs` | 1. **Omit articles** (`a`, `an`, `the`).<br/>2. Omit the object if the verb alone is unambiguous.<br/>3. Use a singular object for single-resource actions (`Create Instance`) and a plural object for batch-only actions or idiomatic plurals (`Add Remarks`, `View Logs`). |
| **Field / Parameter Name & Table Header** | Title Caps | Noun phrase (preferred)<br/>Base verb (+ Object) | `Current User`<br/>`Use Proxy` | Applies to form field labels and table column/row headers. |
| **Field / Parameter Value & Table Body Cell** | Sentence caps | Noun phrase<br/>Base verb (+ Object) | `Read-only user`<br/>`Use PC audio when joining a meeting` | Applies to option values, radio/checkbox labels, and non-header table cells. |
| **Dialog / Toast / Error Prompt** | Sentence caps | Complete sentence | `The network is disconnected. Please try again later.` | End complete sentences with a period. |
| **Static Helper Text** | Sentence caps | Complete sentence | `A maximum of 100 users can be added.` | — |
| **Input Placeholder Text** | Sentence caps | Noun phrase or imperative sentence | `Enter a password.` | — |
| **Descriptive Tooltip** | Sentence caps | Noun phrase or complete sentence | `The value must contain letters, digits, and special characters.` | Hover tooltips explaining a field or parameter. |
| **Icon-Only Button Tooltip** | Title Caps | Base verb<br/>Base verb + Object | `Download Certificate` | Hover tooltips naming the action of an unlabeled icon button. |

---

## 5. Terminology vs. Preferred Expressions

### 5.1 Definitions
- **Term**: A noun or noun phrase with a **single, fixed, authoritative meaning** in a technical domain or product context (concepts, product names, brand terms, legal entities). A term must be translated identically everywhere.
- **Preferred Expression**: A **recommended but context-dependent expression** (verbs, adjectives, or multi-translation concepts) used to maintain stylistic consistency.

### 5.2 Formatting and Glossary Entry Rules
1. **Separate Full Name and Abbreviation**:
   - Store the full name (`Virtual Machine`) and abbreviation (`VM`) in separate fields, never combined in one field as `Virtual Machine (VM)`.
   - In body text, spell out **`full name (abbreviation)`** on first mention, and use the abbreviation alone thereafter:
     > An **availability zone (AZ)** refers to a physical data center within a region that has independent power and networking. The service supports instance migration across **AZs** in the same region.
2. **Casing in Glossaries**:
   - Use exact official casing for proper nouns and acronyms (`SaaS`, `PaaS`).
   - Use **all lowercase** for common technical terms (`pay-as-you-go`, `cloud cluster`, `availability zone`) so translators and AI tools can adapt capitalization to sentence position.
3. **Singular Form**: Normalize countable nouns to the **singular form** (`cloud cluster`, not `cloud clusters`), unless the term is always plural (`cluster details`).
4. **No Articles**: Omit leading articles (`a`, `an`, `the`) in glossary entries unless fixed by grammar.
5. **Noun Principle for Terms**: Only standardize **nouns and noun phrases** as glossary terms. Do not enter UI button verbs (`Create Instance`, `Delete`), toast sentences (`Operation successful`), or layout-truncated abbreviations (`Config`, `Req.`, `Pwd`) as terms.

---

## 6. Multilingual Quality Review Checklist

When writing or reviewing English/multilingual technical documentation, check against these 15 items:

1. **Spelling**: No typos (e.g., `September` vs. `Sepetmber`, `field` vs. `feild`).
2. **Spacing**: No missing or double spaces around words, tags, or punctuation.
3. **Punctuation**:
   - Complete sentences (including English error messages) end with a period.
   - **Replace source exclamation marks with periods (`.`) in English**; avoid exclamation marks in technical English.
   - Avoid comma splices (do not join two independent clauses with only a comma; add a conjunction like `, and` or split into two sentences: `Visit the official website, and refer to the FAQs.`).
4. **Capitalization**:
   - Headings, buttons, and table headers follow **Title Caps**.
   - Body sentences, table cells, and captions follow **Sentence caps** (do not randomly capitalize common nouns mid-sentence like `In primary Mode, users can create an Instance`).
5. **Repeated Words**: No accidental duplicate words (`the the`) or redundant acronym expansions (`VM: VM` instead of `VM: Virtual Machine`).
6. **Grammar & Collocation**: Subject-verb agreement, correct articles (`a/an/the`), natural verb-noun collocations (`SSL disabling failed` or `Failed to disable SSL`, never `Close SSL failed`).
7. **Sequential Numbering**: Ordered steps start at `1.` and increment without gaps.
8. **Hyperlinks**: All source links are preserved and point to the localized target URL.
9. **Inline Styling**: Bold (`**`), inline code (`` ` ``), and highlight colors match the source structure.
10. **No Untranslated Source Characters**: No leftover source-language characters or full-width punctuation (e.g., use `1–100 characters` with an en-dash/hyphen, never a full-width tilde) or corrupted HTML entities (`&nbsp;`, `&#10;`).
11. **Inclusive Wording**: Use `blocklist/allowlist` and `primary/secondary`.
12. **No Omissions**: Numbers, units, regions, prices, timestamps, parameter names/values, and CLI commands are completely preserved.
13. **No Mistranslations of Polarity/Values**:
    - Double-check antonyms (`enable/disable`, `greater than/less than`, `maximum/minimum`, `inbound/outbound`).
    - **Discount conversion**: When translating pay-rate discounts (such as "pay 85% of the original price"), convert accurately to the percentage off (**`15% off`** or **`a 15% discount`**, never `85% off`).
    - **Edition vs. Version**: Translate product feature tiers (Basic, Pro, Enterprise) as **`Edition`**, and software release numbers (`v2.1`) as **`Version`**.
    - **Private Network**: Translate cloud internal virtual networking as **`private network`** (not `intranet`).
14. **Variable & Tag Integrity**:
    - Preserve placeholders verbatim (`{{count}}`, `{maxnumber}`).
    - Handle singular/plural nouns after numeric variables (`{{count}} attendee(s) hidden`).
    - Keep XML/JSX tags balanced (`<1>...</1>`) with proper spacing around tags.
15. **Parallel Heading Structure**: Keep sibling headings grammatically parallel (e.g., all gerund phrases `Creating an Instance` / `Viewing an Instance`, or all base-verb phrases `Create an Instance` / `View an Instance`).
