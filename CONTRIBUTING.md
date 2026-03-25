# Contributing to TaskFlow

Thank you for your interest in contributing to TaskFlow! This document provides guidelines and instructions to help you get started.

---

## Table of Contents

1. [Getting Started](#getting-started)
2. [Development Setup](#development-setup)
3. [Coding Standards](#coding-standards)
4. [Pull Request Process](#pull-request-process)
5. [Reporting Issues](#reporting-issues)

---

## Getting Started

### Prerequisites

- **Node.js** >= 18.x (or the runtime specified in `.nvmrc` / `pyproject.toml`)
- **Git** >= 2.x
- A GitHub account with access to the repository

### Fork & Clone

```bash
# Fork the repository on GitHub, then clone your fork
git clone https://github.com/<your-username>/taskflow.git
cd taskflow

# Add the upstream remote
git remote add upstream https://github.com/serenity-demos/taskflow.git
```

---

## Development Setup

### Install Dependencies

```bash
# Install project dependencies
npm install
# or, if the project uses Python:
pip install -e ".[dev]"
```

### Environment Variables

Copy the example env file and fill in the required values:

```bash
cp .env.example .env
```

Key variables:
| Variable | Description | Default |
|---|---|---|
| `DATABASE_URL` | Database connection string | `sqlite:///taskflow.db` |
| `SECRET_KEY` | App secret key | *(required)* |
| `DEBUG` | Enable debug mode | `false` |

### Running the Application

```bash
# Start development server
npm run dev
# or
python -m taskflow

# Run tests
npm test
# or
pytest
```

---

## Coding Standards

### General Rules

- **Keep files small** — aim for < 500 lines per file; split into modules if larger.
- **No hardcoded secrets** — always use environment variables or config files.
- **Handle errors explicitly** — do not swallow exceptions silently.
- **Write self-documenting code** — prefer clear naming over excessive comments.

### Style Guide

- Follow the project's linter/formatter configuration (`.eslintrc`, `ruff.toml`, `.prettierrc`).
- Run the linter before committing:

```bash
# JavaScript / TypeScript
npm run lint

# Python
ruff check .
```

### Commit Messages

We follow the [Conventional Commits](https://www.conventionalcommits.org/) specification:

```
<type>(<scope>): <short description>

[optional body]

[optional footer]
```

**Types:** `feat`, `fix`, `docs`, `refactor`, `test`, `chore`

**Examples:**
```
feat(tasks): add due date support
fix(auth): handle expired tokens gracefully
docs(contributing): add setup instructions
```

### Branch Naming

| Purpose | Pattern | Example |
|---|---|---|
| New feature | `feat/<short-name>` | `feat/due-dates` |
| Bug fix | `fix/<short-name>` | `fix/token-expiry` |
| Documentation | `docs/<short-name>` | `docs/api-reference` |
| Refactoring | `refactor/<short-name>` | `refactor/task-service` |

---

## Pull Request Process

### Before Submitting

1. **Sync with upstream**:
   ```bash
   git fetch upstream
   git rebase upstream/main
   ```
2. **Run tests** — ensure all tests pass:
   ```bash
   npm test
   # or
   pytest
   ```
3. **Run the linter** — fix all linting errors before opening a PR.
4. **Write tests** — new features and bug fixes should include tests.

### Opening a PR

1. Push your feature branch to your fork:
   ```bash
   git push origin feat/<your-feature>
   ```
2. Open a Pull Request against the `main` branch.
3. Fill in the PR template, including:
   - A clear description of what changes were made and why
   - References to related issues (e.g., `Closes #42`)
   - Screenshots or recordings for UI changes

### Review Process

- At least **one approval** is required before merging.
- Address all review comments before requesting a re-review.
- The PR author is responsible for merging once approved.
- Use **Squash and Merge** to keep the `main` history clean.

### After Merging

- Delete the feature branch after merging.
- Close any related issues if not automatically closed by the PR.

---

## Reporting Issues

- Search [existing issues](https://github.com/serenity-demos/taskflow/issues) before opening a new one.
- Use the appropriate issue template (bug report, feature request).
- Include as much context as possible: OS, version, steps to reproduce, expected vs actual behavior.

---

## Code of Conduct

Please be respectful and constructive in all interactions. We are committed to providing a welcoming and inclusive environment for everyone.

---

*Thank you for contributing to TaskFlow! 🚀*
