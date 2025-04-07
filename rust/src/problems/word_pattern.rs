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

#[cfg(test)]
mod tests {
    use super::Solution;

    #[test]
    fn case_1() {
        let pattern = String::from("abba");
        let s = String::from("dog cat cat dog");
        let result = Solution::word_pattern(pattern, s);
        assert!(result);
    }

    #[test]
    fn case_2() {
        let pattern = String::from("abba");
        let s = String::from("dog cat cat fish");
        let result = Solution::word_pattern(pattern, s);
        assert!(!result);
    }

    #[test]
    fn case_3() {
        let pattern = String::from("aaaa");
        let s = String::from("dog cat cat dog");
        let result = Solution::word_pattern(pattern, s);
        assert!(!result);
    }

    #[test]
    fn case_4() {
        let pattern = String::from("abab");
        let s = String::from("dog cat cat dog");
        let result = Solution::word_pattern(pattern, s);
        assert!(!result);
    }

    #[test]
    fn case_5() {
        let pattern = String::from("abba");
        let s = String::from("dog dog dog dog");
        let result = Solution::word_pattern(pattern, s);
        assert!(!result);
    }

    #[test]
    fn case_6() {
        let pattern = String::from("aaa");
        let s = String::from("aa aa aa aa");
        let result = Solution::word_pattern(pattern, s);
        assert!(!result);
    }
}
