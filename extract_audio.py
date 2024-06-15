import argparse
import os

import ffmpeg
from tqdm import tqdm


def extract_audio(input_folder: str, output_folder: str):
    """Extract audio from video files in the input folder and save as MP3 files in the output folder."""

    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    files = [f for f in os.listdir(input_folder) if os.path.isfile(os.path.join(input_folder, f))]
    total_files = len(files)

    if total_files == 0:
        print("No files found in the input folder.")
        return

    for file in tqdm(files, desc="Converting files", unit="file"):
        input_path = os.path.join(input_folder, file)
        output_path = os.path.join(output_folder, os.path.splitext(file)[0] + '.mp3')

        try:
            # Try to probe the file to check if it's a valid video/audio file
            ffmpeg.probe(input_path)
            # If valid, proceed with conversion
            ffmpeg.input(input_path).output(output_path, codec='libmp3lame').run(overwrite_output=True)
        except ffmpeg.Error as e:
            print(f"Skipping {file}: Not a valid video/audio file or conversion error. Error: {e}")

    print("Conversion completed.")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Convert video/audio files to MP3 format.")
    parser.add_argument('-i', '--input', required=True, help="Path to the input folder containing media files.")
    parser.add_argument('-o', '--output', required=True,
                        help="Path to the output folder where MP3 files will be saved.")

    args = parser.parse_args()

    extract_audio(args.input, args.output)
