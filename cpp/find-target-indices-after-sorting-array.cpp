// https://leetcode.com/problems/find-target-indices-after-sorting-array/

#include <iostream>
#include <numeric>
#include <vector>

class Solution {
  public:
    std::vector<int> targetIndices(std::vector<int>& nums, int target) {
        int target_count = 0;
        int less_than_target = 0;
        for (int num : nums) {
            if (num == target) {
                target_count += 1;
            }
            if (num < target) {
                less_than_target += 1;
            }
        }

        std::vector<int> answer(target_count);
        std::iota(answer.begin(), answer.end(), less_than_target);
        return answer;
    }
};

int main(void) {
    Solution solution;

    std::vector<int> case1 = {1, 2, 5, 2, 3};
    for (int num : solution.targetIndices(case1, 2)) {
        std::cout << num << " ";
    }
    std::cout << std::endl;

    return 0;
}
