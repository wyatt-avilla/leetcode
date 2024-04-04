// https://leetcode.com/problems/left-and-right-sum-differences/

#include <algorithm>
#include <cassert>
#include <cstdlib>
#include <vector>

using namespace std;

class Solution {
  public:
    vector<int> leftRightDifference(vector<int>& nums) {
        vector<int> answer;

        vector<int> left_sum = {0};
        int left_running_sum = 0;
        for (auto it = nums.begin(); it != nums.end() - 1; ++it) {
            left_sum.push_back(*it + left_running_sum);
            left_running_sum += *it;
        }

        vector<int> right_sum = {0};
        int right_running_sum = 0;
        for (auto it = nums.rbegin(); it != nums.rend() - 1; ++it) {
            right_sum.push_back(*it + right_running_sum);
            right_running_sum += *it;
        }
        reverse(right_sum.begin(), right_sum.end());

        for (int i = 0; i < nums.size(); ++i) {
            answer.push_back(abs(left_sum.at(i) - right_sum.at(i)));
        }

        return answer;
    }
};

int main(int argc, char* argv[]) {

    Solution solution;

    vector<int> case1_in = {10, 4, 8, 3};
    vector<int> case1_exp = {15, 1, 11, 22};
    vector<int> case1_res = solution.leftRightDifference(case1_in);
    assert(case1_res == case1_exp);
    return 0;
}
