import os
import sys
import subprocess
import shutil

def adjust_volume(file_path, volume_factor):
    subprocess.run(['ffmpeg', '-i', file_path, '-filter:a', f'volume={volume_factor}', '-y', 'o.wav'])
    shutil.move('o.wav', file_path)

def adjust_volume_for_directory(directory, volume_factor):
    # Create a backup of the input directory with "_old" suffix
    backup_directory = f"{directory}_old"
    shutil.copytree(directory, backup_directory)

    for file_name in os.listdir(directory):
        file_path = os.path.join(directory, file_name)
        if file_name.endswith(('.mp3', '.wav', '.aac', '.flac', '.ogg')):
            adjust_volume(file_path, volume_factor)

if len(sys.argv) != 3:
    print("Usage: python adj_vol.py <directory> <volume_factor>")
    sys.exit(1)

input_directory = sys.argv[1]
volume_factor = float(sys.argv[2])  # Convert to float

adjust_volume_for_directory(input_directory, volume_factor)


print(f"{input_directory} adjusted to {volume_factor}")
