// https://leetcode.com/problems/avoid-flood-in-the-city/

pub struct Solution;
use std::collections::{BTreeSet, HashMap};

impl Solution {
    pub fn avoid_flood(rains: Vec<i32>) -> Vec<i32> {
        let mut zero_idxs: BTreeSet<usize> = BTreeSet::new();
        let mut last_rained: HashMap<i32, usize> = HashMap::new();

        let mut ans = std::iter::repeat_n(-1, rains.len()).collect::<Vec<_>>();
        for (i, x) in rains.into_iter().enumerate() {
            if x == 0 {
                zero_idxs.insert(i);
            } else {
                if let Some(last_rained_idx) = last_rained.get(&x) {
                    let Some(&zero_idx) = zero_idxs.range(last_rained_idx..).min() else {
                        return vec![];
                    };
                    ans[zero_idx] = x;
                    zero_idxs.remove(&zero_idx);
                }
                last_rained.insert(x, i);
            }
        }

        for i in zero_idxs {
            ans[i] = 1;
        }

        ans
    }
}

#[cfg(test)]
mod tests {
    use super::Solution;

    #[test]
    fn case_1() {
        assert_eq!(
            Solution::avoid_flood(vec![1, 2, 3, 4]),
            vec![-1, -1, -1, -1]
        );
    }

    #[test]
    fn case_2() {
        assert_eq!(
            Solution::avoid_flood(vec![1, 2, 0, 0, 2, 1]),
            vec![-1, -1, 2, 1, -1, -1]
        );
    }

    #[test]
    fn case_3() {
        assert_eq!(Solution::avoid_flood(vec![1, 2, 0, 1, 2]), vec![]);
    }

    #[test]
    fn case_4() {
        assert_eq!(Solution::avoid_flood(vec![1, 0, 2, 0]), vec![-1, 1, -1, 1]);
    }

    #[test]
    fn case_5() {
        assert_eq!(Solution::avoid_flood(vec![0, 1, 1, 1]), vec![]);
    }
}
