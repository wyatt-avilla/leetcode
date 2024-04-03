// https://leetcode.com/problems/running-sum-of-1d-array/description/

#include <cassert>
#include <vector>

using namespace std;

class Solution {
  public:
    vector<int> runningSum(vector<int>& nums) {
        vector<int> running_sum;

        unsigned int current_sum = 0;
        for (int n : nums) {
            current_sum += n;
            running_sum.push_back(current_sum);
        }

        return running_sum;
    }
};

int main(int argc, char* argv[]) {
    Solution solution;

    vector<int> case1_in = {1, 2, 3, 4};
    vector<int> case1_exp = {1, 3, 6, 10};
    vector<int> case1_res = solution.runningSum(case1_in);

    assert(case1_exp == case1_res);


    return 0;
}
