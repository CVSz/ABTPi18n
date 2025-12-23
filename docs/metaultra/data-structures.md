# Data Structures & Schemas

This document describes the canonical data structures used in MetaUltra examples and generator metadata.

## Example: Strategy Metadata (`meta.json`)
```json
{
  "name": "example",
  "version": "0.1.0",
  "entrypoint": "tools.metaultra.example_module:ExampleStrategy",
  "schema": {
    "type":"object",
    "properties": {"name":{"type":"string"}}
  }
}
```

## Local Schema Conventions
- Use JSON Schema for interchange and validation
- Keep schemas explicit and avoid polymorphic union types where possible

## In-memory Structures
- Prefer plain dicts / POJOs for configuration
- Use typed dataclasses or interfaces for exported public contract
