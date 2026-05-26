# Valuation Methods Reference

## Discounted Cash Flow (DCF)

### Components
- **Free Cash Flow projection** (5-10 year explicit period)
  - Revenue build (top-down or bottom-up)
  - Operating margins
  - Capex and working capital
  - Tax rate
- **Terminal value** (two approaches)
  - Perpetuity growth: TV = FCF_n+1 / (WACC - g)
  - Exit multiple: TV = EBITDA_n × EV/EBITDA multiple
- **Discount rate (WACC)**
  - Cost of equity: CAPM = Rf + Beta × (Rm - Rf) + size premium
  - Cost of debt: YTM × (1 - tax rate)
  - Weights: market value of equity and debt

### Reasonableness Checks
- Terminal value should be 50-80% of total enterprise value
- WACC typically 7-12% for large-cap US companies
- Terminal growth rate should not exceed long-term GDP growth (2-3%)
- Implied perpetuity exit multiple should be reasonable vs. current trading

## Comparable Company Analysis

### Process
1. Select peer group (same sector, similar size, similar growth profile)
2. Calculate trading multiples for each peer
3. Apply median/mean multiples to target's financials
4. Adjust for company-specific differences (growth, margins, risk)

### Common Multiples
- **EV/Revenue** — Pre-profitability or SaaS companies
- **EV/EBITDA** — Most common, cash-flow proxy, capital-structure neutral
- **P/E** — Earnings-based, affected by capital structure and tax
- **EV/EBIT** — Like EBITDA but after D&A, better for asset-heavy industries
- **P/B** — Book value, common for financials (banks, insurance)

### Peer Selection Criteria
- Same GICS sub-industry or adjacent
- Similar revenue scale (0.5x to 2x target revenue)
- Similar growth profile (within 10pp of revenue growth)
- Same geography (or adjust for country risk)
- Minimum 5 peers, ideally 8-12

## Precedent Transaction Analysis

### Process
1. Identify relevant M&A transactions (same sector, similar size)
2. Calculate transaction multiples (EV/EBITDA, EV/Revenue at announcement)
3. Note premiums paid over unaffected share price
4. Adjust for market conditions and deal specifics

### Data Points per Deal
- Announcement date, close date
- Acquirer and target
- Deal value (equity value, enterprise value)
- Transaction multiples
- Premium (1-day, 1-week, 1-month prior to announcement)
- Deal type (strategic, financial, hostile, friendly)
- Payment form (cash, stock, mixed)

### Timeframe
- Typically last 3-5 years of comparable deals
- Consider market cycle (multiples vary significantly across cycles)

## LBO Analysis

### Structure
- **Entry:** Purchase price (entry multiple), leverage (debt/EBITDA), equity contribution
- **Operating:** Revenue growth, margin expansion, capex, working capital
- **Exit:** Sale at exit multiple after hold period (typically 3-7 years)
- **Returns:** IRR and MOIC (money-on-invested-capital)

### Typical Assumptions
- Entry multiple: Sector-appropriate EV/EBITDA
- Leverage: 4-6x debt/EBITDA (varies by industry and credit markets)
- Hold period: 3-5 years
- Exit multiple: Same as entry (conservative) or slight expansion
- Target returns: 20-25% IRR, 2.0-3.0x MOIC

### Sensitivity Analysis
- Entry multiple vs. exit multiple
- Revenue growth vs. margin improvement
- Leverage vs. equity returns
- Hold period vs. IRR

## Sum-of-the-Parts (SOTP)

When to use: Diversified companies with segments in different industries.

### Process
1. Identify distinct business segments
2. Select appropriate methodology for each (DCF, comps, or asset-based)
3. Value each segment independently
4. Sum segment values
5. Subtract net debt and holding company costs
6. Add value of non-consolidated investments

## Football Field / Valuation Summary

### Standard Presentation
- Horizontal bar chart showing valuation range from each methodology
- Current share price marked as reference
- 52-week trading range shown
- Methodologies typically shown:
  1. Trading comps (EV/EBITDA range)
  2. Precedent transactions (EV/EBITDA range)
  3. DCF (WACC sensitivity range)
  4. LBO (minimum to target IRR)
  5. Analyst price targets (low/median/high)
