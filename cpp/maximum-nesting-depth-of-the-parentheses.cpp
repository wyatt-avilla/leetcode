// https://leetcode.com/problems/maximum-nesting-depth-of-the-parentheses/description/

#include <string>
using namespace std;

class Solution {
  public:
    int maxDepth(string s) {
        int newer = 0;
        unsigned int max_depth = 0;

        int stack = 0;
        for (const char& c : s) {
            switch (c) {
            case '(':
                ++stack;
                max_depth = stack > max_depth ? stack : max_depth;
                break;
            case ')':
                max_depth = stack > max_depth ? stack : max_depth;
                --stack;
                break;
            }
        }

        return max_depth;
    }
};

int main(int argc, char* argv[]) {
    Solution solution;
    solution.maxDepth("test");
    return 0;
}
