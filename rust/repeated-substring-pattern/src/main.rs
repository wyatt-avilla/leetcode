// https://leetcode.com/problems/repeated-substring-pattern/

pub struct Solution;

impl Solution {
    pub fn repeated_substring_pattern(s: String) -> bool {
        let s_len = s.len();
        (1..s_len)
            .filter(|&i| s_len % i == 0)
            .any(|f| &s[0..f].repeat(s_len / f) == &s)
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
        let s = String::from("abab");
        assert_eq!(Solution::repeated_substring_pattern(s), true);
    }

    // Test case 2
    #[test]
    fn case2() {
        let s = String::from("aba");
        assert_eq!(Solution::repeated_substring_pattern(s), false);
    }

    // Test case 3
    #[test]
    fn case3() {
        let s = String::from("abcabcabcabc");
        assert_eq!(Solution::repeated_substring_pattern(s), true);
    }
}
