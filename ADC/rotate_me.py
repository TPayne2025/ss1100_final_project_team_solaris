import random
import os
import sys
import pathlib

script_dir = pathlib.Path(__file__).parent #Gemini AI used to fix file path 
file_name =str(script_dir / "current_state.txt")


def generate_initial_state():
    # Use the same range as the fallback logic (0 to 360)
    return (random.randint(0, 360), random.randint(0, 360), random.randint(0, 360))

if not os.path.exists(file_name): 
    initial_orientation = generate_initial_state()
    initial_line = ','.join(map(str, initial_orientation))
    with open(file_name, 'w') as f:
        f.write(initial_line)

def apply_corrections(current_orientation, corrections):
    random_factor = random.uniform(0.95, 1.05)
    new_tuple = (
        current_orientation[0] + corrections[0] * random_factor,
        current_orientation[1] + corrections[1] * random_factor,
        current_orientation[2] + corrections[2] * random_factor
    )
    return new_tuple
