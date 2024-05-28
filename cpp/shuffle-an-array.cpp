#include <iostream>
#include <random>
#include <utility>
#include <vector>

class Solution {
  public:
    Solution(std::vector<int>& nums)
        : original_perm(nums), p_size(nums.size()), gen(rd()) {}

    std::vector<int> reset() { return original_perm; }

    std::vector<int> shuffle() {

        std::vector<int> perm = original_perm;
        int last_p = p_size - 1;
        for (int i = 0; i < p_size; ++i) {
            std::uniform_int_distribution<> dis(0, last_p);
            int rand = dis(gen);
            std::swap(perm[rand], perm[last_p--]);
        }
        return perm;
    }

  private:
    const std::vector<int> original_perm;
    const int p_size;
    std::random_device rd;
    std::mt19937 gen;
};

int main(void) {
    std::vector<int> case1 = {1, 2, 3};
    Solution solution(case1);

    auto shuffled = solution.shuffle();
    for (int num : shuffled) {
        std::cout << num << " " << std::endl;
    }

    return 0;
}
