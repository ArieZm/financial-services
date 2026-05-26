---
name: fsi-plugin-scaffolder
description: |
  Generate complete plugin directory structures for the financial-services ecosystem — agent-plugins, vertical-plugins, or managed-agent cookbooks. Use this skill whenever someone wants to create a new named agent (like pitch-agent), a new vertical plugin (like fund-admin), a new managed-agent cookbook for headless deployment, or needs to scaffold the full file structure for any new financial services plugin. Also use when converting an existing skill set into a standalone agent or when setting up a new vertical from scratch.
---

# FSI Plugin Scaffolder

You generate complete, standards-compliant plugin directory structures for the Claude financial-services ecosystem. You know the exact conventions for three artifact types: agent-plugins, vertical-plugins, and managed-agent cookbooks.

## Artifact Types

### 1. Agent Plugin
A named agent with its own system prompt, bundled skills, and plugin metadata.
**Location:** `plugins/agent-plugins/<agent-slug>/`
**Examples:** pitch-agent, market-researcher, earnings-reviewer

### 2. Vertical Plugin
A domain-specific skill bundle with MCP providers, commands, and multiple skills.
**Location:** `plugins/vertical-plugins/<vertical-slug>/`
**Examples:** financial-analysis, investment-banking, equity-research

### 3. Managed Agent Cookbook
A headless deployment configuration for running an agent via the Managed Agents API.
**Location:** `managed-agent-cookbooks/<agent-slug>/`
**Examples:** pitch-agent/, gl-reconciler/, earnings-reviewer/

## Workflow

### 1. Determine Artifact Type

Ask or infer:
- **Agent plugin** — if the request is for an autonomous, end-to-end workflow agent ("build an agent that does X from start to finish")
- **Vertical plugin** — if the request is for a domain bundle with multiple related skills ("create a plugin for insurance workflows")
- **Managed agent cookbook** — if an agent-plugin already exists and needs headless deployment ("deploy pitch-agent via API")
- **All three** — if building a complete new domain from scratch

### 2. Scaffold the Structure

Generate all required files with correct content. Use the templates in `references/` for each artifact type.

### 3. Wire Connections

- Register new plugins in `.claude-plugin/marketplace.json`
- Set up MCP provider references in `.mcp.json`
- Cross-reference skills between vertical and agent bundles
- Configure `callable_agents` for multi-agent setups

### 4. Validate

Run `python3 scripts/check.py` to ensure the scaffold passes all invariants.

---

## Agent Plugin Structure

```
plugins/agent-plugins/<agent-slug>/
├── .claude-plugin/
│   └── plugin.json
├── agents/
│   └── <agent-slug>.md          # System prompt
└── skills/                       # Bundled copies (synced from verticals)
    ├── <skill-1>/
    │   └── SKILL.md
    └── <skill-2>/
        └── SKILL.md
```

### plugin.json Template

```json
{
  "name": "<agent-slug>",
  "version": "0.1.0",
  "description": "<One-line description of what the agent does end-to-end>",
  "author": {
    "name": "Anthropic FSI"
  }
}
```

### Agent System Prompt Template (agents/<agent-slug>.md)

```markdown
---
name: <agent-slug>
description: <Detailed description with trigger contexts. When to use this agent vs individual skills.>
tools: Read, Write, Edit, mcp__<primary-provider>__*
---

You are the <Agent Name> — <one-line persona description>.

## What you produce

Given <inputs>, you deliver:

1. **<Artifact 1>** — <description with quality standard>
2. **<Artifact 2>** — <description with quality standard>

## Workflow

1. **<Step name>.** <What to do, which skills/tools to invoke.>
2. **<Step name>.** <Next step with clear handoff criteria.>
...

## Guardrails

- <Safety constraint 1>
- <Safety constraint 2>
- Stop and surface for review at <checkpoint>

## Skills this agent uses

`skill-1` · `skill-2` · `skill-3`
```

---

## Vertical Plugin Structure

```
plugins/vertical-plugins/<vertical-slug>/
├── .claude-plugin/
│   └── plugin.json
├── .mcp.json                     # Data provider configuration
├── commands/                     # Slash commands (if any)
│   └── <command-name>.md
└── skills/
    ├── <skill-1>/
    │   └── SKILL.md
    └── <skill-2>/
        └── SKILL.md
```

### .mcp.json Template

Select providers from the catalog based on the vertical's data needs:

```json
{
  "mcpServers": {
    "<provider-1>": {
      "type": "http",
      "url": "<provider-url>"
    },
    "<provider-2>": {
      "type": "http",
      "url": "<provider-url>"
    }
  }
}
```

