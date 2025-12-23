# CLI Options & Installer Flags

The MetaUltra installer (`scripts/zeaz_meta_installer.sh`) supports the following options:

- `--help`            Show usage information
- `--preview`         Show planned changes without writing files
- `--generate`        Generate artifact files in `./build/metaultra/`
- `--install`         Persist files into the repository (idempotent)
- `--release`         Package a release tarball (requires `--generate`)
- `--dry-run`         Alias for `--preview`
- `--verbose`         Enable detailed logging

### Best practices
- Use `--preview` to validate planned layout before committing
- Combine `--generate` and `--release` to create an importable archive for distribution
- The installer is intentionally conservative and will refuse to overwrite with no `--install` flag
