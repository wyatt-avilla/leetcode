// https://leetcode.com/problems/sum-of-values-at-indices-with-k-set-bits/

#include <cassert>
#include <vector>
using namespace std;

int count_bits(int n) {
    int bit_count = 0;

    for (; n != 0; n >>= 1) {
        if (n & 1) {
            ++bit_count;
        }
    }

    return bit_count;
}

class Solution {
  public:
    int sumIndicesWithKSetBits(std::vector<int>& nums, int k) {
        int sum = 0;

        for (int n = 0; n < nums.size(); n++) {
            int bit_count = count_bits(n);
            if (bit_count == k) {
                sum += nums.at(n);
            }
        }


        return sum;
    }
};

int main(int argc, char* argv[]) {
    Solution solution;

    vector<int> case1 = {5, 10, 1, 5, 2};
    assert(solution.sumIndicesWithKSetBits(case1, 1) == 13);

    return 0;
}
