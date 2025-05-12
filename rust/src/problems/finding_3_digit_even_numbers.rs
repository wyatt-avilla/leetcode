// https://leetcode.com/problems/finding-3-digit-even-numbers/

use std::collections::BTreeSet;

pub struct Solution;

impl Solution {
    pub fn find_even_numbers(digits: Vec<i32>) -> Vec<i32> {
        let even_idxs: Vec<_> = digits
            .iter()
            .enumerate()
            .filter_map(|(i, x)| if x % 2 == 0 { Some(i) } else { None })
            .collect();

        let mut answers: BTreeSet<i32> = BTreeSet::new();

        for i in even_idxs {
            let ones = digits[i];
            for (j, tens) in digits.iter().enumerate() {
                if i == j {
                    continue;
                }
                for (k, huns) in digits.iter().enumerate() {
                    if i == k || j == k || *huns == 0 {
                        continue;
                    }

                    answers.insert(ones + 10 * *tens + 100 * *huns);
                }
            }
        }

        answers.into_iter().collect()
    }
}

#[cfg(test)]
mod tests {
    use super::Solution;
    use std::collections::BTreeSet;

    #[test]
    fn case_1() {
        let result = Solution::find_even_numbers(vec![2, 1, 3, 0]);
        assert_eq!(
            result.into_iter().collect::<BTreeSet<_>>(),
            BTreeSet::from([102, 120, 130, 132, 210, 230, 302, 310, 312, 320])
        );
    }

    #[test]
    fn case_2() {
        let result = Solution::find_even_numbers(vec![2, 2, 8, 8, 2]);
        assert_eq!(
            result.into_iter().collect::<BTreeSet<_>>(),
            BTreeSet::from([222, 228, 282, 288, 822, 828, 882])
        );
    }

    #[test]
    fn case_3() {
        let result = Solution::find_even_numbers(vec![3, 7, 5]);
        assert_eq!(
            result.into_iter().collect::<BTreeSet<_>>(),
            BTreeSet::from([])
        );
    }
}
