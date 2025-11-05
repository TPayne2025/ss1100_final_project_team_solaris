import unittest
import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from thermal_control import process_temperature

class TestTCS(unittest.TestCase):

    def test_process_temperature(self):
        """
        Tests the process_temperature function.
        """
        # Case 1: Current temp is lower than target
        # Difference = 20 - 10 = 10
        # Adjustment = 0.25 * 10 = 2.5
        # New temp = 10 + 2.5 = 12.5
        self.assertAlmostEqual(process_temperature(10, 20), 12.5, places=2)

        # Case 2: Current temp is higher than target
        # Difference = 0 - 10 = -10
        # Adjustment = 0.25 * -10 = -2.5
        # New temp = 10 - 2.5 = 7.5
        self.assertAlmostEqual(process_temperature(10, 0), 7.5, places=2)
        
        # Case 3: Current temp is equal to target
        # Difference = 50 - 50 = 0
        # Adjustment = 0
        # New temp = 50
        self.assertAlmostEqual(process_temperature(50, 50), 50, places=2)

if __name__ == '__main__':
    unittest.main()
