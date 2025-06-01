# https://leetcode.com/problems/distribute-candies-among-children-ii/


class Solution:
    def distributeCandies(self, n: int, limit: int) -> int:
        return sum(
            len([None for j in range(min(limit, n - i) + 1) if n - i - j <= limit])
            for i in range(min(limit, n) + 1)
        )


if __name__ == "__main__":
    assert Solution().distributeCandies(5, 2) == 3
    assert Solution().distributeCandies(3, 3) == 10
