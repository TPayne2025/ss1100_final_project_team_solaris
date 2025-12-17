# For the entire Payload section, Gemini was utilized to develop all of the coding lines below.  
# However, this only occured after about an 2 hours of various attempts at creating a lines of code to process the data.
# Additionally, this code was developed in google colab


import numpy as np
import matplotlib.pyplot as plt

# Determine File Paths
red_data_path = '/content/red.csv'
green_data_path = '/content/green.csv'
blue_data_path = '/content/blue.csv'

# Assuming the CSV files are in the same directory as the script
# Using genfromtxt which is more robust to missing values,
# filling empty strings with NaN (Not a Number)
red_data = np.genfromtxt(red_data_path, delimiter=',', filling_values=np.nan)
green_data = np.genfromtxt(green_data_path, delimiter=',', filling_values=np.nan)
blue_data = np.genfromtxt(blue_data_path, delimiter=',', filling_values=np.nan)

# Optional check:
if not (red_data.shape == green_data.shape and red_data.shape == blue_data.shape):
  print("Error: Band dimensions do not match.")
  # Removed 'return' as it causes SyntaxError outside a function

# Stacking along a new axis (axis=2) creates an image array of shape (rows, columns, 3)
rgb_image_radiance = np.stack([red_data, green_data, blue_data], axis=2)

def visualize_image(image_array, title="RGB Radiance Image"):
    """Visualizes a given image array."""
    # Matplotlib often requires floating-point data to be normalized/scaled between [0, 1]
    # Here, we normalize by the max value in the radiance image for visualization.
    # Handle NaN values if they exist, so np.max() doesn't return NaN.
    max_radiance = np.nanmax(image_array)
    normalized_image = image_array / max_radiance

    plt.figure(figsize=(8, 8))
    plt.imshow(normalized_image)
    plt.title(title)
    plt.axis('off')  # Hide axes for a cleaner image
    plt.show()

# Visualize the combined radiance image
visualize_image(rgb_image_radiance, title="Raw Combined Radiance Image")

ef radiance_to_reflectance(radiance_image, k, b):
    """
    Converts radiance image (L) to reflectance image (R) using R = k*L + b.
    Rescales each pixel to the range [0, 1].
    """
    # Apply the linear transformation
    reflectance_image = (k * radiance_image) + b

    # Ensure the output is rescaled to the range [0, 1]
    # Clip any values outside this range to enforce the constraint.
    reflectance_image_clipped = np.clip(reflectance_image, 0.0, 1.0)

    return reflectance_image_clipped

# Define factors
k_factor = 0.8  # multiplicative scaling factor [cite: 306]
b_factor = 0.1  # additive scaling factor [cite: 306]

# Call the function
rgb_image_reflectance = radiance_to_reflectance(rgb_image_radiance, k_factor, b_factor)

def reflectance_to_8bit_dn(reflectance_image):
    """
    Scales a floating-point reflectance image (range [0, 1]) to 8-bit Digital Numbers (range [0, 255])
    and converts the values to integers.
    """
    # Handle NaN values by replacing them with 0 before scaling and casting
    # This prevents the 'RuntimeWarning: invalid value encountered in cast'
    reflectance_image_no_nan = np.nan_to_num(reflectance_image, nan=0.0)

    # 1. Scale each pixel to fit an 8-bit Digital Number (i.e., [0, 255])
    scaled_image_float = reflectance_image_no_nan * 255.0

    # 2. Convert the values from floats to integers (8-bit requires integers)
    # Using np.rint (round to nearest integer) and then astype(np.uint8) is robust.
    dn_image_8bit = np.rint(scaled_image_float).astype(np.uint8)

    return dn_image_8bit

# Call the function
rgb_image_dn = reflectance_to_8bit_dn(rgb_image_reflectance)

def save_final_image(image_array, file_name, folder_location='.'):
    """
    Saves the final image to a file using an appropriate file format (.png or .jpeg).
    """
    full_path = f"{folder_location}/{file_name}"

    # Visualize the final 8-bit DN image before saving
    visualize_image(image_array, title="Final 8-bit Digital Number Image")

    # Use Matplotlib's imsave which correctly handles the array to an image file.
    # It requires the input to be in the [0, 255] range for 8-bit integer types.
    #     plt.imsave(full_path, image_array)
    print(f"Image successfully saved to {full_path}")

# Define file name and save
file_name = "final_processed_image.png"
save_final_image(rgb_image_dn, file_name, folder_location='Payload') # Assuming a 'Payload' folder exists
