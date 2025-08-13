# https://leetcode.com/problems/power-of-three/


class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        powers = {
            1,
            3,
            9,
            27,
            81,
            243,
            729,
            2187,
            6561,
            19683,
            59049,
            177147,
            531441,
            1594323,
            4782969,
            14348907,
            43046721,
            129140163,
            387420489,
            1162261467,
        }

        return n in powers


if __name__ == "__main__":
    assert Solution().isPowerOfThree(9)
    assert Solution().isPowerOfThree(27)
    assert not Solution().isPowerOfThree(-27)
    assert not Solution().isPowerOfThree(8)
    assert not Solution().isPowerOfThree(-8)
    assert not Solution().isPowerOfThree(0)
    assert not Solution().isPowerOfThree(-1)
