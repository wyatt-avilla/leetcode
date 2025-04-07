// https://leetcode.com/problems/missing-number/

pub struct Solution;

impl Solution {
    pub fn missing_number(nums: Vec<i32>) -> i32 {
        let n = nums.iter().count() as i32;
        (n * (n + 1)) / 2 - nums.iter().sum::<i32>()
    }
}

#[cfg(test)]
mod tests {
    use super::Solution;

    #[test]
    fn case_1() {
        let nums = vec![3, 0, 1];
        assert_eq!(Solution::missing_number(nums), 2);
    }

    #[test]
    fn case_2() {
        let nums = vec![0, 1];
        assert_eq!(Solution::missing_number(nums), 2);
    }

    #[test]
    fn case_3() {
        let nums = vec![9, 6, 4, 2, 3, 5, 7, 0, 1];
        assert_eq!(Solution::missing_number(nums), 8);
    }
}
