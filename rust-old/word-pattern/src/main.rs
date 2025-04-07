// https://leetcode.com/problems/word-pattern/

use std::collections::HashMap;
use std::collections::HashSet;

pub struct Solution;

impl Solution {
    pub fn word_pattern(pattern: String, s: String) -> bool {
        let chars = pattern.chars();
        let words = s.split_whitespace();

        if chars.clone().count() != words.clone().count() {
            return false;
        } // this feels gross

        let mut char_word_assoc: HashMap<char, &str> = HashMap::new();
        for (char, word) in chars.zip(words) {
            match char_word_assoc.insert(char, word) {
                Some(prev_word) => {
                    if prev_word != word {
                        return false;
                    }
                }
                None => (),
            }
        }

        let mut unique_words: HashSet<&str> = HashSet::new();
        for word in char_word_assoc.values() {
            if !unique_words.insert(word) {
                return false;
            } // like bruh what is THIS
        }
        return true;
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
        let pattern = String::from("abba");
        let s = String::from("dog cat cat dog");
        let result = Solution::word_pattern(pattern, s);
        assert_eq!(result, true);
    }

    // Test case 2
    #[test]
    fn case2() {
        let pattern = String::from("abba");
        let s = String::from("dog cat cat fish");
        let result = Solution::word_pattern(pattern, s);
        assert_eq!(result, false);
    }

    // Test case 3
    #[test]
    fn case3() {
        let pattern = String::from("aaaa");
        let s = String::from("dog cat cat dog");
        let result = Solution::word_pattern(pattern, s);
        assert_eq!(result, false);
    }

    // Test case 4
    #[test]
    fn case4() {
        let pattern = String::from("abab");
        let s = String::from("dog cat cat dog");
        let result = Solution::word_pattern(pattern, s);
        assert_eq!(result, false);
    }

    // Test case 5
    #[test]
    fn case5() {
        let pattern = String::from("abba");
        let s = String::from("dog dog dog dog");
        let result = Solution::word_pattern(pattern, s);
        assert_eq!(result, false);
    }

    // Test case 6
    #[test]
    fn case6() {
        let pattern = String::from("aaa");
        let s = String::from("aa aa aa aa");
        let result = Solution::word_pattern(pattern, s);
        assert_eq!(result, false);
    }
}
