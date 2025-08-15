# https://leetcode.com/problems/power-of-four/


class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        powers = {
            1,
            4,
            16,
            64,
            256,
            1024,
            4096,
            16384,
            65536,
            262144,
            1048576,
            4194304,
            16777216,
            67108864,
            268435456,
            1073741824,
        }

        return n in powers


if __name__ == "__main__":
    assert Solution().isPowerOfFour(16)
    assert Solution().isPowerOfFour(16)
    assert not Solution().isPowerOfFour(5)
    assert Solution().isPowerOfFour(1)
