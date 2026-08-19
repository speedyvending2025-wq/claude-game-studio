---
name: studio-autopilot
description: "Run substantial game-development work end-to-end without premature return. Use when the user expects the studio to execute, test, fix, and deliver an outcome."
---

# Studio Autopilot

## Phase 0 — Capability audit
Record capabilities actually available:
- models/model tiers
- sub-agent execution
- file access
- shell/code execution
- browser/web
- image/reference inspection
- computer use
- Blender
- engine/editor access
- Git/version control
- connectors/MCP

Do not claim unavailable capabilities.

## Phase 1 — Mission brief
Create:
- Objective
- Acceptance criteria
- Constraints
- Out of scope
- Definition of Done
- Verification plan

## Phase 2 — Department assembly
Select every relevant specialist. For independent work, dispatch in parallel when supported.

Minimum departments for a substantial feature:
- Producer
- relevant Creative/Design lead
- relevant Technical lead
- implementation specialist
- QA

Add Art/Blender/Audio/Narrative/UI/Performance/Release as applicable.

## Phase 3 — Build
Execute the actual work. Maintain a ledger:
- task
- owner
- status
- evidence
- dependencies
- next action

Do not close a task because a plan was written.

## Phase 4 — Integration
Bring specialist outputs into the real project. Resolve conflicts through the appropriate director. Verify assets are imported, references are correct, scenes load, code compiles, and systems connect.

## Phase 5 — Verification loop
Repeat:
CHECK → FIND FAILURES → FIX ROOT CAUSE → RE-CHECK

For visual work:
REFERENCE → BUILD → CAPTURE → COMPARE → REVISE → CAPTURE AGAIN.

For code:
BUILD → TEST → FIX → REGRESSION TEST.

For gameplay:
LAUNCH → PLAY/SMOKE TEST → CAPTURE FAILURE → FIX → REPLAY.

## Phase 6 — Completion gate
Before returning:
- reconcile the ledger,
- verify every acceptance criterion,
- record evidence,
- check regressions,
- update required project memory,
- ensure no known required work is left.

If work remains and you can continue, continue.

If a blocker requires the user, return only after explaining exactly what is blocked and why.

## Never
- stop after generating a plan when implementation was requested;
- say "ready for you to implement" when the studio can implement;
- mark untested work as passed;
- invent sub-agent/model/tool activity.
