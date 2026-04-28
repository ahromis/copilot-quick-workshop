---
applyTo: "**/*.py"
---

# Python Conventions

- Target Python 3.12+; use modern type hints (`list[int]`, `X | None`).
- Use `pytest` for tests; place them under `tests/` mirroring the source tree.
- Prefer `pathlib.Path` over `os.path`.
- Use `logging` with structured (JSON) output. Never use `print` in library code.
- Validate external inputs with Pydantic v2 models (`model_config`, `Field(..., max_length=...)`).
- Functions that can fail at runtime must raise typed exceptions, not return `None` sentinels.
