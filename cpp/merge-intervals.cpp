// https://leetcode.com/problems/merge-intervals/description/

#include <algorithm>
#include <iostream>
#include <vector>

class Solution {
  public:
    std::vector<std::vector<int>>
    merge(std::vector<std::vector<int>>& intervals) {
        std::sort(intervals.begin(), intervals.end(),
                  [](const std::vector<int>& v1, const std::vector<int>& v2) {
                      return v1[0] < v2[0];
                  });

        std::vector<std::vector<int>> answer = {intervals[0]};
        for (std::vector<int>& interval : intervals) {
            if (interval[0] <= answer.back()[1]) {
                answer.back()[1] = std::max(answer.back()[1], interval[1]);
            } else {
                answer.push_back(interval);
            }
        }

        return answer;
    }
};

int main(void) {
    Solution solution;
    std::vector<std::vector<int>> case_1 = {{1, 3}, {2, 6}, {8, 10}, {11, 18}};

    for (std::vector<int> range : solution.merge(case_1)) {
        std::cout << range[0] << " " << range[1] << std::endl;
    }

    std::cout << "---" << std::endl;

    std::vector<std::vector<int>> case_2 = {{1, 4}, {0, 4}};
    for (std::vector<int> range : solution.merge(case_2)) {
        std::cout << range[0] << " " << range[1] << std::endl;
    }


    return 0;
}
