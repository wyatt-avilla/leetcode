# https://leetcode.com/problems/maximum-69-number/


class Solution:
    def maximum69Number(self, num: int) -> int:
        s = str(num)

        if (i := s.find("6")) == -1:
            return num

        return num + (3 * 10 ** (len(s) - 1 - i))


if __name__ == "__main__":
    assert Solution().maximum69Number(9) == 9
    assert Solution().maximum69Number(6) == 9
    assert Solution().maximum69Number(9669) == 9969
    assert Solution().maximum69Number(9996) == 9999
    assert Solution().maximum69Number(9999) == 9999
