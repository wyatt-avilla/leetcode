from typing import List


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        print("-------")
        if all(nums) > 0:
            return True
        else:
            startIdx = len(nums) - 2
            searching = False
            searchingFrom = -1
            for i in range(startIdx, -1, -1):
                print(f"processing nums[{i}] == {nums[i]}")
                if nums[i] == 0:
                    searching = True
                    searchingFrom = i
                elif searching:
                    if nums[i] > 0:
                        if nums[i] > (searchingFrom - i):
                            searching = False
                        else:
                            return False
            return not searching




assert Solution().canJump([2,3,1,1,4]) is True
assert Solution().canJump([1, 1, 1, 0]) is True
assert Solution().canJump([3,2,1,0,4]) is False
assert Solution().canJump([0, 1]) is False
assert Solution().canJump([0]) is True
assert Solution().canJump([5,9,3,2,1,0,2,3,3,1,0,0]) is True
