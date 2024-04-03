// https://leetcode.com/problems/find-first-palindromic-string-in-the-array/description/

#include <cassert>
#include <string>
#include <vector>

using namespace std;

bool is_palindrome(string word) {
    const size_t len = word.size();

    for (size_t start = 0, end = len - 1; start < len; ++start, --end) {
        if (word.at(start) != word.at(end)) {
            return false;
        }
        if (start >= end) {
            break;
        }
    }

    return true;
}

class Solution {
  public:
    string firstPalindrome(vector<string>& words) {
        for (auto word : words) {
            if (is_palindrome(word)) {
                return word;
            }
        }
        return "";
    }
};

int main(int argc, char* argv[]) {
    Solution solution;


    vector<string> case1_in = {"abc", "car", "ada", "racecar", "cool"};
    string case1_exp = "ada";
    string case1_res = solution.firstPalindrome(case1_in);
    assert(case1_exp == case1_res);
    return 0;
}
