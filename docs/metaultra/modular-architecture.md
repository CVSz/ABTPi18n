# Modular Architecture

This page outlines the module boundaries and recommended layout for building MetaUltra-style plugins and templates.

## Recommended Layout
```
tools/metaultra/
├── example_module.py         # Example strategy implementation (Python)
├── example_module.ts         # TypeScript example (frontend or node)
├── templates/                # Reusable scaffolding templates
└── README.md                 # Overview and how to use the examples
```

## Module Responsibilities
- Small surface area: each module should provide one clear responsibility (e.g., signal generation)
- Clear metadata: include `meta.json` with name, entrypoint, and schema
- Tests: unit tests with deterministic fixtures

## Integration Points
- `meta.json` describes how external tools should load modules
- The installer writes a `build/metaultra/meta.json` as a single manifest for released bundles

> **Tip:** Keep cross-module dependencies minimal to ease packaging and reuse.
