import unittest
import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from your_adc_script import calculate_rotation

class TestACS(unittest.TestCase):

    def test_calculate_rotation(self):
        """
        Tests the calculate_rotation function.
        """
        current = (30, 60, 90)
        target = (0, 10, 15)
        
        # Expected correction = target - current
        expected_correction = (-30, -50, -75)
        
        calculated_correction = calculate_rotation(current, target)
        
        self.assertEqual(calculated_correction, expected_correction,
                         "Calculate rotation function is incorrect.")

if __name__ == '__main__':
    unittest.main()
