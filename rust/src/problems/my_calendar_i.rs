// https://leetcode.com/problems/my-calendar-i/

use std::collections::BTreeSet;

#[derive(Debug, Default)]
struct MyCalendar {
    bookings: BTreeSet<(i32, i32)>,
}

impl MyCalendar {
    fn new() -> Self {
        Self::default()
    }

    fn book(&mut self, start_time: i32, end_time: i32) -> bool {
        if end_time <= start_time {
            return false;
        }

        let prev_ends_before = self
            .bookings
            .range(..=(start_time, i32::MAX))
            .last()
            .is_none_or(|(_, r)| *r <= start_time);

        let next_starts_after = self
            .bookings
            .range((start_time, 0)..)
            .next()
            .is_none_or(|(l, _)| *l >= end_time);

        if prev_ends_before && next_starts_after {
            self.bookings.insert((start_time, end_time));
            true
        } else {
            false
        }
    }
}

#[cfg(test)]
mod tests {
    use super::MyCalendar;

    #[test]
    fn case_1() {
        let mut cal = MyCalendar::new();
        assert!(cal.book(10, 20));
        assert!(!cal.book(15, 25));
        assert!(cal.book(20, 30));
    }

    #[test]
    fn case_2() {
        let mut cal = MyCalendar::new();
        assert!(cal.book(1, 3));
        assert!(cal.book(6, 7));
        assert!(!cal.book(2, 4));
        assert!(cal.book(3, 5));
    }

    #[test]
    fn case_3() {
        let mut cal = MyCalendar::new();
        assert!(cal.book(47, 50));
        assert!(cal.book(33, 41));
        assert!(!cal.book(39, 45));
        assert!(!cal.book(33, 42));
        assert!(cal.book(25, 32));
        assert!(!cal.book(26, 35));
        assert!(cal.book(19, 25));
        assert!(cal.book(3, 8));
        assert!(cal.book(8, 13));
        assert!(!cal.book(18, 27));
    }

    #[test]
    fn case_4() {
        let mut cal = MyCalendar::new();
        assert!(cal.book(19, 25));
        assert!(!cal.book(18, 27));
    }
}
