import argparse

from lib import extract_audio, install_if_missing

install_if_missing('tqdm')

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Convert video/audio files to MP3 format.")
    parser.add_argument('-i', '--input', required=True, help="Path to the input folder containing media files.")
    parser.add_argument('-o', '--output', required=True,
                        help="Path to the output folder where MP3 files will be saved.")

    args = parser.parse_args()

    extract_audio(args.input, args.output)
