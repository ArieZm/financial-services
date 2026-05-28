---
name: garp-screener
description: |
  Growth at a Reasonable Price (GARP) stock screener. Finds undervalued growth stocks — companies where
  financials show strong growth but the stock price hasn't caught up yet. Uses a 5-stage funnel: growth
  filter, value filter, quality filter, catalyst identification, and technical confirmation. Produces a
  ranked shortlist of hidden gems with composite scores and investment theses.

  Triggers on "GARP screen", "undervalued growth stocks", "hidden gems", "growth at reasonable price",
  "find undervalued growth", "stocks about to break out", "value growth stocks", "cheap growth stocks",
  "price hasn't caught up", "stock didn't catch up to growth", or "screen for growth at a discount".
---

# GARP Screener — Growth at a Reasonable Price

## What Is GARP Screening?

GARP (Growth at a Reasonable Price) is an investment strategy that finds the sweet spot between growth investing and value investing. The core idea:

**Find companies that are growing fast, but whose stock price has not yet caught up to the company's improving fundamentals.**

These are "hidden gems" — stocks where the business is getting better quarter after quarter (revenue accelerating, margins expanding, cash flow growing), but the market either hasn't noticed or is still pricing in old fears. When the market finally recognizes the improvement, the stock re-rates upward — often sharply.

### Why This Works

1. **Institutional neglect**: Small-to-mid cap stocks with <10 analysts covering them get less attention. Price discovery is slower.
2. **Sentiment lag**: After a stock has been beaten down, investors are slow to return even when fundamentals improve. The narrative takes time to shift.
3. **Earnings surprise cycle**: Companies with accelerating growth tend to beat estimates repeatedly. Each beat forces upward revisions, creating a sustained re-rating.
4. **Compounding at a discount**: Buying growth cheaply means you get the compounding effect of a growth stock at the multiple of a value stock. When the multiple expands AND earnings grow, returns multiply.

### The GARP Advantage Over Pure Value or Pure Growth

- **Pure value** buys cheap stocks, but many are cheap for a reason (declining business, structural headwinds). These are "value traps."
- **Pure growth** buys fast growers, but often at extreme multiples. Any stumble and the stock crashes 30-50%.
- **GARP** requires BOTH: the company must be growing meaningfully AND the stock must be cheap relative to that growth. This double requirement filters out value traps (no growth) and overpriced momentum stocks (no value).

---

## The 5-Stage Screening Process

The GARP screen is a funnel. Each stage eliminates stocks that don't qualify, narrowing from the full universe down to a shortlist of 5-15 actionable ideas.

```
Universe (~5,000+ stocks)
    │
    ▼ Stage 1: Growth Filter
  (~500 pass)
    │
    ▼ Stage 2: Value Filter
  (~100 pass)
    │
    ▼ Stage 3: Quality Filter
  (~30-50 pass)
    │
    ▼ Stage 4: Catalyst Identification
  (~10-20 with catalysts)
    │
    ▼ Stage 5: Technical Confirmation
  (~5-15 actionable ideas)
```

---

### Stage 1: Growth Filter — Is the Company Growing Fast?

The first cut eliminates companies that are not demonstrating strong growth. A GARP candidate must show that the business is expanding meaningfully.

#### Metrics

**1. Revenue Growth (Year-over-Year)**

- **What it is**: The percentage increase in total sales compared to the same period last year.
- **Formula**: `(Current Period Revenue - Prior Year Revenue) / Prior Year Revenue × 100`
- **What "good" looks like**: >15% YoY. This means the company is meaningfully expanding its top line, outpacing GDP and most industries.
- **What "bad" looks like**: <5% for a supposed "growth" stock, or negative growth. If revenue is flat or declining, this is not a GARP candidate.
- **Common pitfall**: One-time revenue spikes from acquisitions, contract wins, or accounting changes can inflate this. Always check organic growth (excluding acquisitions) and whether the growth is recurring vs. one-time.
- **Example**: Company A had $500M revenue last year and $600M this year. Revenue growth = ($600M - $500M) / $500M = 20%. This passes the >15% threshold.

**2. Revenue Acceleration**

- **What it is**: Whether the growth rate itself is increasing — the "second derivative" of revenue. A company growing 10% → 12% → 15% is accelerating; one growing 20% → 15% → 12% is decelerating.
- **Formula**: `Current Quarter YoY Growth % - Prior Quarter YoY Growth %`
- **What "good" looks like**: Positive. The growth rate is increasing, which means the company is gaining momentum. This is the single strongest predictor of future stock outperformance.
- **What "bad" looks like**: Negative (decelerating). Even if absolute growth is still high, deceleration often signals the stock is about to underperform.
- **Common pitfall**: Tough prior-year comparables can make acceleration look bad even if the business is doing well. Look at multi-quarter trends, not single quarters.
- **Example**: Q1 growth was 18%, Q2 was 20%, Q3 was 23%. The growth rate is accelerating by +2-3 percentage points per quarter. Strong signal.

**3. EPS Growth (Year-over-Year)**

- **What it is**: The percentage increase in earnings per share. This measures whether profitability is growing on a per-share basis.
- **Formula**: `(Current EPS - Prior Year EPS) / |Prior Year EPS| × 100`
- **What "good" looks like**: >20% YoY. Earnings are scaling faster than revenue, which signals operating leverage.
- **What "bad" looks like**: Negative or lagging revenue growth. If revenue grows 20% but EPS grows only 5%, something is eating the margin (rising costs, dilution, etc.).
- **Common pitfall**: EPS can be manipulated through share buybacks (fewer shares = higher EPS even without earnings growth). Always check total net income alongside EPS. Also watch for one-time items inflating EPS.
- **Example**: EPS was $2.00 last year and $2.50 this year. Growth = ($2.50 - $2.00) / $2.00 = 25%. Passes the >20% threshold.

