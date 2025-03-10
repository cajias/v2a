"""Core functionality for Video to Audio Converter."""

import asyncio
from collections.abc import Iterable
from pathlib import Path
from typing import Any, TypeVar

T = TypeVar("T")

try:
    import ffmpeg
    HAS_FFMPEG = True
except ImportError:
    HAS_FFMPEG = False

# Import tqdm if available, otherwise provide a minimal implementation
try:
    from tqdm import tqdm  # type: ignore
    HAS_TQDM = True
except ImportError:
    HAS_TQDM = False
    
    # Simple replacement for tqdm
    def _simple_tqdm(iterable: Iterable[T], **_kwargs: Any) -> Iterable[T]:
        """Simple progress replacement when tqdm is not available."""
        return iterable
    
    tqdm = _simple_tqdm  # type: ignore

try:
    import aioboto3
    HAS_AIOBOTO3 = True
except ImportError:
    HAS_AIOBOTO3 = False


async def upload_file_to_s3(bucket_name: str, file_name: str, file_path: str) -> None:
    """Upload a file to an S3 bucket.

    Args:
        bucket_name: The name of the S3 bucket.
        file_name: The name to give to the file in the S3 bucket.
        file_path: The local path of the file to upload.
    """
    if not HAS_AIOBOTO3:
        msg = "aioboto3 is required for S3 uploads"
        raise ImportError(msg)
        
    async with aioboto3.client("s3") as s3:  # type: ignore
        await s3.upload_file(file_path, bucket_name, file_name)


async def transcribe_file_async(bucket_name: str, file_name: str) -> dict:
    """Transcribe a media file using AWS Transcribe.

    Args:
        bucket_name: The name of the S3 bucket where the media file is stored.
        file_name: The name of the media file to transcribe.

    Returns:
        The transcription result.
    """
    if not HAS_AIOBOTO3:
        msg = "aioboto3 is required for transcription"
        raise ImportError(msg)
        
    async with aioboto3.client("transcribe", region_name="us-west-2") as transcribe_client:  # type: ignore
        job_name = f"transcribeJob{int(asyncio.get_event_loop().time())}"
        job_uri = f"s3://{bucket_name}/{file_name}"

        await transcribe_client.start_transcription_job(
            TranscriptionJobName=job_name,
            Media={"MediaFileUri": job_uri},
            MediaFormat=file_name.split(".")[-1],
            LanguageCode="en-US",
        )

        while True:
            status = await transcribe_client.get_transcription_job(TranscriptionJobName=job_name)
            if status["TranscriptionJob"]["TranscriptionJobStatus"] in {"COMPLETED", "FAILED"}:
                break
            print("Not ready yet...")
            await asyncio.sleep(5)

        return dict(status)


def extract_audio(input_folder: str, output_folder: str) -> None:
    """Extract audio from video files in the input folder and save as MP3 files.

    Args:
        input_folder: Path to the folder containing input video files.
        output_folder: Path to the folder where audio files will be saved.
    """
    if not HAS_FFMPEG:
        msg = "ffmpeg-python is required for audio extraction"
        raise ImportError(msg)
    
    output_path = Path(output_folder)
    if not output_path.exists():
        output_path.mkdir(parents=True)

    input_path = Path(input_folder)
    files = [f for f in input_path.iterdir() if f.is_file()]
    total_files = len(files)

    if total_files == 0:
        print("No files found in the input folder.")
        return

    for file in tqdm(files, desc="Converting files", unit="file"):
        output_file = output_path / f"{file.stem}.mp3"

        try:
            # Try to probe the file to check if it's a valid video/audio file
            ffmpeg.probe(str(file))  # type: ignore
            # If valid, proceed with conversion
            (
                ffmpeg.input(str(file))  # type: ignore
                .output(str(output_file), codec="libmp3lame")
                .run(overwrite_output=True)
            )
        except (ffmpeg.Error, OSError) as e:  # type: ignore
            print(f"Skipping {file.name}: Not a valid media file or conversion error. Error: {e}")

    print("Conversion completed.")