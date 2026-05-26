#!/usr/bin/env python3
"""Scaffold a new plugin directory structure for the financial-services ecosystem.

Usage:
  scaffold_plugin.py agent-plugin <slug> [--skills skill1,skill2]
  scaffold_plugin.py vertical-plugin <slug> [--mcp provider1,provider2]
  scaffold_plugin.py cookbook <slug>
"""
import argparse
import json
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[6]

MCP_PROVIDERS = {
    "daloopa": "https://mcp.daloopa.com/server/mcp",
    "factset": "https://mcp.factset.com/mcp",
    "sp-global": "https://kfinance.kensho.com/integrations/mcp",
    "morningstar": "https://mcp.morningstar.com/mcp",
    "moodys": "https://api.moodys.com/genai-ready-data/m1/mcp",
    "mtnewswire": "https://vast-mcp.blueskyapi.com/mtnewswires",
    "aiera": "https://mcp-pub.aiera.com",
    "lseg": "https://api.analytics.lseg.com/lfa/mcp",
    "pitchbook": "https://premium.mcp.pitchbook.com/mcp",
}


def scaffold_agent_plugin(slug: str, skills: list[str] | None = None):
    base = REPO_ROOT / "plugins" / "agent-plugins" / slug
    if base.exists():
        print(f"ERROR: {base} already exists")
        sys.exit(1)

    (base / ".claude-plugin").mkdir(parents=True)
    (base / "agents").mkdir()
    (base / "skills").mkdir()

    plugin_json = {
        "name": slug,
        "version": "0.1.0",
        "description": f"TODO: Describe what {slug} does end-to-end",
        "author": {"name": "Anthropic FSI"},
    }
    (base / ".claude-plugin" / "plugin.json").write_text(
        json.dumps(plugin_json, indent=2) + "\n"
    )

    agent_md = f"""---
name: {slug}
description: TODO - Add detailed description with trigger contexts.
tools: Read, Write, Edit
---

You are the {slug.replace('-', ' ').title()} agent.

## What you produce

TODO: Describe the artifacts this agent delivers.

## Workflow

1. **Scope the ask.** TODO
2. **Gather data.** TODO
3. **Produce output.** TODO

## Guardrails

- Cite every number with source and as-of date.
- Flag unsourced data as [UNSOURCED].
- Stop and surface for review at key checkpoints.

## Skills this agent uses

TODO: List skills
"""
    (base / "agents" / f"{slug}.md").write_text(agent_md)

    if skills:
        for skill in skills:
            skill_dir = base / "skills" / skill
            skill_dir.mkdir(parents=True)
            skill_md = f"""---
name: {skill}
description: TODO - Add description for {skill}.
---

# {skill.replace('-', ' ').title()}

TODO: Add skill instructions.
"""
            (skill_dir / "SKILL.md").write_text(skill_md)

    print(f"Created agent-plugin: {base.relative_to(REPO_ROOT)}")


def scaffold_vertical_plugin(slug: str, mcp_providers: list[str] | None = None):
    base = REPO_ROOT / "plugins" / "vertical-plugins" / slug
    if base.exists():
        print(f"ERROR: {base} already exists")
        sys.exit(1)

    (base / ".claude-plugin").mkdir(parents=True)
    (base / "commands").mkdir()
    (base / "skills").mkdir()

    plugin_json = {
        "name": slug,
        "version": "0.1.0",
        "description": f"TODO: Describe the {slug} vertical plugin",
        "author": {"name": "Anthropic FSI"},
    }
    (base / ".claude-plugin" / "plugin.json").write_text(
        json.dumps(plugin_json, indent=2) + "\n"
    )

    if mcp_providers:
        mcp_config = {"mcpServers": {}}
        for provider in mcp_providers:
            url = MCP_PROVIDERS.get(provider)
            if url:
                mcp_config["mcpServers"][provider] = {"type": "http", "url": url}
            else:
                mcp_config["mcpServers"][provider] = {
                    "type": "http",
                    "url": f"${{TODO_{provider.upper().replace('-', '_')}_URL}}",
                }
        (base / ".mcp.json").write_text(json.dumps(mcp_config, indent=2) + "\n")

    print(f"Created vertical-plugin: {base.relative_to(REPO_ROOT)}")


