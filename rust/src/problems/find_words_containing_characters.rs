// https://leetcode.com/problems/find-words-containing-character/

pub struct Solution;

impl Solution {
    // first rust program !
    pub fn find_words_containing(words: Vec<String>, x: char) -> Vec<i32> {
        let mut found_char_indices = Vec::new();
        let x = x.to_string();
        for (index, word) in words.iter().enumerate() {
            if word.contains(&x) {
                found_char_indices.push(index.try_into().unwrap())
            }
        }
        found_char_indices
    }
}

#[cfg(test)]
mod tests {
    use super::Solution;

    #[test]
    fn case_1() {
        let words = vec![String::from("leet"), String::from("code")];
        let result = Solution::find_words_containing(words, 'e');
        assert_eq!(result, vec![0, 1]);
    }

    #[test]
    fn case_2() {
        let words = vec![
            String::from("abc"),
            String::from("bcd"),
            String::from("aaaa"),
            String::from("cbc"),
        ];
        let result = Solution::find_words_containing(words, 'a');
        assert_eq!(result, vec![0, 2]);
    }

    #[test]
    fn case_3() {
        let words = vec![
            String::from("abc"),
            String::from("bcd"),
            String::from("aaaa"),
            String::from("cbc"),
        ];
        let result = Solution::find_words_containing(words, 'z');
        assert_eq!(result, vec![]);
    }
}
