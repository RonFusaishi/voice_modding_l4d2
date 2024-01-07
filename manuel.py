import os
import random
import shutil
import sys
import linecache


if len(sys.argv) != 3:
    print("Usage: python manuel.py <dictionary> <character>")
    sys.exit(1)
    
# Command-line arguments
dictionary = sys.argv[1]
character = sys.argv[2]


# Assumes character has sample for this dictionary
samples_dir = os.path.join(character, dictionary)

# Counting lines in the dictionary file
with open(dictionary, 'r') as file:
    loop_end = sum(1 for line in file)

# Random Number Generator Function
def rng():
    return random.randint(0, len(os.listdir(samples_dir)) - 1)
    
# Counter initialization
counter = 1

# Create 'man' directory if it doesn't exist
man_directory = 'man'
os.makedirs(man_directory, exist_ok=True)

# Loop
while counter <= loop_end:
    # Read the current line from the dictionary file using linecache
    audio = linecache.getline(dictionary, counter).strip()

    # Generate a random seed
    seed = rng()

    # Form the path to the selected audio file
    vlines = os.path.join(samples_dir, f"{character}{seed}.wav")

    # Copy the audio file to 'man' directory with verbosity
    destination_path = os.path.join(man_directory, audio)
    
    try:
        shutil.copy2(vlines, destination_path)
        print(f"Copied: {vlines} to {destination_path}")
    except FileNotFoundError:
        print(f"Error: File not found - {vlines}")


    # Increment the counter
    counter += 1    


print(f"{dictionary} has been distributed to the man folder.")
