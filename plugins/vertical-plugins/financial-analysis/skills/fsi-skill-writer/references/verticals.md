# Financial Services Verticals

## Vertical → Skills Map

### financial-analysis (Core)
**Purpose:** Cross-cutting financial modeling and analysis tools used by all verticals.
**Skills:** dcf-model, comps-analysis, lbo-model, 3-statement-model, xlsx-author, pptx-author, deck-refresh, ppt-template-creator, audit-xls, ib-check-deck, clean-data-xls, competitive-analysis
**Typical outputs:** Excel workbooks, PowerPoint decks, data tables
**Primary MCP sources:** Daloopa, FactSet, S&P Kensho

### investment-banking
**Purpose:** Deal execution, pitching, and client advisory workflows.
**Skills:** cim-writer, teaser-drafting, deal-tracker, merger-model, sector-overview
**Typical outputs:** CIMs, teasers, pitch decks, process letters, merger models
**Primary MCP sources:** FactSet, PitchBook, Daloopa
**Regulatory context:** SEC M&A disclosure, FINRA communications, insider trading walls

### equity-research
**Purpose:** Research production — initiations, earnings notes, model updates.
**Skills:** earnings-note, initiation-report, model-update, mosaic-builder
**Typical outputs:** Research notes (PDF/Word), earnings models (Excel), price target updates
**Primary MCP sources:** Aiera (transcripts), Daloopa (financials), S&P Kensho, MT Newswires
**Regulatory context:** Reg AC (analyst certification), research independence, FINRA 2241

### private-equity
**Purpose:** Deal sourcing, screening, due diligence, IC memo preparation.
**Skills:** deal-sourcer, screening-model, dd-checklist, ic-memo-writer
**Typical outputs:** IC memos, screening scorecards, DD checklists, investment summaries
**Primary MCP sources:** PitchBook, Chronograph, Daloopa
**Regulatory context:** ILPA guidelines, LP reporting standards, Form ADV

### wealth-management
**Purpose:** Client advisory, financial planning, portfolio analysis.
**Skills:** client-review, financial-plan, portfolio-rebalancer, client-report
**Typical outputs:** Client presentations, financial plans, portfolio reports, rebalancing recommendations
**Primary MCP sources:** Morningstar, FactSet
**Regulatory context:** Reg BI (best interest), Form CRS, suitability (FINRA 2111)

### fund-admin
**Purpose:** Back-office operations — NAV, reconciliation, reporting.
**Skills:** gl-reconciler, break-tracer, accrual-engine, roll-forward, nav-tieout, variance-commentary
**Typical outputs:** Reconciliation reports, accrual schedules, NAV packages, LP statements
**Primary MCP sources:** Egnyte (documents), internal GL systems
**Regulatory context:** AICPA SOC reporting, ILPA fee reporting, GIPS performance standards

### operations
**Purpose:** Operational compliance workflows.
**Skills:** kyc-parser, sanctions-screener, onboarding-checklist
**Typical outputs:** KYC packets, sanctions reports, onboarding status trackers
**Primary MCP sources:** Moody's (risk data), internal document stores
**Regulatory context:** BSA/AML, OFAC sanctions, CDD Rule (31 CFR 1010.230), CIP requirements

## Adding a New Vertical

When creating a skill for a new vertical (e.g., insurance, commodities, crypto):

1. Create `plugins/vertical-plugins/<vertical-name>/`
2. Add `.claude-plugin/plugin.json` with name, version, description, author
3. Add `.mcp.json` with relevant data providers
4. Add `skills/` directory with at least one skill
5. Register in `.claude-plugin/marketplace.json` at the repo root
6. Update this file with the new vertical's entry
