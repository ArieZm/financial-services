---
description: Screen for undervalued growth stocks using GARP (Growth at a Reasonable Price) methodology
argument-hint: "[criteria, e.g. 'midcap tech PEG<1.5' or 'small cap healthcare accelerating revenue']"
---

Load the `garp-screener` skill and run a 5-stage GARP screen to find stocks where strong growth fundamentals are not yet reflected in the stock price.

If criteria are provided, use them to define the universe and adjust thresholds. Otherwise ask the user for:
- Market cap range (small, mid, large, or all)
- Sector preference (specific sector or cross-sector)
- Geography (US, international, or global)
- Any additional filters (minimum growth rate, maximum PEG, specific themes)

Chain to `comps-analysis` and `dcf-model` skills for deep dives on top candidates. Use `thesis-tracker` to formalize investment theses on highest-conviction ideas.
