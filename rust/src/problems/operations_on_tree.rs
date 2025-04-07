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

#[cfg(test)]
mod tests {
    use super::LockingTree;

    #[test]
    fn case_1() {
        let mut lt = LockingTree::new(vec![-1, 0, 0, 1, 1, 2, 2]);
        assert!(lt.lock(2, 2));
        assert!(!lt.lock(2, 3));
        assert!(lt.lock(4, 5));
        assert!(lt.upgrade(0, 1));
        assert!(!lt.lock(0, 1));
    }

    #[test]
    fn case_2() {
        let mut lt = LockingTree::new(vec![-1, 0, 8, 0, 7, 4, 2, 3, 3, 1]);

        assert!(!lt.upgrade(8, 39));
        assert!(!lt.upgrade(5, 28));
        assert!(!lt.upgrade(6, 33));
        assert!(!lt.upgrade(9, 24));
        assert!(lt.lock(5, 22));
        assert!(!lt.upgrade(1, 3));
        assert!(!lt.lock(5, 20));
        assert!(lt.upgrade(0, 38));
        assert!(lt.lock(5, 14));
        assert!(lt.lock(6, 34));
        assert!(!lt.lock(6, 28));
        assert!(!lt.upgrade(3, 23));
        assert!(!lt.upgrade(4, 45));
        assert!(!lt.upgrade(8, 7));
        assert!(!lt.upgrade(2, 18));
        assert!(lt.lock(3, 35));
        assert!(!lt.upgrade(2, 16));
        assert!(!lt.lock(3, 21));
        assert!(!lt.upgrade(1, 41));
        assert!(!lt.unlock(5, 22));
    }
}
