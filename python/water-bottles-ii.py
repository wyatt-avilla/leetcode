# https://leetcode.com/problems/water-bottles-ii/


class Solution:
    def maxBottlesDrunk(self, num_bottles: int, num_exchange: int) -> int:
        ans = 0
        full = num_bottles
        empty = 0
        while full > 0:
            ans += full

            empty += full
            full = 0
            while empty >= num_exchange:
                full += 1
                empty -= num_exchange
                num_exchange += 1

        return ans


if __name__ == "__main__":
    assert Solution().maxBottlesDrunk(13, 6) == 15
    assert Solution().maxBottlesDrunk(10, 3) == 13