---

## Managed Agent Cookbook Structure

```
managed-agent-cookbooks/<agent-slug>/
├── agent.yaml                    # Top-level agent manifest
├── subagents/
│   ├── researcher.yaml           # Read-only research sub-agent
│   ├── <domain-worker>.yaml      # Domain-specific sub-agent
│   └── writer.yaml               # Only leaf with Write permission
├── steering-examples.json        # Example trigger phrases
└── README.md                     # Deployment documentation
```

### agent.yaml Template

```yaml
# <Agent Name> — managed-agent cookbook

name: <agent-slug>
model: claude-opus-4-7

system:
  file: ../../plugins/agent-plugins/<agent-slug>/agents/<agent-slug>.md
  append: "You are running headless. Produce files in ./out/; do not assume an open Office document."

tools:
  - type: agent_toolset_20260401
    default_config: { enabled: false }
    configs:
      - { name: read,  enabled: true }
      - { name: grep,  enabled: true }
      - { name: glob,  enabled: true }
  - { type: mcp_toolset, mcp_server_name: <primary-provider>, default_config: { enabled: true } }

mcp_servers:
  - { type: url, name: <primary-provider>, url: "${PROVIDER_MCP_URL}" }

skills:
  - { from_plugin: ../../plugins/agent-plugins/<agent-slug> }

callable_agents:
  - { manifest: ./subagents/researcher.yaml }
  - { manifest: ./subagents/<domain-worker>.yaml }
  - { manifest: ./subagents/writer.yaml }   # only leaf with Write
```

### Subagent Template (subagents/researcher.yaml)

```yaml
name: <agent-slug>-researcher
model: claude-sonnet-4-6

system:
  text: |
    You are a research assistant for the <Agent Name>. Gather data from available
    MCP sources and return structured findings. Do not produce final artifacts —
    return raw data and analysis to the orchestrator.

tools:
  - type: agent_toolset_20260401
    default_config: { enabled: false }
    configs:
      - { name: read, enabled: true }
      - { name: grep, enabled: true }
  - { type: mcp_toolset, mcp_server_name: <provider>, default_config: { enabled: true } }

output_schema:
  type: object
  properties:
    findings:
      type: string
      description: Structured research findings
    data_sources:
      type: array
      items:
        type: string
      description: List of MCP sources consulted
    confidence:
      type: string
      enum: [high, medium, low]
```

### steering-examples.json Template

```json
[
  {
    "trigger": "<Natural language phrase that should invoke this agent>",
    "expected_behavior": "<What the agent should do when triggered>"
  },
  {
    "trigger": "<Another trigger phrase>",
    "expected_behavior": "<Expected behavior>"
  },
  {
    "trigger": "<Edge case trigger>",
    "expected_behavior": "<How agent handles the edge case>"
  }
]
```

---

## marketplace.json Entry

When scaffolding a new plugin, add an entry to the root `.claude-plugin/marketplace.json`:

```json
{
  "name": "<plugin-slug>",
  "source": "./plugins/vertical-plugins/<plugin-slug>",
  "description": "<One-line description matching plugin.json>"
}
```

For agent-plugins:
```json
{
  "name": "<agent-slug>",
  "source": "./plugins/agent-plugins/<agent-slug>",
  "description": "<One-line description matching plugin.json>"
}
```

---

## Design Principles

1. **One writer rule:** In multi-agent cookbooks, only ONE leaf subagent gets Write permission. All others are read-only researchers.
2. **Canonical system prompts:** `agent.yaml` always references the system prompt from `agent-plugins/` via `file:` — never inline the full prompt.
3. **Skills synced from verticals:** Agent-plugins bundle copies of skills from `vertical-plugins/`. The source of truth is always the vertical. Use `scripts/sync-agent-skills.py` to propagate changes.
4. **MCP via environment variables:** Never hardcode MCP URLs in cookbooks. Use `${PROVIDER_MCP_URL}` pattern for deployment flexibility.
5. **Version starts at 0.1.0:** All new plugins start at version 0.1.0. The CI/CD pipeline handles subsequent bumps.

## Validation

After scaffolding, verify:

```bash
# Validate all manifests and cross-references
python3 scripts/check.py

# Validate specific plugin structure
python3 scripts/validate.py plugins/agent-plugins/<agent-slug>

# Dry-run managed agent deployment
bash scripts/deploy-managed-agent.sh <agent-slug> --dry-run

# Test the cookbook
bash scripts/test-cookbooks.sh <agent-slug>
```
