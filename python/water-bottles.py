# https://leetcode.com/problems/water-bottles/


class Solution:
    def numWaterBottles(self, num_bottles: int, num_exchange: int) -> int:
        ans = 0
        full = num_bottles
        empty = 0
        while full > 0:
            ans += full

            empty += full
            full = empty // num_exchange
            empty -= full * num_exchange

        return ans


if __name__ == "__main__":
    assert Solution().numWaterBottles(15, 4) == 19
    assert Solution().numWaterBottles(9, 3) == 13
