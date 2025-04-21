import unittest
from bb84 import bb84_simulation, check_for_eavesdropping

class TestBB84(unittest.TestCase):
    def test_key_length(self):
        key = bb84_simulation(10)
        self.assertTrue(len(key) > 0)
    
    def test_eavesdropping_detection(self):
        self.assertFalse(check_for_eavesdropping(np.array([0, 1]), np.array([0, 1]), 1))

if __name__ == "__main__":
    unittest.main()
