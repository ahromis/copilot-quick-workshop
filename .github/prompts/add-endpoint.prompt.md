---
mode: agent
description: Scaffold a new FastAPI endpoint that follows our repo standards.
---

# Add Endpoint

Create a new FastAPI endpoint with:

1. A Pydantic v2 request model with explicit field constraints (`max_length`, `ge`, `le`).
2. A Pydantic v2 response model.
3. A route handler with an OpenAPI `summary` and `description`.
4. Structured JSON logging on entry and on validation failure (no PII).
5. A `pytest` test under `tests/` that covers the happy path and one validation failure.

Ask me for the HTTP method, path, and a one-line description before generating code.