def scaffold_cookbook(slug: str):
    base = REPO_ROOT / "managed-agent-cookbooks" / slug
    agent_plugin = REPO_ROOT / "plugins" / "agent-plugins" / slug

    if base.exists():
        print(f"ERROR: {base} already exists")
        sys.exit(1)

    (base / "subagents").mkdir(parents=True)

    agent_yaml = f"""# {slug.replace('-', ' ').title()} -- managed-agent cookbook

name: {slug}
model: claude-opus-4-7

system:
  file: ../../plugins/agent-plugins/{slug}/agents/{slug}.md
  append: "You are running headless. Produce files in ./out/; do not assume an open Office document."

tools:
  - type: agent_toolset_20260401
    default_config: {{ enabled: false }}
    configs:
      - {{ name: read,  enabled: true }}
      - {{ name: grep,  enabled: true }}
      - {{ name: glob,  enabled: true }}

skills:
  - {{ from_plugin: ../../plugins/agent-plugins/{slug} }}

callable_agents:
  - {{ manifest: ./subagents/researcher.yaml }}
  - {{ manifest: ./subagents/writer.yaml }}   # only leaf with Write
"""
    (base / "agent.yaml").write_text(agent_yaml)

    researcher_yaml = f"""name: {slug}-researcher
model: claude-sonnet-4-6

system:
  text: |
    You are a research assistant for the {slug.replace('-', ' ').title()} agent.
    Gather data from available MCP sources and return structured findings.

tools:
  - type: agent_toolset_20260401
    default_config: {{ enabled: false }}
    configs:
      - {{ name: read, enabled: true }}
      - {{ name: grep, enabled: true }}

output_schema:
  type: object
  properties:
    findings:
      type: string
    data_sources:
      type: array
      items:
        type: string
    confidence:
      type: string
      enum: [high, medium, low]
"""
    (base / "subagents" / "researcher.yaml").write_text(researcher_yaml)

    writer_yaml = f"""name: {slug}-writer
model: claude-sonnet-4-6

system:
  text: |
    You are the output writer for the {slug.replace('-', ' ').title()} agent.
    Produce final artifacts based on research findings.

tools:
  - type: agent_toolset_20260401
    default_config: {{ enabled: false }}
    configs:
      - {{ name: read,  enabled: true }}
      - {{ name: write, enabled: true }}
      - {{ name: edit,  enabled: true }}
"""
    (base / "subagents" / "writer.yaml").write_text(writer_yaml)

    steering = [
        {
            "trigger": f"TODO: Natural language phrase for {slug}",
            "expected_behavior": "TODO: What the agent should do",
        }
    ]
    (base / "steering-examples.json").write_text(
        json.dumps(steering, indent=2) + "\n"
    )

    readme = f"""# {slug.replace('-', ' ').title()} — Managed Agent Cookbook

## Deployment

```bash
bash scripts/deploy-managed-agent.sh {slug}
```

## Prerequisites

- Agent plugin at `plugins/agent-plugins/{slug}/`
- MCP provider API keys in environment

## Architecture

- **{slug}** (orchestrator) — routes work to subagents
  - **{slug}-researcher** (read-only) — gathers data from MCP sources
  - **{slug}-writer** (write-enabled) — produces final output artifacts
"""
    (base / "README.md").write_text(readme)

    print(f"Created cookbook: {base.relative_to(REPO_ROOT)}")


def main():
    parser = argparse.ArgumentParser(description="Scaffold FSI plugin structures")
    parser.add_argument(
        "type", choices=["agent-plugin", "vertical-plugin", "cookbook"]
    )
    parser.add_argument("slug", help="Plugin/agent slug (lowercase-hyphenated)")
    parser.add_argument("--skills", help="Comma-separated skill names to include")
    parser.add_argument("--mcp", help="Comma-separated MCP provider names")

    args = parser.parse_args()

    if args.type == "agent-plugin":
        skills = args.skills.split(",") if args.skills else None
        scaffold_agent_plugin(args.slug, skills)
    elif args.type == "vertical-plugin":
        providers = args.mcp.split(",") if args.mcp else None
        scaffold_vertical_plugin(args.slug, providers)
    elif args.type == "cookbook":
        scaffold_cookbook(args.slug)


if __name__ == "__main__":
    main()
