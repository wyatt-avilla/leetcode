// https://leetcode.com/problems/find-the-lexicographically-largest-string-from-the-box-i/

pub struct Solution;

use std::collections::BinaryHeap;

impl Solution {
    pub fn answer_string(word: String, num_friends: i32) -> String {
        let num_friends = num_friends as usize;
        let wlen = word.len();
        let max_len = wlen - (num_friends - 1);

        let bound_idxs = (0..word.len()).filter_map(|i| {
            let end = std::cmp::min(wlen, i + max_len);
            let rem_chars = wlen - (end - i);
            let rem_friends = num_friends - 1;

            if rem_friends == 0 {
                if rem_chars == 0 { Some((i, end)) } else { None }
            } else if rem_chars >= rem_friends {
                Some((i, end))
            } else {
                None
            }
        });

        bound_idxs
            .map(|(s, e)| (word[s..e].as_ref()))
            .collect::<BinaryHeap<&str>>()
            .pop()
            .expect("problem constraints")
            .to_string()
    }
}

#[cfg(test)]
mod tests {
    use super::Solution;

    #[test]
    fn case_1() {
        assert_eq!(
            Solution::answer_string("dbca".to_string(), 2),
            "dbc".to_string()
        );
    }

    #[test]
    fn case_2() {
        assert_eq!(
            Solution::answer_string("gggg".to_string(), 4),
            "g".to_string()
        );
    }

    #[test]
    fn case_3() {
        assert_eq!(
            Solution::answer_string("gh".to_string(), 1),
            "gh".to_string()
        );
    }

    #[test]
    fn case_4() {
        assert_eq!(
            Solution::answer_string("aann".to_string(), 2),
            "nn".to_string()
        );
    }
}
