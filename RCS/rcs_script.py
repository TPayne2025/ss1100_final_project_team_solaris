max_thrust= 100
max_flow_rate =0.05
max_velocity= 2000
thruster_names = {0:"Thruster 1", 1: "Thruster 2", 2: "Thruster 3"}

def malfunction_detection(thrust_values):
    """
    Checks input thrust values and angles for each thruster against set limits.
    If a thruster is outside of these limits, it prints a message.
    """
    #
    for i, (mass_flow_rate, exhaust_velocity, time_elapsed) in enumerate(thrust_values):
        thruster_name= thruster_names[i]
        thrust=mass_flow_rate*exhaust_velocity
        if thrust> max_thrust:
          thrust_diff= thrust-max_thrust
          print(f"{thruster_name}: Thrust exceeds maximum by {thrust_diff:.2f} N")
        if mass_flow_rate>max_flow_rate:
            print(f"{thruster_name}: Flow rate exceeds maximum by {mass_flow_rate-max_flow_rate:.2f} kg/s")
        if exhaust_velocity>max_velocity:
            print(f"{thruster_name}: Velocity exceeds maximum by {exhaust_velocity-max_velocity:.2f} m/s")
        
    pass

def velocity_change_calculation(mass_flow_rate, exhaust_velocity, time_elapsed):
    """
    Performs calculations to determine the change in velocity resulting from a maneuver event.
    """
    thrust = mass_flow_rate * exhaust_velocity
    delta_v = (thrust * time_elapsed)/500

    return delta_v

def main():
    """
    Main function to test the RCS functions.
    """

    test_cases = [
        (0.02, 1000, 5),
        (0.06, 1000, 3),
        (0.05, 2000, 10)
    ]

    for i, (m_dot, v_e, t) in enumerate(test_cases):
        print(f"--- Test Case {i+1} ---")
        delta_v = velocity_change_calculation(m_dot, v_e, t)
        print(f"Calculated delta_v: {delta_v:.2f} m/s")
        print("-" * 20)

    print("\n--- Malfunction Detection ---")
    malfunction_detection(test_cases)

if __name__ == "__main__":
    main()
