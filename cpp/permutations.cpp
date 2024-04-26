// https://leetcode.com/problems/permutations/

#include <algorithm>
#include <iostream>
#include <stack>
#include <vector>

class Solution {
  public:
    std::vector<std::vector<int>> permute(std::vector<int>& nums) {
        std::vector<std::vector<int>> solution;
        std::stack<std::vector<int>> stack;

        stack.push(std::vector<int>());
        while (!stack.empty()) {
            std::vector<int> perm = stack.top();
            stack.pop();

            for (int num : nums) {
                if (std::find(perm.begin(), perm.end(), num) == perm.end()) {
                    std::vector<int> new_perm(perm.begin(), perm.end());
                    new_perm.push_back(num);

                    new_perm.size() == nums.size()
                        ? solution.push_back(new_perm)
                        : stack.push(new_perm);
                }
            }
        }

        return solution;
    }
};

int main(void) {

    Solution solution;

    std::vector<int> inp_1 = {1, 2, 3};
    std::vector<std::vector<int>> res_1 = solution.permute(inp_1);

    for (auto vec : res_1) {
        std::cout << "{ ";
        for (int num : vec) {
            std::cout << num << " ";
        }
        std::cout << "}" << std::endl;
    }


    return 0;
}
