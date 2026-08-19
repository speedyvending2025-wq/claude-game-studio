---
name: completion-gate
description: "Enforce evidence-based Definition of Done and prevent premature completion claims."
---

# Completion Gate

A task is COMPLETE only if:
1. Every explicit user requirement maps to an acceptance criterion.
2. Every criterion has PASS evidence.
3. Requested implementation exists in the actual project.
4. Relevant tests/checks were run.
5. Known failures were fixed or are documented as blockers.
6. Required assets are imported and wired into the engine.
7. Visual targets are checked when relevant.
8. Documentation/project memory is updated when required.
9. No requested item is silently deferred.

Statuses:
- PASS — verified with evidence
- FAIL — verified failure; return to implementation
- BLOCKED — cannot proceed without an external dependency/authorization
- NOT APPLICABLE — explain why

A generated plan, screenshot of a plan, or agent statement is not evidence of implementation.

Final verdict:
Start with `RESULT: COMPLETE` only when every required criterion is PASS.
Otherwise use `RESULT: BLOCKED` or `RESULT: PARTIAL` and list unresolved items.
