// https://leetcode.com/problems/maximum-xor-after-operations/

pub struct Solution;

impl Solution {
    pub fn maximum_xor(nums: Vec<i32>) -> i32 {
        nums.iter().fold(0, |acc, n| acc | n)
    }
}

#[cfg(test)]
mod tests {
    use super::Solution;

    #[test]
    fn case_1() {
        let nums = vec![3, 2, 4, 6];
        let result = Solution::maximum_xor(nums);
        assert_eq!(result, 7);
    }

    #[test]
    fn case_2() {
        let nums = vec![1, 2, 3, 9, 2];
        let result = Solution::maximum_xor(nums);
        assert_eq!(result, 11);
    }
}
