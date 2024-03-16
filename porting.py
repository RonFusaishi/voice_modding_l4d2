import os
import sys
import shutil

if len(sys.argv) < 2:
    print("Usage: python porting.py <survivor>")
    sys.exit(1)

input_dir = sys.argv[1]
output_dir = input_dir + "_port"
file_list_path = os.path.join("..", "meta", "fl")  # Adjusted the file path

# Ensure output_dir exists
if not os.path.exists(output_dir):
    os.makedirs(os.path.join(input_dir, output_dir))
    print(f"Created directory: {output_dir}")

# Change directory to input_dir
os.chdir(input_dir)

# Read file names from the file_list_path
with open(file_list_path, 'r') as file:
    file_list = file.read().splitlines()

# Move files from input_dir to output_dir
for filename in file_list:
    src = filename  # Assuming filenames are relative to meta_dir
    dst = os.path.join(output_dir, filename)
    try:
        shutil.move(src, dst)
    except FileNotFoundError:
        continue

    print(f"Moved {src} to {dst}")

# Move output_dir back to the parent directory
shutil.move(output_dir, "..")
print(f"Moved {output_dir} back to parent directory")
