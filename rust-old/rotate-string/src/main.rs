// https://leetcode.com/problems/rotate-string/

pub struct Solution;

impl Solution {
    // the alternative "double s" solution to this is really clever
    pub fn rotate_string(s: String, goal: String) -> bool {
        let s_len = s.len();
        let goal: Vec<char> = goal.chars().collect();
        let mut s: Vec<char> = s.chars().collect();

        (0..s_len).any(|_| {
            s.rotate_right(1); // ty core <3. wouldve used a queue otherwise...
            s == goal
        })
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
        let s = "abcde".to_string();
        let goal = "cdeab".to_string();
        assert_eq!(Solution::rotate_string(s, goal), true);
    }

    // Test case 2
    #[test]
    fn case2() {
        let s = "abcde".to_string();
        let goal = "abced".to_string();
        assert_eq!(Solution::rotate_string(s, goal), false);
    }
}
