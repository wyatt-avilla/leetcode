// https://leetcode.com/problems/search-a-2d-matrix-ii/

#include <cassert>
#include <iostream>
#include <vector>

class Solution {
  public:
    bool searchMatrix(std::vector<std::vector<int>>& matrix, int target) {
        const int n = matrix.size();
        const int m = matrix.front().size();

        int upper_row = 0;
        int upper_col = matrix.front().size() - 1;

        int lower_row = matrix.size() - 1;
        int lower_col = 0;

        bool one_moved = true;
        while (one_moved) {
            one_moved = false;
            if (upper_col >= 0 && upper_row < n) {
                if (matrix[upper_row][upper_col] > target) {
                    upper_col -= 1;
                } else if (matrix[upper_row][upper_col] < target) {
                    upper_row += 1;
                } else {
                    return true;
                }
                one_moved = true;
            }

            if (lower_row >= 0 && lower_col < m) {
                if (matrix[lower_row][lower_col] > target) {
                    lower_row -= 1;
                } else if (matrix[lower_row][lower_col] < target) {
                    lower_col += 1;
                } else {
                    return true;
                }
                one_moved = true;
            }
        }

        return false;
    }
};

int main(void) {
    Solution solution;
    std::vector<std::vector<int>> case1 = {{1, 4, 7, 11, 15},
                                           {2, 5, 8, 12, 19},
                                           {3, 6, 9, 16, 22},
                                           {10, 13, 14, 17, 24},
                                           {18, 21, 23, 26, 30}};

    assert(solution.searchMatrix(case1, 21));

    return 0;
}
