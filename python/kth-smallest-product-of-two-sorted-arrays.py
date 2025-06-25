# https://leetcode.com/problems/kth-smallest-product-of-two-sorted-arrays/


from bisect import bisect_left, bisect_right


class Solution:
    def products_leq(self, nums2: list[int], x_1: int, bs_mid: int) -> int:
        if x_1 > 0:
            return bisect_right(nums2, bs_mid // x_1)
        elif x_1 < 0:
            return len(nums2) - bisect_left(nums2, -(-bs_mid // x_1))
        else:
            return len(nums2) if bs_mid >= 0 else 0

    def kthSmallestProduct(self, nums1: list[int], nums2: list[int], k: int) -> int:
        left = -(10**10)
        right = 10**10

        while left <= right:
            mid = (left + right) // 2
            count = 0
            for x_1 in nums1:
                count += self.products_leq(nums2, x_1, mid)
            if count < k:
                left = mid + 1
            else:
                right = mid - 1
        return left


if __name__ == "__main__":
    assert Solution().kthSmallestProduct([-2, -1, 0, 1, 2], [-3, -1, 2, 4, 5], 3) == -6
    assert Solution().kthSmallestProduct([-4, -2, 0, 3], [2, 4], 6) == 0
    assert Solution().kthSmallestProduct([2, 5], [3, 4], 2) == 8
