# https://leetcode.com/problems/count-hills-and-valleys-in-an-array/


from collections.abc import Generator


class Solution:
    def clear_contig_adjacents(self, nums: list[int]) -> Generator[int, None, None]:
        yield nums[0]

        yield from (b for a, b in zip(nums, nums[1:]) if a != b)

    def countHillValley(self, nums: list[int]) -> int:
        nums = list(self.clear_contig_adjacents(nums))

        return sum(
            (mid > left and mid > right) or (mid < left and mid < right)
            for left, mid, right in zip(nums, nums[1:], nums[2:])
        )


if __name__ == "__main__":
    assert Solution().countHillValley([2, 4, 1, 1, 6, 5]) == 3
    assert Solution().countHillValley([6, 6, 5, 5, 4, 1]) == 0
