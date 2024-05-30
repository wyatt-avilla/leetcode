// https://leetcode.com/problems/smallest-range-covering-elements-from-k-lists/

#include <algorithm>
#include <iostream>
#include <queue>
#include <vector>

class Solution {
  public:
    std::vector<int> smallestRange(std::vector<std::vector<int>>& nums) {
        std::vector<IterWrapper> const_iters;
        std::transform(
            nums.cbegin(), nums.cend(), std::back_inserter(const_iters),
            [](const std::vector<int>& inner_vec) {
                return IterWrapper(inner_vec.cbegin(), inner_vec.cend());
            });

        std::priority_queue<IterWrapper, std::vector<IterWrapper>,
                            std::greater<>>
            min_heap(const_iters.begin(), const_iters.end());

        int upper_bound = **std::max_element(
            const_iters.begin(), const_iters.end(),
            [](const auto& a, const auto& b) { return *a < *b; });

        std::vector<int> answer = {*min_heap.top(), upper_bound};
        while (!min_heap.empty()) {
            auto it = min_heap.top();
            min_heap.pop();
            if (upper_bound - *it < answer[1] - answer[0]) {
                answer[0] = *it;
                answer[1] = upper_bound;
            }

            if ((++it).is_end()) {
                break;
            }

            upper_bound = std::max(upper_bound, *it);
            min_heap.push(it);
        }

        return answer;
    }

  private:
    struct IterWrapper {
        std::vector<int>::const_iterator it;
        std::vector<int>::const_iterator end;

        IterWrapper(std::vector<int>::const_iterator it,
                    std::vector<int>::const_iterator end)
            : it(it), end(end) {}

        int operator*() const { return *it; }

        IterWrapper& operator++() {
            ++it;
            return *this;
        }

        bool operator>(const IterWrapper& other) const {
            return *it > *other.it;
        }

        bool is_end() const { return it == end; }
    };
};


int main(void) {
    Solution solution;

    std::vector<std::vector<int>> case1 = {
        {4, 10, 15, 24, 25},
        {0, 9, 12, 20},
        {5, 18, 22, 30},
    };

    auto res1 = solution.smallestRange(case1);
    // std::cout << "[" << res1[0] << "," << res1[1] << "]" << std::endl;

    std::vector<std::vector<int>> case2 = {
        {1, 2, 3},
        {1, 2, 3},
        {1, 2, 3},
    };

    auto res2 = solution.smallestRange(case2);
    // std::cout << "[" << res2[0] << "," << res2[1] << "]" << std::endl;


    return 0;
}
