// https://leetcode.com/problems/count-complete-subarrays-in-an-array/

use std::collections::{HashMap, HashSet};

pub struct Solution;

fn count_unique(nums: &[i32]) -> usize {
    HashSet::<i32>::from_iter(nums.to_owned()).len()
}

impl Solution {
    pub fn count_complete_subarrays(nums: Vec<i32>) -> i32 {
        let unique = count_unique(&nums);
        let mut complete_count = 0;

        let mut window_counts: HashMap<i32, i32> = HashMap::new();
        let mut window: HashSet<i32> = HashSet::new();

        let mut left = 0;
        let mut right = 0;

        while left < nums.len() {
            if window.len() != unique && right < nums.len() {
                *window_counts.entry(nums[right]).or_default() += 1;
                window.insert(nums[right]);
                right += 1;
            } else {
                if window.len() == unique {
                    complete_count += 1 + nums.len() - right;
                }
                let left_count = window_counts
                    .get_mut(&nums[left])
                    .expect("problem constraints");
                *left_count -= 1;

                if *left_count == 0 {
                    window.remove(&nums[left]);
                }

                left += 1;
            }
        }

        complete_count as i32
    }
}

#[cfg(test)]
mod tests {
    use super::Solution;

    #[test]
    fn case_1() {
        assert_eq!(Solution::count_complete_subarrays(vec![1, 3, 1, 2, 2]), 4);
    }

    #[test]
    fn case_2() {
        assert_eq!(Solution::count_complete_subarrays(vec![5, 5, 5, 5]), 10);
    }
}
