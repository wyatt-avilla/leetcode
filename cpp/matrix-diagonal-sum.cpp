// https://leetcode.com/problems/matrix-diagonal-sum/description/

#include <cassert>
#include <vector>

using namespace std;

class Solution {
  public:
    int diagonalSum(vector<vector<int>>& mat) {
        size_t sum = 0;
        size_t dim = mat.size();
        size_t quadrant_size = dim / 2 + dim % 2;

        for (size_t i = 0; i < quadrant_size; ++i) {
            int edge = (dim - 1) - i;

            if (i == edge) {
                sum += mat.at(i).at(i);
                continue;
            }

            sum += mat.at(i).at(i);       // top left
            sum += mat.at(i).at(edge);    // top right
            sum += mat.at(edge).at(i);    // bottom left
            sum += mat.at(edge).at(edge); // bottom right
        }
        return sum;
    }
};

int main(int argc, char* argv[]) {
    Solution solution;

    vector<vector<int>> case1_in = {{1, 2, 3}, {4, 5, 6}, {7, 8, 9}};
    int case1_exp = 25;
    int case1_res = solution.diagonalSum(case1_in);
    assert(case1_exp == case1_res);


    return 0;
}
