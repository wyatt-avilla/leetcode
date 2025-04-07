// https://leetcode.com/problems/smallest-number-in-infinite-set/

use std::cmp::Reverse;
use std::collections::{BinaryHeap, HashSet};
use std::iter::Peekable;
use std::ops::RangeFrom;

struct SmallestInfiniteSet {
    generator: Peekable<RangeFrom<i32>>,
    heap: BinaryHeap<Reverse<i32>>,
    heap_set: HashSet<i32>,
}

impl SmallestInfiniteSet {
    fn new() -> Self {
        SmallestInfiniteSet {
            generator: (1..).peekable(),
            heap: BinaryHeap::new(),
            heap_set: HashSet::new(),
        }
    }

    fn pop_smallest(&mut self) -> i32 {
        let e = String::from("none from infinite range");

        if self.heap.is_empty() {
            self.generator.next().expect(&e)
        } else {
            let popped = self.heap.pop().expect(&e).0;
            self.heap_set.remove(&popped);
            popped
        }
    }

    fn add_back(&mut self, num: i32) {
        if num < *self.generator.peek().expect("none from infinite range")
            && !self.heap_set.contains(&num)
        {
            self.heap_set.insert(num);
            self.heap.push(Reverse(num));
        }
    }
}

#[cfg(test)]
mod tests {
    use super::SmallestInfiniteSet;

    #[test]
    fn case_1() {
        let mut sis = SmallestInfiniteSet::new();
        sis.add_back(2);
        assert_eq!(sis.pop_smallest(), 1);
        assert_eq!(sis.pop_smallest(), 2);
        assert_eq!(sis.pop_smallest(), 3);
        sis.add_back(1);
        assert_eq!(sis.pop_smallest(), 1);
        assert_eq!(sis.pop_smallest(), 4);
        assert_eq!(sis.pop_smallest(), 5);
    }

    #[test]
    fn case_2() {
        let mut sis = SmallestInfiniteSet::new();
        assert_eq!(sis.pop_smallest(), 1);
        sis.add_back(1);
        assert_eq!(sis.pop_smallest(), 1);
        assert_eq!(sis.pop_smallest(), 2);
        assert_eq!(sis.pop_smallest(), 3);
        sis.add_back(2);
        sis.add_back(3);
        assert_eq!(sis.pop_smallest(), 2);
        assert_eq!(sis.pop_smallest(), 3);
    }
}
