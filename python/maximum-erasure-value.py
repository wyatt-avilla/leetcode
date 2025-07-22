# https://leetcode.com/problems/maximum-erasure-value/


class Solution:
    def maximumUniqueSubarray(self, nums: list[int]) -> int:
        back_idx = 0
        curr_sum = best_sum = nums[0]
        included = {nums[0]}

        for num in nums[1:]:
            if num not in included:
                curr_sum += num
                best_sum = max(best_sum, curr_sum)
                included.add(num)
            else:
                while nums[back_idx] != num:
                    included.remove(nums[back_idx])
                    curr_sum -= nums[back_idx]
                    back_idx += 1
                back_idx += 1

        return best_sum


if __name__ == "__main__":
    assert Solution().maximumUniqueSubarray([4, 2, 4, 5, 6]) == 17
    assert Solution().maximumUniqueSubarray([5, 2, 1, 2, 5, 2, 1, 2, 5]) == 8
    assert (
        Solution().maximumUniqueSubarray([10000, 1, 10000, 1, 1, 1, 1, 1, 1]) == 10001
    )
    assert (
        Solution().maximumUniqueSubarray(
            [
                187,
                470,
                25,
                436,
                538,
                809,
                441,
                167,
                477,
                110,
                275,
                133,
                666,
                345,
                411,
                459,
                490,
                266,
                987,
                965,
                429,
                166,
                809,
                340,
                467,
                318,
                125,
                165,
                809,
                610,
                31,
                585,
                970,
                306,
                42,
                189,
                169,
                743,
                78,
                810,
                70,
                382,
                367,
                490,
                787,
                670,
                476,
                278,
                775,
                673,
                299,
                19,
                893,
                817,
                971,
                458,
                409,
                886,
                434,
            ],
        )
        == 16911
    )
