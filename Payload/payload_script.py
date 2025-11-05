import numpy as np
# Note: Students might need to install matplotlib if they don't have it
# pip install matplotlib
import matplotlib.pyplot as plt

def load_and_combine_bands(red_file, green_file, blue_file):
    """
    Loads the raw R, G, and B band data from CSV files, ensures they are of
    the same dimensions, and combines them into a single RGB image.
    """
    # YOUR CODE HERE
    # Hint: Use np.loadtxt to load the CSV files and np.stack to combine them.
    return None

def convert_radiance_to_reflectance(rgb_image, k=0.8, b=0.1):
    """
    Converts radiance values to reflectance.
    """
    # YOUR CODE HERE
    return None

def rescale_to_8bit(reflectance_image):
    """
    Converts the floating point reflectance values to 8-bit integers (0-255).
    """
    # YOUR CODE HERE
    return None

def save_image(image, filename):
    """
    Saves the image to a file.
    """
    # YOUR CODE HERE
    # Hint: Use plt.imsave
    pass

def main():
    """
    Main function to process the remote sensing data.
    """
    # File paths for the CSV data
    red_file = 'red.csv'
    green_file = 'green.csv'
    blue_file = 'blue.csv'

    # Task 1: Load and combine bands
    radiance_image = load_and_combine_bands(red_file, green_file, blue_file)
    if radiance_image is not None:
        print("Successfully loaded and combined image bands.")
        # Optional: visualize the raw radiance image
        # plt.imshow(radiance_image)
        # plt.title("Radiance Image")
        # plt.show()

    # "Check Plus" Tasks
    # Task 2: Convert to reflectance
    reflectance_image = convert_radiance_to_reflectance(radiance_image)
    if reflectance_image is not None:
        print("Successfully converted to reflectance.")

    # Task 3: Rescale to 8-bit
    final_image = rescale_to_8bit(reflectance_image)
    if final_image is not None:
        print("Successfully rescaled to 8-bit.")

    # Task 4: Visualize and save the final image
    if final_image is not None:
        plt.imshow(final_image)
        plt.title("Final Processed Image")
        plt.show()
        save_image(final_image, 'final_image.png')
        print("Saved final image to final_image.png")

if __name__ == "__main__":
    main()
