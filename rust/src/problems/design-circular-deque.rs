// https://leetcode.com/problems/design-circular-deque/

use std::collections::VecDeque;

struct MyCircularDeque {
    k: usize,
    vec: VecDeque<i32>,
}

impl MyCircularDeque {
    fn new(k: i32) -> Self {
        MyCircularDeque {
            k: k as usize,
            vec: VecDeque::with_capacity(k as usize),
        }
    }

    fn insert_front(&mut self, value: i32) -> bool {
        if !self.is_full() {
            self.vec.push_front(value);
            true
        } else {
            false
        }
    }

    fn insert_last(&mut self, value: i32) -> bool {
        if !self.is_full() {
            self.vec.push_back(value);
            true
        } else {
            false
        }
    }

    fn delete_front(&mut self) -> bool {
        self.vec.pop_front().is_some()
    }

    fn delete_last(&mut self) -> bool {
        self.vec.pop_back().is_some()
    }

    fn get_front(&self) -> i32 {
        *self.vec.front().unwrap_or(&-1)
    }

    fn get_rear(&self) -> i32 {
        *self.vec.back().unwrap_or(&-1)
    }

    fn is_empty(&self) -> bool {
        self.vec.is_empty()
    }

    fn is_full(&self) -> bool {
        self.vec.len() == self.k
    }
}
