---
name: visual-pipeline
description: Orchestrates concept/reference-driven visual production from art direction through Blender, engine implementation, and visual QA.
---

# Visual Production Pipeline

Use whenever a task changes the game's visual quality, environment, characters, props, UI, lighting, materials, camera, or presentation.

## Required pipeline
1. **Reference intake** — identify approved concept/reference images and any existing Visual Bible.
2. **Art direction (Opus)** — define the target and measurable acceptance criteria.
3. **Asset breakdown** — classify hero assets, modular assets, dressing, materials, UI, VFX, and technical requirements.
4. **Blender production (Sonnet)** — create/refine authored 3D assets when appropriate.
5. **Technical art (Sonnet)** — import/export, materials, lighting, shaders, optimization, and engine integration.
6. **Scene/UI implementation (Sonnet)** — assemble the result in the target engine.
7. **Visual QA (Sonnet; Haiku for lightweight checks when available)** — compare the result to the reference and Visual Bible.
8. **Revision loop** — failed visual QA returns to the responsible specialist; do not ship a known visual miss.
9. **Approval gate** — major visual direction changes require user approval.

## Quality rule
A working prototype is not a visual pass. Do not describe a result as "matching the concept" unless the visual QA criteria support that conclusion.

## Output
Always report: target, assets required, work performed, visual gaps remaining, QA status, and next iteration.
