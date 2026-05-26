---
name: fsi-skill-writer
description: |
  Create new financial-services skills with proper SKILL.md structure, MCP data-provider wiring, and domain-accurate instructions. Use this skill whenever someone wants to build a new skill for any financial vertical — investment banking, equity research, private equity, wealth management, fund administration, operations, or a new vertical entirely. Also use when adapting an existing skill template for a different financial domain, or when writing a skill that needs to reference market data providers, financial models, or regulatory frameworks.
---

# FSI Skill Writer

You create production-quality SKILL.md files for the Claude financial-services plugin ecosystem. Every skill you produce follows the Agent Skills standard (agentskills.io), fits the conventions of this repository, and embeds the financial domain knowledge needed for accurate outputs.

## Workflow

### 1. Scope the Skill

Before writing anything, establish:

- **Vertical:** Which vertical plugin does this skill belong to? Read `references/verticals.md` for the full map. If it spans verticals, pick the primary one and note cross-references.
- **Intent:** What specific task does this skill automate? Be precise — "build a DCF model" not "do financial analysis."
- **Inputs:** What does the user provide? (ticker, filing, spreadsheet, natural language request)
- **Outputs:** What artifact does the skill produce? (Excel workbook, slide deck, memo, structured data)
- **Data sources:** Which MCP providers are needed? Read `references/mcp-providers.md` for the full catalog. Default to MCP sources over web search.
- **Regulatory context:** Are there compliance considerations? Read `references/regulatory-frameworks.md` if the skill touches regulated workflows.

### 2. Write the SKILL.md

Follow this structure exactly:

```markdown
---
name: skill-slug-here
description: |
  One paragraph explaining what the skill does and when to trigger it.
  Be "pushy" — list specific user phrases and contexts that should activate this skill.
  Include both "perfect for" and "not ideal for" guidance.
---

# Skill Title

## Data Source Priority (if skill uses market data)

1. MCP data sources (list specific ones)
2. Fallback sources
3. What to do if no data is available

## What You Produce

Describe the output artifact(s) clearly.

## Step-by-Step Process

Numbered steps the agent follows. Each step should be specific enough to execute without ambiguity.

## Guardrails

- Cite every number
- Flag unsourced data as [UNSOURCED]
- Stop and surface for review at key checkpoints

## Output Format

Exact structure of the deliverable.
```

### 3. Write the Description

The description is the most important part — it controls when the skill triggers. Follow these rules:

- **Lead with the action:** "Build institutional-grade..." not "A skill for building..."
- **List trigger contexts:** "Use when...", "Perfect for...", "Invoke when the user mentions..."
- **Be pushy:** Claude under-triggers skills by default. Explicitly list phrases and scenarios.
- **Include negative triggers:** "Not ideal for..." helps prevent mis-triggers.

### 4. Create Bundled Resources

Depending on complexity, create:

- `references/` — Domain documentation the skill loads on demand (methodology guides, field mappings, regulatory checklists)
- `scripts/` — Deterministic helper scripts (validation, data transformation, template generation)
- `templates/` — Starter files for output artifacts (Excel templates, slide templates)
- `assets/` — Static resources (logos, style configs)

### 5. Wire MCP Providers

If the skill needs market data, create or update `.mcp.json` references. Use the provider catalog in `references/mcp-providers.md` to select the right sources:

| Need | Primary Provider | Fallback |
|------|-----------------|----------|
| Fundamentals & filings | Daloopa, FactSet | SEC EDGAR |
| Trading data & multiples | S&P Kensho, FactSet | Bloomberg |
| Credit ratings & risk | Moody's | S&P Global |
| Earnings calls & events | Aiera | MT Newswires |
| PE/VC deal data | PitchBook, Chronograph | — |
| Fixed income & derivatives | LSEG | — |

### 6. Generate Initial Evals

Every skill ships with eval test cases. Create `evals/evals.json`:

```json
[
  {
    "prompt": "Realistic user prompt that exercises the skill",
    "expected_behavior": "What a correct output looks like",
    "assertions": [
      "Specific, objectively verifiable check #1",
      "Specific, objectively verifiable check #2"
    ]
  }
]
```

Write 2-3 test cases covering:
- **Happy path:** Standard use case with good data
- **Edge case:** Missing data, unusual inputs, or boundary conditions
- **Domain-specific:** Financial accuracy checks (balances tie, rates reasonable, regulatory fields present)

### 7. Validate

Run the validation script to check your SKILL.md:

```bash
python3 scripts/validate_skill_md.py path/to/SKILL.md
```

Checks: frontmatter present and valid, name is lowercase-hyphenated, description is non-empty and includes trigger language.

## Financial Domain Reference

When writing skills, load these references as needed:

- `references/verticals.md` — Maps each vertical to its skills, data sources, and output types
- `references/mcp-providers.md` — Full MCP provider catalog with endpoints, capabilities, and field mappings
- `references/regulatory-frameworks.md` — Regulatory requirements by jurisdiction and workflow type
- `references/output-formats.md` — Standard output format conventions for pitch decks, CIMs, research notes, LP statements, models

## Quality Checklist

Before delivering a skill, verify:

- [ ] Frontmatter has `name` and `description`
- [ ] Description is pushy with explicit trigger contexts
- [ ] Data source priority section present (if skill uses data)
- [ ] Steps are numbered and specific
- [ ] Guardrails section present
- [ ] Output format clearly defined
- [ ] MCP providers correctly referenced
- [ ] At least 2 eval test cases created
- [ ] No hardcoded API keys or credentials
- [ ] No PII in examples
