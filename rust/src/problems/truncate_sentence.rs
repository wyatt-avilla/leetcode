// https://leetcode.com/problems/truncate-sentence/

pub struct Solution;

impl Solution {
    pub fn truncate_sentence(s: String, k: i32) -> String {
        let (final_space_index, _) = s
            .match_indices(" ")
            .nth((k - 1).try_into().unwrap())
            .unwrap_or((s.len(), &""));

        s[0..final_space_index].to_string()
    }
}

#[cfg(test)]
mod tests {
    use super::Solution;

    #[test]
    fn case_1() {
        let s = "Hello how are you Contestant".to_string();
        let k = 4;
        assert_eq!(
            Solution::truncate_sentence(s, k),
            "Hello how are you".to_string()
        );
    }

    #[test]
    fn case_2() {
        let s = "What is the solution to this problem".to_string();
        let k = 4;
        assert_eq!(
            Solution::truncate_sentence(s, k),
            "What is the solution".to_string()
        );
    }

    #[test]
    fn case_3() {
        let s = "chopper is not a tanuki".to_string();
        let k = 5;
        assert_eq!(
            Solution::truncate_sentence(s, k),
            "chopper is not a tanuki".to_string()
        );
    }
}
