from command_dict import command_dict

def parse_command(command_string):
    """
    Parses a command string and returns a tuple with the full subsystem name,
    the command description, and the parameter value.
    """
    # YOUR CODE HERE
    return (None, None, None)

def main():
    """
    Main function to test the command parser.
    """
    test_commands = [
        "EPS:CMD01:0",
        "ACS:CMD04:-1",
        "RCS:INVALID:0"
    ]

    for cmd in test_commands:
        subsystem, description, value = parse_command(cmd)
        print(f"Command: {cmd}")
        print(f" -> Subsystem: {subsystem}")
        print(f" -> Description: {description}")
        print(f" -> Value: {value}")
        print("-" * 20)

if __name__ == "__main__":
    main()