**4. EBITDA Growth**

- **What it is**: Growth in Earnings Before Interest, Taxes, Depreciation, and Amortization — a proxy for operating cash generation before capital structure and accounting effects.
- **Formula**: `(Current EBITDA - Prior Year EBITDA) / Prior Year EBITDA × 100`
- **What "good" looks like**: >15% YoY. Operating cash earnings are expanding.
- **What "bad" looks like**: Declining EBITDA while revenue grows. This means the company is spending more to grow — a red flag.
- **Common pitfall**: EBITDA ignores stock-based compensation (SBC). For tech companies with heavy SBC, EBITDA can look great while real cash flow is poor. Check SBC as a percentage of revenue.
- **Example**: EBITDA was $100M last year and $120M this year. Growth = 20%. Good.

**5. Free Cash Flow Growth**

- **What it is**: Growth in the actual cash the business generates after all operating expenses and capital expenditures.
- **Formula**: `FCF = Operating Cash Flow - Capital Expenditures`. Then: `(Current FCF - Prior Year FCF) / |Prior Year FCF| × 100`
- **What "good" looks like**: >10% YoY. Real cash is growing. This is the hardest metric to manipulate.
- **What "bad" looks like**: Negative FCF or declining FCF while EBITDA grows. This means "earnings" aren't translating to actual cash — a major warning sign.
- **Common pitfall**: FCF can be lumpy due to working capital swings and CapEx timing. Look at trailing 12-month (LTM) FCF to smooth seasonality.
- **Example**: LTM FCF was $80M last year and $95M now. Growth = 18.75%. Passes.

**6. Gross Margin Expansion**

- **What it is**: Whether the company's gross profit as a percentage of revenue is improving over time. Expanding gross margins signal pricing power or cost efficiency.
- **Formula**: `Gross Margin = (Revenue - COGS) / Revenue × 100`. Look at the change: `Current Gross Margin - Prior Year Gross Margin`
- **What "good" looks like**: Expanding by 50+ basis points per year (0.5 percentage points). A company going from 42% to 43% gross margin shows improving unit economics.
- **What "bad" looks like**: Compressing gross margins, especially if revenue is growing. This often means the company is cutting prices to drive growth — unsustainable.
- **Common pitfall**: Product mix changes can affect gross margins without reflecting underlying economics. A shift toward lower-margin products can mask improving margins in the core business.
- **Example**: Gross margin was 45.0% last year, now 46.2%. Expansion of 120 basis points. Strong signal.

**7. EBITDA Margin Expansion**

- **What it is**: Whether operating profitability as a percentage of revenue is improving. This reflects operating leverage — the company is growing revenue faster than expenses.
- **Formula**: `EBITDA Margin = EBITDA / Revenue × 100`. Look at the change over time.
- **What "good" looks like**: Expanding. Any improvement signals operating leverage kicking in.
- **What "bad" looks like**: Flat or compressing despite revenue growth. The company lacks pricing power or cost discipline.
- **Common pitfall**: One-time cost reductions can create temporary margin expansion that doesn't sustain.
- **Example**: EBITDA margin went from 18% to 21% in two years. The company is scaling efficiently.

**8. Net Revenue Retention (SaaS/Subscription Only)**

- **What it is**: For subscription businesses, this measures how much revenue a cohort of existing customers generates over time, including upsells, downgrades, and churn.
- **Formula**: `NRR = (Starting Revenue from Cohort + Expansion - Contraction - Churn) / Starting Revenue from Cohort × 100`
- **What "good" looks like**: >110%. Existing customers are spending more over time. At 120%+ NRR, the company grows even without acquiring a single new customer.
- **What "bad" looks like**: <100% means the company is shrinking from its existing base and must acquire new customers just to stay flat.
- **Common pitfall**: NRR can be high because of price increases rather than genuine expansion. Check if customers are actually using more of the product or just paying more.
- **Example**: A SaaS company has 115% NRR. For every $100 of revenue from existing customers last year, they now generate $115 from the same customers this year.

#### Stage 1 Pass Criteria

A stock passes Stage 1 if it meets **at least 4 of 8** growth metrics:

| # | Metric | Threshold |
|---|--------|-----------|
| 1 | Revenue Growth YoY | >15% |
| 2 | Revenue Acceleration | Positive (growth rate increasing) |
| 3 | EPS Growth YoY | >20% |
| 4 | EBITDA Growth YoY | >15% |
| 5 | FCF Growth YoY | >10% |
| 6 | Gross Margin Expansion | >50 bps/year |
| 7 | EBITDA Margin Expansion | Any positive expansion |
| 8 | Net Revenue Retention | >110% (SaaS only, skip for non-subscription) |

---

### Stage 2: Value Filter — Is the Stock Cheap Relative to Its Growth?

This is where GARP separates from pure growth investing. The company may be growing fast, but if the stock already prices in that growth at 50x earnings, there's no margin of safety. Stage 2 finds the disconnect between growth and price.

#### Metrics

**1. PEG Ratio (THE Key GARP Metric)**

