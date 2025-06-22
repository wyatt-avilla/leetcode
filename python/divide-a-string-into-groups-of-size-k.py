# https://leetcode.com/problems/divide-a-string-into-groups-of-size-k/


class Solution:
    def divideString(self, s: str, k: int, fill: str) -> list[str]:
        if len(s) % k != 0:
            s += fill * (k - len(s) % k)

        return [
            s[start:end] for start, end in ((i, i + k) for i in range(0, len(s), k))
        ]


if __name__ == "__main__":
    assert Solution().divideString("abcdefghij", 3, "x") == ["abc", "def", "ghi", "jxx"]
    assert Solution().divideString("abcdefghi", 3, "x") == ["abc", "def", "ghi"]
