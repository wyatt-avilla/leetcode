// https://leetcode.com/problems/rotate-string/

pub struct Solution;

impl Solution {
    // the alternative "double s" solution to this is really clever
    pub fn rotate_string(s: String, goal: String) -> bool {
        let s_len = s.len();
        let goal: Vec<char> = goal.chars().collect();
        let mut s: Vec<char> = s.chars().collect();

        (0..s_len).any(|_| {
            s.rotate_right(1);
            s == goal
        })
    }
}

#[cfg(test)]
mod tests {
    use super::Solution;

    #[test]
    fn case_1() {
        let s = "abcde".to_string();
        let goal = "cdeab".to_string();
        assert!(Solution::rotate_string(s, goal));
    }

    #[test]
    fn case_2() {
        let s = "abcde".to_string();
        let goal = "abced".to_string();
        assert!(!Solution::rotate_string(s, goal));
    }
}
