# v2a - Video to Audio Converter

This project contains a Python package that converts video files to audio files. It specifically converts video files to `.mp3` format.

[![Python Tests](https://github.com/cajias/v2a/actions/workflows/python-tests.yml/badge.svg)](https://github.com/cajias/v2a/actions/workflows/python-tests.yml)

## Prerequisites

- Python 3.12+
- ffmpeg (system dependency)

## Installation

### From PyPI

```bash
pip install v2a
```

### From Source

1. Clone this repository: 
```bash
git clone https://github.com/cajias/v2a.git
cd v2a
```

2. Install the package in development mode:
```bash
pip install -e ".[dev]"
```

## Usage

### Command Line

After installation, you can use the command-line interface:

```bash
v2a -i <input_folder> -o <output_folder>
```

Or with optional S3 upload:

```bash
v2a -i <input_folder> -o <output_folder> -b <bucket_name> -r <region>
```

### As a Python Package

```python
from v2a.core import extract_audio

extract_audio("input_folder", "output_folder")
```

## Development

### Setup Development Environment

```bash
# Clone the repository
git clone https://github.com/cajias/v2a.git
cd v2a

# Install development dependencies
pip install -e ".[dev]"

# Install pre-commit hooks
pre-commit install
```

### Running Tests

```bash
pytest
```

### Type Checking

```bash
mypy .
```

### Linting

```bash
ruff check .
ruff format .
```

## Release Process

The project includes an automated release process that:

1. Creates GitHub releases when version tags are pushed
2. Updates the Homebrew formula in [cajias/homebrew-tools](https://github.com/cajias/homebrew-tools)

### Creating a New Release

```bash
# Bump the version (patch, minor, or major)
./scripts/bump_version.py patch

# Push the changes and tag
git push && git push origin --tags
```

This will:
1. Increase the version number in both `pyproject.toml` and `v2a/__init__.py`
2. Create a git commit and tag
3. When pushed, GitHub Actions will:
   - Create a new GitHub release
   - Update the Homebrew formula with the new version

### Installing from Homebrew

```bash
# Add the tap (first time only)
brew tap cajias/tools

# Install the package
brew install v2a
```

