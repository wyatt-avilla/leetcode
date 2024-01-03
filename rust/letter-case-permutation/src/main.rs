// https://leetcode.com/problems/letter-case-permutation/

pub struct Solution;

impl Solution {
    pub fn letter_case_permutation(s: String) -> Vec<String> {
        let mut all_possible: Vec<String> = Vec::new();
        let letter_count = s.chars().filter(|c| c.is_alphabetic()).count();
        let total_bin_vals: u16 = 2_u16.pow(letter_count.try_into().unwrap());

        for i in 0..total_bin_vals {
            let bin_str = format!("{:0width$b}", i, width = letter_count.into());
            let mut current_perm: Vec<char> = Vec::new();
            let mut case_representations = bin_str.chars();

            for c in s.chars().map(|c| c.to_ascii_lowercase() ) {
                if c.is_numeric() {
                    current_perm.push(c);
                    continue;
                }
                current_perm.push(if case_representations.next().unwrap() == '0' { c } else { c.to_ascii_uppercase() })
            }

            all_possible.push(current_perm.iter().collect());
        }

        return all_possible;
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
        let s = String::from("a1b2");
        let mut result = Solution::letter_case_permutation(s);
        let mut expected = vec!["a1b2", "a1B2", "A1b2", "A1B2"];
        result.sort();
        expected.sort();
        assert_eq!(expected, result);
    }

    // Test case 2
    #[test]
    fn case2() {
        let s = String::from("3z4");
        let mut result = Solution::letter_case_permutation(s);
        let mut expected = vec!["3z4", "3Z4"];
        result.sort();
        expected.sort();
        assert_eq!(expected, result);
    }

    // Test case 3
    #[test]
    fn case3() {
        let s = String::from("C");
        let mut result = Solution::letter_case_permutation(s);
        let mut expected = vec!["c", "C"];
        result.sort();
        expected.sort();
        assert_eq!(expected, result);
    }
    
    // Test case 4
    #[test]
    fn case4() {
        let s = String::from("ggg");
        let mut result = Solution::letter_case_permutation(s);
        let mut expected = vec!["ggg", "ggG", "gGg", "gGG", "Ggg", "GgG", "GGg", "GGG"];
        result.sort();
        expected.sort();
        assert_eq!(expected, result);
    }
}
