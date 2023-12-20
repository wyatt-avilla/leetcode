// https://leetcode.com/problems/maximum-odd-binary-number/

pub struct Solution;

impl Solution {
    pub fn maximum_odd_binary_number(s: String) -> String {
        let mut max_odd_bin = String::new();
        let total_ones = s.chars().filter(|&c| c == '1').count();
        let total_zeros = s.len() - total_ones;

        let left_ones: String = std::iter::repeat("1").take(total_ones-1).collect();
        let zeros: String = std::iter::repeat("0").take(total_zeros).collect();

        max_odd_bin.push_str(&left_ones);
        max_odd_bin.push_str(&zeros);
        max_odd_bin.push_str("1");
        max_odd_bin
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
        let s = String::from("010");
        let result = Solution::maximum_odd_binary_number(s);
        assert_eq!(result, String::from("001"));
    }

    // Test case 2
    #[test]
    fn case2() {
        let s = String::from("0101");
        let result = Solution::maximum_odd_binary_number(s);
        assert_eq!(result, String::from("1001"));
    }
}
