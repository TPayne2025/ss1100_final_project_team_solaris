import unittest
import sys
import os

# Add the parent directory to the path 
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from rcs_script import velocity_change_calculation

class TestRCS(unittest.TestCase):

    def test_velocity_change_calculation(self):
        """
        Tests the velocity_change_calculation function with a simple case.
        """
        # From the project description:
        # Spacecraft mass = 500 kg
        # T = m_dot * v_e
        # delta_v = (T * delta_t) / m_0
        
        # Test Case 1: m_dot = 0.02, v_e = 1000, t = 5
        # T = 0.02 * 1000 = 20 N
        # delta_v = (20 * 5) / 500 = 0.2 m/s
        
        m_dot = 0.02
        v_e = 1000
        t = 5
        expected_delta_v = 0.2
        
        # The function needs to be implemented correctly for this to pass
        calculated_delta_v = velocity_change_calculation(m_dot, v_e, t)
        
        self.assertAlmostEqual(calculated_delta_v, expected_delta_v, places=2,
                             msg="Velocity change calculation is incorrect.")

if __name__ == '__main__':
    unittest.main()
