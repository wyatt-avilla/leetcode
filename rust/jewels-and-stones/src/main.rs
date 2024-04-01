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
        let jewels = String::from("aA");
        let stones = String::from("aAAbbbb");
        let result = Solution::num_jewels_in_stones(jewels, stones);
        assert_eq!(result, 3);
    }

    // Test case 2
    #[test]
    fn case2() {
        let jewels = String::from("z");
        let stones = String::from("ZZ");
        let result = Solution::num_jewels_in_stones(jewels, stones);
        assert_eq!(result, 0);
    }
}
