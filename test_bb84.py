import unittest
import numpy as np
from bb84 import bb84_simulation, check_for_eavesdropping

class TestBB84(unittest.TestCase):
    def test_key_generation(self):
        key = bb84_simulation(10)
        self.assertTrue(len(key) > 0, "Empty")

    def test_no_eavesdropping(self):
        alice_key = np.array([0, 1, 0])
        bob_key = np.array([0, 1, 0])
        result = check_for_eavesdropping(alice_key, bob_key, 2)
        self.assertFalse(result, "Same keys")

if __name__ == "__main__":
    unittest.main()
