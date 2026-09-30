# https://leetcode.com/problems/plus-one/


class Solution:
    def plusOne(self, digits: list[int]) -> list[int]:
        d_len = len(digits)

        for i in reversed(range(d_len)):
            if digits[i] != 9:
                digits[i] += 1
                return digits
            digits[i] = 0

        return [1] + [0 for _ in range(d_len)]


if __name__ == "__main__":
    assert Solution().plusOne([1, 2, 3]) == [1, 2, 4]
    assert Solution().plusOne([4, 3, 2, 1]) == [4, 3, 2, 2]
    assert Solution().plusOne([9]) == [1, 0]
    assert Solution().plusOne([9, 9, 9]) == [1, 0, 0, 0]
