---
name: credit-analysis
description: |
  Build institutional-grade credit analyses: credit memos, covenant reviews, debt capacity assessments, and credit risk scorecards in Excel/spreadsheet and Word/memo format.

  **Perfect for:**
  - Credit memos for leveraged finance transactions (new issuance, refinancing, amendments)
  - Covenant compliance analysis and early-warning monitoring
  - Debt capacity and leverage analysis for M&A or recapitalization
  - Credit risk assessment for counterparty or portfolio exposure
  - Leveraged buyout debt structuring (sizing the capital structure)
  - Distressed debt analysis and recovery estimation
  - Bank credit committee presentations

  **Not ideal for:**
  - Equity valuation (use comps-analysis or dcf-model)
  - Consumer/retail credit scoring (FICO, mortgage underwriting)
  - Sovereign credit analysis (different methodology)
  - Simple bond pricing (use LSEG plugin directly)

  Use this skill whenever someone mentions "credit memo", "credit analysis", "covenant", "leverage ratio", "debt capacity", "credit rating", "default risk", "recovery rate", "credit spreads", "debt sizing", "interest coverage", or "credit committee".
---

# Credit Analysis

## Data Source Priority

**ALWAYS follow this data source hierarchy:**

1. **Moody's MCP** — Credit ratings, default probabilities, loss given default, ESG scores, economic forecasts
2. **S&P Kensho MCP** — Capital structure data, credit spreads, debt instruments, transaction history
3. **LSEG MCP** — Bond pricing, yield curves, swap rates, credit default swap spreads, relative value
4. **Daloopa MCP / FactSet MCP** — Historical financials, leverage metrics, cash flow data from filings
5. **SEC EDGAR** — Only if MCP sources are unavailable. Pull 10-K, 10-Q, credit agreements from EDGAR
6. **NEVER use web search as a primary data source** for credit analysis — it lacks the precision and audit trail required for credit decisions

---

## Output Types

This skill produces four types of credit analysis. Determine which the user needs before starting.

### Type 1: Credit Memo
A structured written document for credit committee approval. Word/PDF format.

### Type 2: Credit Scorecard
A quantitative scoring framework in Excel with weighted factors and an overall credit rating.

### Type 3: Covenant Analysis
An Excel workbook tracking covenant compliance with projected headroom and early-warning flags.

### Type 4: Debt Capacity Analysis
An Excel model sizing the maximum debt a company can support at various rating levels.

---

## Type 1: Credit Memo

### Required Sections

#### 1. Executive Summary (1 page max)
- **Recommendation:** Approve / Approve with Conditions / Decline
- **Facility:** Type, amount, tenor, pricing, security
- **Borrower:** Name, industry, ownership (public/PE-backed/family)
- **Purpose:** Acquisition financing, refinancing, working capital, growth capex
- **Key credit strengths** (3-5 bullets)
- **Key credit risks** (3-5 bullets)
- **Rating:** Moody's / S&P / Internal (pull from Moody's MCP)

#### 2. Company Overview
- Business description, market position, competitive dynamics
- Revenue mix by segment, geography, customer concentration
- Management team and track record
- Ownership structure and sponsor history (if PE-backed)

#### 3. Industry Analysis
- Sector outlook, growth drivers, headwinds
- Competitive landscape and barriers to entry
- Cyclicality and sensitivity to macro factors
- Regulatory environment

#### 4. Financial Analysis

**Historical Performance (3-5 years):**

| Metric | FY-2 | FY-1 | FY0 | LTM |
|--------|------|------|-----|-----|
| Revenue | | | | |
| EBITDA | | | | |
| EBITDA Margin | | | | |
| Capex | | | | |
| Free Cash Flow | | | | |
| Total Debt | | | | |
| Net Debt | | | | |
| Total Debt / EBITDA | | | | |
| Net Debt / EBITDA | | | | |
| EBITDA / Interest | | | | |
| (EBITDA - Capex) / Interest | | | | |
| FCF / Total Debt | | | | |

**Pro Forma Capitalization** (for new transactions):

| Tranche | Amount | Rate | Maturity | Security |
|---------|--------|------|----------|----------|
| Revolver | | | | |
| Term Loan A | | | | |
| Term Loan B | | | | |
| Senior Notes | | | | |
| Sub Notes | | | | |
| **Total Debt** | | | | |
| Cash | | | | |
| **Net Debt** | | | | |
| Equity Value | | | | |
| **Total Capitalization** | | | | |

**Projected Performance (3-5 years):**
- Revenue and EBITDA projections with growth assumptions
- Mandatory and optional debt repayment schedule
- Leverage trajectory (total debt/EBITDA declining over time)
- Interest coverage trajectory
- Free cash flow available for debt service

