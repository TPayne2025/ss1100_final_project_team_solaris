from command_dict import command_dict
#comment
def parse_command(message:str):

    subsystem_table = {
        "RCS": "Reaction Control System",
        "TCS": "Thermal Control System",
        "ACS": "Attitude Control System",
        "CDH": "Command and Data Handling",
        "TTC": "Telemetry and Telecommand",
        "EPS": "Electrical Power System",
        "PL": "Payload",
    }
        
    command_table = {
    "RCS": {
        "CMD01": "THRUSTX",
        "CMD02": "THRUSTY",
        "CMD03": "THRUSTZ",
        "CMD04": "SAFEMODE",
    },
    "TCS": {
        "CMD01": "HEATERON",
        "CMD02": "HEATEROFF",
        "CMD03": "VENTOPENRADIATOR",
        "CMD04": "TEMPSETPOINT",
    },
    "ACS": {
        "CMD01": "ROTATEX",
        "CMD02": "ROTATEY",
        "CMD03": "ROTATEZ",
        "CMD04": "SAFEMODE",
    },
    "CDH": {
        "CMD01": "TRANSMITHIGH",
        "CMD02": "TRANSMITLOW",
        "CMD03": "RECEIVEMODE",
        "CMD04": "SAFEMODE",
    },
    "TTC": {
        "CMD01": "TRANSMITMODE",
        "CMD02": "RECEIVEMODE",
        "CMD03": "TRACKINGMODE",
        "CMD04": "SAFEMODE",
    },
    "EPS": {
        "CMD01": "BATTERYCHARGEMODE",
        "CMD02": "POWERONMODULE",
        "CMD03": "POWEROFFMODULE",
        "CMD04": "VOLTAGESETPOINT",
    },
    "PL": {
        "CMD01": "STARTDATAACQUISITION",
        "CMD02": "STOPDATAACQUISITION",
        "CMD03": "CALIBRATESENSOR",
        "CMD04": "SAFEMODE",
    }
}
# --- Split message into components ---
    parts = message.split(":")
    if len(parts) != 3:
        #raise ValueError("Invalid format: expected <SUBSYS>:<CMDxx>:<PARAM>")
        print("Invalid format: expected <SUBSYS>:<CMDxx>:<PARAM>")
        return (None, None, None)
    
    subsystem_code, command_code, parameter_str = parts

    # --- Validate subsystem ---
    if subsystem_code not in subsystem_table:
        #raise ValueError(f"Unknown subsystem:{subsystem_code}, You need to input a valid Subsystem code RCS, TCS, ACS, CDH, TTC, EPS, PL")
        print(f"Unknown subsystem:{subsystem_code}, You need to input a valid Subsystem code RCS, TCS, ACS, CDH, TTC, EPS, PL")
        return (None, None, None)
    
    full_subsystem_name = subsystem_table[subsystem_code]

    # --- Validate command code format ---
    # Propmt to ChatGPT to seperate check of CDM and numbers
    if not (command_code.startswith("CMD") and
            len(command_code) == 5 and
            command_code[3:].isdigit()):
        #raise ValueError(f"Invalid command code format: {command_code}")
        print(f"Invalid command code format: {command_code}, need to input CMD01-CMD04")
        return (None, None, None)

    # --- Validate command exists ---
    if command_code not in command_table[subsystem_code]:
        #raise ValueError(f"Unknown command code: {command_code}, need to input CMD01-CMD04")
        print(f"Unknown command code: {command_code}")
        return (None, None, None)
   
    #Fixed with AI because whole dictitiary was called instead of specific comamnd des.
    command_description = command_table[subsystem_code][command_code]

    # --- Validate numeric parameter ---
    try:
        parameter = float(parameter_str)
    except ValueError:
        raise ValueError("Parameter must be numeric (int or float).")

    # --- Return structured output ---
    return (full_subsystem_name, command_description, parameter) 

#Test = parse_command(test_command)
#print(Test)
#return (None, None, None)

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