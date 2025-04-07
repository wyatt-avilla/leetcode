// https://leetcode.com/problems/jewels-and-stones/

pub struct Solution;

impl Solution {
    pub fn num_jewels_in_stones(jewels: String, stones: String) -> i32 {
        let mut num_jewels: i32 = 0;
        for char in jewels.chars() {
            let stones_per_jewel: i32 = stones
                .chars()
                .filter(|&c| c == char)
                .count()
                .try_into()
                .unwrap();
            num_jewels += stones_per_jewel
        }
        num_jewels
    }
}

#[cfg(test)]
mod tests {
    use super::Solution;

    #[test]
    fn case_1() {
        let jewels = String::from("aA");
        let stones = String::from("aAAbbbb");
        let result = Solution::num_jewels_in_stones(jewels, stones);
        assert_eq!(result, 3);
    }

    #[test]
    fn case_2() {
        let jewels = String::from("z");
        let stones = String::from("ZZ");
        let result = Solution::num_jewels_in_stones(jewels, stones);
        assert_eq!(result, 0);
    }
}
