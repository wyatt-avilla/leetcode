// https://leetcode.com/problems/merge-sorted-array/

#include "data_structures.h"

#include <vector>

class Solution {
  public:
    void merge(std::vector<int>& nums1, int m, std::vector<int>& nums2, int n) {
        int p1 = m - 1;
        int p2 = n - 1;
        int pi = nums1.size() - 1;

        while (pi >= 0) {
            if (p1 < 0) {
                nums1[pi] = nums2[p2--];
            } else if (p2 < 0) {
                nums1[pi] = nums1[p1--];
            } else {
                if (nums1[p1] >= nums2[p2]) {
                    nums1[pi] = nums1[p1--];
                } else {
                    nums1[pi] = nums2[p2--];
                }
            }

            pi -= 1;
        }
    }
};

int main(void) {
    Solution solution;
    std::vector<int> nums1_case1 = {1, 2, 3, 0, 0, 0};
    std::vector<int> nums2_case1 = {2, 5, 6};
    solution.merge(nums1_case1, 3, nums2_case1, 3);

    for (int num : nums1_case1) {
        std::cout << num << " ";
    }
    std::cout << std::endl;

    return 0;
}
