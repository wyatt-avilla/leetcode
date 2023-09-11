from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        sortedNums = sorted(set(nums))
        numsLen = len(sortedNums)
        longestSequence = 0
        currentSequence = 1
        for i in range(numsLen - 1):
            if sortedNums[i+1] == (sortedNums[i] + 1):
                currentSequence += 1
            else:
                longestSequence = max(currentSequence, longestSequence)
                currentSequence = 1
        return max(currentSequence, longestSequence) if numsLen >= 1 else 0
            
            
            

            

assert Solution().longestConsecutive([100,4,200,1,3,2]) == 4
assert Solution().longestConsecutive([0,3,7,2,5,8,4,6,0,1]) == 9
assert Solution().longestConsecutive([]) == 0
