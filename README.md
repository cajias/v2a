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

