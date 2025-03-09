"""Tests for the CLI functionality of the v2a package."""

from unittest.mock import Mock, patch

from v2a.cli import main, parse_args


def test_parse_args() -> None:
    """Test that argument parsing works correctly."""
    args = parse_args(["-i", "input_dir", "-o", "output_dir"])
    assert args.input == "input_dir"
    assert args.output == "output_dir"
    assert args.bucket is None
    assert args.region is None

    args = parse_args(["-i", "input_dir", "-o", "output_dir", "-b", "my-bucket", "-r", "us-west-2"])
    assert args.input == "input_dir"
    assert args.output == "output_dir"
    assert args.bucket == "my-bucket"
    assert args.region == "us-west-2"


@patch("v2a.cli.extract_audio")
def test_main_success(mock_extract_audio: Mock) -> None:
    """Test that main function works correctly."""
    result = main(["-i", "input_dir", "-o", "output_dir"])
    assert result == 0
    mock_extract_audio.assert_called_once_with("input_dir", "output_dir")


@patch("v2a.cli.extract_audio")
def test_main_error(mock_extract_audio: Mock) -> None:
    """Test that main function handles errors correctly."""
    mock_extract_audio.side_effect = Exception("Test error")
    result = main(["-i", "input_dir", "-o", "output_dir"])
    assert result == 1