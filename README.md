# Claude Game Studio Marketplace v1.2

Universal AI game-development studio for Claude Desktop and Cowork.

## v1.2 production upgrade

Game Studio emphasizes **end-to-end delivery rather than plan-only assistance**:

- Studio Coordinator / Executive Producer owns the outcome.
- Studio Autopilot drives plan → delegate → build → integrate → test → fix → verify.
- Completion Gate prevents premature "complete" claims.
- Tool Utilization Audit checks what the runtime actually exposes and uses relevant capabilities.
- Model routing assigns meaningful work to Opus, Sonnet, and Haiku when those tiers are actually available.
- Sub-agent orchestration uses all relevant specialists and parallelizes independent work when supported.
- Visual production retains Art Director → Blender → Technical Art → Engine → Visual QA loops.

## Runtime reality

The plugin can define orchestration policy, but Claude Desktop/Cowork controls which models, sub-agent execution mechanisms, and tools are actually available in a session. The studio never claims a model switched or a sub-agent ran unless the runtime provides evidence.

For long-running multi-step implementation, Cowork is the preferred surface because Anthropic documents Cowork as supporting task decomposition, parallel workstreams, sub-agent coordination, long-running tasks, and local file access on Desktop.
