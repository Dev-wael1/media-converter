import ffmpeg
import os

def convert_media(input_file, output_file):
    try:
        # Run ffmpeg to convert the input file to the output format
        ffmpeg.input(input_file).output(output_file).run()
        print(f"Conversion complete: {output_file}")
    except ffmpeg.Error as e:
        print(f"Error during conversion: {e.stderr.decode()}")
    except Exception as ex:
        print(f"An unexpected error occurred: {ex}")

def get_output_filename(input_file, output_format):
    # Get the input filename without the extension
    base_name = os.path.splitext(input_file)[0]
    # Create the new filename with the desired output format
    return f"{base_name}.{output_format}"

if __name__ == "__main__":
    input_file = input("Enter the path to the input file: ")
    output_format = input("Enter the desired output format (e.g., mp4, mp3, mkv): ")

    # Create the output filename
    output_file = get_output_filename(input_file, output_format)
    
    # Convert the media file
    convert_media(input_file, output_file)