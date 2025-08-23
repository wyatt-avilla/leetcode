// https://leetcode.com/problems/my-calendar-ii/

use std::collections::BTreeSet;

#[derive(Default)]
struct MyCalendarTwo {
    single_booked: BTreeSet<(i32, i32)>,
    double_booked: BTreeSet<(i32, i32)>,
}

impl MyCalendarTwo {
    fn new() -> Self {
        Self::default()
    }

    fn overlapping(set: &BTreeSet<(i32, i32)>, start_time: i32, end_time: i32) -> Vec<(i32, i32)> {
        let mut overlapping = match set.range(..(start_time, 0)).last() {
            Some((_, r)) if *r > start_time => vec![(start_time, *r)],
            _ => vec![],
        };

        overlapping.extend(
            set.range((start_time, 0)..(end_time, 0))
                .map(std::borrow::ToOwned::to_owned),
        );

        if let Some(tup) = overlapping.last_mut() {
            tup.1 = std::cmp::min(tup.1, end_time);
        }

        overlapping
    }

    fn clear_in_range(set: &mut BTreeSet<(i32, i32)>, start_time: i32, end_time: i32) {
        if let Some(&(l, r)) = set.range(..(start_time, 0)).last()
            && r > start_time
        {
            set.remove(&(l, r));
            set.insert((l, start_time));
            set.insert((start_time, r));
        }

        if let Some(&(l, r)) = set.range(..(end_time, 0)).last()
            && r > end_time
        {
            set.remove(&(l, r));
            set.insert((end_time, r));
        }

        set.retain(|&(l, _)| l < start_time || l >= end_time);
    }

    fn book(&mut self, start_time: i32, end_time: i32) -> bool {
        if !Self::overlapping(&self.double_booked, start_time, end_time).is_empty() {
            return false;
        }

        let overlapping = Self::overlapping(&self.single_booked, start_time, end_time);

        Self::clear_in_range(&mut self.single_booked, start_time, end_time);
        self.single_booked.insert((start_time, end_time));

        self.double_booked.extend(overlapping);

        true
    }
}

#[cfg(test)]
mod tests {
    use super::MyCalendarTwo;

    #[test]
    fn case_1() {
        let mut cal = MyCalendarTwo::new();
        assert!(cal.book(10, 20));
        assert!(cal.book(50, 60));
        assert!(cal.book(10, 40));
        assert!(!cal.book(5, 15));
        assert!(cal.book(5, 10));
        assert!(cal.book(25, 55));
    }

    #[test]
    fn case_2() {
        let mut cal = MyCalendarTwo::new();
        assert!(cal.book(10, 20));
        assert!(cal.book(15, 18));
        assert!(cal.book(10, 15));
        assert!(cal.book(18, 20));
        assert!(!cal.book(10, 20));
        assert!(!cal.book(11, 13));
    }

    #[test]
    fn case_3() {
        let mut cal = MyCalendarTwo::new();
        assert!(cal.book(10, 50));
        assert!(cal.book(5, 15));
        assert!(cal.book(20, 30));
        assert!(cal.book(15, 20));
        assert!(cal.book(5, 10));
        assert!(!cal.book(4, 10));
    }

    #[test]
    fn case_4() {
        let mut cal = MyCalendarTwo::new();
        assert!(cal.book(47, 50));
        assert!(cal.book(1, 10));
        assert!(cal.book(27, 36));
        assert!(cal.book(40, 47));
        assert!(cal.book(20, 27));
        assert!(cal.book(15, 23));
        assert!(cal.book(10, 18));
        assert!(cal.book(27, 36));
        assert!(!cal.book(17, 25));
        assert!(!cal.book(8, 17));
        assert!(!cal.book(24, 33));
        assert!(!cal.book(23, 28));
        assert!(!cal.book(21, 27));
        assert!(cal.book(47, 50));
        assert!(!cal.book(14, 21));
        assert!(!cal.book(26, 32));
        assert!(!cal.book(16, 21));
        assert!(cal.book(2, 7));
        assert!(!cal.book(24, 33));
        assert!(!cal.book(6, 13));
        assert!(!cal.book(44, 50));
        assert!(!cal.book(33, 39));
        assert!(!cal.book(30, 36));
        assert!(!cal.book(6, 15));
        assert!(!cal.book(21, 27));
        assert!(!cal.book(49, 50));
        assert!(cal.book(38, 45));
        assert!(!cal.book(4, 12));
        assert!(!cal.book(46, 50));
        assert!(!cal.book(13, 21));
    }

    #[test]
    fn case_5() {
        let mut cal = MyCalendarTwo::new();
        assert!(cal.book(33, 44));
        assert!(cal.book(85, 95));
        assert!(cal.book(20, 37));
        assert!(cal.book(91, 100));
        assert!(!cal.book(89, 100));
        assert!(cal.book(77, 87));
        assert!(!cal.book(80, 95));
        assert!(cal.book(42, 61));
        assert!(!cal.book(40, 50));
        assert!(!cal.book(85, 99));
        assert!(!cal.book(74, 91));
        assert!(cal.book(70, 82));
        assert!(cal.book(5, 17));
        assert!(!cal.book(77, 89));
        assert!(cal.book(16, 26));
        assert!(!cal.book(21, 31));
        assert!(!cal.book(30, 43));
        assert!(cal.book(96, 100));
        assert!(!cal.book(27, 39));
        assert!(cal.book(44, 55));
        assert!(!cal.book(15, 34));
        assert!(!cal.book(85, 99));
        assert!(!cal.book(74, 93));
        assert!(!cal.book(84, 94));
        assert!(!cal.book(82, 94));
        assert!(!cal.book(46, 65));
        assert!(!cal.book(31, 49));
        assert!(cal.book(58, 73));
        assert!(!cal.book(86, 99));
        assert!(!cal.book(73, 84));
        assert!(!cal.book(68, 80));
        assert!(!cal.book(5, 18));
        assert!(!cal.book(75, 87));
        assert!(!cal.book(88, 100));
        assert!(!cal.book(25, 41));
        assert!(!cal.book(66, 79));
        assert!(!cal.book(28, 41));
        assert!(!cal.book(60, 70));
        assert!(!cal.book(62, 73));
        assert!(!cal.book(16, 33));
    }
}
