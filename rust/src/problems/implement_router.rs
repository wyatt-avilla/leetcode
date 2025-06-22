// https://leetcode.com/problems/implement-router/description/

use std::{
    cmp::Reverse,
    collections::{BinaryHeap, HashMap, HashSet, VecDeque},
};

type Source = i32;
type Destination = i32;
type TimeStamp = i32;
type TimeStampOrdering = usize;

#[derive(Debug)]
struct Router {
    max_packets: usize,
    curr_packets: usize,
    packets_for: HashMap<
        Destination,
        (
            HashSet<(TimeStamp, Source)>,
            VecDeque<(TimeStamp, TimeStampOrdering, Source)>,
        ),
    >,
    next_forward: BinaryHeap<(Reverse<TimeStamp>, Reverse<TimeStampOrdering>, Destination)>,
    order_at: HashMap<TimeStamp, TimeStampOrdering>,
}

impl Router {
    fn new(memory_limit: i32) -> Self {
        Self {
            max_packets: memory_limit.try_into().expect("problem constraints"),
            curr_packets: 0,
            packets_for: HashMap::new(),
            next_forward: BinaryHeap::new(),
            order_at: HashMap::new(),
        }
    }

    fn add_packet(&mut self, source: i32, destination: i32, timestamp: i32) -> bool {
        let (set, queue) = self.packets_for.entry(destination).or_default();

        if !set.insert((timestamp, source)) {
            return false;
        }

        let timestamp_ordering = *self
            .order_at
            .entry(timestamp)
            .and_modify(|c| *c += 1)
            .or_insert(0);

        if queue.is_empty() {
            self.next_forward
                .push((Reverse(timestamp), Reverse(timestamp_ordering), destination));
        }

        queue.push_back((timestamp, timestamp_ordering, source));

        if self.curr_packets == self.max_packets {
            let _ = self.forward_packet();
        }
        self.curr_packets += 1;

        true
    }

    fn forward_packet(&mut self) -> Vec<i32> {
        if self.curr_packets == 0 {
            vec![]
        } else {
            let destination = self.next_forward.pop().expect("invalid `curr_packets`").2;
            let (set, queue) = self.packets_for.entry(destination).or_default();

            let (timestamp, _, source) = queue.pop_front().expect("invalid `curr_packets`");
            set.remove(&(timestamp, source));

            if let Some((timestamp, timestamp_ordering, _)) = queue.front() {
                self.next_forward.push((
                    Reverse(*timestamp),
                    Reverse(*timestamp_ordering),
                    destination,
                ));
            }

            self.curr_packets -= 1;
            vec![source, destination, timestamp]
        }
    }

    fn get_count(&self, destination: i32, start_time: i32, end_time: i32) -> i32 {
        if let Some((_, queue)) = self.packets_for.get(&destination) {
            let left = queue.partition_point(|(timestamp, _, _)| *timestamp < start_time);
            let right = queue.partition_point(|(timestamp, _, _)| *timestamp <= end_time);

            (right - left).try_into().expect("problem constraints")
        } else {
            0
        }
    }
}

#[cfg(test)]
mod tests {
    use super::Router;

    #[test]
    fn case_1() {
        let mut router = Router::new(3);
        assert!(router.add_packet(1, 4, 90));
        assert!(router.add_packet(2, 5, 90));
        assert!(!router.add_packet(1, 4, 90));
        assert!(router.add_packet(3, 5, 95));
        assert!(router.add_packet(4, 5, 105));
        assert_eq!(router.forward_packet(), vec![2, 5, 90]);
        assert!(router.add_packet(5, 2, 110));
        assert_eq!(router.get_count(5, 100, 110), 1);
    }

    #[test]
    fn case_2() {
        let mut router = Router::new(3);
        assert!(router.add_packet(7, 4, 90));
        assert_eq!(router.forward_packet(), vec![7, 4, 90]);
        assert_eq!(router.forward_packet(), vec![]);
    }

    #[test]
    fn case_3() {
        let mut router = Router::new(2);
        assert!(router.add_packet(5, 2, 4));
        assert!(router.add_packet(4, 2, 4));
        assert_eq!(router.forward_packet(), vec![5, 2, 4]);
        assert_eq!(router.get_count(2, 4, 4), 1);
    }

    #[test]
    fn case_4() {
        let mut router = Router::new(2);
        assert!(router.add_packet(3, 4, 1));
        assert!(router.add_packet(2, 4, 1));
        assert!(router.add_packet(4, 5, 1));
        assert_eq!(router.forward_packet(), vec![2, 4, 1]);
        assert!(router.add_packet(5, 4, 1));
    }

    #[test]
    fn case_5() {
        let mut router = Router::new(2);
        assert!(router.add_packet(1, 5, 1));
        assert!(router.add_packet(2, 5, 1));
        assert!(router.add_packet(1, 2, 1));
        dbg!(&router);
        assert_eq!(router.get_count(2, 1, 1), 1);
        assert_eq!(router.forward_packet(), vec![2, 5, 1]);
        assert_eq!(router.forward_packet(), vec![1, 2, 1]);
        assert_eq!(router.forward_packet(), vec![]);
    }
}
