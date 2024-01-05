import sys
import subprocess
import linecache
import shutil
import os


# File paths
survivor = sys.argv[1]
file_list = os.path.join("meta", "fl")
sample_rates_meta = os.path.join("meta", "sr")

if len(sys.argv) != 2:
    print("Usage: python fix_vo.py <survivor>")
    sys.exit(1)

# How many lines does file_list have?
with open(file_list, 'r') as file:
    limmy = sum(1 for _ in file)
    
   


def probe(file_path):
    result = subprocess.run(['ffprobe', '-i', file_path, '-show_entries', 'format=duration', '-v', 'quiet', '-of', 'csv=p=0'], capture_output=True, text=True)
    return result.stdout.strip()

try:    
    counter = 1
    while counter != limmy:
        audio = os.path.join(survivor, linecache.getline(file_list, counter).strip())

        if not os.path.exists(audio):
            print(f"{audio} Doesn't Exist, Skipping")
            counter += 1
            continue

        sample_rate = linecache.getline(sample_rates_meta, counter).strip()

        subprocess.run(['ffmpeg', '-i', audio, '-ac', '1', '-ar', sample_rate, 'o.wav'])
        shutil.move('o.wav', audio)

        counter += 1

except Exception as e:
    print(f"An error occurred: {e}")
    sys.exit(1)  # Exit with a non-zero status code indicating an error

print("Audio successfully Fixed.")
sys.exit(0)  # Exit with a status code of 0 for successful execution


