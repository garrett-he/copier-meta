# AGENTS.md

## Project Overview

This is a Copier meta-template for bootstrapping new template scaffolds. It generates complete Copier templates with
tests, CI, and documentation.

## Tech Stack

- **Language**: Python 3.12+
- **Package Manager**: uv
- **Task Runner**: just
- **Linter/Formatter**: ruff (line-length: 120, single quotes, LF line endings)
- **Type Checker**: pyrefly (strict preset)
- **Testing**: pytest with pytest-copie
- **Markdown Linter**: rumdl

## Development Commands

```bash
# Install dependencies
just install-dev

# Run linters and type checkers
just check

# Format code
just format

# Run tests
just test
```

## Project Structure

- `copier/` - Copier configuration and extensions for meta-template
- `meta-template/` - The generated template structure
  - `template/` - Template files with Jinja2 syntax
  - `tests/` - Tests for the generated template
  - `copier/` - Copier configuration and extensions for template
- `tests/` - Tests for the meta-template itself
- `copier.yml` - Main Copier configuration

## Code Style

- **Indentation**: 4 spaces
- **Quotes**: Single quotes
- **Line Endings**: LF
- **Max Line Length**: 120 characters
- **Docstrings**: Google style
- **Imports**: Sorted by ruff (isort compatible)

## Testing

Tests use `pytest-copie` to test Copier template generation. The `copie` fixture generates temporary projects from the
template, and tests verify the generated files and structure.

Key test patterns:

- `base_answers` fixture provides random test data via `chance` library
- Tests verify file existence, content, and template variable substitution
- Generated template tests run in subprocess to verify they pass independently

## Commit Convention

Use Conventional Commits format:

- Prefixes: `feat | fix | ci | refactor | chore | docs | test`
- English language
- Max 70 characters per line in body

## Important Notes

- Always run `just test` before committing
- The `meta-template/` directory is ignored by pytest (via `--ignore=meta-template`)
- Template files use Jinja2 syntax with `{% raw %}` blocks for literal curly braces
- License templates are conditionally generated based on `copyright_license` variable
