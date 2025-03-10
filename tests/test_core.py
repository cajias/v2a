"""Tests for the core functionality of the v2a package."""

import tempfile
from pathlib import Path
from unittest.mock import MagicMock, Mock, patch

from v2a.core import extract_audio


def test_extract_audio_empty_folder() -> None:
    """Test that extract_audio handles empty folders correctly."""
    with tempfile.TemporaryDirectory() as input_dir, tempfile.TemporaryDirectory() as output_dir:
        extract_audio(input_dir, output_dir)
        # Should not raise an exception


@patch("v2a.core.ffmpeg")
@patch("v2a.core.Path.iterdir")
def test_extract_audio_conversion(mock_iterdir: Mock, mock_ffmpeg: Mock) -> None:
    """Test that extract_audio converts files correctly."""
    # Create a mock file
    mock_file = MagicMock(spec=Path)
    mock_file.is_file.return_value = True
    mock_file.stem = "test"
    mock_file.name = "test.mp4"

    # Set a safe temporary path
    temp_path = str(Path(tempfile.gettempdir()) / "test.mp4")
    mock_str = MagicMock(return_value=temp_path)
    # Use type ignoring for this test-only code
    mock_file.__str__ = mock_str  # type: ignore

    # Set up the mock to return our test file
    mock_iterdir.return_value = [mock_file]

    # Set up ffmpeg mocks
    mock_ffmpeg.probe.return_value = {}
    mock_ffmpeg.input.return_value.output.return_value.run = MagicMock()

    with tempfile.TemporaryDirectory() as input_dir, tempfile.TemporaryDirectory() as output_dir:
        extract_audio(input_dir, output_dir)

        # Check if ffmpeg was called correctly
        mock_ffmpeg.probe.assert_called_once()
        mock_ffmpeg.input.assert_called_once()
        mock_ffmpeg.input.return_value.output.assert_called_once()
        mock_ffmpeg.input.return_value.output.return_value.run.assert_called_once()
