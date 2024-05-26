// https://leetcode.com/problems/partition-array-according-to-given-pivot/

#include <iostream>
#include <vector>

class Solution {
  public:
    std::vector<int> pivotArray_constant_space(std::vector<int>& nums,
                                               int pivot) {
        int lesser_count = 0;
        int equal_count = 0;

        for (int num : nums) {
            if (num < pivot) {
                lesser_count += 1;
            } else if (num == pivot) {
                equal_count += 1;
            }
        }

        int mid_start = lesser_count;
        int mid_end = lesser_count + equal_count - 1;

        for (int i = 0; i < nums.size(); ++i) {
            int found_idx = i;
            while (
                (i < mid_start && nums[found_idx] >= pivot) ||
                (i > mid_end && nums[found_idx] <= pivot) ||
                (i >= mid_start && i <= mid_end && nums[found_idx] != pivot)) {
                found_idx += 1;
            }

            int found_num = nums[found_idx];
            for (int j = found_idx; j > i; --j) {
                nums[j] = nums[j - 1];
            }
            nums[i] = found_num;
        }

        return nums;
    }

    std::vector<int> pivotArray(std::vector<int>& nums, int pivot) {
        std::vector<int> answer;
        int lesserp = 0;
        int pivot_p = 0;
        int greater_p = 0;

        for (int num : nums) {
            auto vbegin = answer.begin();
            if (num < pivot) {
                answer.insert(vbegin + lesserp, num);
                lesserp += 1;
                pivot_p += 1;
                greater_p += 1;
            } else if (num == pivot) {
                answer.insert(vbegin + pivot_p, num);
                pivot_p += 1;
                greater_p += 1;
            } else { // num > pivot
                answer.insert(vbegin + greater_p, num);
                greater_p += 1;
            }
        }

        return answer;
    }
};

int main(void) {
    Solution solution;

    std::vector<int> case1 = {9, 12, 5, 10, 14, 3, 10};
    std::vector<int> res1 = solution.pivotArray(case1, 10);

    for (int num : res1) {
        std::cout << num << " ";
    }
    std::cout << std::endl;

    std::vector<int> case2 = {-3, 4, 3, 2};
    solution.pivotArray(case2, 2);

    for (int num : case2) {
        std::cout << num << " ";
    }
    std::cout << std::endl;

    return 0;
}
