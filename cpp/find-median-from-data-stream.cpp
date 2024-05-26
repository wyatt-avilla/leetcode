// https://leetcode.com/problems/find-median-from-data-stream/

#include <iostream>
#include <vector>

class MedianFinder {
  public:
    MedianFinder() {}

    void addNum(int num) {
        stream.insert(stream.begin() + insert_idx(0, stream.size(), num), num);
    }

    double findMedian() {
        int ss = stream.size();
        if (ss % 2 == 1) {
            return stream[ss / 2];
        } else {
            return (stream[ss / 2] + stream[ss / 2 - 1]) / 2.0;
        }
    }

    friend std::ostream& operator<<(std::ostream& os, const MedianFinder& m) {
        os << "{ ";
        for (int num : m.stream) {
            os << num << " ";
        }
        os << "}";
        return os;
    }

  private:
    std::vector<int> stream;

    int insert_idx(int l, int r, int num) {
        int mid = l + (r - l) / 2;

        if (l >= r) {
            return l;
        }

        if (stream[mid] > num) {
            return insert_idx(l, mid, num);
        } else if (stream[mid] < num) {
            return insert_idx(mid + 1, r, num);
        } else {
            return mid;
        }
    }
};

int main(void) {
    MedianFinder mf;
    mf.addNum(5);
    mf.addNum(4);
    mf.addNum(3);
    mf.addNum(2);
    mf.addNum(1);
    std::cout << mf.findMedian() << std::endl;
    return 0;
}
