# v2a - Video to Audio Converter

This project contains a Python script that converts video files to audio files. It specifically converts `.m4a` and `.mp4` files to `.mp3` format.

## Prerequisites

- Python 3
- ffmpeg-python
- tqdm

## Installation

1. Clone this repository: 
```bash
git clone https://github.com/cajias/v2a.git
cd v2a
```

3. Install the required Python packages:
```bash
pip install -r requirements.txt
```

## Usage

To use the script, navigate to the directory containing the script and run the following command:

```bash
python extract_audio.py <input_folder> <output_folder>
```

Where `<input_folder>` is the folder containing the video files to be converted and `<output_folder>` is the folder where the converted audio files will be saved.

