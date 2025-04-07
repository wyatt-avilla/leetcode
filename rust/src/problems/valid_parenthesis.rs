// https://leetcode.com/problems/valid-parenthesis/

pub struct Solution;

impl Solution {
    pub fn is_valid(s: String) -> bool {
        let mut stack: Vec<char> = Vec::new();
        for c in s.chars() {
            let sub_valid: Option<bool> = match c {
                '(' => {
                    stack.push(c);
                    None
                }
                ')' => Some(stack.pop() == Some('(')),
                '[' => {
                    stack.push(c);
                    None
                }
                ']' => Some(stack.pop() == Some('[')),
                '{' => {
                    stack.push(c);
                    None
                }
                '}' => Some(stack.pop() == Some('{')),
                _ => panic!(),
            };
            if sub_valid.is_some() && sub_valid.unwrap() == false {
                return false;
            }
        }
        stack.len() == 0
    }
}

#[cfg(test)]
mod tests {
    use super::Solution;

    #[test]
    fn case_1() {
        let s = String::from("()");
        let result = Solution::is_valid(s);
        assert!(result);
    }

    #[test]
    fn case_2() {
        let s = String::from("()[]{}");
        let result = Solution::is_valid(s);
        assert!(result);
    }

    #[test]
    fn case_3() {
        let s = String::from("(]");
        let result = Solution::is_valid(s);
        assert!(!result);
    }

    #[test]
    fn case_4() {
        let s = String::from("([)]");
        let result = Solution::is_valid(s);
        assert!(!result);
    }
}
