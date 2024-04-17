import rd_functions_p
import math


class BitGenerator(object):
    # This started as a generator (with yield) but needed to move
    # away from that pattern in order to support passing a row for the checkerboard.

    def __init__(self, random: bool = True):
        self.totalBitsGenerated = 0
        self.rdObj = rd_functions_p.RdFunctions()
        self.bitGenerator = None
        if random:
            self.bits = []
            self.BitsGeneratorRefillRandom()
            self.bitGenerator = self.BitsGeneratorRandom
            self._user_next = self.__random_next__
        else:
            self.rowCounter = 0
            self.lastRow = 1
            self.bitGenerator = self.BitsGeneratorCheckerboard
            self._user_next = self.__checkerboard_next__

    def __random_next__(self, row=None):
        return self.bitGenerator()

    def __checkerboard_next__(self, row):
        if row is None:
            row = self.rowCounter
        return self.BitsGeneratorCheckerboard(row)

    def getBit(self, row=None):
        return self._user_next(row)

    def __iter__(self):
        return self

    def BitsGeneratorRandom(self):
        while self.bits:
            res = self.bits.pop(0)
            return_val = res
            if (len(self.bits)) == 0:
                self.BitsGeneratorRefillRandom()
            return return_val

    def BitsGeneratorCheckerboard(self, row=0):
        if self.lastRow != row % 2:
            # restart the row
            self.lastRow = row % 2
            start = bool(row % 2)
            self.last = start
            self.totalBitsGenerated += 1
            result = int(start)
        else:
            self.last = not self.last
            self.totalBitsGenerated += 1
            result = int(self.last)
        return result

    def BitsGeneratorRefillRandom(self):
        strnum = format(
            self.rdObj.RdRand64_Retry(), "064b"
        )  # to get any leading zeroes, need to use 064 in format string
        b = [int(c) for c in str(strnum)]
        self.totalBitsGenerated += len(b)
        self.bits.extend(b)


if __name__ == "__main__":
    bg = BitGenerator(True)
    bg.testGenerator()
    # testGenerator(False)
    # testGenerator2(False)
    # testGenerator2(True)
    # testGenerator2(False)
