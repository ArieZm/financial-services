# Output Format Conventions

## Pitch Decks (PowerPoint)

### Standard Sections
1. Cover slide (bank logo, target name, date, confidential watermark)
2. Situation overview (1-2 slides)
3. Company snapshot (business description, key metrics, org chart)
4. Valuation summary — football field chart
5. Trading comps detail (2-3 slides)
6. Precedent transactions detail (1-2 slides)
7. DCF analysis (assumptions + sensitivity)
8. LBO analysis (illustrative, if applicable)
9. Process recommendations
10. Appendix (detailed data tables, methodology notes)

### Formatting Rules
- Every number must trace to a named range in the companion Excel model
- Footnotes on every data slide citing the source and as-of date
- Confidential watermark on every slide
- Date in footer: "Prepared [Month YYYY]"
- Page numbers bottom-right

## CIMs (Confidential Information Memoranda)

### Standard Sections
1. Disclaimer / Forward-Looking Statements
2. Executive Summary
3. Investment Highlights (5-7 bullet points)
4. Company Overview
5. Products & Services
6. Industry Overview & Market Opportunity
7. Financial Overview (historical + projections)
8. Management Team
9. Transaction Summary / Process Overview
10. Appendices

### Formatting Rules
- 30-50 pages typical length
- Professional serif font for body, sans-serif for headers
- All financial tables in consistent format ($ in thousands/millions, clearly labeled)
- Source citations on all market data
- "Draft — Subject to Review" watermark until final

## Research Notes

### Earnings Notes
- Header: Ticker, Company Name, Rating, Price Target, Current Price
- Summary paragraph (2-3 sentences: beat/miss, guidance, our take)
- Key metrics table (revenue, EPS, margins vs. consensus and prior)
- Management commentary highlights (3-5 bullet points with quotes)
- Model changes table (old estimate → new estimate, % change)
- Valuation update (if target changes)
- Risks paragraph

### Initiation Reports
- 20-40 pages
- Investment thesis (1 page executive summary)
- Company overview and history
- Industry analysis and competitive positioning
- Financial model walkthrough (revenue build, margin bridge)
- Valuation (multiple approaches: DCF, comps, sum-of-parts)
- Risk factors
- Appendix: detailed model, management bios, glossary

## Excel Models

### 3-Statement Model
- Tab order: Assumptions, Income Statement, Balance Sheet, Cash Flow, Schedules
- Color coding: Blue = hardcoded input, Black = formula, Green = linked from another tab
- Balance check row on Balance Sheet (Assets − L&E = 0)
- Named ranges for all key assumptions
- Print area set for standard letter/A4

### DCF Model
- Explicit projection period (typically 5-10 years)
- Terminal value via both perpetuity growth and exit multiple
- WACC build-up with source citations
- Sensitivity tables (WACC × terminal growth, WACC × exit multiple)
- Implied share price calculation

### LBO Model
- Sources & Uses table
- Operating model (revenue build, EBITDA margins)
- Debt schedule with mandatory/optional repayment
- Returns analysis (IRR, MOIC) at multiple exit years and multiples
- Sensitivity: entry multiple × exit multiple, leverage × growth

## LP Statements

### Quarterly Statement
- Fund summary (committed capital, called, distributed, NAV)
- Performance table (since inception IRR, TVPI, DPI, RVPI)
- Portfolio company detail (name, industry, cost, fair value, multiple)
- Cash flow waterfall (contributions, distributions, net)
- Fee summary (management fee, expenses, carry accrual)

### Annual Report
- All quarterly statement content plus:
- Market commentary
- Portfolio company operational updates
- Valuation methodology disclosure
- Auditor reference

## Reconciliation Reports

### GL Reconciliation
- Header: Entity, Account, Period, Preparer, Reviewer
- Opening balance (from prior period close)
- Activity detail (line-by-line with posting reference)
- Adjustments (with explanation and approval reference)
- Closing balance
- Variance to sub-ledger/counterparty
- Break identification (unmatched items flagged)
- Sign-off section
