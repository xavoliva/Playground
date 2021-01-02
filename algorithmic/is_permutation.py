import unittest
from collections import Counter


# Solution to https://www.hackerrank.com/challenges/ctci-ransom-note/problem
def is_permutation(a, b):
    if len(a) != len(b):
        return False
    return Counter(a) == Counter(b)


class test_permutation(unittest.TestCase):
    t_list = [("hey", "yeh")]
    f_list = [("hey", "yeah")]

    def test_t(self):
        for t in self.t_list:
            self.assertTrue(is_permutation(*t))

    def test_f(self):
        for f in self.f_list:
            self.assertFalse(is_permutation(*f))


if __name__ == "__main__":
    unittest.main()
