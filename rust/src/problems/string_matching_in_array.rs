// https://leetcode.com/string-matching-in-an-array/

pub struct Solution;

impl Solution {
    pub fn string_matching(words: Vec<String>) -> Vec<String> {
        words
            .iter()
            .filter(|&inner| {
                words
                    .iter()
                    .any(|outer| outer.contains(inner) && outer != inner)
            })
            .cloned()
            .collect()
    }
}

#[cfg(test)]
mod tests {
    use super::Solution;

    #[test]
    fn case_1() {
        let words = vec![
            "mass".to_string(),
            "as".to_string(),
            "hero".to_string(),
            "superhero".to_string(),
        ];
        let expected = vec!["as".to_string(), "hero".to_string()];
        assert_eq!(Solution::string_matching(words), expected);
    }

    #[test]
    fn case_2() {
        let words = vec!["leetcode".to_string(), "et".to_string(), "code".to_string()];
        let expected = vec!["et".to_string(), "code".to_string()];
        assert_eq!(Solution::string_matching(words), expected);
    }

    #[test]
    fn case_3() {
        let words = vec!["blue".to_string(), "green".to_string(), "bu".to_string()];
        let expected = Vec::<String>::new();
        assert_eq!(Solution::string_matching(words), expected);
    }
}
