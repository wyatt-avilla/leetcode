# https://leetcode.com/problems/number-of-zero-filled-subarrays/


class Solution:
    @staticmethod
    def subarrays(n: int) -> int:
        return ((n + 1) * n) // 2

    @staticmethod
    def contig_zero_block_sizes(nums: list[int]) -> list[int]:
        ans: list[int] = []
        count = int(nums[0] == 0)

        for d in nums[1:]:
            if d != 0:
                if count > 0:
                    ans.append(count)
                count = 0
            else:
                count += 1

        if count > 0:
            ans.append(count)

        return ans

    def zeroFilledSubarray(self, nums: list[int]) -> int:
        contig_block_sizes = Solution.contig_zero_block_sizes(nums)
        return sum(Solution.subarrays(cbs) for cbs in contig_block_sizes)


if __name__ == "__main__":
    assert Solution().zeroFilledSubarray([1, 3, 0, 0, 2, 0, 0, 4]) == 6
    assert Solution().zeroFilledSubarray([0, 0, 0, 2, 0, 0]) == 9
    assert Solution().zeroFilledSubarray([2, 10, 2019]) == 0
