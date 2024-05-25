// https://leetcode.com/problems/maximum-subarray/

#include <algorithm>
#include <iostream>
#include <vector>

class Solution {
  public:
    int maxSubArray(std::vector<int>& nums) {
        int max_sum = nums[0];
        int cur_sum = nums[0];
        for (int i = 1; i < nums.size(); ++i) {
            cur_sum = std::max(nums[i], cur_sum + nums[i]);
            max_sum = std::max(max_sum, cur_sum);
        }
        return max_sum;
    }
};

int main(void) {
    Solution solution;

    std::vector<int> case_1 = {-2, 1, -3, 4, -1, 2, 1, -5, 4};
    std::cout << solution.maxSubArray(case_1) << std::endl;

    return 0;
}
