---
name: tool-utilization-audit
description: "Audit and deliberately use relevant tools, sub-agents, model tiers, and external capabilities available in the current Claude runtime."
---

# Tool Utilization Audit

Before substantial work, determine what the runtime actually exposes.

Capability classes:
- file system/local project access
- shell/code execution
- browser/web
- image/reference inspection
- computer use
- Blender
- Godot/Unity/Unreal editor
- Git/version control
- connectors/MCP
- sub-agent/task orchestration
- model tiers

Use relevant capabilities, prioritizing direct and reliable tools.

## Model policy
When multiple tiers are exposed:
- Opus: direction, architecture, difficult reasoning, arbitration, final review.
- Sonnet: implementation and specialist production.
- Haiku: quick checks, triage, transformations, smoke validation.

Use all available tiers when each has a meaningful role. Do not manufacture work merely to exercise a model.

## Sub-agent policy
When sub-agents are available:
- dispatch independent specialists in parallel,
- give each complete context,
- collect outputs,
- integrate them,
- send failures back to the owning specialist,
- use a final lead/director review.

Use every relevant specialist, not every specialist in the repository.

## Evidence
At the end, report only actual tool/model/sub-agent activity the runtime exposed.
