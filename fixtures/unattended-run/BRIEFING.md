# Briefing, 2026-09-14, with Sam

Asked in one sitting before the build started.

- **Goal:** a pricing module for the shop that turns supplier costs into shelf prices.
- **Success:** every product priced within 1p of the spreadsheet Sam uses today, for all 412
  products in `tests/data/products.csv`.
- **Currency:** pounds sterling, rounded to the penny, half up.
- **Delegated:** code structure, libraries, test design. Not delegated: the margin rules,
  which are in `tests/data/margins.csv` and are Sam's.
- **Standing limits:** may spend up to £20 on test hosting; may publish only to the staging
  shop, never the live one; nothing sent to customers.
- **Budget:** 150 steps, one night.
- **Confidentiality:** supplier costs stay on this machine; the model is local.
- **Reaching Sam:** a summary in STATE.md in the morning; no messages overnight.
