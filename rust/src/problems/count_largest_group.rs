// https://leetcode.com/problems/count-largest-group/

use std::collections::HashMap;

pub struct Solution;

fn sum_digits(mut x: i32) -> i32 {
    std::iter::from_fn(move || {
        if x > 0 {
            let digit = x % 10;
            x /= 10;
            Some(digit)
        } else {
            None
        }
    })
    .sum()
}

impl Solution {
    pub fn count_largest_group(n: i32) -> i32 {
        let mut map: HashMap<i32, i32> = HashMap::new();

        for s in (1..=n).map(sum_digits) {
            *map.entry(s).or_insert(0) += 1;
        }

        let largest_group_size = if let Some((_, &v)) = map.iter().max_by_key(|(_, v)| **v) {
            v
        } else {
            1
        };

        map.values().filter(|&&v| v == largest_group_size).count() as i32
    }
}

#[cfg(test)]
mod tests {
    use super::Solution;

    #[test]
    fn case_1() {
        assert_eq!(Solution::count_largest_group(13), 4);
    }

    #[test]
    fn case_2() {
        assert_eq!(Solution::count_largest_group(2), 2);
    }
}
