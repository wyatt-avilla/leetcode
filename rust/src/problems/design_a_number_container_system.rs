// https://leetcode.com/problems/design-a-number-container-system/

use std::collections::{BTreeSet, HashMap};

#[derive(Debug)]
struct NumberContainers {
    idx_to_num: HashMap<i32, i32>,
    num_to_idxs: HashMap<i32, BTreeSet<i32>>,
}

impl NumberContainers {
    fn new() -> Self {
        NumberContainers {
            idx_to_num: HashMap::new(),
            num_to_idxs: HashMap::new(),
        }
    }

    fn change(&mut self, index: i32, number: i32) {
        if let Some(prev_number) = self.idx_to_num.get_mut(&index) {
            self.num_to_idxs
                .entry(*prev_number)
                .or_default()
                .remove(&index);
            *prev_number = number;
        } else {
            self.idx_to_num.insert(index, number);
        }

        self.num_to_idxs.entry(number).or_default().insert(index);
    }

    fn find(&mut self, number: i32) -> i32 {
        *self
            .num_to_idxs
            .entry(number)
            .or_default()
            .first()
            .unwrap_or(&-1)
    }
}

#[cfg(test)]
mod tests {
    use super::NumberContainers;

    #[test]
    fn case_1() {
        let mut nc = NumberContainers::new();
        assert_eq!(nc.find(10), -1);
        nc.change(1, 10);
        nc.change(2, 10);
        nc.change(3, 10);
        nc.change(5, 10);
        assert_eq!(nc.find(10), 1);
        dbg!(&nc);
        nc.change(1, 20);
        dbg!(&nc);
        assert_eq!(nc.find(10), 2);
    }
}
