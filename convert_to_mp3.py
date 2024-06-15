import os
import sys
import subprocess
import pkg_resources

# List of required packages
required = {'tqdm', 'ffmpeg-python'}

# Check and install missing packages
installed = {pkg.key for pkg in pkg_resources.working_set}
missing = required - installed

if missing:
    print(f"Installing missing packages: {', '.join(missing)}")
    python = sys.executable
    subprocess.check_call([python, '-m', 'pip', 'install', *missing], stdout=subprocess.DEVNULL)

import ffmpeg
from tqdm import tqdm

def convert_to_mp3(input_folder, output_folder):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    files = [f for f in os.listdir(input_folder) if f.endswith(('.m4a', '.mp4'))]
    total_files = len(files)

    if total_files == 0:
        print("No M4A or MP4 files found in the input folder.")
        return

    for file in tqdm(files, desc="Converting files", unit="file"):
        input_path = os.path.join(input_folder, file)
        output_path = os.path.join(output_folder, os.path.splitext(file)[0] + '.mp3')

        try:
            ffmpeg.input(input_path).output(output_path, codec='libmp3lame').run(overwrite_output=True)
        except ffmpeg.Error as e:
            print(f"Error converting {file}: {e}")

    print("Conversion completed.")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python convert_to_mp3.py <input_folder> <output_folder>")
    else:
        input_folder = sys.argv[1]
        output_folder = sys.argv[2]
        convert_to_mp3(input_folder, output_folder)