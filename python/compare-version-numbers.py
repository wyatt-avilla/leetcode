# https://leetcode.com/problems/compare-version-numbers/


class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        v1_split = version1.split(".")
        v2_split = version2.split(".")

        if len(v1_split) > len(v2_split):
            v2_split.extend(["0" for _ in range(len(v1_split) - len(v2_split))])
        else:
            v1_split.extend(["0" for _ in range(len(v2_split) - len(v1_split))])

        first_diff = next(
            filter(
                lambda t: t[0] != t[1],
                ((int(a), int(b)) for a, b in zip(v1_split, v2_split)),
            ),
            None,
        )

        if first_diff is None:
            return 0

        return 1 if first_diff[0] > first_diff[1] else -1


if __name__ == "__main__":
    assert Solution().compareVersion("1.10", "1.2") == 1
    assert Solution().compareVersion("1.2", "1.10") == -1
    assert Solution().compareVersion("1.01", "1.001") == 0
    assert Solution().compareVersion("1.0", "1.0.0.0") == 0
