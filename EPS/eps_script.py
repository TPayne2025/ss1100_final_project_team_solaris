def available_power(voltage, current):
    """
    Calculates the instantaneous incoming power from the solar panels,
    checking for inputs that exceed the solar panels' maximum limits.
    """
    # YOUR CODE HERE
    return 0

def battery_charging(power_delivered, time_elapsed):
    """
    Calculates the total energy available for battery charging.
    """
    # YOUR CODE HERE
    return 0

def main():
    """
    Main function to test the EPS functions.
    """
    # Example test cases from the project description
    test_cases = [
        (25, 10, 3600),
        (30, 8, 1800),
        (15, 12, 7200)
    ]

    for i, (v, i_current, t) in enumerate(test_cases):
        print(f"--- Test Case {i+1} ---")
        power = available_power(v, i_current)
        print(f"Available Power: {power:.2f} W")
        energy = battery_charging(power, t)
        print(f"Energy for charging: {energy:.2f} J")
        print("-" * 20)

if __name__ == "__main__":
    main()
