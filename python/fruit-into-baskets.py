# https://leetcode.com/problems/fruit-into-baskets/


class Solution:
    def totalFruit(self, fruits: list[int]) -> int:
        t1 = -1
        t1_left = -1
        t1_right = -1
        t2 = -1
        t2_left = -1
        t2_right = -1

        ans = 0
        for i, t in enumerate(fruits):
            if t == t1:
                t1_right = i
            elif t == t2:
                t2_right = i
            else:
                ans = max(ans, max(t1_right, t2_right) - min(t1_left, t2_left))
                if t1_right > t2_right:
                    t1_left = t2_right + 1

                    t2 = t
                    t2_left = i
                    t2_right = i
                else:
                    t2_left = t1_right + 1

                    t1 = t
                    t1_left = i
                    t1_right = i

        return max(ans, max(t1_right, t2_right) - min(t1_left, t2_left)) + 1


if __name__ == "__main__":
    assert Solution().totalFruit([1, 2, 1]) == 3
    assert Solution().totalFruit([0, 1, 2, 2]) == 3
    assert Solution().totalFruit([1, 2, 3, 2, 2]) == 4
    assert Solution().totalFruit([1, 2, 3, 4, 5]) == 2
    assert Solution().totalFruit([1, 2, 2, 3, 4, 4]) == 3
    assert Solution().totalFruit([4, 1, 4, 1, 2, 2, 2]) == 4
