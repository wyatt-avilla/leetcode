// https://leetcode.com/problems/top-k-frequent-elements/

#include <iostream>
#include <numeric>
#include <unordered_map>
#include <vector>

class Solution {
  public:
    std::vector<int> topKFrequent(std::vector<int>& nums, int k) {
        const std::unordered_map<int, int> num_freq = std::accumulate(
            nums.begin(), nums.end(), std::unordered_map<int, int>{},
            [](auto& map, int num) {
                ++map[num];
                return map;
            });

        std::vector<std::vector<int>> bucket;
        bucket.resize(nums.size() + 1);
        for (const auto& pair : num_freq) {
            bucket[pair.second].push_back(pair.first);
        }

        std::vector<int> answer;
        answer.reserve(k);

        for (int i = bucket.size() - 1; i >= 0 && answer.size() < k; --i) {
            if (bucket[i].empty()) {
                continue;
            }

            if (answer.size() + bucket[i].size() <= k) {
                answer.insert(answer.end(), bucket[i].begin(), bucket[i].end());
            } else {
                answer.insert(answer.end(), bucket[i].begin(),
                              bucket[i].begin() + (k - answer.size()));
            }
        }

        return answer;
    }
};

int main(void) {
    Solution solution;
    std::vector<int> case1 = {1, 1, 1, 1, 2, 2, 3};
    for (int num : solution.topKFrequent(case1, 2)) {
        std::cout << num << " ";
    }
    std::cout << std::endl;


    return 0;
}