**Checkpoint:** Surface for review after completing the financial analysis. The credit officer confirms the historical data, pro forma capitalization, and projections before proceeding to the qualitative assessment.

#### 5. Credit Strengths & Mitigants
For each strength, explain WHY it supports the credit and cite evidence:
- Market position and competitive moat
- Revenue visibility and contract structure
- Cash flow stability and conversion
- Asset coverage and collateral value
- Sponsor support and equity cushion
- Management quality and track record

#### 6. Credit Risks & Mitigants
For each risk, explain the SEVERITY, LIKELIHOOD, and MITIGANT:
- Customer/revenue concentration
- Industry cyclicality and macro sensitivity
- Execution risk (integration, growth plan, turnaround)
- Leverage and refinancing risk
- Regulatory or litigation exposure
- Key person risk

#### 7. Covenant and Structure Analysis
- Financial covenants: levels, headroom, trajectory
- Reporting requirements
- Restricted payments and debt incurrence baskets
- Change of control provisions
- Cross-default and cross-acceleration provisions

#### 8. Downside / Stress Scenario
- Base case, downside case, severe downside case
- Key assumptions changed in each scenario (revenue decline %, margin compression)
- Leverage and coverage metrics under stress
- Covenant compliance under stress (when do covenants break?)
- Liquidity analysis under stress (revolver availability, cash burn rate)

**Checkpoint:** Surface for review after completing the stress test. The credit officer validates the downside assumptions and covenant break points before finalizing the recommendation.

#### 9. Recommendation
- Restate the recommendation with conditions
- Pricing and structural suggestions
- Monitoring requirements and early-warning triggers
- Required approvals and next steps

### Formatting Standards
- Professional serif font (Times New Roman or Georgia)
- Single-spaced body text, 1.5-spaced between sections
- All financial tables right-aligned with consistent decimal precision
- Blue text for sourced data, black for analysis
- Source citations in footnotes: "Source: Moody's MCP, as of [date]"
- Confidential watermark on every page
- Table of contents for memos >10 pages

---

## Type 2: Credit Scorecard

### Scoring Framework

Build an Excel workbook with weighted credit factors:

#### Quantitative Factors (60% weight)

| Factor | Weight | Score Range | How to Score |
|--------|--------|-------------|--------------|
| **Leverage (Debt/EBITDA)** | 15% | 1-10 | <2x=10, 2-3x=8, 3-4x=6, 4-5x=5, 5-6x=3, >6x=1 |
| **Interest Coverage (EBITDA/Interest)** | 12% | 1-10 | >6x=10, 5-6x=8, 3-5x=6, 2-3x=4, 1-2x=2, <1x=1 |
| **FCF/Debt** | 10% | 1-10 | >20%=10, 15-20%=8, 10-15%=6, 5-10%=4, 0-5%=2, <0%=1 |
| **Revenue Stability** | 8% | 1-10 | Based on YoY variance and contract/recurring % |
| **Margin Stability** | 8% | 1-10 | Based on EBITDA margin variance over 3-5 years |
| **Liquidity** | 7% | 1-10 | (Cash + Revolver) / (Annual Debt Service + Capex) |

#### Qualitative Factors (40% weight)

| Factor | Weight | Score Range | How to Score |
|--------|--------|-------------|--------------|
| **Market Position** | 10% | 1-10 | #1-2 in market=9-10, top 5=7-8, fragmented=4-6 |
| **Industry Outlook** | 8% | 1-10 | Secular growth=9-10, stable=6-7, cyclical=4-5, declining=1-3 |
| **Management Quality** | 7% | 1-10 | Track record, depth, alignment with creditors |
| **Business Diversification** | 5% | 1-10 | Revenue mix, geographic mix, customer concentration |
| **Asset Coverage** | 5% | 1-10 | Tangible assets / debt, collateral quality |
| **Sponsor/Owner Quality** | 5% | 1-10 | For PE-backed: sponsor track record, fund vintage, equity cushion |

#### Rating Mapping

| Weighted Score | Internal Rating | Moody's Equivalent | S&P Equivalent |
|---------------|-----------------|--------------------|--------------------|
| 8.5-10.0 | 1 (Excellent) | Aa3-Aaa | AA- to AAA |
| 7.0-8.4 | 2 (Strong) | A3-A1 | A- to A+ |
| 5.5-6.9 | 3 (Satisfactory) | Baa3-Baa1 | BBB- to BBB+ |
| 4.0-5.4 | 4 (Acceptable) | Ba3-Ba1 | BB- to BB+ |
| 2.5-3.9 | 5 (Watch) | B3-B1 | B- to B+ |
| 1.0-2.4 | 6 (Substandard) | Caa-C | CCC to C |

