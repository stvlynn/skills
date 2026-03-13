---
name: atlassian-design
description: Use this skill whenever the user mentions Atlassian Design System, Atlaskit, Jira-style UI, Confluence-style UI, ADS components, design tokens, xcss, @atlaskit/css, primitives, navigation system, or wants to build/refactor React interfaces to match Atlassian patterns. This skill helps choose the right ADS component, combine multiple ADS patterns, and implement code grounded in the mirrored documentation under references/docs.
---

# Atlassian Design

Use this skill to answer implementation and design questions with the mirrored Atlassian Design System docs from `jjcall/ads-docs-mirror`.

## What is bundled

- A full local mirror of the upstream `docs/` directory in `references/docs/`
- A routing guide in `references/index.md`
- Component and pattern docs for layout, forms, navigation, feedback, styling, data display, media, and accessibility-related utilities

## When to reach for this skill

- The user asks which Atlaskit or ADS component fits a UI requirement
- The user wants code using `@atlaskit/*`, `@atlassian/navigation-system`, `@atlaskit/primitives`, `xcss`, or `@atlaskit/css`
- The user wants Jira-like or Confluence-like navigation, layout, forms, or feedback patterns
- The user needs migration guidance around primitives, compiled styling, or token-first CSS
- The user asks for prop names, appearances, installation packages, or examples from Atlassian docs

## Working rules

1. Start by identifying the task type: lookup, component selection, implementation, refactor, or migration.
2. If the right file is not obvious, open `references/index.md` first and route to the smallest relevant set of docs.
3. Read only the docs needed for the current task. For compound tasks, combine a few precise files instead of opening everything.
4. Keep package names, component names, token names, and prop names exact. Do not invent APIs.
5. Treat the mirrored docs as scraped source material. Some files contain malformed headings, duplicated snippets, or noisy formatting. Clean that up before presenting an answer or code sample.
6. Prefer the documented imports and usage patterns shown in the mirror. When examples are verbose, trim them without changing behavior.
7. State clearly when you are inferring beyond the mirror, especially for project setup, bundler config, or version-specific behavior.
8. Respond in the user's language unless the task or surrounding codebase strongly suggests another language.

## Default workflow

1. Map the user's request to one or more components or patterns.
2. Open the relevant files in `references/docs/`.
3. Extract the minimum useful facts:
   - which package to install or import
   - which component or primitive to use
   - which props, appearances, or states matter
   - any styling or layout constraints
4. If the user wants implementation, produce adapted code that fits their app instead of pasting a raw mirror example.
5. If the user wants guidance, explain the recommended component choice and call out nearby alternatives only when the distinction matters.
6. Mention the reference files you used so the answer stays auditable.

## Routing shortcuts

- Styling and tokens: `references/docs/xcss.md`, `references/docs/css.md`, `references/docs/cssReset.md`, `references/docs/focusRing.md`
- Primitives and responsive layout: `references/docs/primitivesOverview.md`, `references/docs/box.md`, `references/docs/inline.md`, `references/docs/stack.md`, `references/docs/flex.md`, `references/docs/grid.md`, `references/docs/responsive.md`
- Application layout and navigation: `references/docs/navigationSystem.md`, `references/docs/atlassianNavigation.md`, `references/docs/topNavigation.md`, `references/docs/sideNavigation.md`, `references/docs/pageLayout.md`, `references/docs/pageHeader.md`
- Forms and input controls: `references/docs/form.md`, `references/docs/textField.md`, `references/docs/textArea.md`, `references/docs/select.md`, `references/docs/checkbox.md`, `references/docs/radio.md`, `references/docs/datePicker.md`, `references/docs/timePicker.md`
- Feedback, overlays, and messaging: `references/docs/modalDialog.md`, `references/docs/drawer.md`, `references/docs/popup.md`, `references/docs/inlineDialog.md`, `references/docs/flag.md`, `references/docs/sectionMessage.md`, `references/docs/tooltip.md`
- Data display and content: `references/docs/table.md`, `references/docs/dynamicTable.md`, `references/docs/tableTree.md`, `references/docs/code.md`, `references/docs/codeBlock.md`, `references/docs/tabs.md`, `references/docs/tag.md`

## Combination patterns

- Form screen: start with `form.md`, then add field-specific docs such as `textField.md`, `select.md`, `checkbox.md`, and action docs such as `button.md`.
- Token-first styling: start with `xcss.md` or `css.md`, then pair with primitives such as `box.md`, `stack.md`, or `inline.md`.
- Product shell: combine `navigationSystem.md` or `atlassianNavigation.md` with `pageLayout.md`, `pageHeader.md`, `breadcrumbs.md`, and menu-related docs.
- Tables or structured content: combine `table.md` or `dynamicTable.md` with status and feedback docs like `badge.md`, `lozenge.md`, `tooltip.md`, or `flag.md`.

## Output expectations

- For implementation tasks, provide concrete code with the correct imports and only the relevant props.
- For design-choice tasks, explain why a component fits and mention tradeoffs if a nearby component could be mistaken for it.
- For migration tasks, call out the relevant styling/runtime boundary, such as `xcss` versus `@atlaskit/css` or compiled primitives versus older patterns.
- For all tasks, prefer precise, doc-grounded answers over generic React advice.
