# https://leetcode.com/problems/finding-pairs-with-a-certain-sum/


from bisect import bisect_right
from collections import Counter


class FindSumPairs:
    def __init__(self, nums1: list[int], nums2: list[int]) -> None:
        counts = Counter(nums1)
        self.nums1_counts = sorted(counts.items())
        self.n1_max_occ = max(counts.values())

        self.nums2 = nums2
        self.nums2_counts = Counter(nums2)

    def add(self, index: int, val: int) -> None:
        n2_prev_val = self.nums2[index]
        self.nums2_counts[n2_prev_val] -= 1
        if self.nums2_counts[n2_prev_val] == 0:
            del self.nums2_counts[n2_prev_val]

        self.nums2[index] += val
        self.nums2_counts[self.nums2[index]] += 1

    def count(self, tot: int) -> int:
        r_bound = bisect_right(self.nums1_counts, (tot - 1, self.n1_max_occ))
        return sum(
            self.nums2_counts[tot - part] * occs
            for part, occs in self.nums1_counts[:r_bound]
            if (tot - part) in self.nums2_counts
        )


if __name__ == "__main__":
    find_sum_pairs = FindSumPairs([1, 1, 2, 2, 2, 3], [1, 4, 5, 2, 5, 4])
    assert find_sum_pairs.count(7) == 8
    find_sum_pairs.add(3, 2)
    assert find_sum_pairs.count(8) == 2
    assert find_sum_pairs.count(4) == 1
    find_sum_pairs.add(0, 1)
    find_sum_pairs.add(1, 1)
    assert find_sum_pairs.count(7) == 11