### Excel Layout
- **Tab 1: Summary** — Company name, date, overall score, rating, key metrics
- **Tab 2: Quantitative Scoring** — Each factor with formula-driven score and evidence
- **Tab 3: Qualitative Scoring** — Each factor with analyst assessment and justification
- **Tab 4: Historical Financials** — Source data feeding the quantitative scores
- **Tab 5: Peer Comparison** — Same scorecard applied to 3-5 comparable credits
- **Tab 6: Score History** — Track rating migration over time (if updating an existing scorecard)

### Formatting
- Score cells use conditional formatting: green (8-10), yellow (5-7), red (1-4)
- Weighted score formulas visible and auditable
- Blue font for inputs, black for formulas
- Each qualitative score cell has a comment with the analyst's rationale

---

## Type 3: Covenant Analysis

### Excel Workbook Structure

**Tab 1: Covenant Summary Dashboard**

| Covenant | Definition | Level | Actual | Cushion | Status |
|----------|-----------|-------|--------|---------|--------|
| Max Total Leverage | Total Debt / LTM EBITDA | ≤ 5.0x | 4.2x | 0.8x | PASS |
| Min Interest Coverage | LTM EBITDA / Interest | ≥ 2.0x | 3.1x | 1.1x | PASS |
| Max Capex | Annual capex limit | ≤ $50M | $42M | $8M | PASS |
| Min Liquidity | Cash + Revolver availability | ≥ $25M | $38M | $13M | PASS |

- Status column uses conditional formatting: green PASS, yellow WARNING (<20% cushion), red BREACH
- Warning threshold: flag when cushion < 20% of the covenant level

**Tab 2: Covenant Projections**

Project covenant metrics quarterly for 8-12 quarters:

| Quarter | EBITDA (LTM) | Total Debt | Leverage | Covenant | Cushion | Status |
|---------|-------------|------------|----------|----------|---------|--------|
| Q1 2026 | | | | ≤ 5.0x | | |
| Q2 2026 | | | | ≤ 4.75x | | |
| ... | | | | (step-down) | | |

Note: Many credit agreements have step-down schedules where covenant levels tighten over time. Read the credit agreement carefully.

**Tab 3: Stress Test**

Apply revenue decline scenarios and show when covenants break:

| Scenario | Revenue Δ | EBITDA Δ | Leverage | Coverage | First Breach |
|----------|----------|---------|----------|----------|--------------|
| Base | 0% | 0% | 4.2x | 3.1x | None |
| Mild (-5% rev) | -5% | -8% | 4.6x | 2.8x | None |
| Moderate (-10%) | -10% | -18% | 5.1x | 2.4x | **Leverage Q3** |
| Severe (-20%) | -20% | -35% | 6.5x | 1.8x | **Both Q2** |

**Tab 4: EBITDA Adjustments**

Credit agreements define "EBITDA" differently than GAAP. Track the adjustments:

| Line Item | Amount | Permitted? | Reference |
|-----------|--------|-----------|-----------|
| GAAP Net Income | | — | — |
| + Interest Expense | | Yes | Section 1.01 |
| + Taxes | | Yes | Section 1.01 |
| + D&A | | Yes | Section 1.01 |
| + Stock-Based Comp | | Yes | Section 1.01 |
| + Non-Recurring Charges | | Capped at X% | Section 1.01 |
| + Cost Savings (Run-Rate) | | Capped / time-limited | Section 1.01 |
| + Pro Forma Acquisition EBITDA | | Yes, with conditions | Section 1.01 |
| **= Adjusted EBITDA** | | | |

**Tab 5: Debt Document Summary**
- Credit agreement date, parties, agent
- Maturity dates by tranche
- Amortization schedule
- Prepayment provisions (call protection, make-whole)
- Restricted payments basket sizes
- Permitted indebtedness baskets
- Change of control triggers

---

## Type 4: Debt Capacity Analysis

### Purpose
Determine the maximum debt a company can support at target credit metrics.

### Excel Workbook Structure

**Tab 1: Capacity Summary**

| Rating Target | Max Leverage | EBITDA | Max Debt | Current Debt | Incremental Capacity |
|--------------|-------------|--------|----------|-------------|---------------------|
| BBB (IG) | 3.0x | $500M | $1,500M | $1,200M | $300M |
| BB+ | 4.0x | $500M | $2,000M | $1,200M | $800M |
| BB | 5.0x | $500M | $2,500M | $1,200M | $1,300M |
| B+ | 6.0x | $500M | $3,000M | $1,200M | $1,800M |

**Tab 2: Cash Flow Capacity**

Work backward from minimum debt service coverage:

