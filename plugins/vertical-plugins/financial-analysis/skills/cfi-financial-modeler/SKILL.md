---
name: cfi-financial-modeler
description: |
  Build a fully integrated 3-statement financial model following the CFI (Corporate Finance Institute) methodology — structured, step-by-step, with explicit quality checks at each stage. Use this skill whenever someone wants to build a financial model from scratch, create a 3-statement model following best practices, learn financial modeling methodology, or needs a disciplined framework for modeling a company's financials. Also use when someone mentions "CFI", "financial modeling guide", "integrated model", "build a model step by step", or wants to model a company's income statement, balance sheet, and cash flow statement together in Excel.

  **Perfect for:**
  - Building a 3-statement model from SEC filings or annual reports
  - Learning financial modeling with a structured, pedagogical approach
  - Creating models that follow institutional best practices (color coding, circular reference handling, error checks)
  - Preparing models for investment banking, equity research, or corporate finance interviews

  **Not ideal for:**
  - Quick back-of-envelope valuations (use dcf-model instead)
  - Existing model updates (use model-update skill)
  - Sector-specific models with unique drivers (e.g., bank models with NIM, REITs with FFO)
---

# CFI Financial Modeler

Build fully integrated 3-statement financial models following the Corporate Finance Institute methodology. Every model you produce is structured, auditable, and follows institutional best practices.

## Data Source Priority

1. **MCP data sources first** — Use Daloopa MCP for historical financials extraction from SEC filings. Use FactSet or S&P Kensho for consensus estimates and trading data.
2. **SEC EDGAR** — If MCP sources are unavailable, pull 10-K/10-Q filings directly.
3. **Company investor relations** — Annual reports, earnings presentations, guidance.
4. **Flag gaps** — If a data point cannot be sourced, mark it as `[ASSUMPTION]` with your reasoning.

## What You Produce

A single Excel workbook with the following tab structure:

| Tab | Purpose | Color |
|-----|---------|-------|
| **Cover** | Company name, ticker, model date, analyst, version | White |
| **Assumptions** | All hardcoded inputs in one place | Light blue |
| **Income Statement** | Historical + projected P&L | Yellow |
| **Balance Sheet** | Historical + projected B/S | Green |
| **Cash Flow** | Historical + projected CF | Orange |
| **Supporting Schedules** | D&A, working capital, debt | Gray |
| **DCF** | Optional valuation overlay | Purple |
| **Checks** | Balance checks, error flags | Red |

## Step-by-Step Modeling Process

Follow these stages in order. Complete each stage fully before moving to the next. Surface for review at each checkpoint.

### Stage 1: Historical Data Entry

**Objective:** Populate 3-5 years of historical financial data.

1. Pull historical income statement, balance sheet, and cash flow statement from Daloopa MCP or SEC filings
2. Enter data on the **Assumptions** tab with blue font (hardcoded inputs)
3. Link historical columns on the financial statement tabs to the Assumptions tab
4. Verify: historical balance sheet balances (Assets = L + E)

**Checkpoint:** Surface the historical data for review before proceeding.

### Stage 2: Revenue Build

**Objective:** Create a bottoms-up or top-down revenue projection.

1. Analyze historical revenue growth rates and segment breakdown
2. On the **Assumptions** tab, create revenue drivers:
   - **Top-down:** Total revenue growth rate assumptions by year
   - **Bottoms-up:** Units × Price, or Segment revenue × Growth for each segment
3. Project revenue for 3-5 forecast years
4. Link projected revenue to the **Income Statement**

**Quality check:** Revenue growth should decelerate toward long-term GDP growth (2-3%) by the terminal year unless there's a specific thesis.

### Stage 3: Expense Projection

**Objective:** Project operating expenses as % of revenue or absolute amounts.

1. Calculate historical margins: Gross margin, EBITDA margin, EBIT margin
2. On **Assumptions**, set margin assumptions for the forecast period
3. Project COGS, SG&A, R&D, and other operating expenses
4. Link to the **Income Statement**

**Quality check:** Margins should trend consistently — avoid sudden jumps without explicit thesis justification.

### Stage 4: Working Capital Schedule

**Objective:** Project current assets and liabilities to derive changes in working capital.

1. Calculate historical days metrics:
   - Days Sales Outstanding (DSO) = Receivables / Revenue × 365
   - Days Inventory Outstanding (DIO) = Inventory / COGS × 365
   - Days Payable Outstanding (DPO) = Payables / COGS × 365
