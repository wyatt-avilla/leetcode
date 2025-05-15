// https://leetcode.com/problems/range-sum-query-immutable/

struct NumArray {
    prefix_sums: Vec<i32>,
}

impl NumArray {
    fn new(nums: Vec<i32>) -> Self {
        NumArray {
            prefix_sums: nums
                .iter()
                .scan(0, |s, &x| {
                    *s += x;
                    Some(*s)
                })
                .collect(),
        }
    }

    fn sum_range(&self, left: i32, right: i32) -> i32 {
        if left == 0 {
            self.prefix_sums[right as usize]
        } else {
            self.prefix_sums[right as usize] - self.prefix_sums[left as usize - 1]
        }
    }
}

#[cfg(test)]
mod tests {
    use super::NumArray;

    #[test]
    fn case_1() {
        let na = NumArray::new(vec![-2, 0, 3, -5, 2, -1]);
        dbg!(&na.prefix_sums);
        assert_eq!(na.sum_range(0, 2), 1);
        assert_eq!(na.sum_range(2, 5), -1);
        assert_eq!(na.sum_range(0, 5), -3);
    }
}
