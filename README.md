# Claude Game Studio Marketplace

Universal AI game-development studio for Claude Desktop and Cowork.

## Included plugin

- `game-studio` — the universal game-development studio with agents, skills, workflows, review gates, and model-routing guidance.

## Installation

Add this repository as a Claude plugin marketplace. Then install the `game-studio` plugin from the marketplace.

## Engines

The studio is designed to be engine-agnostic, with workflows for Godot, Unity, and Unreal Engine.

## Model strategy

- Opus: directors, architecture, complex reasoning, major reviews
- Sonnet: primary implementation and specialist development
- Haiku: lightweight checks, summaries, and repetitive tasks

The runtime ultimately controls which model is available to a given plugin/agent workflow; the routing files describe the intended responsibility split.
