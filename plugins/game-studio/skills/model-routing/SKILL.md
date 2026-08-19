---
name: model-routing
description: "Route game-development work to the appropriate Claude model tier. Use when deciding whether a task should be handled by Opus, Sonnet, or Haiku, or when coordinating specialist work."
---

# Model Routing

Use the following policy unless the user explicitly chooses a model.

## Opus — think, architect, arbitrate
Use for: game vision, major design decisions, architecture, difficult debugging, cross-system failures, large document synthesis, director-level reviews, conflict resolution, and final review of high-risk changes.

## Sonnet — build
Use as the default workhorse for: gameplay code, systems, Godot/Unity/Unreal implementation, Blender/asset workflows, level design, UI, shaders, animation logic, ordinary debugging, documentation, and most specialist tasks.

## Haiku — check and accelerate
Use for: quick inspection, simple validation, status checks, repetitive transformations, naming checks, lightweight QA, summaries, and other low-complexity work.

## Escalation
- Start with Sonnet for normal implementation.
- Escalate to Opus when the task becomes architectural, ambiguous, cross-system, or unusually difficult.
- Use Haiku for quick checks before spending a stronger model on them.
- Never let a lightweight check silently override a director-level decision.

## Important Desktop/Cowork limitation
The routing policy is the studio's decision framework. Actual model availability and automatic sub-agent model selection depend on the Claude Desktop/Cowork plugin runtime. Never claim a model was switched unless the runtime actually reports that model.