- **What it is**: The Price/Earnings ratio divided by the expected earnings growth rate. Created by Peter Lynch, this is the definitive GARP metric. It answers: "How much am I paying per unit of growth?"
- **Formula**: `PEG = (P/E Ratio) / (Annual EPS Growth Rate %)`
  - Use forward P/E (based on next 12 months' expected EPS) for the numerator
  - Use expected EPS growth rate (analyst consensus or your estimate) for the denominator
- **What "good" looks like**: <1.0 is the classic "undervalued" signal. A PEG of 0.7 means you're paying 70 cents for every dollar of growth. <1.5 is still acceptable.
- **What "bad" looks like**: >2.0 means the stock is expensive even relative to its growth. >3.0 is danger territory.
- **Common pitfall**: PEG breaks down when growth is very low (<5%) or very high (>50%) — the ratio becomes extreme. Also, PEG doesn't account for quality of earnings, balance sheet strength, or sustainability of growth.
- **Example**: Stock trades at 25x forward P/E with expected 30% EPS growth. PEG = 25 / 30 = 0.83. This is below 1.0 — the stock is cheap relative to its growth rate.

**2. Forward P/E Ratio**

- **What it is**: The current stock price divided by the expected earnings per share for the next 12 months (NTM). This is what the market is currently willing to pay for each dollar of future earnings.
- **Formula**: `Forward P/E = Current Stock Price / NTM EPS Estimate`
- **What "good" looks like**: Below the sector median forward P/E. If the tech sector trades at 28x and your stock trades at 18x with similar or better growth, it's undervalued.
- **What "bad" looks like**: Above sector median AND above the stock's own 5-year average forward P/E. The market is pricing in peak expectations.
- **Common pitfall**: Low P/E can be a value trap if earnings are about to decline. Always pair forward P/E with growth metrics from Stage 1.
- **Example**: Stock price is $50, NTM EPS estimate is $3.33. Forward P/E = 15.0x. Sector median is 22x. The stock trades at a 32% discount to peers.

**3. EV/EBITDA**

- **What it is**: Enterprise Value divided by EBITDA. Enterprise Value includes debt and excludes cash, making it capital-structure-neutral. This is the most commonly used valuation multiple in professional investing.
- **Formula**: `EV/EBITDA = (Market Cap + Total Debt - Cash) / LTM EBITDA`
- **What "good" looks like**: Below the sector median AND below the stock's own 5-year average EV/EBITDA. This double test ensures you're buying at a genuine discount.
- **What "bad" looks like**: Significantly above both sector median and own history. The market is pricing in perfection.
- **Common pitfall**: Companies with high depreciation/amortization (asset-heavy businesses) will have much higher EBITDA than EBIT or FCF. EV/EBITDA can make capital-intensive companies look deceptively cheap.
- **Example**: Market cap $2B, net debt $500M, EBITDA $300M. EV = $2.5B. EV/EBITDA = 8.3x. Sector median is 12x. Stock is 31% cheaper than peers.

**4. EV/Revenue**

- **What it is**: Enterprise Value divided by Revenue. Useful for comparing companies with different profitability profiles, especially high-growth companies that aren't yet profitable.
- **Formula**: `EV/Revenue = (Market Cap + Total Debt - Cash) / LTM Revenue`
- **What "good" looks like**: Below peers with similar growth rates. A company growing 25% at 3x EV/Revenue while peers growing 20% trade at 6x EV/Revenue is a clear disconnect.
- **What "bad" looks like**: High EV/Revenue with low margins and decelerating growth. You're paying a premium for revenue that doesn't convert to profit.
- **Common pitfall**: EV/Revenue ignores profitability entirely. A company with 5% margins at 3x EV/Revenue is very different from one with 30% margins at 3x EV/Revenue.
- **Example**: EV is $1.5B, revenue is $500M. EV/Revenue = 3.0x. A peer growing at the same rate trades at 5.5x EV/Revenue. Clear undervaluation.

**5. Free Cash Flow Yield**

- **What it is**: The amount of free cash flow the company generates for each dollar of market capitalization. Think of it as the "cash return" on your investment — the inverse of the price you're paying for cash flow.
- **Formula**: `FCF Yield = LTM Free Cash Flow / Market Cap × 100`
- **What "good" looks like**: >5%. This means for every $100 of market cap, the company generates $5+ in free cash. For a growing company, this is very attractive — you're getting paid to wait for the stock to re-rate.
- **What "bad" looks like**: <2% or negative. Either the stock is expensive relative to its cash generation, or the company isn't generating cash at all.
- **Common pitfall**: FCF can be temporarily elevated by delaying CapEx or drawing down working capital. Look at the multi-year trend, not just one period.
- **Example**: Market cap is $3B, LTM FCF is $210M. FCF yield = 7.0%. Excellent. The company generates strong cash relative to its price.

**6. Price/Book (P/B)**

- **What it is**: The stock price divided by book value per share. Book value = total shareholder equity / shares outstanding. This measures what you're paying relative to the company's net asset value.
- **Formula**: `P/B = Stock Price / (Total Shareholders' Equity / Shares Outstanding)`
- **What "good" looks like**: <1.5x for a growing company. Below 1.0x means the market values the company at less than its liquidation value — extreme undervaluation if the business is healthy.
- **What "bad" looks like**: >5x without extraordinary return on equity to justify it. High P/B only makes sense if ROE is also very high.
- **Common pitfall**: P/B is less meaningful for asset-light businesses (software, services) where most value is in intangibles not on the balance sheet. More useful for financials, industrials, and asset-heavy businesses.
- **Example**: Stock price $40, book value per share $30. P/B = 1.33x. For a company with 18% ROE and 20% revenue growth, this is very cheap.

**7. EV/EBITDA-to-Growth Ratio**

- **What it is**: The enterprise-level equivalent of PEG. Takes the EV/EBITDA multiple and divides by the EBITDA growth rate. Answers: "How much am I paying per unit of operating earnings growth?"
- **Formula**: `EV/EBITDA-to-Growth = (EV/EBITDA) / (EBITDA Growth Rate %)`
- **What "good" looks like**: <1.0. You're paying less than 1x for each percentage point of EBITDA growth. This is a bargain.
- **What "bad" looks like**: >2.0. You're overpaying relative to the growth in operating earnings.
- **Common pitfall**: Same as PEG — breaks down at extreme growth rates. Use as a confirming signal, not a primary screen.
- **Example**: EV/EBITDA is 10x, EBITDA is growing 18%. Ratio = 10/18 = 0.56. Below 1.0 — very attractive.

**8. Price/Sales (P/S)**

- **What it is**: Market capitalization divided by total revenue. The simplest valuation metric — what are you paying per dollar of sales?
- **Formula**: `P/S = Market Cap / LTM Revenue`
- **What "good" looks like**: Below peers with similar growth and margin profiles. A company with 30% margins at 2x P/S is much cheaper than a peer with 15% margins at 2x P/S.
- **What "bad" looks like**: High P/S with low margins. If a company trades at 8x P/S but has 10% EBITDA margins, the implied EV/EBITDA is 80x — insane.
- **Common pitfall**: P/S ignores profitability. Always combine P/S with margin data to avoid buying unprofitable revenue at a premium.
- **Example**: Market cap $1.2B, revenue $600M. P/S = 2.0x. Peer group average is 4.5x. Stock trades at a 56% discount on revenue.

#### Stage 2 Pass Criteria

A stock passes Stage 2 if it meets **at least 3 of 8** value metrics:

| # | Metric | Threshold |
|---|--------|-----------|
| 1 | PEG Ratio | <1.5 (ideal <1.0) |
| 2 | Forward P/E | Below sector median |
| 3 | EV/EBITDA | Below sector median AND own 5yr average |
| 4 | EV/Revenue | Below peers with similar growth |
| 5 | FCF Yield | >5% |
| 6 | Price/Book | <1.5x (for asset-heavy; skip for asset-light) |
| 7 | EV/EBITDA-to-Growth | <1.0 |
| 8 | Price/Sales | Below peer group median |

---

### Stage 3: Quality Filter — Is It a Good Company, Not a Value Trap?

A stock can be growing fast and look cheap, but if the business quality is poor, you're buying a trap. Stage 3 filters for companies with strong fundamentals, honest accounting, and sustainable competitive advantages.

#### Metrics

**1. Return on Equity (ROE)**

- **What it is**: How much net income the company generates for each dollar of shareholder equity. Measures management's ability to turn investor capital into profits.
- **Formula**: `ROE = Net Income / Average Shareholders' Equity × 100`
- **What "good" looks like**: >15%. The company generates strong returns on the capital invested. Warren Buffett famously targets companies with consistently high ROE.
- **What "bad" looks like**: <10% or declining for 3+ consecutive years. Low ROE means capital is being used inefficiently.
- **Red flag**: Very high ROE (>40%) driven by excessive leverage, not operating performance. Always check if high ROE comes from high margins or high debt.
- **Common pitfall**: ROE can be artificially inflated by share buybacks (which reduce equity) or high debt (which also reduces equity). Look at ROE alongside debt levels.
- **Example**: Net income $150M, average equity $800M. ROE = 18.75%. Consistent at 17-19% for 5 years. This is a high-quality business.

**2. Return on Invested Capital (ROIC)**

- **What it is**: How efficiently the company uses ALL capital (both equity and debt) to generate operating profits. This is the single best measure of business quality.
- **Formula**: `ROIC = NOPAT / Invested Capital × 100` where `NOPAT = EBIT × (1 - Tax Rate)` and `Invested Capital = Total Equity + Total Debt - Cash`
- **What "good" looks like**: >12% and ideally above the company's WACC (weighted average cost of capital). If ROIC > WACC, every dollar invested creates value.
- **What "bad" looks like**: Below WACC. The company is destroying value with every dollar it invests. This is a fundamental red flag.
- **Common pitfall**: ROIC can vary wildly by industry. Capital-light software companies may have 30%+ ROIC, while asset-heavy industrials may be excellent at 12%. Compare within the same industry.
- **Example**: NOPAT $200M, invested capital $1.2B. ROIC = 16.7%. WACC is 10%. The company creates 6.7 cents of value for every dollar invested. Excellent.

**3. Gross Margin**

- **What it is**: The percentage of revenue remaining after subtracting the direct costs of producing goods/services. Reflects pricing power and cost efficiency at the product level.
- **Formula**: `Gross Margin = (Revenue - Cost of Goods Sold) / Revenue × 100`
- **What "good" looks like**: >40% for most industries. >70% for software. Indicates strong pricing power — customers are willing to pay a significant premium over cost.
- **What "bad" looks like**: Below industry average or compressing without a clear strategic reason (like entering a new market with initial losses).
- **Red flag**: Gross margin compressing while revenue grows often means the company is cutting prices to buy growth — unsustainable.
- **Common pitfall**: Gross margin definitions vary by company. Some include depreciation in COGS, others don't. Ensure you're comparing apples to apples across peers.
- **Example**: Revenue $500M, COGS $275M. Gross margin = 45%. Industry average is 38%. The company has above-average pricing power.

**4. Free Cash Flow Conversion**

- **What it is**: What percentage of EBITDA actually converts into free cash flow. Measures the "quality" of earnings — is the company turning accounting profits into real cash?
- **Formula**: `FCF Conversion = Free Cash Flow / EBITDA × 100`
- **What "good" looks like**: >70%. Most EBITDA is converting to cash. At 90%+, the company has excellent cash economics.
- **What "bad" looks like**: <50%. More than half of "earnings" are being consumed by CapEx, working capital, or other cash drains. Reported earnings are overstating actual cash generation.
- **Red flag**: FCF conversion declining while EBITDA grows. This often signals rising CapEx needs, working capital bloat, or accounting games.
- **Common pitfall**: Capital-intensive businesses (manufacturing, telco) naturally have lower FCF conversion due to high CapEx. Compare within industry.
- **Example**: EBITDA $200M, FCF $160M. Conversion = 80%. Strong. For every dollar of operating earnings, 80 cents turns into actual cash.

**5. Debt/Equity Ratio**

- **What it is**: Total debt divided by total shareholders' equity. Measures how much the company relies on borrowed money vs. owner capital.
- **Formula**: `D/E = Total Debt / Total Shareholders' Equity`
- **What "good" looks like**: <1.0x. The company has more equity than debt. Conservative capital structure with room to borrow if needed.
- **What "bad" looks like**: >2.0x without clear justification. High leverage amplifies both gains and losses, increasing risk.
- **Red flag**: Debt/Equity rising rapidly (company taking on more and more debt) while growth slows. This can signal desperation.
- **Common pitfall**: Some industries naturally carry more debt (financials, utilities, REITs). A bank with 8x D/E is normal; a tech company at 2x is concerning.
- **Example**: Total debt $400M, equity $600M. D/E = 0.67x. Conservative balance sheet.

**6. Interest Coverage Ratio**

- **What it is**: How many times the company's operating earnings (EBIT) can cover its interest payments. Measures whether the company can comfortably service its debt.
- **Formula**: `Interest Coverage = EBIT / Interest Expense`
- **What "good" looks like**: >5x. The company earns 5x more than it needs to pay interest. Comfortable margin of safety.
- **What "bad" looks like**: <3x. The company is stretching to make interest payments. Below 1.5x is debt stress territory.
- **Red flag**: Interest coverage declining while debt stays flat or increases. Rising interest rates can compress this ratio quickly.
- **Common pitfall**: Variable-rate debt means interest coverage can deteriorate rapidly in a rising rate environment without the company taking on any new debt.
- **Example**: EBIT $250M, interest expense $30M. Coverage = 8.3x. Very comfortable.

**7. Insider Ownership**

- **What it is**: The percentage of outstanding shares owned by company executives and board members. High insider ownership means management's interests are aligned with shareholders.
- **Formula**: `Insider Ownership % = Shares Owned by Insiders / Total Shares Outstanding × 100`
- **What "good" looks like**: >5%. Management has meaningful "skin in the game." They profit when you profit.
- **What "bad" looks like**: <1% for a mid/small cap company. Management has little personal financial stake in the stock price.
- **Red flag**: Insider ownership declining over time through constant selling. If management is selling while telling investors the stock is undervalued, believe their actions, not their words.
- **Common pitfall**: For large caps ($50B+), even 1-2% insider ownership is billions of dollars, so the threshold is less meaningful. This metric matters most for small-to-mid caps.
- **Example**: CEO owns 3.2M shares out of 50M total = 6.4%. CFO owns 500K shares. Board members collectively own 2M shares. Total insider ownership = 11.4%. Excellent alignment.

**8. Insider Buying (Recent)**

- **What it is**: Whether company executives have been purchasing shares on the open market with their own money in the last 90 days. This is the strongest signal of management confidence.
- **What "good" looks like**: Any open-market purchases by CEO, CFO, or board members in the last 90 days. Cluster buying (multiple insiders buying within the same window) is especially bullish.
- **What "bad" looks like**: No insider buying AND significant insider selling during a period where the company claims strong prospects.
- **Red flag**: Insider selling accelerating right after a big earnings beat or positive guidance. If the business is doing so well, why is management cashing out?
- **Common pitfall**: Distinguish between open-market purchases (bullish signal) and option exercises or 10b5-1 plan sales (less meaningful — these are often automated). Focus on discretionary purchases.
- **Example**: CEO purchased 50,000 shares at $45 on the open market on 2026-04-15. CFO purchased 20,000 shares at $44.80 on 2026-04-18. Two insiders buying within 3 days = cluster buying. Very bullish.

**9. Altman Z-Score**

- **What it is**: A formula that predicts the probability of bankruptcy within 2 years. Combines five financial ratios into a single score. Created by Professor Edward Altman in 1968, still widely used.
- **Formula**: `Z = 1.2×(Working Capital/Assets) + 1.4×(Retained Earnings/Assets) + 3.3×(EBIT/Assets) + 0.6×(Market Cap/Total Liabilities) + 1.0×(Revenue/Assets)`
- **What "good" looks like**: >3.0 (safe zone). The company is financially healthy with very low bankruptcy risk.
- **What "bad" looks like**: <1.8 (distress zone). The company has a meaningful probability of financial distress within 2 years. Between 1.8 and 3.0 is the "grey zone."
- **Red flag**: Z-Score declining from safe zone toward grey zone over consecutive quarters.
- **Common pitfall**: The Z-Score was designed for manufacturing companies. It's less reliable for financial companies (banks, insurance) and service businesses. Use as one input, not the sole indicator.
- **Example**: Working Capital/Assets = 0.25, Retained Earnings/Assets = 0.40, EBIT/Assets = 0.15, Market Cap/Liabilities = 2.0, Revenue/Assets = 1.2. Z = 1.2(0.25) + 1.4(0.40) + 3.3(0.15) + 0.6(2.0) + 1.0(1.2) = 0.30 + 0.56 + 0.50 + 1.20 + 1.20 = 3.76. Safe zone.

#### Stage 3 Pass Criteria

A stock passes Stage 3 if it meets **at least 5 of 9** quality metrics:

| # | Metric | Threshold |
|---|--------|-----------|
| 1 | ROE | >15% |
| 2 | ROIC | >12% (and > estimated WACC) |
| 3 | Gross Margin | >40% (industry-adjusted) |
| 4 | FCF Conversion | >70% |
| 5 | Debt/Equity | <1.0x |
| 6 | Interest Coverage | >5x |
| 7 | Insider Ownership | >5% |
| 8 | Insider Buying | Any open-market purchase in 90 days |
| 9 | Altman Z-Score | >3.0 |

---

### Stage 4: Catalyst Identification — What Will Trigger the Re-Rating?

A stock can pass all three fundamental filters and still sit at a low price for years. You need a catalyst — an upcoming event or inflection that will force the market to re-price the stock higher. Without a catalyst, being early is the same as being wrong.

#### Catalyst Types

**1. Earnings Surprise Potential**

Look for conditions that create positive earnings surprises:
- **Low analyst coverage**: <5 analysts covering the stock means less efficient price discovery. When these companies beat estimates, the reaction is often outsized.
- **Wide estimate dispersion**: High spread between the highest and lowest analyst estimates signals uncertainty. Positive resolution of that uncertainty drives big moves.
- **Consensus too low**: If your growth analysis (Stage 1) shows significantly higher growth than consensus expects, the next earnings report is your catalyst.

**2. Margin Inflection**

The company is at a tipping point where margins are about to expand meaningfully:
- Crossing the scale threshold where fixed costs are absorbed and each incremental dollar of revenue drops to the bottom line
- Sunsetting a high-cost product line
- Completion of a major capital investment cycle (CapEx decreasing, FCF increasing)

**3. Product or Market Expansion**

- Major new product launch in next 6 months
- Entering a new geographic market
- Winning a large contract or partnership
- Regulatory approval (FDA, FCC, etc.)

**4. Analyst Coverage Initiation**

- Underfollowed stocks (<5 analysts) where major brokerages are initiating coverage
- When Goldman, Morgan Stanley, or JPMorgan starts covering a stock, institutional capital follows

**5. Index Inclusion**

- Companies approaching the size/liquidity thresholds for index inclusion (S&P 500, Russell 1000, etc.)
- Index inclusion triggers mandatory buying from trillions of dollars in passive funds

**6. Capital Return Programs**

- New or increased share buyback authorization
- Dividend initiation or increase
- These signal management confidence in future cash flow AND reduce share count (boosting EPS)

**7. Management or Strategic Changes**

- New CEO/CFO at an underperforming company
- Strategic review or restructuring announcement
- Activist investor involvement (usually pushes for value creation)

**8. Thematic / Sector Tailwinds**

- Company positioned to benefit from a major theme (AI, reshoring, energy transition, aging demographics)
- Sector rotation: money flowing into the company's sector after underperformance
- Government spending or regulatory changes benefiting the industry

#### Stage 4 Assessment

For each stock that passed Stages 1-3, identify:
- **Primary catalyst**: The most likely event to trigger re-rating (with estimated timing)
- **Secondary catalysts**: Additional potential triggers
- **Anti-catalyst**: What could go wrong / delay the re-rating

Stocks with clear catalysts in the next 3-6 months get priority.

---

### Stage 5: Technical Confirmation — Is It About to Break Out?

Technical analysis doesn't replace fundamental analysis, but it can improve timing. After finding a fundamentally strong, undervalued stock with catalysts, check whether the chart confirms the setup.

#### Signals to Look For

**1. Price Consolidation Near Highs (Coiled Spring)**

The stock has moved up, then consolidated sideways for weeks or months near the highs rather than pulling back significantly. This "basing pattern" shows sellers are exhausted and buyers are absorbing all supply. A breakout above the consolidation range often leads to a fast move higher.

**2. Volume Confirmation**

- Volume increasing on up days and decreasing on down days = accumulation (institutions are buying)
- Volume increasing on down days = distribution (institutions are selling)
- Look for above-average volume on any breakout attempt

**3. Relative Strength**

- Stock outperforming its sector and the broader market over the last 3-6 months
- Relative strength improving even if absolute price is flat = hidden strength (market is weak but this stock holds up)

**4. Moving Average Convergence**

- 50-day moving average crossing above the 200-day moving average ("golden cross") = long-term trend turning positive
- Stock price trading above both the 50-day and 200-day MA = confirmed uptrend

**5. Short Interest Declining**

- Short interest falling from elevated levels means bearish bets are being unwound
- Short covering = forced buying, which adds fuel to any upward move
- Check the "days to cover" ratio (short interest / average daily volume)

#### Stage 5 Assessment

Technical confirmation is a bonus, not a requirement. If a stock passes Stages 1-4 but the chart isn't ideal, it may just need more time. Don't skip a fundamentally strong stock because of one poor technical indicator.

**Ideal GARP setup**: Strong fundamentals (Stages 1-3) + clear catalyst (Stage 4) + constructive chart pattern (Stage 5). When all five align, that's your highest-conviction idea.

---

## The GARP Composite Scoring System

After screening, rank candidates using a weighted composite score:

### Score Components

| Component | Weight | Inputs |
|-----------|--------|--------|
| **Growth Score** | 30% | Revenue growth, EPS growth, revenue acceleration, margin expansion |
| **Value Score** | 30% | PEG ratio, forward P/E discount to sector, FCF yield, EV/EBITDA discount |
| **Quality Score** | 25% | ROE, ROIC, FCF conversion, balance sheet strength (D/E, interest coverage) |
| **Catalyst Score** | 15% | Number of catalysts, timing (sooner = better), strength of primary catalyst |

### Scoring Rubric (0-10 per component)

**Growth Score**:
- 9-10: Revenue >25% + EPS >30% + accelerating + margins expanding
- 7-8: Revenue >20% + EPS >20% + at least 2 other growth signals
- 5-6: Revenue >15% + EPS >15% + mixed signals
- 3-4: Revenue 10-15% + some growth but decelerating
- 1-2: Revenue <10% or growth inconsistent

**Value Score**:
- 9-10: PEG <0.7 + forward P/E >30% below sector + FCF yield >7%
- 7-8: PEG <1.0 + forward P/E >20% below sector + FCF yield >5%
- 5-6: PEG <1.5 + at least 2 value metrics pass
- 3-4: PEG 1.5-2.0 + mixed valuation signals
- 1-2: PEG >2.0 or no clear value case

**Quality Score**:
- 9-10: ROE >20% + ROIC >15% + FCF conversion >80% + D/E <0.5x + insider buying
- 7-8: ROE >15% + ROIC >12% + FCF conversion >70% + clean balance sheet
- 5-6: Most quality metrics pass + no major red flags
- 3-4: Mixed quality + some concerns (high debt or declining margins)
- 1-2: Multiple quality failures + red flags present

**Catalyst Score**:
- 9-10: Clear catalyst in next 1-3 months + high probability + potentially transformative
- 7-8: Catalyst in 3-6 months + multiple supporting catalysts
- 5-6: Catalyst identified but timing uncertain (6-12 months)
- 3-4: Potential catalyst exists but weak or distant
- 1-2: No clear catalyst identified

### Composite Score

`GARP Score = (Growth × 0.30) + (Value × 0.30) + (Quality × 0.25) + (Catalyst × 0.15)`

**Interpretation**:
- **8.0-10.0**: Highest conviction — strong buy candidate
- **6.5-7.9**: High conviction — buy candidate, suitable for a concentrated position
- **5.0-6.4**: Moderate conviction — watchlist, wait for better entry or additional catalyst
- **Below 5.0**: Low conviction — does not pass the GARP screen, revisit later

---

## Red Flags — Avoiding Value Traps

A "value trap" is a stock that looks cheap but stays cheap (or gets cheaper) because the business is fundamentally deteriorating. These are the most dangerous situations because every quantitative screen says "buy" but the qualitative reality is "avoid."

### Critical Red Flags

**1. Revenue Growing but Margins Compressing**

The company is "buying" growth by cutting prices, running promotions, or entering low-margin segments. Revenue goes up but profitability goes down. This is unsustainable — eventually the company has to choose between growth and profits.

*Check*: Compare revenue growth to EBITDA margin trend. If revenue is +20% but EBITDA margin dropped from 25% to 18%, that growth is coming at a high cost.

**2. Positive EBITDA but Negative/Declining Free Cash Flow**

EBITDA looks great on paper, but the company's actual cash flow tells a different story. Common causes: massive CapEx (spending more than depreciation), working capital bloat, or heavy stock-based compensation.

*Check*: FCF conversion ratio (FCF/EBITDA). If <50%, dig deeper. If negative, treat EBITDA as meaningless.

**3. Insider Selling During "Growth Phase"**

Management tells investors the company is growing and the stock is undervalued, but they're personally selling shares. Actions speak louder than earnings calls.

*Check*: SEC Form 4 filings. Look for discretionary open-market sales (not 10b5-1 plan sales or option exercises). Cluster selling by multiple insiders is especially alarming.

**4. Receivables Growing Faster Than Revenue**

Accounts receivable (money owed by customers) growing faster than revenue is a classic sign of "channel stuffing" — shipping product to customers who haven't really demanded it, or extending generous payment terms to pull revenue forward.

*Check*: Days Sales Outstanding (DSO) = (Receivables / Revenue) × 365. If DSO is rising while revenue grows, the growth quality is suspect.

**5. Inventory Buildup**

Inventory growing faster than sales signals that demand isn't matching production. The company may have to take write-downs, cut prices, or slow production — all of which hurt future earnings.

*Check*: Inventory Turnover = COGS / Average Inventory. If turnover is declining (inventory sitting longer), that's a problem.

**6. Accounting Red Flags**

- Frequent changes in accounting methods or estimates
- Auditor changes (especially switching to a smaller firm)
- Restatements of prior period financials
- Large discrepancies between GAAP and non-GAAP earnings
- Growing "other" or "one-time" adjustments that happen every quarter

*Check*: Read the notes to financial statements. Look for a pattern of adjustments that always seem to benefit reported earnings.

**7. Customer Concentration**

If >30% of revenue comes from a single customer, the business is fragile. Losing that customer would be devastating, and the customer has enormous bargaining power.

*Check*: 10-K filing, "Revenue Concentration" or "Major Customers" section.

**8. Stock-Based Compensation (SBC) >15% of Revenue**

Heavy SBC means the company is paying employees in stock rather than cash. While this preserves cash flow, it dilutes existing shareholders. A company with 20% revenue growth but 15% SBC is really growing at 5% for shareholders after dilution.

*Check*: SBC as a percentage of revenue on the cash flow statement. Compare to peers. If it's meaningfully higher, adjust your growth expectations downward.

---

## Workflow — How to Run a GARP Screen

### Using This Repo's Existing Tools

This skill integrates with other skills in the equity-research and financial-analysis plugins:

**Step 1: Initial Screen**

Use the `idea-generation` skill (or `/screen` command) with these GARP-specific criteria:
- Direction: Long
- Style: "Growth at a Reasonable Price" or "GARP"
- Apply Stage 1 growth filters and Stage 2 value filters as quantitative criteria

**Step 2: Fundamental Deep Dive**

For each candidate that passes the initial screen:
- Use the `equity-research` skill (LSEG) to pull consensus estimates, fundamentals, and price history
- Use the `tear-sheet` skill (S&P Global) to generate a comprehensive company profile
- Cross-reference growth metrics from Stage 1 and value metrics from Stage 2

**Step 3: Peer Comparison**

- Use the `comps-analysis` skill to build a comparable company table
- Identify where the candidate sits vs. peers on growth, margins, and multiples
- Quantify the valuation discount to peers

**Step 4: Intrinsic Value**

For top candidates (GARP Score >6.5):
- Use the `dcf-model` skill to build a full DCF with Bear/Base/Bull scenarios
- Calculate implied upside from current price to base-case fair value
- Target candidates with >20% implied upside in the base case

**Step 5: Thesis Formation & Tracking**

- Use the `thesis-tracker` skill to document the investment thesis
- Define key pillars, risks, catalysts, and exit triggers
- Monitor thesis health with ongoing data points

### Standalone Process (Without MCP Data Sources)

If MCP data providers are not available, the process works with publicly available data:

1. **Screen**: Use financial screening websites (e.g., Finviz, Wisesheets, Stock Rover) with the Stage 1 and 2 criteria
2. **Validate**: Pull SEC filings (10-K, 10-Q) from EDGAR to verify growth metrics
3. **Compare**: Build manual peer comparisons using public filing data
4. **Value**: Build a DCF model using the dcf-model skill with manually sourced inputs
5. **Track**: Document the thesis and monitor quarterly

---

## Output Format

### Screening Results Table

For each stock that passes the 5-stage funnel, present:

| Rank | Ticker | Company | GARP Score | Growth | Value | Quality | Catalyst | Key Thesis |
|------|--------|---------|------------|--------|-------|---------|----------|------------|
| 1 | XXXX | Company A | 8.2 | 8.5 | 8.0 | 8.0 | 8.5 | ... |
| 2 | YYYY | Company B | 7.6 | 7.0 | 8.5 | 7.5 | 7.0 | ... |
| ... | ... | ... | ... | ... | ... | ... | ... | ... |

### Per-Stock Summary Card

For each top candidate:

**[Company Name] ([TICKER]) — GARP Score: X.X/10**

| Category | Metric | Value | vs. Peers | Signal |
|----------|--------|-------|-----------|--------|
| Growth | Revenue Growth YoY | XX% | +X pp | Strong |
| Growth | EPS Growth YoY | XX% | +X pp | Strong |
| Growth | Revenue Acceleration | +X pp QoQ | — | Positive |
| Value | PEG Ratio | X.Xx | vs X.Xx median | Undervalued |
| Value | Forward P/E | XX.Xx | XX% below sector | Undervalued |
| Value | FCF Yield | X.X% | vs X.X% median | Attractive |
| Quality | ROE | XX% | Top quartile | Strong |
| Quality | ROIC | XX% | > WACC by X pp | Value creating |
| Quality | FCF Conversion | XX% | vs XX% median | Strong |

**Thesis (3-5 bullets):**
- Why this stock is mispriced (the core disconnect)
- What the market is missing or underappreciating
- Primary catalyst and expected timing
- Estimated upside to fair value (Base case: +XX%, Bull case: +XX%)

**Key Risks:**
- Risk 1: What would make this wrong
- Risk 2: What could delay the re-rating

**Suggested Next Steps:**
- [ ] Build full DCF model (use `/dcf` command)
- [ ] Run comps analysis (use `/comps` command)
- [ ] Track thesis (use `/thesis` command)
- [ ] Set earnings calendar alert for next report

---

## Sector-Specific Adjustments

Different industries require different metric emphasis:

### Technology / Software (SaaS)

**Emphasize**: Revenue growth, NRR, gross margins (>70%), Rule of 40, EV/Revenue
**De-emphasize**: P/B (meaningless for asset-light), Altman Z-Score
**Key GARP signal**: Growing >20% with PEG <1.5 and improving operating margins

### Financials (Banks, Insurance)

**Emphasize**: ROE, ROA, Net Interest Margin, Efficiency Ratio, P/E, P/B
**De-emphasize**: EV/EBITDA (not meaningful), gross margin, FCF conversion
**Key GARP signal**: ROE >15% with P/B <1.5x and growing book value

### Healthcare / Biotech

**Emphasize**: Revenue growth from approved products, R&D pipeline value, gross margins
**De-emphasize**: Current P/E (may be distorted by R&D spend)
**Key GARP signal**: Revenue inflecting from new product launch with multiple still compressed from historical losses

### Industrials / Manufacturing

**Emphasize**: EBITDA margins, ROIC, asset turnover, CapEx efficiency, backlog growth
**De-emphasize**: Revenue growth (cyclical), NRR (not subscription)
**Key GARP signal**: Cycle trough with expanding backlog, margins inflecting, EV/EBITDA at historical lows

### Consumer / Retail

**Emphasize**: Same-store sales growth, gross margins, inventory turnover, e-commerce penetration
**De-emphasize**: CapEx metrics (unless store expansion), NRR
**Key GARP signal**: Revenue accelerating from successful product/brand revitalization at low P/E

### Energy / Materials

**Emphasize**: FCF yield (often very high), production growth, reserve replacement, debt reduction
**De-emphasize**: P/E (volatile earnings), revenue growth (commodity price dependent)
**Key GARP signal**: Trading at deep FCF yield (>8%) with production growing and management returning capital

---

## Important Notes

- GARP screening surfaces candidates, not conclusions. Every screen output requires fundamental deep-dive work using the repo's `equity-research`, `comps-analysis`, and `dcf-model` skills before becoming an investment decision.
- The best GARP ideas often sit at the intersection of growth and value — companies where the market has anchored to an old narrative while the fundamentals have quietly improved.
- Position sizing matters: even the best screen has a hit rate of 40-60%. Size positions to survive being wrong on any single name.
- Time horizon: GARP ideas typically play out over 6-18 months. If a catalyst hasn't materialized in 12 months, revisit the thesis.
- Diversification: run the screen quarterly and maintain 10-20 names on the watchlist. Rotate as theses mature or fail.
- Track performance: maintain a log of every screen output, thesis, and outcome. Over time, you'll learn which metrics and setups produce the best results for your style.
- Markets are adaptive: screens that work today may become crowded tomorrow. The edge is in execution speed, thesis quality, and the discipline to sell when the thesis is fully priced in.
