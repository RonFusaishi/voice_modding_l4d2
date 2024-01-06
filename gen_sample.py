import os
import random
import sys
import linecache
import shutil

# Command-line arguments
survivor = os.sys.argv[1]
character = os.sys.argv[2]



# Define metadata path
file_list = os.path.join("meta", "fl")

# Check if meta directory exists
if not os.path.exists(file_list):
    print(f"Error: '{file_list}' does not exist.")
    sys.exit(69)


# Assumes character has a generic folder
gen_dir = os.path.join(character, "generic")

# Check if generic directory exists
if not os.path.exists(gen_dir):
    print(f"Error: '{gen_dir}' does not exist.")
    sys.exit(69)

# Create a directory with the name specified in 'survivor'
os.makedirs(survivor, exist_ok=True)


# Determine the number of lines in the 'fl' file
with open(file_list, 'r') as file:
    loop_end = sum(1 for _ in file)

# Define the RNG function
def rng():
    return random.randint(0, len(os.listdir(gen_dir)) - 1)
    
    
counter = 1

while counter <= loop_end:
    seed = rng()
    audio = linecache.getline(file_list, counter).strip()

    vline = os.path.join(gen_dir, f"{character}{seed}.wav")
    destination_path = os.path.join(survivor, audio)

    # Copy the audio file to the 'survivor' directory
    try:
        shutil.copy2(vline, destination_path)
        print(f"Copied: {vline} to {destination_path}")
    except FileNotFoundError:
        print(f"Error: File not found - {vline}")

    counter += 1

print(f"Generic {survivor} has been created.")
sys.exit(0)

