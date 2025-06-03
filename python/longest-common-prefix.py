# https://leetcode.com/problems/longest-common-prefix/


def longest_between(a: str, b: str) -> int:
    count = 0
    for c_1, c_2 in zip(a, b):
        if c_1 == c_2:
            count += 1
        else:
            break
    return count


class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        prev_common = strs[0]
        for s in strs:
            prev_common = s[: longest_between(prev_common, s)]

        return prev_common


if __name__ == "__main__":
    assert Solution().longestCommonPrefix(["flower", "flow", "flight"]) == "fl"
    assert Solution().longestCommonPrefix(["dog", "racecar", "car"]) == ""
