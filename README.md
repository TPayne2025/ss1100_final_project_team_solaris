# SS1100: Intro to Programming for Space Applications
## Final Project: Programming Spacecraft Systems

This repository contains the starter code and resources for the SS1100 Final Project. The goal of this project is to apply your programming skills to solve a variety of problems related to spacecraft subsystems.

### Project Structure

The project is organized into folders, one for each spacecraft subsystem:

- **/RCS/**: Reaction Control Subsystem
- **/TCS/**: Thermal Control Subsystem
- **/ADC/**: Attitude Control Subsystem (Note: ADC is used in the folder name for brevity)
- **/C&DH/**: Command and Data Handling
- **/EPS/**: Electrical Power Subsystem
- **/Payload/**: Remote Sensing Payload

Each folder contains the necessary scripts and data files for that subsystem's tasks.

### Getting Started

For each subsystem, you will find a primary Python script (e.g., `rcs_script.py`, `thermal_control.py`, etc.). Your task is to complete the functions within these scripts according to the instructions in the main project document (`Final Project Instructions.pdf`).

### Verifying Your Code with Unit Tests

Each subsystem folder also contains a `/test` directory with a unit test script (e.g., `test_rcs.py`). These tests are designed to help you verify that your code is working correctly.

To run the tests for a specific subsystem, navigate to that subsystem's directory in your terminal and run the test script. For example, to test your RCS code:

```bash
cd RCS
python test/test_rcs.py
```

If your functions are implemented correctly, the tests should pass without errors.

### Capstone: Mission Simulation

Once you have completed the tasks for all the individual subsystems, you can tackle the final capstone challenge in `mission_simulation.py`. This script, located in the root directory, is designed to integrate the functions you've written into a single, cohesive mission sequence.

---

## Questions for Writeup

LCDR Payne Response
1. Overall collaboration was great. We split the tackled two subsystems in groups and divided up the remaining payload amongst ourselves.  Github writ large is not difficult to use, but slightly tedious to manage. As the manager, I should have spent more time understanding how to utilize this program.
   
2. From group discussion, likely the Command and Data Handling and the Payload sections.  From my perspective, the payload was challenging because it required correctly loading in files (CSV) and importing the correct libraries.  I spent several iterations of coding sessions trying to understand why Gemini attempted to force pandas as opposed to numby/matplotlib.

3. This is listed in the Payload code, but I used Gemini for the entire payload section.  I started by plugging in various lines of code by attempting to distill my requirements for visualization.  One negative of Google Colab was it would consistently prompt me to utilize pandas vice matplotlib/numby. Additionally there were several issues in terms of the code running completely through, but after several prompts it recognized specific lines of code were buried instead of being called out. 

4. I did not use any other resources outside of googling to understand pandas versus numby.

5. Overall, I think this was a great final coding project.  The integration with GitHub allowed us to see our teammates coding and understand how they arrived at that line of code.

Capt Eshleman Reponse
1. We tested our subsystems separately using our chosen IDEs and the test files provided. We each were responsible for 1 subsystem and then each pair had to complete one other subsystem together. We each forked our own branch off the main to work without jeopardizing each other's work. 

2. (I'm a little biased but I think ADC was tough (maybe not the hardest idk) because for the check plus requirement, I had to create and import my code as it's own module as well as ensuring my 4 files were creating and pulling from the correct file path, feel free to put whatever though. 

3. I used Gemini AI to help fix the file path in the ADC section, my prompt was "When I run the provided rotate_me.py script, it creates current_state.txt in the wrong folder, how do I correct this to ensure that current_state.txt will always be created in the same folder as rotate_me.py in order for my script to function correctly?"

4. I asked Jeffrey and a little Gemini really and that's it. 

5. This project could be improved for future quarters if other labs required use of Github so that students are more familiar with it prior to using it for the final project. 

