// https://leetcode.com/problems/sum-of-beauty-of-all-substrings/

#include <cassert>
#include <iostream>
#include <limits>
#include <map>
#include <set>
#include <stack>
#include <string>
#include <vector>

void print_vec(std::vector<std::string>& vec) {
    std::cout << "{ ";
    for (std::string s : vec) {
        std::cout << s << " ";
    }
    std::cout << "}";
}

class Solution {
  public:
    int calculate_beauty(std::string s) {
        std::map<char, int> freq;

        for (char c : s) {
            freq[c] += 1;
        }

        int min = std::numeric_limits<int>::max();
        int max = 0;
        for (const auto& pair : freq) {
            if (pair.second < min) {
                min = pair.second;
            }
            if (pair.second > max) {
                max = pair.second;
            }
        }

        return max - min;
    }

    std::set<std::string> generate_all_substrings(std::string s) {
        std::set<std::string> all_substrings;
        std::stack<std::pair<std::string, std::string>> stack;
        stack.push(std::make_pair("", s));

        while (!stack.empty()) {
            std::string used = stack.top().first;
            std::string rem = stack.top().second;
            stack.pop();

            all_substrings.insert(used);

            std::cout << "[" << used << "-" << rem << "]" << std::endl;

            std::string new_used = used;
            new_used.push_back(rem.front());

            std::string new_rem = rem.substr(1);

            if (new_rem.size() > 0) {
                stack.push(std::make_pair(new_used, new_rem));
            }
        }

        return all_substrings;
    }

    int beautySum(std::string s) {
        int sum = 0;
        for (std::string str : all_subs_stack(s)) {
            int beauty = calculate_beauty(str);
            sum += calculate_beauty(str);
        }
        return sum;
    }

    std::pair<std::vector<std::string>, std::vector<std::string>>
    all_subs_rec(std::string s) {
        if (s.size() == 0) {
            return std::pair<std::vector<std::string>,
                             std::vector<std::string>>();
        }

        auto res = all_subs_rec(s.substr(1));
        std::vector<std::string> include = res.first;
        std::vector<std::string> no_include = res.second;

        std::vector<std::string> new_include;
        std::string prefix = s.substr(0, 1);
        new_include.push_back(prefix);

        for (std::string s : include) {
            no_include.push_back(s);

            new_include.push_back(prefix + s);
        }


        return std::make_pair(new_include, no_include);
    }

    std::vector<std::string> all_subs_stack(std::string s) {
        std::vector<std::string> all_subs;

        std::stack<std::string> prefix_stack;

        for (char prefix : s) {
            prefix_stack.push(std::string({prefix}));
        }

        std::vector<std::string> generated_subs;
        while (!prefix_stack.empty()) {
            std::string prefix = prefix_stack.top();
            prefix_stack.pop();

            for (std::string& sub : generated_subs) {
                std::string cpy = sub;
                all_subs.push_back(cpy);
                sub.insert(0, prefix);
            }
            generated_subs.push_back(prefix);
        }


        all_subs.insert(all_subs.end(), generated_subs.begin(),
                        generated_subs.end());
        return all_subs;
    }
};


int main(void) {
    Solution solution;

    assert(solution.beautySum("aabcb") == 5);
    assert(solution.beautySum("aabcbaa") == 17);

    return 0;
}
