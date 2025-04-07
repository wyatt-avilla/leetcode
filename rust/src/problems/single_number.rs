// https://leetcode.com/problems/single-number/

pub struct Solution;

impl Solution {
    pub fn single_number_old(mut nums: Vec<i32>) -> i32 {
        let nums_len = nums.len();
        if nums_len == 1 {
            return nums[0];
        }

        nums.sort(); // "quasi-linear"
        let mut iter = nums.iter();
        let mut left: &i32;
        let mut right: &i32;
        for _ in 0..nums_len / 2 {
            left = iter.next().unwrap();
            right = iter.next().unwrap();
            if (*left ^ *right) != 0 {
                println!("l:{}, r:{}, res:{}", *left, *right, *left ^ *right);
                let next = iter.next().unwrap();
                return if *left ^ *next != 0 { *left } else { *right };
            }
        }
        nums[nums_len - 1]
    }

    pub fn single_number(nums: Vec<i32>) -> i32 {
        // sheesh. me when xor
        nums.iter().fold(0, |acc, &next| acc ^ next)
    }
}

#[cfg(test)]
mod tests {
    use super::Solution;

    #[test]
    fn case_1() {
        let nums = vec![2, 2, 1];
        assert_eq!(Solution::single_number(nums), 1);
    }

    #[test]
    fn case_2() {
        let nums = vec![4, 1, 2, 1, 2];
        assert_eq!(Solution::single_number(nums), 4);
    }

    #[test]
    fn case_3() {
        let nums = vec![1];
        assert_eq!(Solution::single_number(nums), 1);
    }

    #[test]
    fn case_4() {
        let nums = vec![2, 1, 2, 1, 4];
        assert_eq!(Solution::single_number(nums), 4);
    }

    #[test]
    fn case_5() {
        let nums = vec![
            -336, 513, -560, -481, -174, 101, -997, 40, -527, -784, -283, -336, 513, -560, -481,
            -174, 101, -997, 40, -527, -784, -283, 354,
        ];
        assert_eq!(Solution::single_number(nums), 354);
    }

    #[test]
    fn case_6() {
        let nums = vec![1, 2, 2];
        assert_eq!(Solution::single_number(nums), 1);
    }
}
