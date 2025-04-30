// https://leetcode.com/problems/exam-room/

use std::collections::BTreeSet;

struct ExamRoom {
    seats: i32,
    occupancy: BTreeSet<i32>,
}

impl ExamRoom {
    fn new(n: i32) -> Self {
        ExamRoom {
            seats: n,
            occupancy: BTreeSet::new(),
        }
    }

    fn seat(&mut self) -> i32 {
        if self.occupancy.is_empty() {
            self.occupancy.insert(0);
            return 0;
        }

        let bounds = self.occupancy.iter().skip(1).scan(
            self.occupancy.first().expect("nonempty occupancy"),
            |left, right| {
                let p = (*left, right);
                *left = right;
                Some(p)
            },
        );

        let best_seat = bounds
            .map(|(left, right)| {
                let dist = right - left;
                let mid = left + dist / 2;
                (mid, dist / 2)
            })
            .chain([
                (0, *self.occupancy.first().unwrap()),
                (
                    self.seats - 1,
                    self.seats - 1 - *self.occupancy.last().unwrap(),
                ),
            ])
            .fold(Vec::new(), |mut acc, p| {
                match acc.first() {
                    None => acc.push(p),
                    Some(first) => match first.1.cmp(&p.1) {
                        std::cmp::Ordering::Less => {
                            acc.clear();
                            acc.push(p);
                        }
                        std::cmp::Ordering::Equal => acc.push(p),
                        std::cmp::Ordering::Greater => {}
                    },
                }
                acc
            })
            .into_iter()
            .min_by_key(|(i, _)| *i)
            .unwrap()
            .0;

        self.occupancy.insert(best_seat);
        best_seat
    }

    fn leave(&mut self, p: i32) {
        self.occupancy.remove(&p);
    }
}

#[cfg(test)]
mod tests {
    use super::ExamRoom;

    #[test]
    fn case_1() {
        let mut er = ExamRoom::new(10);

        assert_eq!(er.seat(), 0);
        assert_eq!(er.seat(), 9);
        assert_eq!(er.seat(), 4);
        assert_eq!(er.seat(), 2);
        er.leave(4);
        assert_eq!(er.seat(), 5);
    }

    #[test]
    fn case_2() {
        let mut er = ExamRoom::new(4);

        assert_eq!(er.seat(), 0);
        assert_eq!(er.seat(), 3);
        assert_eq!(er.seat(), 1);
        assert_eq!(er.seat(), 2);
        er.leave(1);
        er.leave(3);
        assert_eq!(er.seat(), 1);
        assert_eq!(er.seat(), 3);
    }

    #[test]
    fn case_3() {
        let mut er = ExamRoom::new(10);

        assert_eq!(er.seat(), 0);
        assert_eq!(er.seat(), 9);
        assert_eq!(er.seat(), 4);
        er.leave(0);
        er.leave(4);
        assert_eq!(er.seat(), 0);
        assert_eq!(er.seat(), 4);
        assert_eq!(er.seat(), 2);
        assert_eq!(er.seat(), 6);
        assert_eq!(er.seat(), 1);
        assert_eq!(er.seat(), 3);
        assert_eq!(er.seat(), 5);
        assert_eq!(er.seat(), 7);
        assert_eq!(er.seat(), 8);
        er.leave(0);
        er.leave(4);
        assert_eq!(er.seat(), 0);
        assert_eq!(er.seat(), 4);
        er.leave(7);
        assert_eq!(er.seat(), 7);
        er.leave(3);
        assert_eq!(er.seat(), 3);
        er.leave(3);
        assert_eq!(er.seat(), 3);
        er.leave(9);
        assert_eq!(er.seat(), 9);
        er.leave(0);
        er.leave(8);
        assert_eq!(er.seat(), 0);
        assert_eq!(er.seat(), 8);
        er.leave(0);
        er.leave(8);
        assert_eq!(er.seat(), 0);
        assert_eq!(er.seat(), 8);
        er.leave(2);
    }

    #[test]
    fn case_4() {
        let mut er = ExamRoom::new(8);

        assert_eq!(er.seat(), 0);
        assert_eq!(er.seat(), 7);
        assert_eq!(er.seat(), 3);
        er.leave(0);
        er.leave(7);
        assert_eq!(er.seat(), 7);
        assert_eq!(er.seat(), 0);
        assert_eq!(er.seat(), 5);
        assert_eq!(er.seat(), 1);
        assert_eq!(er.seat(), 2);
        assert_eq!(er.seat(), 4);
        assert_eq!(er.seat(), 6);
    }
}
