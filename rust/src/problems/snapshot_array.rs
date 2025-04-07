// https://leetcode.com/problems/snapshot-array/

use std::collections::BTreeMap;

struct SnapshotArray {
    snap_id: i32,
    arr: Vec<BTreeMap<i32, i32>>,
}

impl SnapshotArray {
    fn new(length: i32) -> Self {
        SnapshotArray {
            snap_id: 0,
            arr: vec![BTreeMap::from([(0, 0)]); length as usize],
        }
    }

    fn set(&mut self, index: i32, val: i32) {
        self.arr[index as usize].insert(self.snap_id, val);
    }

    fn snap(&mut self) -> i32 {
        let id = self.snap_id;
        self.snap_id += 1;
        id
    }

    fn get(&self, index: i32, snap_id: i32) -> i32 {
        let map = &self.arr[index as usize];
        match map.range(..=snap_id).next_back() {
            Some((_, &v)) => v,
            None => unreachable!("problem constraints"),
        }
    }
}

#[cfg(test)]
mod tests {
    use super::SnapshotArray;

    #[test]
    fn case_1() {
        let mut sa = SnapshotArray::new(3);
        sa.set(0, 5);
        assert_eq!(sa.snap(), 0);
        sa.set(0, 6);
        assert_eq!(sa.get(0, 0), 5);
    }

    #[test]
    fn case_2() {
        let mut sa2 = SnapshotArray::new(1);
        sa2.set(0, 15);
        sa2.snap();
        sa2.snap();
        sa2.snap();
        assert_eq!(sa2.get(0, 2), 15);
        sa2.snap();
        sa2.snap();
        assert_eq!(sa2.get(0, 0), 15);
    }
}
