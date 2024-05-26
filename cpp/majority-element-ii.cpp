// https://leetcode.com/problems/majority-element-ii/

#include <algorithm>
#include <iostream>
#include <map>
#include <vector>

class Solution {
  public:
    std::vector<int> majorityElement(std::vector<int>& nums) {
        std::vector<int> answer;

        const int part_size = 3;
        const int threshold = nums.size() / part_size;

        std::map<int, int> counts;

        for (int num : nums) {
            counts[num] += 1;

            if (counts.size() >= part_size) {
                std::map<int, int> new_counts;
                for (const auto& pair : counts) {
                    if (pair.second > 1) {
                        new_counts[pair.first] = pair.second - 1;
                    }
                }
                counts = new_counts;
            }
        }

        for (const auto& pair : counts) {
            if (std::count(nums.begin(), nums.end(), pair.first) > threshold) {
                answer.push_back(pair.first);
            }
        }

        return answer;
    }
};

int main(void) {
    Solution solution;

    std::vector<int> case1 = {3, 2, 3};
    for (int num : solution.majorityElement(case1)) {
        std::cout << num << " ";
    }
    std::cout << std::endl;

    return 0;
}
