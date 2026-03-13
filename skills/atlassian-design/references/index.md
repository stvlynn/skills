# Atlassian Design Reference Map

This skill mirrors the Markdown docs from `https://github.com/jjcall/ads-docs-mirror/tree/main/docs`.

Use this file to route to the right document quickly. The full mirrored corpus lives in `references/docs/`.

## Notes about the mirror

- The source is a scraped documentation mirror, not the original authoring source.
- Some files contain duplicated code blocks, malformed headings, or formatting noise.
- Prefer component titles, prose, package imports, prop names, and JSX examples. Clean up artifacts before reusing examples.

## Quick routing

### Foundations and styling

- Primitives overview: `docs/primitivesOverview.md`
- Styling systems: `docs/xcss.md`, `docs/css.md`, `docs/cssReset.md`
- Responsive utilities: `docs/responsive.md`, `docs/responsiveBreakpoints.md`, `docs/responsiveHide.md`, `docs/responsiveShow.md`
- Accessibility helpers: `docs/focusRing.md`, `docs/visuallyHidden.md`
- Basic layout building blocks: `docs/box.md`, `docs/inline.md`, `docs/stack.md`, `docs/flex.md`, `docs/grid.md`, `docs/gridColumn.md`, `docs/bleed.md`
- Layout scaffolding: `docs/layout.md`, `docs/layoutGrid.md`, `docs/designGrid.md`, `docs/page.md`, `docs/pageLayout.md`

### Navigation and wayfinding

- Product shell and modern nav: `docs/navigationSystem.md`, `docs/atlassianNavigation.md`
- Legacy/page-level nav: `docs/topNavigation.md`, `docs/sideNavigation.md`, `docs/pageHeader.md`, `docs/breadcrumbs.md`
- Menus and navigation actions: `docs/menu.md`, `docs/dropdownMenu.md`, `docs/dropdownItem.md`, `docs/dropdownItemCheckbox.md`, `docs/dropdownItemRadio.md`, `docs/popup.md`, `docs/popper.md`
- Tabs and paging: `docs/tabs.md`, `docs/pagination.md`

### Actions, forms, and input

- Buttons and actions: `docs/button.md`, `docs/buttonGroup.md`, `docs/iconButton.md`, `docs/linkButton.md`, `docs/linkIconButton.md`, `docs/splitButton.md`, `docs/pressable.md`
- Form wrapper and field composition: `docs/form.md`
- Text input: `docs/textField.md`, `docs/textArea.md`, `docs/inlineEdit.md`, `docs/inlineEditableTextfield.md`
- Selection controls: `docs/checkbox.md`, `docs/checkboxSelect.md`, `docs/radio.md`, `docs/radioGroup.md`, `docs/radioSelect.md`, `docs/toggle.md`, `docs/range.md`
- Select variants: `docs/select.md`, `docs/asyncSelect.md`, `docs/creatableSelect.md`, `docs/asyncCreatableSelect.md`, `docs/popupSelect.md`, `docs/countrySelect.md`
- Date and time: `docs/calendar.md`, `docs/datePicker.md`, `docs/datetimePicker.md`, `docs/timePicker.md`

### Feedback, dialogs, and overlays

- Dialogs and surfaces: `docs/modalDialog.md`, `docs/drawer.md`, `docs/drawerLegacy.md`, `docs/blanket.md`, `docs/portal.md`, `docs/inlineDialog.md`
- Messages and status: `docs/banner.md`, `docs/flag.md`, `docs/autoDismissFlag.md`, `docs/flagGroup.md`, `docs/inlineMessage.md`, `docs/sectionMessage.md`, `docs/tooltip.md`
- Progress and loading: `docs/spinner.md`, `docs/skeleton.md`, `docs/avatarSkeleton.md`, `docs/progressBar.md`, `docs/transparentProgressBar.md`, `docs/successProgressBar.md`, `docs/progressIndicator.md`, `docs/progressTracker.md`
- Spotlight and onboarding: `docs/spotlightCard.md`, `docs/onboardingSpotlight.md`, `docs/benefitsModal.md`

### Data display, content, and identity

