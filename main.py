import os
import sys

print("AOC 2022")

sys.argv.append("day_5")  # default for rn

if sys.argv[1] not in [f"day_{x+1}" for x in range(25)]:
    raise ValueError("Invalid day")

os.system(sys.executable + f" {sys.argv[1]}/main.py")
