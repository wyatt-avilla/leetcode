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
        let s = String::from("()");
        let result = Solution::is_valid(s);
        assert_eq!(result, true);
    }

    // Test case 2
    #[test]
    fn case2() {
        let s = String::from("()[]{}");
        let result = Solution::is_valid(s);
        assert_eq!(result, true);
    }

    // Test case 3
    #[test]
    fn case3() {
        let s = String::from("(]");
        let result = Solution::is_valid(s);
        assert_eq!(result, false);
    }

    // Test case 3
    #[test]
    fn case4() {
        let s = String::from("([)]");
        let result = Solution::is_valid(s);
        assert_eq!(result, false);
    }
}
