---
name: fsi-publisher
description: |
  Validate, version-bump, sync, and publish financial-services plugins and agents to the marketplace. Use this skill whenever someone wants to publish a new skill or plugin, deploy a managed agent, create a release PR, or run the full pre-publish validation suite. Also use when someone says "publish this", "ship it", "deploy", "create a PR for this plugin", or "is this ready to publish".
---

# FSI Publisher

You handle the final mile of the plugin lifecycle: validation, version bumping, syncing, marketplace registration, PR creation, and managed agent deployment.

## Pre-Publish Checklist

Before publishing any artifact, verify ALL of the following:

### 1. Validation Gates

Run the validation suite:

```bash
# Full manifest and cross-reference validation
python3 scripts/check.py

# Validate specific plugin structure
python3 scripts/validate.py <plugin-path>
```

Both must pass with zero errors.

### 2. Eval Quality Gate

Check that the skill/agent has been evaluated and meets thresholds:

- Overall pass rate >= 80%
- Financial accuracy assertions >= 90%
- No critical failures
- With-skill performance >= baseline

Look for `evals/benchmark.json` in the skill directory. If it doesn't exist, the skill has not been evaluated — block publishing and recommend running `fsi-eval-runner`.

### 3. Compliance Gate

Check that security/compliance review has passed:

- Look for a compliance verdict (from `fsi-compliance-reviewer`)
- `passes` must be `true`
- Zero violations
- All FSI compliance checks passed

If no compliance review exists, block publishing and recommend running `fsi-compliance-reviewer`.

### 4. Skill Sync

If publishing an agent-plugin that bundles skills from vertical-plugins:

```bash
python3 scripts/sync-agent-skills.py
```

This ensures bundled skills in agent-plugins match their canonical sources in vertical-plugins.

### 5. Version Bump

Bump the patch version:

```bash
python3 scripts/version_bump.py <plugin-path>
```

Convention: one patch bump per branch, not per commit. The CI/CD `version-bump.yml` workflow also auto-bumps on PR.

### 6. Marketplace Registration

For new plugins, add an entry to `.claude-plugin/marketplace.json`:

```json
{
  "name": "<plugin-slug>",
  "source": "./plugins/<type>/<plugin-slug>",
  "description": "<One-line description matching plugin.json>"
}
```

Verify the entry doesn't duplicate an existing plugin name.

### 7. Managed Agent Cookbook (if applicable)

For agent-plugins that need headless deployment:

```bash
# Dry-run deployment validation
bash scripts/deploy-managed-agent.sh <agent-slug> --dry-run

# Test the cookbook
bash scripts/test-cookbooks.sh <agent-slug>
```

Verify:
- `agent.yaml` references the correct system prompt path
- `subagents/` directory has required sub-agent configs
- `steering-examples.json` has at least 3 trigger examples
- `README.md` documents deployment prerequisites

## Publishing Workflow

### For a New Skill

1. Verify skill is in the correct vertical: `plugins/vertical-plugins/<vertical>/skills/<skill-slug>/`
2. Run validation: `python3 scripts/check.py`
3. Check eval results: `evals/benchmark.json` meets thresholds
4. Check compliance: security review passed
5. Bump version of the vertical plugin
6. Create PR with descriptive title and body

### For a New Agent

1. Verify agent-plugin structure: `plugins/agent-plugins/<agent-slug>/`
2. Sync skills: `python3 scripts/sync-agent-skills.py`
3. Run validation: `python3 scripts/check.py`
4. Check eval results for each bundled skill
5. Check compliance review
6. Bump version
7. Register in marketplace
8. If headless deployment needed: scaffold and validate cookbook
9. Create PR

### For a New Vertical

1. Verify vertical-plugin structure: `plugins/vertical-plugins/<vertical-slug>/`
2. All skills within the vertical pass evals
3. Compliance review covers the full vertical
4. Register in marketplace
5. Bump version
6. Create PR

## PR Template

When creating the publish PR:

```markdown
## Summary

- **Artifact:** <skill/agent/vertical name>
- **Type:** <new skill | new agent | new vertical | update>
- **Vertical:** <vertical name>

## Changes

- <bullet list of what was added/changed>

## Quality Gates

- [ ] `check.py` passes
- [ ] Eval pass rate >= 80% (actual: X%)
- [ ] Financial accuracy >= 90% (actual: X%)
- [ ] Compliance review passed
- [ ] Skills synced (if agent-plugin)
- [ ] Marketplace entry added (if new)
- [ ] Cookbook validated (if managed agent)
```

## Rollback

If a published plugin needs to be reverted:

1. Revert the marketplace.json entry
2. Revert the plugin directory changes
3. Bump version (don't reuse old version numbers)
4. Create revert PR with explanation
