# Instructions for Claude

This file contains helpful information and commands for Claude to assist with the v2a project.

## Contribution Workflow

When making changes to the codebase:

1. **Always use feature branches**:
   ```bash
   # Create a new branch for each feature/change
   git checkout -b feature/descriptive-name
   ```

2. **Make focused, atomic commits**:
   ```bash
   # Stage your changes
   git add path/to/changed/files
   
   # Create a descriptive commit
   git commit -m "[type] Clear description of changes"
   ```

3. **Submit changes via PR**:
   ```bash
   # Push feature branch
   git push -u origin feature/descriptive-name
   
   # Create PR using gh cli
   gh pr create --title "Descriptive title" --body "Detailed description"
   ```

4. **Address PR feedback**:
   - When the user comments on a PR with feedback, make additional commits to address the comments
   - Push the changes to the same feature branch
   - Mention which feedback was addressed in commit messages

## Project Overview
v2a is a Python package that converts video files to audio files in MP3 format. It features:
- Command-line interface
- Python API
- Optional S3 upload and AWS Transcribe integration
- Homebrew formula for easy installation

## Important Commands

### Development

```bash
# Install dev dependencies
pip install -e ".[dev]"

# Run tests
pytest

# Run tests with coverage
pytest --cov=v2a

# Type checking
mypy .

# Linting
ruff check .
ruff format .

# Install pre-commit hooks
pre-commit install
```

### Release Process

```bash
# Bump version (patch, minor, major)
./scripts/bump_version.py patch

# Push changes and tags
git push && git push origin --tags
```

## Code Style Preferences

- Use double quotes for strings
- Line length: 100 characters
- Use pathlib for file operations
- Include type annotations for all functions
- Place imports in this order: standard library, third-party, local
- Use f-strings for string formatting

## Project Structure

- `v2a/`: Main package
  - `__init__.py`: Package initialization and version
  - `cli.py`: Command-line interface
  - `core.py`: Core functionality
- `tests/`: Test suite
- `scripts/`: Utility scripts
- `.github/workflows/`: CI/CD workflows

## Frequently Used Tasks

### Adding a new feature

1. Create a feature branch: `git checkout -b feature/name`
2. Implement the feature in the appropriate module
3. Add tests in the tests directory
4. Ensure tests, type checking, and linting pass
5. Create a PR through GitHub

### Releasing a new version

1. Run version bump script: `./scripts/bump_version.py patch`
2. Push changes: `git push && git push origin --tags`
3. GitHub Actions will automatically:
   - Create a GitHub release
   - Update the Homebrew formula