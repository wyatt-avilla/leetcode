from typing import List, Dict


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freqDict: Dict[int, int] = {x: nums.count(x) for x in range(min(nums), max(nums) + 1)}
        print(freqDict)
        freqDictDescending = dict(sorted(freqDict.items(), key=lambda item: item[1], reverse=True))
        print(freqDictDescending)
        return [key for key in freqDictDescending.keys()][:k]


assert set(Solution().topKFrequent([1,1,1,2,2,3], 2)) == set([1,2])
assert set(Solution().topKFrequent([1], 1)) == set([1])
assert set(Solution().topKFrequent([-1, -1], 1)) == set([-1])
