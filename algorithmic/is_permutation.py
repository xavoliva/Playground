import unittest
from collections import Counter


def is_permutation(a, b):
    if len(a) != len(b):
        return False
    return Counter(a) == Counter(b)

class test_permutation(unittest.TestCase):
    t_list = [("hey", "yeh")]
    f_list = [("hey", "yeah")]

    def test_t(self):
        for t in range(t_list):
        self.asserTrue(is_permutation(t[0], t[1]))

    def test_f(self):
        for f in range(f_list):
        self.assertFalse(is_permutation())


if __name__ == "__main__":
    unittest.main()