2. Set forecast assumptions for DSO, DIO, DPO on **Assumptions**
3. Calculate projected receivables, inventory, payables on **Supporting Schedules**
4. Calculate change in net working capital for the **Cash Flow** statement

### Stage 5: Depreciation & Capex Schedule

**Objective:** Project PP&E, depreciation, and capital expenditures.

1. Calculate historical Capex / Revenue ratio and D&A / Prior PP&E ratio
2. Set forecast assumptions on **Assumptions**
3. Build PP&E roll-forward on **Supporting Schedules**:
   - Beginning PP&E + Capex − Depreciation = Ending PP&E
4. Link depreciation to **Income Statement** and capex to **Cash Flow**

### Stage 6: Debt Schedule

**Objective:** Project debt balances, interest expense, and mandatory repayments.

1. Catalog existing debt instruments from the latest filing (term loans, revolver, bonds)
2. Build the debt schedule on **Supporting Schedules**:
   - Beginning balance + draws − repayments = ending balance
   - Interest expense = average balance × interest rate
3. Link interest expense to the **Income Statement**
4. Link debt balances to the **Balance Sheet**

**Circular reference note:** Interest depends on debt, which depends on cash flow, which depends on interest. Handle this with:
- Option A: Use prior-period debt balance for interest calculation (slight simplification, avoids circularity)
- Option B: Enable iterative calculation and use a circular reference toggle on the **Assumptions** tab

Default to Option A unless the user explicitly requests circular references.

### Stage 7: Complete the Income Statement

1. Calculate EBITDA, EBIT, EBT (Earnings Before Tax)
2. Apply the effective tax rate (from historical analysis or statutory rate)
3. Calculate Net Income
4. Calculate EPS (basic and diluted) using share count from **Assumptions**

### Stage 8: Complete the Balance Sheet

1. Link all projected line items:
   - Current assets from working capital schedule
   - PP&E from D&A/capex schedule
   - Debt from debt schedule
   - Retained earnings = prior RE + net income − dividends
2. Cash is the **plug** — derived from the cash flow statement
3. **Balance check:** Assets = Liabilities + Equity on every projected period

### Stage 9: Complete the Cash Flow Statement

1. Start with Net Income
2. Add back non-cash items (D&A, stock-based compensation)
3. Subtract changes in working capital
4. **Cash from Operations** = Net Income + non-cash + working capital changes
5. **Cash from Investing** = −Capex + asset sales
6. **Cash from Financing** = Debt draws − repayments − dividends − buybacks
7. Net change in cash → links back to Balance Sheet cash line

### Stage 10: Build the Checks Tab

1. **Balance check:** Assets − (Liabilities + Equity) = 0 for every period
2. **Cash flow check:** Ending cash on CF = Cash on B/S for every period
3. **Retained earnings check:** RE roll-forward ties
4. **Interest check:** Interest on IS = Interest on debt schedule
5. Display all checks with conditional formatting: green = pass, red = fail

**Checkpoint:** Surface the completed model for review. All checks must pass.

### Stage 11: DCF Valuation (Optional)

If requested, add a DCF overlay:

1. Calculate Unlevered Free Cash Flow from the projection
2. Build WACC (reference the Assumptions tab for beta, risk-free rate, equity risk premium)
3. Calculate terminal value (perpetuity growth method)
4. Discount cash flows to present value
5. Bridge from Enterprise Value to Equity Value to Implied Share Price
6. Build sensitivity table: WACC × Terminal Growth Rate

## Formatting Standards

- **Blue font:** Hardcoded inputs (all on Assumptions tab)
- **Black font:** Formulas
- **Green font:** Links to other tabs
- **Yellow highlight:** Cells requiring user review or override
- **Named ranges:** Every assumption cell gets a named range
- **Number format:** Consistent decimals (revenue in $M with 1 decimal, margins as % with 1 decimal, multiples with 1 decimal)
- **Row 1:** Section headers (frozen)
- **Column A:** Line item labels
- **Column B:** Units indicator ($M, %, x, #)

## Guardrails

- **Cite every data point.** Historical data must reference the MCP source or filing (e.g., "Source: Daloopa, AAPL 10-K FY2025").
- **Flag all assumptions.** Every projected input must be marked `[ASSUMPTION]` with brief rationale.
- **No magic numbers.** Every hardcoded value lives on the Assumptions tab with a named range. Zero hardcodes in formula cells.
- **Balance sheet must balance.** If it doesn't, stop and debug before proceeding. Never force-balance with a plug other than cash.
- **Surface for review** at Stage 1 (historical data) and Stage 10 (completed model) checkpoints.
