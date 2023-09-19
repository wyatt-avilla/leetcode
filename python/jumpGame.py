from typing import List


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        numsLen = len(nums)
        if all(nums) > 0 or (numsLen == 1):
            return True
        if nums[0] == 0 and numsLen > 1:
            return False

        reachableFrom: List[List[int]] = [[] for _ in range(numsLen)]
        reachableFrom[0]
        for i in range(numsLen - 1):
            if nums[i] > 0:
                for j in range(i+1, i+1+nums[i]):
                    if j >= numsLen:
                        break
                    reachableFrom[j].append(i)

        searchIDXs: list[int] = reachableFrom[numsLen - 1]
        seenIdxs: set[int] = set()
        while len(searchIDXs) > 0:
            currentlySearching = searchIDXs.pop(0)
            if currentlySearching in seenIdxs:
                continue
            if 0 in reachableFrom[currentlySearching]:
                return True
            searchIDXs.extend([idx for idx in reachableFrom[currentlySearching]])
            seenIdxs.add(currentlySearching)
            

        return False






cases = [
        ([1,0,1,0], False),
        ([2,3,1,1,4], True),
        ([1,1,1,1,0], True),
        ([3,2,1,0,4], False),
        ([0, 1], False),
        ([0], True),
        ([5,9,3,2,1,0,2,3,3,1,0,0], True),
        ([2,0], True),
        ]

for case in cases:
    inp, exp = case
    res = Solution().canJump(inp)
    if exp != res:
        print(f"{inp} should yield {exp}")
