import unittest


class TestUtils(unittest.TestCase):
    def TestRange(self, listToTest, bitsExpected):
        max_val = (2**bitsExpected) - 1
        min_val = 0
        print(f"listToTest is  {listToTest}")
        for x in listToTest:

            self.assertIsInstance(x, str)
            self.assertLessEqual(int(x), max_val)
            self.assertGreaterEqual(int(x), min_val)
