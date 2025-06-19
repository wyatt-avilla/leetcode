# https://leetcode.com/problems/divide-array-into-arrays-with-max-difference/


class Solution:
    def divideArray(self, nums: list[int], k: int) -> list[list[int]]:
        nums.sort()
        n = len(nums)

        ans = []
        for i in range(0, n, 3):
            if (
                abs(nums[i] - nums[i + 1]) > k
                or abs(nums[i + 1] - nums[i + 2]) > k
                or abs(nums[i] - nums[i + 2]) > k
            ):
                return []
            ans.append(nums[i : i + 3])

        return ans


if __name__ == "__main__":
    assert Solution().divideArray([1, 3, 4, 8, 7, 9, 3, 5, 1], 2) == [
        [1, 1, 3],
        [3, 4, 5],
        [7, 8, 9],
    ]

    assert Solution().divideArray([2, 4, 2, 2, 5, 2], 2) == []

    assert Solution().divideArray(
        [4, 2, 9, 8, 2, 12, 7, 12, 10, 5, 8, 5, 5, 7, 9, 2, 5, 11], 14
    ) == [
        [2, 2, 12],
        [4, 8, 5],
        [5, 9, 7],
        [7, 8, 5],
        [5, 9, 10],
        [11, 12, 2],
    ]
