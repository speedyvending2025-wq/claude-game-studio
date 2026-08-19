---
name: qa-loop
description: "Run the universal game-development verification loop after implementation: inspect, test, reproduce failures, fix, and re-test. Use when code, assets, scenes, levels, or gameplay systems change."
---

# QA Loop

1. Identify the intended behavior.
2. Run the cheapest relevant validation first.
3. If it fails, capture the exact failure and likely owning specialist.
4. Fix the smallest root cause.
5. Re-run the test.
6. For high-risk changes, perform regression checks around adjacent systems.
7. Report what passed, what remains uncertain, and what should be escalated.
