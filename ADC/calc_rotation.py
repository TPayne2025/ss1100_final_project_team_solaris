def orientation_error(orientation_list):
    """
    Calculates the rotation required to move from current to desired orientation.
    Input: A two-item list [(current_x, current_y, current_z), (target_x, target_y, target_z)]
    Output: A tuple (x_diff, y_diff, z_diff) representing the required rotation along each axis.
    """
    
    # Validation of inputs
    if len(orientation_list) != 2:
        raise ValueError("Input must be a two-item list: [current, desired].")
        
    current = orientation_list[0]
    desired = orientation_list[1]

    if len(current) != 3 or len(desired) != 3:
        raise ValueError("Each orientation must contain exactly 3 values (X, Y, Z).")

    # Calculation (Target - Current)
    x_correction = desired[0] - current[0]
    y_correction = desired[1] - current[1]
    z_correction = desired[2] - current[2]

    return (x_correction, y_correction, z_correction)
