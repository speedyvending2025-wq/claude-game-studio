---
name: engine-routing
description: "Choose and apply the correct engine-specific workflow for Godot, Unity, or Unreal. Use whenever engine-specific implementation or setup is requested."
---

# Engine Routing

Detect the engine from project files before acting.

- Godot: `project.godot`, `.gd`, scenes, resources.
- Unity: `ProjectSettings`, `.unity`, `.prefab`, C# scripts.
- Unreal: `.uproject`, Blueprints, C++ source, Config.

Route to the matching specialist agent and preserve engine-native conventions. If the engine is unknown, ask or run project detection first.
