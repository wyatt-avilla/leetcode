// https://leetcode.com/problems/seat-reservation-manager/

use std::{cmp::Reverse, collections::BinaryHeap};

struct SeatManager {
    heap: BinaryHeap<Reverse<i32>>,
}

impl SeatManager {
    fn new(n: i32) -> Self {
        SeatManager {
            heap: (1..=n).map(Reverse).collect(),
        }
    }

    fn reserve(&mut self) -> i32 {
        self.heap.pop().expect("problem constraints").0
    }

    fn unreserve(&mut self, seat_number: i32) {
        self.heap.push(Reverse(seat_number));
    }
}

#[cfg(test)]
mod tests {
    use super::SeatManager;

    #[test]
    fn case_1() {
        let mut sm = SeatManager::new(5);
        assert_eq!(sm.reserve(), 1);
        assert_eq!(sm.reserve(), 2);
        sm.unreserve(2);
        assert_eq!(sm.reserve(), 2);
        assert_eq!(sm.reserve(), 3);
        assert_eq!(sm.reserve(), 4);
        assert_eq!(sm.reserve(), 5);
        sm.unreserve(5);
    }

    #[test]
    fn case_2() {
        let mut sm = SeatManager::new(5);
        assert_eq!(sm.reserve(), 1);
        assert_eq!(sm.reserve(), 2);
        assert_eq!(sm.reserve(), 3);
        sm.unreserve(1);
        assert_eq!(sm.reserve(), 1);
        assert_eq!(sm.reserve(), 4);
    }
}
