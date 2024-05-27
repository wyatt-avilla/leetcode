// https://leetcode.com/problems/find-peak-element/

#include <climits>
#include <iostream>
#include <vector>

class Solution {
  public:
    int findPeakElement(std::vector<int>& nums) {
        int l = 0;
        int r = nums.size();
        int l_adj, r_adj, mid, target;
        while (l <= r) {
            mid = l + (r - l) / 2;

            target = nums[mid];
            l_adj = (mid - 1 >= 0) ? nums[mid - 1] : target;
            r_adj = (mid + 1 < nums.size()) ? nums[mid + 1] : target;


            if (l_adj <= target && r_adj <= target) {
                return mid;
            }

            if (l_adj >= target) {
                r = mid;
            } else {
                l = mid + 1;
            }
        }

        return -1;
    }
};

int main(void) {
    Solution solution;

    std::vector<int> case1 = {1, 2, 3, 1};
    std::cout << solution.findPeakElement(case1) << std::endl;

    std::vector<int> case2 = {1, 2, 1, 3, 5, 6, 4};
    std::cout << solution.findPeakElement(case2) << std::endl;

    std::vector<int> case3 = {1};
    std::cout << solution.findPeakElement(case3) << std::endl;

    return 0;
}
