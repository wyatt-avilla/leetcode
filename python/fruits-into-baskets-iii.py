# https://leetcode.com/problems/fruits-into-baskets-iii/

import math


class Solution:
    def numOfUnplacedFruits(self, fruits: list[int], baskets: list[int]) -> int:
        n = len(baskets)
        m = int(math.sqrt(n))
        section = (n + m - 1) // m
        count = 0
        max_v = [0] * section

        for i in range(n):
            max_v[i // m] = max(max_v[i // m], baskets[i])

        for fruit in fruits:
            unset = 1
            for sec in range(section):
                if max_v[sec] < fruit:
                    continue
                choose = 0
                max_v[sec] = 0
                for i in range(m):
                    pos = sec * m + i
                    if pos < n and baskets[pos] >= fruit and not choose:
                        baskets[pos] = 0
                        choose = 1
                    if pos < n:
                        max_v[sec] = max(max_v[sec], baskets[pos])
                unset = 0
                break
            count += unset
        return count


if __name__ == "__main__":
    assert Solution().numOfUnplacedFruits([4, 2, 5], [3, 5, 4]) == 1
    assert Solution().numOfUnplacedFruits([3, 6, 1], [6, 4, 7]) == 0
