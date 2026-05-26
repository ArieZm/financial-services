#!/usr/bin/env python3
"""Validate a SKILL.md file against the Agent Skills standard conventions."""
import re
import sys
from pathlib import Path


def validate_skill_md(path: str) -> list[str]:
    """Validate a SKILL.md file. Returns list of issues found."""
    issues = []
    filepath = Path(path)

    if not filepath.exists():
        return [f"File not found: {path}"]

    content = filepath.read_text()

    # Check frontmatter exists
    if not content.startswith("---"):
        issues.append("Missing YAML frontmatter (must start with ---)")
        return issues

    parts = content.split("---", 2)
    if len(parts) < 3:
        issues.append("Malformed frontmatter (missing closing ---)")
        return issues

    frontmatter = parts[1].strip()
    body = parts[2].strip()

    # Check required frontmatter fields
    if not re.search(r"^name:\s*\S+", frontmatter, re.MULTILINE):
        issues.append("Missing required field: name")

    name_match = re.search(r"^name:\s*(.+)$", frontmatter, re.MULTILINE)
    if name_match:
        name = name_match.group(1).strip()
        if not re.match(r"^[a-z0-9][a-z0-9-]*[a-z0-9]$", name) and len(name) > 1:
            issues.append(
                f"Name '{name}' should be lowercase-hyphenated (e.g., 'my-skill')"
            )

    if not re.search(r"^description:\s*", frontmatter, re.MULTILINE):
        issues.append("Missing required field: description")
    else:
        desc_match = re.search(
            r"^description:\s*\|?\s*\n?([\s\S]*?)(?=^[a-z]|\Z)",
            frontmatter,
            re.MULTILINE,
        )
        if desc_match:
            desc = desc_match.group(1).strip()
            if len(desc) < 50:
                issues.append(
                    f"Description too short ({len(desc)} chars). "
                    "Should be detailed with trigger contexts."
                )

            # Check for pushy trigger language
            trigger_phrases = ["use when", "use this", "invoke when", "perfect for"]
            has_trigger = any(p in desc.lower() for p in trigger_phrases)
            if not has_trigger:
                issues.append(
                    "Description lacks trigger language. "
                    "Add 'Use when...', 'Perfect for...', or 'Invoke when...' phrasing."
                )

    # Check body content
    if not body:
        issues.append("Empty skill body")

    if body and "# " not in body:
        issues.append("Body should have at least one markdown heading")

    # Check for guardrails section (recommended for FSI skills)
    if "guardrail" not in body.lower() and "guard rail" not in body.lower():
        issues.append(
            "[WARNING] No guardrails section found. "
            "Recommended for financial skills."
        )

    # Check for hardcoded secrets
    secret_patterns = [
        r"(?:api[_-]?key|token|secret|password)\s*[:=]\s*['\"][^'\"]{8,}['\"]",
        r"sk-[a-zA-Z0-9]{20,}",
        r"Bearer\s+[a-zA-Z0-9._-]{20,}",
    ]
    for pattern in secret_patterns:
        if re.search(pattern, content, re.IGNORECASE):
            issues.append("[CRITICAL] Possible hardcoded secret/credential detected")
            break

    return issues


def main():
    if len(sys.argv) < 2:
        print("Usage: validate_skill_md.py <path/to/SKILL.md>")
        sys.exit(1)

    path = sys.argv[1]
    issues = validate_skill_md(path)

    if not issues:
        print(f"OK: {path}")
        sys.exit(0)

    print(f"ISSUES in {path}:")
    for issue in issues:
        print(f"  - {issue}")
    sys.exit(1)


if __name__ == "__main__":
    main()
