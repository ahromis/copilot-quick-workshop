# GitHub Copilot Instructions

## Code Standards
- Use Python 3.12+ features and type hints throughout
- Follow PEP 8 style conventions
- Use Pydantic v2 model syntax for all data models
- All API endpoints must include docstrings with OpenAPI descriptions
- Use structured JSON logging (never print statements)

## Security Requirements
- All user inputs must be validated with Pydantic models with explicit size/range limits
- CORS must be restricted to an explicit allowlist of approved domains
- Never log sensitive data (PII, credentials, tokens)
- All Dockerfiles must use non-root users

## Cloud & Deployment
- Kubernetes manifests must include resource limits, health probes, and pod disruption budgets
- Use environment variables for all configuration (12-factor app)
- Container images must be based on slim/distroless base images

## Testing
- All new endpoints must have corresponding unit tests
- Use pytest as the test framework
- Tests must be in the tests/ directory
