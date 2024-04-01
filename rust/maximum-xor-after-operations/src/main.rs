// https://leetcode.com/problems/maximum-xor-after-operations/

pub struct Solution;

impl Solution {
    pub fn maximum_xor(nums: Vec<i32>) -> i32 {
        nums.iter().fold(0, |acc, n| acc | n)
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
        let nums = vec![3, 2, 4, 6];
        let result = Solution::maximum_xor(nums);
        assert_eq!(result, 7);
    }

    // Test case 2
    #[test]
    fn case2() {
        let nums = vec![1, 2, 3, 9, 2];
        let result = Solution::maximum_xor(nums);
        assert_eq!(result, 11);
    }
}
