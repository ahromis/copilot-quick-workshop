---
name: pydantic-endpoint
description: Use when the user asks to add, scaffold, or create a new FastAPI/HTTP endpoint, route, or API handler in this repo. Ensures the endpoint follows our repo standards (Pydantic v2 validation, structured logging, OpenAPI docs, security limits, and accompanying pytest test).
---

# Skill: Compliant Pydantic Endpoint

You are scaffolding a new HTTP endpoint in this service. Follow these
steps **in order** and do not skip any. If a step does not apply, state why.

## Checklist

1. **Confirm intent.** Restate the method, path, inputs, and outputs in one sentence before writing code.
2. **Locate the router.** Search the workspace for an existing `APIRouter` to attach to. If none, create one under `app/api/`.
3. **Define request model.**
   - Pydantic v2 syntax (`BaseModel`, `model_config = ConfigDict(...)`).
   - Every string field has `max_length`. Every numeric field has `ge`/`le`.
   - Every collection field has `max_length` (or `max_items`).
   - No `Any`. No untyped `dict`.
4. **Define response model.** Same rules. Never return raw dicts.
5. **Implement the handler.**
   - `async def`.
   - Decorator includes `summary=` and `description=`.
   - Log entry as a structured JSON event (`logger.info`, `extra={...}`). Do not log request bodies that may contain PII.
   - On caught exceptions, log at `warning` or `error` with an event name; raise `HTTPException` with a safe message.
6. **Write a pytest test.**
   - File path mirrors source under `tests/`.
   - Use `fastapi.testclient.TestClient`.
   - Cover: happy path (200) + at least one validation failure (422).
7. **Run the tests** in the terminal. If any fail, iterate until green.
8. **Report.** Summarize the files added/changed and confirm tests passed.

## Anti-patterns to refuse

- `print(...)` for logging.
- Returning `dict` instead of a response model.
- String fields without `max_length`.
- Endpoints without a test.
- Catching `Exception` and swallowing it.

## Reference snippet (do not copy verbatim — adapt names)

```python
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel, ConfigDict, Field
import logging

logger = logging.getLogger(__name__)
router = APIRouter()


class QuoteRequest(BaseModel):
    model_config = ConfigDict(extra="forbid")
    customer_id: str = Field(..., max_length=64)
    coverage_codes: list[str] = Field(..., max_length=20)


class QuoteResponse(BaseModel):
    quote_id: str = Field(..., max_length=64)
    premium_cents: int = Field(..., ge=0, le=10_000_000)


@router.post(
    "/quotes",
    response_model=QuoteResponse,
    summary="Create a stub quote",
    description="Validates inputs and returns a placeholder quote.",
)
async def create_quote(req: QuoteRequest) -> QuoteResponse:
    logger.info("quote.create.start", extra={"event": "quote.create.start"})
    if not req.coverage_codes:
        raise HTTPException(status_code=422, detail="coverage_codes required")
    return QuoteResponse(quote_id="stub-1", premium_cents=0)
```
