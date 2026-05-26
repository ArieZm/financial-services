# MCP Data Provider Catalog

## Available Providers

### Daloopa
**URL:** `https://mcp.daloopa.com/server/mcp`
**Capabilities:** Automated financial data extraction from SEC filings, earnings transcripts, and company presentations. Provides structured, auditable data points.
**Best for:** Historical financials, quarterly metrics, KPI extraction from filings
**Key fields:** Revenue, EBITDA, margins, segment data, guidance figures
**Verticals:** All (core financial data)

### FactSet
**URL:** `https://mcp.factset.com/mcp`
**Capabilities:** Comprehensive market data, fundamentals, estimates, ownership, and analytics.
**Best for:** Trading multiples, consensus estimates, ownership data, screening
**Key fields:** EV/EBITDA, P/E, EPS estimates, institutional holdings, index membership
**Verticals:** financial-analysis, investment-banking, equity-research, wealth-management

### S&P Global (Kensho)
**URL:** `https://kfinance.kensho.com/integrations/mcp`
**Capabilities:** Capital IQ data via Kensho — fundamentals, transactions, credit.
**Best for:** Precedent transactions, capital structure, credit ratings, M&A data
**Key fields:** Transaction multiples, deal terms, credit spreads, debt instruments
**Verticals:** investment-banking, private-equity, financial-analysis

### Morningstar
**URL:** `https://mcp.morningstar.com/mcp`
**Capabilities:** Fund data, ETF analytics, portfolio holdings, performance attribution.
**Best for:** Mutual fund/ETF analysis, portfolio construction, style box, performance
**Key fields:** Star rating, expense ratio, category rank, holdings overlap, risk metrics
**Verticals:** wealth-management

### Moody's
**URL:** `https://api.moodys.com/genai-ready-data/m1/mcp`
**Capabilities:** Credit ratings, default probabilities, ESG scores, economic forecasts.
**Best for:** Credit risk assessment, KYC/AML risk data, economic scenarios
**Key fields:** Credit rating, outlook, probability of default, loss given default, ESG score
**Verticals:** operations, fund-admin, investment-banking

### MT Newswires
**URL:** `https://vast-mcp.blueskyapi.com/mtnewswires`
**Capabilities:** Real-time and historical financial news, corporate events, press releases.
**Best for:** News monitoring, event-driven analysis, earnings surprise context
**Key fields:** Headlines, summaries, event types, sentiment, corporate actions
**Verticals:** equity-research, investment-banking

### Aiera
**URL:** `https://mcp-pub.aiera.com`
**Capabilities:** Earnings call transcripts, event scheduling, NLP-derived insights.
**Best for:** Earnings analysis, management commentary extraction, sentiment tracking
**Key fields:** Transcript text, speaker attribution, key quotes, guidance language, tone shifts
**Verticals:** equity-research

### LSEG (London Stock Exchange Group)
**URL:** `https://api.analytics.lseg.com/lfa/mcp`
**Capabilities:** Fixed income analytics, derivatives pricing, FX, swap curves.
**Best for:** Bond relative value, swap pricing, options vol surfaces, FX carry analysis
**Key fields:** Yield curves, OAS, duration, swap rates, implied vol, FX forwards
**Verticals:** financial-analysis (fixed income)

### PitchBook
**URL:** `https://premium.mcp.pitchbook.com/mcp`
**Capabilities:** Private market data — VC/PE deals, valuations, fund performance.
**Best for:** Deal sourcing, comp set for private companies, fundraising data, LP commitments
**Key fields:** Pre/post-money valuation, deal size, investors, fund IRR, TVPI, DPI
**Verticals:** private-equity

### Chronograph
**URL:** (configured per deployment)
**Capabilities:** PE/VC portfolio monitoring, LP reporting, fund accounting.
**Best for:** Portfolio company tracking, NAV calculations, waterfall distributions
**Key fields:** NAV, unrealized value, cash flows, IRR by vintage, fee calculations
**Verticals:** private-equity, fund-admin

### Egnyte
**URL:** (configured per deployment)
**Capabilities:** Enterprise document management, file search, content access.
**Best for:** Accessing client documents, prior work product, templates, deal files
**Key fields:** File metadata, content search, access permissions, version history
**Verticals:** fund-admin, operations

## Provider Selection Guide

| Use Case | Primary | Secondary | Fallback |
|----------|---------|-----------|----------|
| Public company fundamentals | Daloopa | FactSet | SEC EDGAR (web) |
| Trading multiples & valuation | FactSet | S&P Kensho | — |
| M&A precedent transactions | S&P Kensho | PitchBook | — |
| Earnings analysis | Aiera | Daloopa | MT Newswires |
| Credit & risk | Moody's | S&P Kensho | — |
| Private market data | PitchBook | Chronograph | — |
| Fund/ETF analytics | Morningstar | — | — |
| Fixed income & derivatives | LSEG | — | — |
| Real-time news | MT Newswires | — | — |
| Document retrieval | Egnyte | — | — |

## .mcp.json Configuration Pattern

```json
{
  "mcpServers": {
    "provider-name": {
      "type": "http",
      "url": "https://endpoint.example.com/mcp"
    }
  }
}
```

For providers requiring auth headers:
```json
{
  "mcpServers": {
    "provider-name": {
      "type": "http",
      "url": "https://endpoint.example.com/mcp",
      "headers": {
        "Authorization": "Bearer ${PROVIDER_API_KEY}"
      }
    }
  }
}
```
