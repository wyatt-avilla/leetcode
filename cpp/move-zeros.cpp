// https://leetcode.com/problems/move-zeroes/

#include <iostream>
#include <vector>
class Solution {
  public:
    void moveZeroes(std::vector<int>& nums) {
        int num_size = nums.size();
        int pend = 0;
        int zero_count = 0;

        for (int i = 0; i < num_size; ++i) {
            if (nums[i] != 0) {
                nums[pend++] = nums[i];
            }
        }

        for (int i = pend; i < num_size; ++i) {
            nums[i] = 0;
        }
    }
};

int main(void) {
    Solution solution;

    std::vector<int> case1 = {0, 1, 0, 3, 12};
    solution.moveZeroes(case1);
    for (int num : case1) {
        std::cout << num << " ";
    }
    std::cout << std::endl;

    std::vector<int> case2 = {0, 0, 1};
    solution.moveZeroes(case2);
    for (int num : case2) {
        std::cout << num << " ";
    }
    std::cout << std::endl;

    return 0;
}
