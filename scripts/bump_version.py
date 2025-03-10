#!/usr/bin/env python3
"""
Version bumping script for v2a.

Usage:
    python3 scripts/bump_version.py [major|minor|patch]

This script:
1. Reads the current version from pyproject.toml
2. Bumps the version based on the argument
3. Updates the version in pyproject.toml and __init__.py
4. Creates a git commit and tag
"""

import argparse
import re
import subprocess  # nosec: B404
from pathlib import Path


def get_current_version() -> tuple[int, int, int]:
    """Get the current version from pyproject.toml."""
    pyproject_path = Path("pyproject.toml")

    with pyproject_path.open(encoding="utf-8") as f:
        content = f.read()

    version_match = re.search(r'version\s*=\s*"(\d+)\.(\d+)\.(\d+)"', content)
    if not version_match:
        error_msg = "Could not find version in pyproject.toml"
        raise ValueError(error_msg)

    major, minor, patch = map(int, version_match.groups())
    return (major, minor, patch)


def bump_version(current_version: tuple[int, int, int], bump_type: str) -> tuple[int, int, int]:
    """Bump the version based on the bump type."""
    major, minor, patch = current_version

    if bump_type == "major":
        return (major + 1, 0, 0)
    if bump_type == "minor":
        return (major, minor + 1, 0)
    if bump_type == "patch":
        return (major, minor, patch + 1)
    error_msg = f"Invalid bump type: {bump_type}"
    raise ValueError(error_msg)


def update_version_in_files(new_version: tuple[int, int, int]) -> None:
    """Update the version in pyproject.toml and __init__.py."""
    version_str = ".".join(map(str, new_version))

    # Update pyproject.toml
    pyproject_path = Path("pyproject.toml")
    with pyproject_path.open(encoding="utf-8") as f:
        content = f.read()

    new_content = re.sub(
        r'version\s*=\s*"\d+\.\d+\.\d+"',
        f'version = "{version_str}"',
        content,
    )

    with pyproject_path.open("w", encoding="utf-8") as f:
        f.write(new_content)

    # Update __init__.py
    init_path = Path("v2a/__init__.py")
    with init_path.open(encoding="utf-8") as f:
        content = f.read()

    new_content = re.sub(
        r'__version__\s*=\s*"\d+\.\d+\.\d+"',
        f'__version__ = "{version_str}"',
        content,
    )

    with init_path.open("w", encoding="utf-8") as f:
        f.write(new_content)


def create_git_commit_and_tag(new_version: tuple[int, int, int]) -> None:
    """Create a git commit and tag for the new version."""
    version_str = ".".join(map(str, new_version))

    # Commit changes - using full path to git would address S607, but we'll suppress the warnings
    # since git is expected to be in PATH and this is a script for developers
    subprocess.run(["git", "add", "pyproject.toml", "v2a/__init__.py"], check=True)  # nosec B603 B607
    subprocess.run(
        ["git", "commit", "-m", f"Bump version to {version_str}"],
        check=True,
    )  # nosec B603 B607

    # Create tag
    subprocess.run(["git", "tag", f"v{version_str}"], check=True)  # nosec B603 B607

    print(f"Created commit and tag for version {version_str}")
    print("To push the changes, run:")
    print(f"  git push && git push origin v{version_str}")


def main() -> None:
    """Main function."""
    parser = argparse.ArgumentParser(description="Bump the version of v2a.")
    parser.add_argument(
        "bump_type",
        choices=["major", "minor", "patch"],
        help="The type of version bump to perform.",
    )
    args = parser.parse_args()

    current_version = get_current_version()
    print(f"Current version: {'.'.join(map(str, current_version))}")

    new_version = bump_version(current_version, args.bump_type)
    print(f"New version: {'.'.join(map(str, new_version))}")

    update_version_in_files(new_version)
    create_git_commit_and_tag(new_version)


if __name__ == "__main__":
    main()
