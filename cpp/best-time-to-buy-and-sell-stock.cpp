// https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

#include <iostream>
#include <vector>

class Solution {
  public:
    int maxProfit(std::vector<int>& prices) {
        int arr_size = prices.size();
        int max_profit = 0;

        int l = 0;
        int r = 1;

        while (r < arr_size) {
            if (prices[l] > prices[r]) {
                l = r;
            } else {
                max_profit = std::max(max_profit, prices[r] - prices[l]);
            }
            r += 1;
        }

        return max_profit;
    }
};

int main(void) {
    Solution solution;

    std::vector<int> case1 = {1, 8, 5, 6, 3, 2};
    std::cout << solution.maxProfit(case1) << std::endl;

    std::vector<int> case2 = {1, 2, 11, 4, 7};
    std::cout << solution.maxProfit(case2) << std::endl;

    return 0;
}
