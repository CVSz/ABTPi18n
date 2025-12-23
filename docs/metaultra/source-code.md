# Source Code, Examples & Snippets

This file points to canonical example modules and short snippets for quick reference.

## Example Layout
- `tools/metaultra/example_module.py` — Python example with lifecycle hooks
- `tools/metaultra/example_module.ts` — TypeScript example for frontend integration

## Snippet: Loading a Module (Python)
```py
import importlib
module = importlib.import_module('tools.metaultra.example_module')
strategy = module.ExampleStrategy({'name':'demo'})
```

## Snippet: Minimal TypeScript Interface
```ts
export interface StrategyConfig { name: string; params?: Record<string, any> }
```

## Notes
- Keep examples small and readable; the goal is pedagogical clarity
- Cross-reference functions.md and algorithms.md for behavioral context
