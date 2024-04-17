import unittest
import math
import bitGenerator

# test by running python -m pytest tests (not pytest tests, as the docs say)

# from function_app import my_second_function
from function_app import randuints
from testUtils import TestUtils
import draw_random


class TestFunction(unittest.TestCase):
    # testing on this platform established that an uint is 4 bytes (32 bits)
    def __init__(self, methodName: str = "runTest") -> None:
        super().__init__(methodName)
        self.testUtils = TestUtils()

    def test_BitGenerator_randomtest1(self):
        rb = bitGenerator.BitGenerator(True)
        myrange = 10
        for idx, a in enumerate(range(10)):
            print("idx: {0} bit: {1}".format(idx, rb.getBit()))
        print(rb.totalBitsGenerated)
        self.assertEqual(rb.totalBitsGenerated, 64)

    def test_BitGenerator_random10(self):
        randombits = bitGenerator.BitGenerator(True)
        s = []
        c = 1
        print()
        for idx, a in enumerate(range(64 * 10)):
            s.append(randombits.getBit())
            if len(s) == 64:
                # print("s: {0} bits: {1}".format(c, "".join([str(i) for i in s])))
                print("s: {:02} bits: {}".format(c, "".join([str(i) for i in s])))
                s.clear()
                c += 1
        print(randombits.totalBitsGenerated)
        self.assertEqual(randombits.totalBitsGenerated, 704)

    def test_BitGenerator_random64_noRepeats(self):
        rb = bitGenerator.BitGenerator(True)
        testruns = 10000
        res = []
        for ctr in range(testruns):
            accum = []
            for _ in range(64):
                accum.append(str(rb.getBit()))

            mystr = "".join(accum)
            num = int(mystr, 2)
            res.append(num)
        s = set(res)
        self.assertEqual(len(res), testruns)
        self.assertEqual(len(s), len(res))

        print(rb.totalBitsGenerated)
        self.assertEqual(rb.totalBitsGenerated, (64 * testruns) + 64)

    def test_BitGeneratorCheckerboard(self):
        randombits = bitGenerator.BitGenerator(False)
        lineIter = 0
        print()
        lines = 10
        columns = 64

        for lineIter in range(0, lines):
            line = []
            for column in range(0, columns):
                line.append(randombits.getBit(lineIter))
                if len(line) == columns:
                    # print("s: {0} bits: {1}".format(c, "".join([str(i) for i in s])))
                    print(
                        "row: {0} bits: {1}".format(
                            lineIter, "".join([str(i) for i in line])
                        )
                    )
                    line.clear()

    def test_BitGenerator_RandomType(self):
        randombits = bitGenerator.BitGenerator(True)
        result = randombits.getBit()
        self.assertIsInstance(result, int)

    def test_BitGenerator_CheckerBoardType(self):
        randombits = bitGenerator.BitGenerator(False)
        sum = 0
        for x in range(10):
            result = randombits.getBit()
            self.assertIsInstance(result, int)
            sum += result
        self.assertEqual(sum, 5)
