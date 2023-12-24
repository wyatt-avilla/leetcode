// https://leetcode.com/problems/single-number/

pub struct Solution;

impl Solution {
    pub fn single_number_old(mut nums: Vec<i32>) -> i32 {
        let nums_len = nums.len();
        if nums_len == 1 { return nums[0] }

        nums.sort(); // "quasi-linear"
        let mut iter = nums.iter();
        let mut left: &i32;
        let mut right: &i32;
        for _ in 0..nums_len/2 {
            left = iter.next().unwrap();
            right = iter.next().unwrap();
            if (*left ^ *right) != 0 {
                println!("l:{}, r:{}, res:{}", *left, *right, *left ^ *right);
                let next = iter.next().unwrap();
                return if *left ^ *next != 0 {*left} else {*right}
            }
        }
        nums[nums_len-1]
    }

    pub fn single_number(nums: Vec<i32>) -> i32 { // sheesh. me when xor
        nums.iter().fold(0, |acc, &next| acc ^ next)
    }
}

fn main() {
    println!("main executed")
}

// Import the necessary modules
#[cfg(test)]
mod tests {
    // Import the Solution struct (assuming it's in the same module or crate)
    use super::Solution;

    // Test case 1
    #[test]
    fn case1() {
        let nums = vec![2,2,1];
        assert_eq!(Solution::single_number(nums), 1);
    }

    // Test case 2
    #[test]
    fn case2() {
        let nums = vec![4,1,2,1,2];
        assert_eq!(Solution::single_number(nums), 4);
    }
    
    // Test case 3
    #[test]
    fn case3() {
        let nums = vec![1];
        assert_eq!(Solution::single_number(nums), 1);
    }

    // Test case 4
    #[test]
    fn case4() {
        let nums = vec![2,1,2,1,4];
        assert_eq!(Solution::single_number(nums), 4);
    }

    // Test case 5
    #[test]
    fn case5() {
        let nums = vec![-336,513,-560,-481,-174,101,-997,40,-527,-784,-283,-336,513,-560,-481,-174,101,-997,40,-527,-784,-283,354];
        assert_eq!(Solution::single_number(nums), 354);
    }

    // Test case 6
    #[test]
    fn case6() {
        let nums = vec![1,2,2];
        assert_eq!(Solution::single_number(nums), 1);
    }
}
