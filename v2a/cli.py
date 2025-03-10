"""Command-line interface for Video to Audio Converter."""

import argparse
import sys
from collections.abc import Sequence
from typing import Optional

from v2a.core import extract_audio


def parse_args(args: Optional[Sequence[str]] = None) -> argparse.Namespace:
    """Parse command line arguments.

    Args:
        args: Command line arguments. Defaults to sys.argv[1:].

    Returns:
        Parsed arguments.
    """
    parser = argparse.ArgumentParser(description="Convert video/audio files to MP3 format.")
    parser.add_argument("-b", "--bucket", help="Name of the S3 bucket to store media files.")
    parser.add_argument("-r", "--region", help="AWS region where the S3 bucket is located.")
    parser.add_argument("-i", "--input", required=True, help="Input folder containing media files.")
    parser.add_argument("-o", "--output", required=True, help="Output folder for MP3 files.")

    return parser.parse_args(args)


def main(args: Optional[Sequence[str]] = None) -> int:
    """Run the command-line interface.

    Args:
        args: Command line arguments. Defaults to sys.argv[1:].

    Returns:
        Exit code.
    """
    parsed_args = parse_args(args)
    try:
        extract_audio(parsed_args.input, parsed_args.output)
    except Exception as e:  # noqa: BLE001
        print(f"Error: {e}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())