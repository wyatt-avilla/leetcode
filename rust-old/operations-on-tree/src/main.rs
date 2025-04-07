// https://leetcode.com/problems/operations-on-tree/

use std::{
    collections::{HashSet, VecDeque},
    iter,
};

struct LockingTree {
    parents: Vec<i32>,
    children: Vec<HashSet<i32>>,
    locks: Vec<Option<i32>>,
}

impl LockingTree {
    fn new(parent: Vec<i32>) -> Self {
        let n = parent.len();
        let mut children = vec![HashSet::<i32>::new(); n];

        for (i, &p) in parent.iter().enumerate() {
            if p >= 0 {
                children[p as usize].insert(i as i32);
            }
        }

        LockingTree {
            children,
            parents: parent,
            locks: iter::repeat_n(None, n).collect(),
        }
    }

    fn lock(&mut self, num: i32, user: i32) -> bool {
        let idx: usize = num.try_into().unwrap();

        if self.locks[idx].is_none() {
            self.locks[idx] = Some(user);
            true
        } else {
            false
        }
    }

    fn unlock(&mut self, num: i32, user: i32) -> bool {
        let idx: usize = num.try_into().unwrap();

        if let Some(u) = self.locks[idx] {
            if u == user {
                self.locks[idx] = None;
                return true;
            }
        }
        false
    }

    fn upgrade(&mut self, num: i32, user: i32) -> bool {
        let idx: usize = num.try_into().unwrap();

        if self.locks[idx].is_none()
            && !self.has_locked_ancestor(num)
            && self.unlock_children_of(num)
        {
            self.locks[idx] = Some(user);
            true
        } else {
            false
        }
    }

    fn unlock_children_of(&mut self, num: i32) -> bool {
        let mut any_unlocked = false;
        let mut queue = VecDeque::from([num]);
        while let Some(curr) = queue.pop_front() {
            for &child in &self.children[curr as usize] {
                if self.locks[child as usize].is_some() {
                    self.locks[child as usize] = None;
                    any_unlocked = true;
                }
            }
            queue.extend(&self.children[curr as usize]);
        }

        any_unlocked
    }

    fn has_locked_ancestor(&self, idx: i32) -> bool {
        if idx < 0 {
            return false;
        }

        if self.locks[idx as usize].is_none() {
            self.has_locked_ancestor(self.parents[idx as usize])
        } else {
            true
        }
    }
}

fn main() {
    let mut lt = LockingTree::new(vec![-1, 0, 0, 1, 1, 2, 2]);
    assert!(lt.lock(2, 2) == true);
    assert!(lt.lock(2, 3) == false);
    assert!(lt.lock(4, 5) == true);
    assert!(lt.upgrade(0, 1) == true);
    assert!(lt.lock(0, 1) == false);

    let mut lt2 = LockingTree::new(vec![-1, 0, 8, 0, 7, 4, 2, 3, 3, 1]);

    assert!(lt2.upgrade(8, 39) == false);
    assert!(lt2.upgrade(5, 28) == false);
    assert!(lt2.upgrade(6, 33) == false);
    assert!(lt2.upgrade(9, 24) == false);
    assert!(lt2.lock(5, 22) == true);
    assert!(lt2.upgrade(1, 3) == false);
    assert!(lt2.lock(5, 20) == false);
    assert!(lt2.upgrade(0, 38) == true);
    assert!(lt2.lock(5, 14) == true);
    assert!(lt2.lock(6, 34) == true);
    assert!(lt2.lock(6, 28) == false);
    assert!(lt2.upgrade(3, 23) == false);
    assert!(lt2.upgrade(4, 45) == false);
    assert!(lt2.upgrade(8, 7) == false);
    assert!(lt2.upgrade(2, 18) == false);
    assert!(lt2.lock(3, 35) == true);
    assert!(lt2.upgrade(2, 16) == false);
    assert!(lt2.lock(3, 21) == false);
    assert!(lt2.upgrade(1, 41) == false);
    assert!(lt2.unlock(5, 22) == false);
}
