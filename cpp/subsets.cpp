// https://leetcode.com/problems/subsets/

#include <iostream>
#include <set>
#include <stack>
#include <utility>
#include <vector>

void print_vec(std::vector<int>& vec) {
    std::cout << "{ ";
    for (int num : vec) {
        std::cout << num << " ";
    }
    std::cout << "}";
}

class Solution {
  public:
    // i know this is a binary enumeration problem, but i wanted to practice
    // recursion w/ stacks
    std::vector<std::vector<int>> subsets(std::vector<int>& nums) {
        std::set<std::vector<int>> solution;

        std::stack<std::pair<std::vector<int>, std::vector<int>>> stack;
        stack.push(std::make_pair(std::vector<int>(), nums));

        while (!stack.empty()) {
            std::vector<int> used = stack.top().first;
            std::vector<int> remaining = stack.top().second;
            stack.pop();

            for (auto it = remaining.begin(); it != remaining.end(); ++it) {
                std::vector<int> include(used.begin(), used.end());
                std::vector<int> no_include(used.begin(), used.end());

                include.push_back(*it);
                std::vector<int> new_remaining(it + 1, remaining.end());

                if (new_remaining.size() == 0) {
                    solution.insert(include);
                    solution.insert(no_include);
                } else {
                    stack.push(std::make_pair(include, new_remaining));
                    stack.push(std::make_pair(no_include, new_remaining));
                }
            }
        }

        return std::vector<std::vector<int>>(solution.begin(), solution.end());
    }
};

int main(void) {
    Solution solution;

    std::vector<int> inp_1 = {1, 2, 3};
    std::vector<std::vector<int>> res_1 = solution.subsets(inp_1);

    for (auto vec : res_1) {
        print_vec(vec);
        std::cout << std::endl;
    }


    return 0;
}
