# FSI Architect — Managed Agent Cookbook

Pipeline orchestrator for creating, evaluating, and publishing financial-services plugins.

## Deployment

```bash
bash scripts/deploy-managed-agent.sh fsi-architect
```

## Prerequisites

- Agent plugin at `plugins/agent-plugins/fsi-architect/`
- All specialist agent skills installed in the target environment

## Architecture

- **fsi-architect** (orchestrator) — routes work to specialist sub-agents
  - **fsi-domain-expert** (read-only) — financial domain knowledge and requirements analysis
  - **fsi-skill-writer** (read-only) — creates SKILL.md files
  - **fsi-plugin-scaffolder** (read-only) — generates plugin directory structures
  - **fsi-eval-runner** (read-only) — runs evaluations and benchmarks
  - **fsi-publisher** (write-enabled) — validates, versions, and publishes artifacts
