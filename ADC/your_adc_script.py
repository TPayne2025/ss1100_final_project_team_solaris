import rotate_me
import calc_rotation as math_module #this is my student code module
import time
import math
import os


def main():
    """
    Main function to run the attitude control simulation.
    """
    target_orientation = (100, 200, 300)  # Desired target orientation
    tolerance = 0.1
    max_iterations = 20

    print(f"Target orientation: {target_orientation}")

    for i in range(max_iterations):
        print(f"\n--- Iteration {i+1} ---")
        current_orientation = rotate_me.read_orientation_from_file(rotate_me.file_name)
        print(f"Current orientation: ({current_orientation[0]:.2f}, {current_orientation[1]:.2f}, {current_orientation[2]:.2f})")

        # Check if we are within tolerance
        error = math.sqrt(sum([(c - t)**2 for c, t in zip(current_orientation, target_orientation)]))
        if error <= tolerance:
            print("Target orientation reached!")
            break
        input_list = [current_orientation, target_orientation]

        # Calculate the required corrections using imported student module
        corrections = math_module.orientation_error(input_list)
        print(f"Applying corrections: {corrections}")

        # Apply the corrections using the rotate_me script
        rotate_me.main(corrections)
        time.sleep(1) # Pause for a moment to see the result
    else:
        print("\nMax iterations reached. Could not reach target orientation.")

if __name__ == "__main__":
    main()
