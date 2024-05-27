// https://leetcode.com/problems/kth-largest-element-in-a-stream/

#include <algorithm>
#include <iostream>
#include <vector>

class KthLargest {
  public:
    KthLargest(int k, std::vector<int>& nums) : k(k) {
        stream = nums;
        std::sort(stream.begin(), stream.end());
    }

    int add(int val) {
        int idx = insert_idx(0, stream.size(), val);
        stream.insert(stream.begin() + idx, val);
        return stream[stream.size() - k];
    }

    friend std::ostream& operator<<(std::ostream& os, const KthLargest& obj) {
        os << "{ ";
        for (int num : obj.stream) {
            os << num << " ";
        }
        os << "}";
        return os;
    }

  private:
    const int k;

    int insert_idx(int l, int r, int num) {
        int mid = l + (r - l) / 2;
        if (l == r) {
            return mid;
        }

        if (stream[mid] > num) {
            return insert_idx(l, mid, num);
        } else if (stream[mid] < num) {
            return insert_idx(mid + 1, r, num);
        } else {
            return mid;
        }
    }
    std::vector<int> stream;
};

int main(void) {
    std::vector<int> nums = {4, 5, 8, 2};
    KthLargest obj = KthLargest(3, nums);

    std::cout << obj.add(3) << std::endl;
    std::cout << obj << std::endl;
    std::cout << obj.add(5) << std::endl;
    std::cout << obj << std::endl;
    std::cout << obj.add(10) << std::endl;
    std::cout << obj.add(9) << std::endl;
    std::cout << obj.add(4) << std::endl;

    return 0;
}
