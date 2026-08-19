# Claude Game Studio Universal

A universal AI game-development studio for Claude Desktop and Cowork, remixed from Claude Code Game Studios.

## What is included
- 50 studio agents (49 adapted specialists + Studio Coordinator)
- 79 skills (73 adapted workflows + 6 universal core skills)
- Godot, Unity, and Unreal workflows
- Professional design, architecture, production, art, narrative, programming, and QA processes
- Opus/Sonnet/Haiku routing policy
- No Claude Code hooks or project settings required

## Important
This package uses the Claude plugin structure documented by Anthropic. Skills and agents are at the plugin root; only the manifest lives under `.claude-plugin/`.

## Desktop/Cowork
Install the plugin through Claude Desktop's plugin interface. Once installed, its skills are available in chat and Cowork. Connect the user's game folder as the working folder. Run the project bootstrap workflow first.

## Model policy
Opus: strategic/architectural/high-risk reasoning.
Sonnet: default implementation work.
Haiku: quick checks and lightweight work.
Actual model selection is controlled by the host runtime; the plugin never pretends a model switch occurred when it did not.

## Project data
The plugin does not require a `.claude/` folder. It recommends a `.game-studio/` folder inside the user's game project for portable studio state.

## Original project
This remix is derived from the MIT-licensed Claude Code Game Studios project by Donchitos.
