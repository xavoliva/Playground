import unittest


def unique(s):
    return len(s) == len(set(s))


def all_unique_2(s):
    pass


class Test(unittest.TestCase):
    dataT = [('abcd'), ('s4fad'), ('')]
    dataF = [('23ds2'), ('hb 627jh=j ()')]

    def test_t(self):
        # true check
        for test_string in self.dataT:
            actual = unique(test_string)
            self.assertTrue(actual)

    def test_f(self):
        # false check
        for test_string in self.dataF:
            actual = unique(test_string)
            self.assertFalse(actual)


if __name__ == "__main__":
    unittest.main()
