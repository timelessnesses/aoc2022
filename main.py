import os
import sys

print("AOC 2022")

<<<<<<< HEAD
sys.argv.append("day_4") # default for rn
=======
sys.argv.append("day_3")  # default for rn
>>>>>>> origin/main

if sys.argv[1] not in [f"day_{x}" for x in range(30)]:
    raise ValueError("Invalid day")

os.system(sys.executable + f" {sys.argv[1]}/main.py")
