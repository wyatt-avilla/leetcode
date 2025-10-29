# https://leetcode.com/problems/smallest-number-with-all-set-bits/


class Solution:
    def smallestNumber(self, n: int) -> int:
        return int(str(bin(n))[2:].replace("0", "1"), base=2)


if __name__ == "__main__":
    assert Solution().smallestNumber(5) == 7
    assert Solution().smallestNumber(10) == 15
    assert Solution().smallestNumber(3) == 3
