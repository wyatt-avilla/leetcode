# https://leetcode.com/problems/maximum-manhattan-distance-after-k-changes/


class Solution:
    def maxDistance(self, s: str, k: int) -> int:
        ans = 0

        north, south, east, west = (0, 0, 0, 0)
        for c in s:
            if c == "N":
                north += 1
            elif c == "S":
                south += 1
            elif c == "E":
                east += 1
            elif c == "W":
                west += 1

            vert_diff = min(north, south, k)
            hori_diff = min(east, west, k - vert_diff)

            ans = max(
                ans,
                abs(north - south) + 2 * vert_diff + abs(east - west) + 2 * hori_diff,
            )

        return ans


if __name__ == "__main__":
    assert Solution().maxDistance("NSWWEW", 3) == 6
    assert Solution().maxDistance("NWSE", 1) == 3
