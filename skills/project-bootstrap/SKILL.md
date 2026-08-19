---
name: project-bootstrap
description: "Initialize or inspect a game project for the Universal Game Studio. Use when a user says start a new game, set up the studio, onboard an existing game, or configure Godot, Unity, or Unreal."
---

# Project Bootstrap

1. Inspect the selected project folder.
2. Detect engine, version if available, source layout, asset layout, existing design documents, tests, and production artifacts.
3. Ask only for missing decisions that materially affect setup.
4. Create a `.game-studio/` folder if appropriate, containing lightweight project metadata and active-session state.
5. Never overwrite existing game files without approval.
6. If the project is already established, preserve its structure and adapt the studio to it.
7. Recommend the smallest useful set of specialists and workflows rather than activating everything at once.

Suggested metadata:
- `.game-studio/project-profile.md`
- `.game-studio/active.md`
- `.game-studio/decisions/`
- `.game-studio/reviews/`
- `.game-studio/production/`
