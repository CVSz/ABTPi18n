# Functions, Interfaces & Contracts

This document outlines the top-level functions and interface contracts that MetaUltra exposes via its example modules and templates.

## Example Interface (Python)
```py
class StrategyInterface:
    def __init__(self, config: dict):
        """Initialize with a validated config"""

    def on_tick(self, tick: dict) -> None:
        """Process a market tick"""

    def generate_signals(self) -> list:
        """Return a list of signals"""
```

## Interface Notes
- Interfaces are intentionally minimal; implementations should be composable and stateless where possible
- Respect typed contracts and document side-effects (I/O, network, DB)

## Advanced: Hooking into the generator
- The generator produces `meta.json` with metadata describing all included modules and their entrypoints
- Consumers may use the `meta.json` to dynamically load modules in other contexts