- Tables and structured data: `docs/table.md`, `docs/dynamicTable.md`, `docs/tableTree.md`
- Text and code: `docs/text.md`, `docs/heading.md`, `docs/code.md`, `docs/codeBlock.md`, `docs/comment.md`
- Status and labeling: `docs/badge.md`, `docs/lozenge.md`, `docs/tag.md`, `docs/tagGroup.md`
- Media and identity: `docs/avatar.md`, `docs/avatarContent.md`, `docs/avatarGroup.md`, `docs/avatarItem.md`, `docs/image.md`, `docs/icon.md`, `docs/iconLegacy.md`, `docs/customIconLegacy.md`, `docs/customSvg.md`, `docs/iconObject.md`, `docs/iconTile.md`, `docs/logo.md`
- Utility display components: `docs/anchor.md`, `docs/link.md`, `docs/emptyState.md`

## Full file list

- `docs/anchor.md`
- `docs/asyncCreatableSelect.md`
- `docs/asyncSelect.md`
- `docs/atlassianNavigation.md`
- `docs/autoDismissFlag.md`
- `docs/avatar.md`
- `docs/avatarContent.md`
- `docs/avatarGroup.md`
- `docs/avatarItem.md`
- `docs/avatarSkeleton.md`
- `docs/badge.md`
- `docs/banner.md`
- `docs/benefitsModal.md`
- `docs/blanket.md`
- `docs/bleed.md`
- `docs/box.md`
- `docs/breadcrumbs.md`
- `docs/button.md`
- `docs/buttonGroup.md`
- `docs/calendar.md`
- `docs/checkbox.md`
- `docs/checkboxSelect.md`
- `docs/code.md`
- `docs/codeBlock.md`
- `docs/comment.md`
- `docs/countrySelect.md`
- `docs/creatableSelect.md`
- `docs/css.md`
- `docs/cssReset.md`
- `docs/customIconLegacy.md`
- `docs/customSvg.md`
- `docs/datePicker.md`
- `docs/datetimePicker.md`
- `docs/designGrid.md`
- `docs/drawer.md`
- `docs/drawerLegacy.md`
- `docs/dropdownItem.md`
- `docs/dropdownItemCheckbox.md`
- `docs/dropdownItemRadio.md`
- `docs/dropdownMenu.md`
- `docs/dynamicTable.md`
- `docs/emptyState.md`
- `docs/flag.md`
- `docs/flagGroup.md`
- `docs/flagsProvider.md`
- `docs/flex.md`
- `docs/focusRing.md`
- `docs/form.md`
- `docs/grid.md`
- `docs/gridColumn.md`
- `docs/heading.md`
- `docs/icon.md`
- `docs/iconButton.md`
- `docs/iconLegacy.md`
- `docs/iconObject.md`
- `docs/iconTile.md`
- `docs/image.md`
- `docs/inline.md`
- `docs/inlineDialog.md`
- `docs/inlineEdit.md`
- `docs/inlineEditableTextfield.md`
- `docs/inlineMessage.md`
- `docs/layout.md`
- `docs/layoutGrid.md`
- `docs/link.md`
- `docs/linkButton.md`
- `docs/linkIconButton.md`
- `docs/logo.md`
- `docs/lozenge.md`
- `docs/menu.md`
- `docs/modalDialog.md`
- `docs/navigationSystem.md`
- `docs/onboardingSpotlight.md`
- `docs/page.md`
- `docs/pageHeader.md`
- `docs/pageLayout.md`
- `docs/pagination.md`
- `docs/popper.md`
- `docs/popup.md`
- `docs/popupSelect.md`
- `docs/portal.md`
- `docs/pressable.md`
- `docs/primitivesOverview.md`
- `docs/progressBar.md`
- `docs/progressIndicator.md`
- `docs/progressTracker.md`
- `docs/radio.md`
- `docs/radioGroup.md`
- `docs/radioSelect.md`
- `docs/range.md`
- `docs/responsive.md`
- `docs/responsiveBreakpoints.md`
- `docs/responsiveHide.md`
- `docs/responsiveShow.md`
- `docs/sectionMessage.md`
- `docs/select.md`
- `docs/sideNavigation.md`
- `docs/skeleton.md`
- `docs/spinner.md`
- `docs/splitButton.md`
- `docs/spotlightCard.md`
- `docs/stack.md`
- `docs/successProgressBar.md`
- `docs/table.md`
- `docs/tableTree.md`
- `docs/tabs.md`
- `docs/tag.md`
- `docs/tagGroup.md`
- `docs/text.md`
- `docs/textArea.md`
- `docs/textField.md`
- `docs/timePicker.md`
- `docs/toggle.md`
- `docs/tooltip.md`
- `docs/topNavigation.md`
- `docs/transparentProgressBar.md`
- `docs/visuallyHidden.md`
- `docs/xcss.md`
