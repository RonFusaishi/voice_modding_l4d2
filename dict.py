import os
import re
import sys


# Check if the correct number of command-line arguments are provided
if len(sys.argv) != 3:
    print("Usage: python dict.py <pattern> <output_file_path>")
    sys.exit(1)

# Get command-line arguments
pattern_str = sys.argv[1]
output_file_path = sys.argv[2]

# Compile the pattern
pattern = re.compile(pattern_str)

# Define the path to the file
file_path = os.path.join('meta', 'fl')

try:
    with open(file_path, 'r') as input_file:
        limmy = input_file.readlines()

    # Filter lines containing the specified pattern
    filtered_lines = [line for line in limmy if pattern.search(line)]

    # Write the filtered lines to the specified output file
    with open(output_file_path, 'w') as output_file:
        output_file.writelines(filtered_lines)

finally:
    # Close all file operations before exiting
    if 'input_file' in locals() and not input_file.closed:
        input_file.close()

    if 'output_file' in locals() and not output_file.closed:
        output_file.close()

