// https://leetcode.com/problems/check-if-a-word-occurs-as-a-prefix-of-any-word-in-a-sentence/

pub struct Solution;

impl Solution {
    pub fn is_prefix_of_word(sentence: String, search_word: String) -> i32 {
        sentence.split_whitespace()
            .enumerate()
            .filter(|(_, w)| w.starts_with(&search_word)) // .position() would've been better here
            .map(|(i, _)| (i+1) as i32)
            .next()
            .unwrap_or(-1)
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
        let sentence = String::from("i love eating burger");
        let search_word = String::from("burg");
        let result = Solution::is_prefix_of_word(sentence, search_word);
        assert_eq!(result, 4);
    }

    // Test case 2
    #[test]
    fn case2() {
        let sentence = String::from("this problem is an easy problem");
        let search_word = String::from("pro");
        let result = Solution::is_prefix_of_word(sentence, search_word);
        assert_eq!(result, 2);
    }

    // Test case 3
    #[test]
    fn case3() {
        let sentence = String::from("i am tired");
        let search_word = String::from("you");
        let result = Solution::is_prefix_of_word(sentence, search_word);
        assert_eq!(result, -1);
    }
}
