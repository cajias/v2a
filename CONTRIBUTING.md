# Contributing to v2a

Thank you for your interest in contributing to v2a! This document outlines the process for contributing to this project.

## Contribution Process

We use a feature branch workflow with pull requests for all changes. Here's how to contribute:

### 1. Set Up Development Environment

```bash
# Clone the repository
git clone https://github.com/cajias/v2a.git
cd v2a

# Install development dependencies
pip install -e ".[dev]"

# Install pre-commit hooks
pre-commit install
```

### 2. Create a Feature Branch

Always create a feature branch for your changes:

```bash
git checkout -b feature/descriptive-name
```

Use a descriptive name that clearly indicates what you're working on, such as:
- `feature/add-wav-support`
- `bugfix/fix-mp3-encoding`
- `docs/update-readme`
- `refactor/improve-error-handling`

### 3. Make Changes

Follow these guidelines when making changes:

- Write clean, readable code following the project's code style
- Include type annotations for all functions
- Add tests for new functionality
- Update documentation as needed

Before committing, make sure your changes pass all checks:

```bash
# Run tests
pytest

# Type checking
mypy .

# Linting
ruff check .
ruff format .
```

### 4. Commit Your Changes

Make focused, atomic commits with clear messages:

```bash
git add path/to/changed/files
git commit -m "[type] Clear description of changes"
```

Commit message types:
- `[feature]` - New functionality 
- `[fix]` - Bug fixes
- `[docs]` - Documentation updates
- `[refactor]` - Code refactoring without functionality changes
- `[test]` - Adding or improving tests
- `[chore]` - Maintenance tasks, dependency updates, etc.

### 5. Submit a Pull Request

Push your branch and create a pull request:

```bash
git push -u origin feature/descriptive-name
```

Then use GitHub's interface or the GitHub CLI to create a PR:

```bash
gh pr create --title "Descriptive title" --body "Detailed description of changes"
```

In your PR description:
- Explain what changes you've made and why
- Reference any related issues
- Describe how to test the changes
- Note any potential concerns or questions

### 6. Address Feedback

If reviewers request changes:
1. Make the requested changes on your feature branch
2. Commit and push the changes
3. Respond to the feedback in the PR conversation

### 7. Merge

Once your PR is approved, it will be merged into the main branch.

## Code Style

- Use double quotes for strings
- Line length: 100 characters
- Use pathlib for file operations
- Include type annotations for all functions
- Place imports in this order: standard library, third-party, local
- Use f-strings for string formatting

## Release Process

Releases are managed by the maintainers using the version bumping script:

```bash
./scripts/bump_version.py patch  # or minor or major
git push && git push origin --tags
```

The GitHub Actions workflows will automatically create a GitHub release and update the Homebrew formula.

## Questions?

If you have any questions or need help, please open an issue on GitHub.