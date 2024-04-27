// https://leetcode.com/problems/valid-anagram/

#include <cassert>
#include <iostream>
#include <set>
#include <stack>
#include <string>

class Solution {
  public:
    std::set<std::string> generate_anagrams(std::string s) {
        std::set<std::string> anagrams;
        std::stack<std::pair<std::string, std::string>> stack;
        stack.push(std::make_pair("", s));

        while (!stack.empty()) {
            std::string used = stack.top().first;
            std::string rem = stack.top().second;
            stack.pop();

            for (auto it = rem.begin(); it != rem.end(); ++it) {
                std::string include = used;

                include.push_back(*it);

                std::string new_rem = rem;
                new_rem.erase(new_rem.find(*it), 1);

                if (new_rem.size() == 0) {
                    anagrams.insert(include);
                } else {
                    stack.push(std::make_pair(include, new_rem));
                }
            }
        }

        return anagrams;
    }

    bool isAnagram(std::string s, std::string t) {
        for (char c : t) {
            size_t match = s.find(c);
            if (match == std::string::npos) {
                return false;
            }
            s.erase(match, 1);
        }
        return s.size() == 0;
    }
};


int main(void) {
    Solution solution;
    assert(solution.isAnagram("anagram", "nagaram"));
    assert(!solution.isAnagram("rat", "car"));

    return 0;
}
