// https://leetcode.com/problems/find-k-closest-elements/

#include <iostream>
#include <vector>

class Solution {
  public:
    std::vector<int> findClosestElements(std::vector<int>& arr, int k, int x) {
        int x_idx = iter_bin_search(arr, x);

        int start = x_idx;
        int end = x_idx;

        for (int i = 0; i < k - 1; ++i) {
            if (start <= 0) {
                end += 1;
            } else if (end >= arr.size() - 1) {
                start -= 1;
            } else {
                int a = arr[start - 1];
                int b = arr[end + 1];
                if ((std::abs(a - x) < std::abs(b - x)) ||
                    (std::abs(a - x) == std::abs(b - x) && a < b)) {
                    start -= 1;
                } else {
                    end += 1;
                }
            }
        }

        return std::vector<int>(arr.begin() + start, arr.begin() + end + 1);
    }

  private:
    int iter_bin_search(const std::vector<int>& arr, int x) {
        int l = 0;
        int r = arr.size() - 1;

        int best_val = arr[0];
        int best_idx = 0;

        int mid, curr_diff, best_diff;
        while (l <= r) {
            mid = l + (r - l) / 2;

            curr_diff = std::abs(arr[mid] - x);
            best_diff = std::abs(best_val - x);

            if ((curr_diff < best_diff) ||
                (curr_diff == best_diff && (arr[mid] < best_val))) {
                best_val = arr[mid];
                best_idx = mid;
            }

            if (arr[mid] > x) {
                r = mid - 1;
            } else if (arr[mid] < x) {
                l = mid + 1;
            } else {
                break;
            }
        }

        return best_idx;
    }
};

int main(void) {
    Solution solution;

    std::vector<int> case1 = {1, 2, 3, 4, 5};
    for (int num : solution.findClosestElements(case1, 3, 4)) {
        std::cout << num << " ";
    }
    std::cout << std::endl;

    std::vector<int> case2 = {1, 2, 4, 5};
    for (int num : solution.findClosestElements(case2, 2, 3)) {
        std::cout << num << " ";
    }
    std::cout << std::endl;

    std::vector<int> case3 = {1};
    for (int num : solution.findClosestElements(case3, 1, 0)) {
        std::cout << num << " ";
    }
    std::cout << std::endl;

    std::vector<int> case4 = {1, 1, 8, 10, 10, 10};
    for (int num : solution.findClosestElements(case4, 3, 9)) {
        std::cout << num << " ";
    }
    std::cout << std::endl;

    std::vector<int> case5 = {0, 0, 1, 2, 3, 3, 4, 7, 7, 8};
    for (int num : solution.findClosestElements(case5, 3, 5)) {
        std::cout << num << " ";
    }
    std::cout << std::endl;
    return 0;
}
