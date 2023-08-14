from typing import List

class Solution:
    def countBits(self, n: int) -> List[int]:
        def power_generator():
            n = 1
            while True:
                yield 2**n
                n += 1

        bitRepresentation = [0] * (n + 1)
        if n > 0:
            bitRepresentation[1] = 1

        rangeGenerator = power_generator()
        nextRangeStartIndex = next(rangeGenerator)

        i = 2
        while i < (n + 1):
            if i == nextRangeStartIndex:
                for j in range(i//2, i):
                    bitRepresentation[i] = bitRepresentation[j]

                    if i >= n:
                        break
                    i += 1
                nextRangeStartIndex = next(rangeGenerator)
                continue


            binaryVal = i
            bitCount = 0
            while binaryVal > 0:
                if binaryVal & 1 == 1:
                    bitCount += 1
                binaryVal = binaryVal >> 1

            bitRepresentation[i] = bitCount

            i += 1



        return bitRepresentation


print(Solution().countBits(20))
