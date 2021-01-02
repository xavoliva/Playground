import unittest


def is_unique(s: str):
    return len(s) == len(set(s))


class Test(unittest.TestCase):
    data_t = [('abcd'), ('s4fad'), ('')]
    data_f = [('23ds2'), ('hb 627jh=j ()')]

    def test_t(self):
        # true check
        for true_string in self.data_t:
            self.assertTrue(is_unique(true_string))

    def test_f(self):
        # false check
        for false_string in self.data_f:
            self.assertFalse(is_unique(false_string))


if __name__ == "__main__":
    unittest.main()
