// https://leetcode.com/problems/next-greater-element-ii/

#include <iostream>
#include <vector>
class Solution {
  public:
    std::vector<int> nextGreaterElements(std::vector<int>& nums) {
        int num_len = nums.size();
        std::vector<int> answer;

        for (int i = 0; i < num_len; ++i) {

            int s = i + 1;
            for (int j = 0; j < num_len; ++j) {
                s %= num_len;

                if (nums[s] > nums[i]) {
                    answer.push_back(nums[s]);
                    break;
                }
                s += 1;
            }

            if (answer.size() == i) {
                answer.push_back(-1);
            }
        }

        return answer;
    }
};

int main(void) {

    Solution solution;
    std::vector<int> case_1 = {1, 2, 1};

    for (int num : solution.nextGreaterElements(case_1)) {
        std::cout << num << " ";
    }
    std::cout << std::endl;

    return 0;
}
