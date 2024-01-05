import subprocess
import shutil
import os
import sys
import linecache


# Figures out Audio duration
def probe(file_path):
    result = subprocess.run(["ffprobe", "-i", file_path, "-show_entries", "format=duration", "-v", "quiet", "-of", "csv=p=0"], capture_output=True, text=True)
    return float(result.stdout.strip())


# Shrinks Audio based on metadata difference
def shrink(duration, file_path):
    subprocess.run(["ffmpeg", "-t", str(duration), "-i", file_path, "o.wav"])
    shutil.move("o.wav", file_path)
    
# Does the opposite lol    
def extend(current_duration, uniform_duration, file_path):
    difference = abs(current_duration - uniform_duration)

    # Remove existing o.wav, if any
    try:
        shutil.rmtree("o.wav")
    except FileNotFoundError:
        pass

    subprocess.run(["ffmpeg", "-i", file_path, "-af", f"apad=pad_dur={difference}", "o.wav"])
    shutil.move("o.wav", file_path)
    
# Determine Method
def det(current_duration, uniform_duration, file_path):
    if current_duration > uniform_duration:
        shrink(uniform_duration, file_path)
    elif current_duration < uniform_duration:
        extend(current_duration, uniform_duration, file_path)
    else:
        # If they are equal, do nothing
        pass
        

# Check if the correct number of command-line arguments is provided
if len(sys.argv) != 2:
    print("Usage: python correct_vo.py <survivor>")
    sys.exit(1)

# First argument is the survivor directory
survivor = sys.argv[1]

# Loop variables
counter = 1

# File paths
file_listing = os.path.join("meta", "fl")
durations_meta = os.path.join("meta", "durg")

if not os.path.exists(file_listing):
    print(f"Error: {file_listing} does not exist.")
    sys.exit(1)

if not os.path.exists(durations_meta):
    print(f"Error: {durations_meta} does not exist.")
    sys.exit(1)

# Calculate the number of lines in fl.txt
limmy = sum(1 for _ in open(file_listing))

try:
    # Loop
    while counter != limmy:
        # Read values from files
        audio = os.path.join(survivor, linecache.getline(file_listing, counter).strip())
        if not os.path.exists(audio):
            print(f"Warning: {audio} does not exist. Skipping loop iteration {counter}.")
            counter += 1
            continue
            
        uniform_duration = float(linecache.getline(durations_meta, counter).strip())

        current_duration = probe(audio)
        det(current_duration, uniform_duration, audio)
        counter += 1

except Exception as e:
    print(f"An error occurred: {e}")
    sys.exit(1)  # Exit with a non-zero status code indicating an error

print("Duration successfully corrected.")
sys.exit(0)  # Exit with a status code of 0 for successful execution



    
 

