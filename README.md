# AI Copilot Monorepo

This repository contains a minimal skeleton for an AI-powered automation platform. The layout roughly follows the multi-step plan described in the prompt.

## Services

- **API Gateway** (`services/api_gateway`): Entry point for requests.
- **Auth Service** (`services/auth_svc`): Handles authentication and tenant user management.
- **AI Gateway** (`services/ai_gateway`): Forwards completion requests to LLM providers.
- **Ingestion Worker** (`services/ingestion_worker`): Example CLI that ingests data.
- **Automation Service** (`services/automation_svc`): Simple orchestration layer that
  calls the AI gateway and stores task results.
- **UI** (`ui`): Placeholder front-end.

## Getting Started

Ensure Docker and docker-compose are installed. Run:

```bash
make develop
```

This will build and start the services along with Postgres and Redis.

### Pre-commit Hooks

Install pre-commit and run the hooks locally:

```bash
pip install pre-commit
pre-commit install
make precommit
```

### Pushing to GitHub

To push this repository to your own GitHub account:

```bash
git remote add origin git@github.com:<YOUR-USER>/<YOUR-REPO>.git
git push -u origin work
```

Replace `<YOUR-USER>` and `<YOUR-REPO>` with your GitHub details. After pushing, you can open a pull request on GitHub.

## Auth Service Endpoints

The auth service exposes two simple endpoints:

- `POST /auth/signup` with `username`, `password`, and `tenant_name` parameters returns a JWT for the new admin user.
- `GET /tenants/{id}/users` lists all users for a tenant.

These endpoints run against a SQLite database by default when started locally.
