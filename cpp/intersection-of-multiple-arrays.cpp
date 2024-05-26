// https://leetcode.com/problems/intersection-of-multiple-arrays/

#include <algorithm>
#include <iostream>
#include <vector>
class Solution {
  public:
    std::vector<int> intersection(std::vector<std::vector<int>>& nums) {
        std::vector<int> answer;

        int biggest_idx = 0;
        for (int i = 0; i < nums.size(); ++i) {
            if (nums[i].size() > nums[biggest_idx].size()) {
                biggest_idx = i;
            }
        }

        std::vector<int> biggest_vec = nums[biggest_idx];
        nums.erase(nums.begin() + biggest_idx);

        for (int num : biggest_vec) {
            bool in_all = true;
            for (std::vector<int>& vec : nums) {
                if (std::find(vec.begin(), vec.end(), num) == vec.end()) {
                    in_all = false;
                    break;
                }
            }
            if (in_all) {
                answer.push_back(num);
            }
        }

        std::sort(answer.begin(), answer.end());
        return answer;
    }
};

int main(void) {
    Solution solution;
    std::vector<std::vector<int>> case1 = {
        {3, 1, 2, 4, 5}, {1, 2, 3, 4}, {3, 4, 5, 6}};

    for (int num : solution.intersection(case1)) {
        std::cout << num << " ";
    }
    std::cout << std::endl;

    return 0;
}
