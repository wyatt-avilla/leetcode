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

#[cfg(test)]
mod tests {
    use super::Solution;

    #[test]
    fn case_1() {
        let s = String::from("abab");
        assert!(Solution::repeated_substring_pattern(s));
    }

    #[test]
    fn case_2() {
        let s = String::from("aba");
        assert!(!Solution::repeated_substring_pattern(s));
    }

    #[test]
    fn case_3() {
        let s = String::from("abcabcabcabc");
        assert!(Solution::repeated_substring_pattern(s));
    }
}
