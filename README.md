
# Media Converter

A Python-based media converter that uses FFmpeg to convert video and audio files between various formats, such as MKV, MP4, MP3, and more.

## Features

- Convert between different video formats (e.g., MKV to MP4)
- Convert between different audio formats (e.g., MP3 to WAV)
- Supports a wide range of media formats
- Simple command-line interface

## Prerequisites

- **FFmpeg**: The project relies on FFmpeg. Install it from [FFmpeg's official website](https://ffmpeg.org/download.html) and ensure it's available in your system's PATH.
- **Python**: Ensure you have Python 3.6 or later installed.
- **ffmpeg-python**: The Python wrapper for FFmpeg. Install it using pip.

## Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/Dev-wael1/media-converter.git
   cd media-converter
   ```

2. **Install dependencies:**

   ```bash
   pip install ffmpeg-python
   ```

## Usage

1. **Run the script:**

   ```bash
   python media_converter.py
   ```

2. **Follow the prompts:**

   - Enter the path to the input file.
   - Enter the desired output format (e.g., `mp4`, `mp3`).

   The script will create a converted file with the specified format in the same directory as the input file.

## Example

To convert `example.mkv` to `example.mp4`, run the script and provide `example.mkv` as the input file and `mp4` as the desired format.

## Troubleshooting

- **FFmpeg not found**: Ensure FFmpeg is installed and added to your system's PATH.
- **Conversion errors**: Check the error messages in the console for details. They may provide information on unsupported formats or other issues.

## Contributing

Feel free to submit issues, suggest improvements, or contribute code via pull requests. Please follow the contribution guidelines in the `CONTRIBUTING.md` file.

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.

## Contact

For questions or feedback, you can reach me at [mrwael13@outlook.com](mailto:your-email@example.com).

