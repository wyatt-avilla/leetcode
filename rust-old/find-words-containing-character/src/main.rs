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

fn main() {
    println!("main executed")
}

// Import the necessary modules
#[cfg(test)]
mod tests {
    // Import the Solution struct (assuming it's in the same module or crate)
    use super::Solution;

    // A helper function to compare vectors for equality
    fn assert_eq_vec(actual: Vec<i32>, expected: Vec<i32>) {
        assert_eq!(actual, expected);
    }

    // Test case 1
    #[test]
    fn case1() {
        let words = vec![String::from("leet"), String::from("code")];
        let result = Solution::find_words_containing(words, 'e');
        assert_eq_vec(result, vec![0, 1]);
    }

    // Test case 2
    #[test]
    fn case2() {
        let words = vec![
            String::from("abc"),
            String::from("bcd"),
            String::from("aaaa"),
            String::from("cbc"),
        ];
        let result = Solution::find_words_containing(words, 'a');
        assert_eq_vec(result, vec![0, 2]);
    }

    // Test case 3
    #[test]
    fn case3() {
        let words = vec![
            String::from("abc"),
            String::from("bcd"),
            String::from("aaaa"),
            String::from("cbc"),
        ];
        let result = Solution::find_words_containing(words, 'z');
        assert_eq_vec(result, vec![]);
    }
}