```
EBITDA                           $500M
- Cash Taxes                     ($75M)
- Maintenance Capex              ($50M)
- Working Capital Change         ($10M)
= Cash Available for Debt Service $365M

÷ Min DSCR (1.5x)               = Max Annual Debt Service: $243M
- Interest (at assumed rate)      = Max Principal Repayment
→ Implies Max Debt at X% Rate    = $Y
```

**Tab 3: Comparable Leverage**

Pull leverage data for rated peers from Moody's/S&P MCP:

| Peer | Rating | Debt/EBITDA | EBITDA/Interest | Debt/Capital |
|------|--------|-------------|-----------------|--------------|
| | | | | |

Use peer median leverage at each rating level to benchmark capacity.

**Tab 4: Sensitivity Analysis**

Matrix: EBITDA level × interest rate → max debt, with leverage ratio shown:

| | Rate 5% | Rate 6% | Rate 7% | Rate 8% |
|------|---------|---------|---------|---------|
| EBITDA $400M | | | | |
| EBITDA $500M | | | | |
| EBITDA $600M | | | | |

**Tab 5: Optimal Structure**

Recommend a capital structure:

| Tranche | Amount | % of Cap | Rate | Maturity | Rationale |
|---------|--------|----------|------|----------|-----------|
| Revolver | $100M | — | S+175 | 5yr | Liquidity buffer |
| TLA | $500M | 25% | S+200 | 5yr | Amortizing, lower cost |
| TLB | $800M | 40% | S+350 | 7yr | Institutional, bullet |
| Sr Notes | $500M | 25% | 6.5% | 8yr | Diversify lender base |
| Sub Notes | $200M | 10% | 8.0% | 10yr | Junior cushion |

---

## Key Credit Metrics Reference

### Leverage Ratios
- **Total Debt / EBITDA** — Primary leverage metric. <3x = IG quality, 3-5x = BB, 5-7x = B, >7x = stressed
- **Net Debt / EBITDA** — Adjusts for cash on hand. More relevant for cash-rich companies
- **Secured Debt / EBITDA** — Important for senior secured lenders
- **Debt / Total Capitalization** — Shows leverage relative to equity cushion

### Coverage Ratios
- **EBITDA / Interest** — Minimum 2.0x for most credits, >3.0x for IG
- **(EBITDA - Capex) / Interest** — More conservative, adjusts for maintenance capex
- **EBITDA / (Interest + Debt Amortization)** — Fixed charge coverage, captures mandatory repayment
- **FCF / Total Debt** — Repayment capacity. >10% = healthy, <5% = constrained

### Liquidity Metrics
- **Cash + Revolver Availability** — Absolute liquidity
- **Liquidity / Annual Debt Service** — Can the company cover next 12 months?
- **Revolver Utilization** — % drawn. >50% = potential stress signal

### Credit Quality Indicators
- **Revenue Variability** — Standard deviation of YoY revenue growth
- **EBITDA Margin Stability** — Range of margins over cycle
- **Customer Concentration** — Top 10 customers as % of revenue. >30% = risk
- **Capex Flexibility** — Maintenance vs. growth capex split

---

## Guardrails

- **Cite every credit metric.** Source and as-of date for all financial data. Use Moody's MCP for ratings, Daloopa for financials.
- **Flag all assumptions.** Every projected number must state the assumption and rationale.
- **No unsupported ratings.** Internal credit ratings must map to the scoring framework — never assign a rating without showing the work.
- **Stress test everything.** Every credit memo must include at least a base case and downside case. Show when covenants break.
- **Read the credit agreement.** Adjusted EBITDA definitions vary by deal. Never assume standard GAAP EBITDA equals covenant EBITDA.
- **Distinguish secured from unsecured.** Recovery rates differ dramatically by position in the capital structure.
- **Surface for review** after completing the financial analysis section and again after the stress test. The credit officer approves each stage before proceeding.
- **Conservative bias.** When uncertain, use the more conservative assumption. Credit analysis penalizes optimism.

---

## Output Checklist

Before delivering any credit analysis:
- [ ] All financial data cites MCP source or filing reference with as-of date
- [ ] Leverage and coverage ratios calculated correctly and consistently
- [ ] Pro forma capitalization table complete (for new transactions)
- [ ] Stress test shows covenant break points
- [ ] EBITDA adjustments documented and referenced to credit agreement
- [ ] Peer comparison included (3-5 comparable credits)
- [ ] Recommendation clearly stated with conditions
- [ ] Confidential watermark on all pages
- [ ] Excel uses blue/black/green convention; all inputs on Assumptions tab
- [ ] Conditional formatting on covenant status (green/yellow/red)
- [ ] No hardcoded values in formula cells
