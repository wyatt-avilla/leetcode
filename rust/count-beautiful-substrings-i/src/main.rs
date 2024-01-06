// https://leetcode.com/problems/count-beautiful-substrings-i/ 

pub struct Solution;

impl Solution {
    pub fn beautiful_substrings(s: String, k: i32) -> i32 {
        let mut total_beautiful = 0;
        let vowels = ['a', 'e', 'i', 'o', 'u'];

        let slen = s.len();
        let mut vowel_count: i32 = s[0..slen - 1].chars().filter(|&c| vowels.contains(&c)).count().try_into().unwrap();

        let mut left_bound = 0;
        let mut right_bound = slen;
        let mut prev_direction = true;
        let mut direction = true;
        while (right_bound - left_bound) > 1 {
            let sub = &mut s[left_bound..right_bound].chars();
            let left_char = sub.next().unwrap();
            let right_char = sub.last().unwrap();

            if (prev_direction == direction) && direction == false && vowels.contains(&left_char) ||
                (prev_direction == direction) && direction == true && vowels.contains(&right_char) {
                    vowel_count += 1
                }

            if vowel_count == ((right_bound - left_bound) as i32 - vowel_count) &&
                (vowel_count as i32 * ((right_bound - left_bound) as i32 - vowel_count) as i32) % k == 0 {
                    total_beautiful += 1
                }


            match direction {
                false => { // <-
                    if left_bound == 0 {
                        direction = true;
                    } else {
                        left_bound -= 1;
                    }

                    if vowels.contains(&right_char) {
                        vowel_count -= 1;
                    }
                    right_bound -= 1;
                    prev_direction = false;
                },
                true => { // ->
                    if right_bound == slen {
                        direction = false;
                    } else {
                        right_bound += 1;
                    }

                    if vowels.contains(&left_char) {
                        vowel_count -= 1;
                    }
                    left_bound += 1;
                    prev_direction = true;
                },
            }
        }
        total_beautiful
    }
}

fn main() {
    println!("main executed");
    let s = "baeyh".to_string();
    let k = 2;
    let result = Solution::beautiful_substrings(s, k);
}

// Import the necessary modules
#[cfg(test)]
mod tests {
    // Import the Solution struct (assuming it's in the same module or crate)
    use super::Solution;

    // Test case 1
    #[test]
    fn case1() {
        let s = "baeyh".to_string();
        let k = 2;
        let result = Solution::beautiful_substrings(s, k);
        assert_eq!(result, 2);
    }

    // Test case 2
    #[test]
    fn case2() {
        let s = "abba".to_string();
        let k = 1;
        let result = Solution::beautiful_substrings(s, k);
        assert_eq!(result, 3);
    }

    // Test case 3
    #[test]
    fn case3() {
        let s = "bcdf".to_string();
        let k = 1;
        let result = Solution::beautiful_substrings(s, k);
        assert_eq!(result, 0);
    }
    
    // Test case 4
    #[test]
    fn case4() {
        let s = "a".to_string();
        let k = 1;
        let result = Solution::beautiful_substrings(s, k);
        assert_eq!(result, 0);
    }

    // Test case 5
    #[test]
    fn case5() {
        let s = "b".to_string();
        let k = 1;
        let result = Solution::beautiful_substrings(s, k);
        assert_eq!(result, 0);
    }
}
