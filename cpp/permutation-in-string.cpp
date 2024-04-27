// https://leetcode.com/problems/permutation-in-string/

#include <iostream>
#include <set>
#include <stack>
#include <string>
#include <utility>

class Solution {
  public:
    std::set<std::string> generate_permutations(std::string s) {
        std::set<std::string> permutations;
        std::stack<std::pair<std::string, std::string>> stack;
        stack.push(std::make_pair("", s));

        while (!stack.empty()) {
            std::string used = stack.top().first;
            std::string rem = stack.top().second;
            stack.pop();

            for (auto it = rem.begin(); it != rem.end(); ++it) {
                std::string new_used = used;
                new_used.push_back(*it);

                std::string new_rem = rem;
                new_rem.erase(new_rem.find(*it), 1);

                if (new_rem.size() == 0) {
                    permutations.insert(new_used);
                } else {
                    stack.push(std::make_pair(new_used, new_rem));
                }
            }
        }

        return permutations;
    }

    bool checkInclusion(std::string s1, std::string s2) {
        for (std::string perm : generate_permutations(s1)) {
            if (s2.find(perm) != std::string::npos) {
                return true;
            }
        }
        return false;
    }
};

int main(void) {
    Solution solution;

    solution.checkInclusion("abc", "abc");

    return 0;
}
