// https://leetcode.com/problems/intersection-of-two-arrays/

use std::collections::HashSet;

pub struct Solution;

impl Solution {
    pub fn intersection(nums1: Vec<i32>, nums2: Vec<i32>) -> Vec<i32> {
        let nums1: HashSet<i32> = nums1.into_iter().collect();
        let nums2: HashSet<i32> = nums2.into_iter().collect();
        nums1
            .into_iter()
            .filter(|num| nums2.contains(num))
            .collect()
    }
}

fn main() {
    println!("main executed")
}

#[cfg(test)]
mod tests {
    use super::Solution;

    #[test]
    fn case_1() {
        let nums1 = vec![1, 2, 2, 1];
        let nums2 = vec![2, 2];
        assert_eq!(Solution::intersection(nums1, nums2), vec![2]);
    }

    #[test]
    fn case_2() {
        let nums1 = vec![4, 9, 5];
        let nums2 = vec![9, 4, 9, 8, 4];
        assert_eq!(Solution::intersection(nums1, nums2), vec![4, 9]);
    }
}
