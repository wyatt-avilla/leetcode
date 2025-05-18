// https://leetcode.com/problems/design-circular-queue/

#[derive(Debug)]
struct MyCircularQueue {
    capacity: u16,
    used: u16,
    elements: Vec<u16>,
    front_idx: usize,
    back_idx: usize,
}

impl MyCircularQueue {
    fn new(k: i32) -> Self {
        let k = u16::try_from(k).expect("problem constraints");
        MyCircularQueue {
            capacity: k,
            used: 0,
            elements: vec![0; k as usize],
            front_idx: 0,
            back_idx: 0,
        }
    }

    fn en_queue(&mut self, value: i32) -> bool {
        if self.is_full() {
            false
        } else {
            self.back_idx = if self.is_empty() {
                self.back_idx
            } else {
                (self.back_idx + 1) % self.capacity as usize
            };

            self.elements[self.back_idx % self.capacity as usize] =
                u16::try_from(value).expect("problem constraints");
            self.used += 1;
            true
        }
    }

    fn de_queue(&mut self) -> bool {
        if self.is_empty() {
            false
        } else {
            self.front_idx = if self.used == 1 {
                self.front_idx
            } else {
                (self.front_idx + 1) % self.capacity as usize
            };
            self.used -= 1;
            true
        }
    }

    fn front(&self) -> i32 {
        if self.is_empty() {
            -1
        } else {
            self.elements[self.front_idx].into()
        }
    }

    fn rear(&self) -> i32 {
        if self.is_empty() {
            -1
        } else {
            self.elements[self.back_idx].into()
        }
    }

    fn is_empty(&self) -> bool {
        self.used == 0
    }

    fn is_full(&self) -> bool {
        self.used == self.capacity
    }
}

#[cfg(test)]
mod tests {
    use super::MyCircularQueue;

    #[test]
    fn case_1() {
        let mut q = MyCircularQueue::new(3);

        assert!(q.en_queue(1));
        assert!(q.en_queue(2));
        assert!(q.en_queue(3));
        assert!(!q.en_queue(4));

        assert_eq!(q.rear(), 3);
        assert!(q.is_full());
        assert!(q.de_queue());
        assert!(q.en_queue(4));
        assert_eq!(q.rear(), 4);
    }

    #[test]
    fn case_2() {
        let mut q = MyCircularQueue::new(3);

        assert!(q.en_queue(2));

        assert_eq!(q.rear(), 2);
        assert_eq!(q.front(), 2);
    }

    #[test]
    fn case_3() {
        let mut q = MyCircularQueue::new(81);

        assert!(q.en_queue(69));
        assert!(q.de_queue());
        dbg!(&q);
        assert!(q.en_queue(92));
        assert!(q.en_queue(12));
        assert!(q.de_queue());
        assert!(!q.is_full());
        assert!(!q.is_full());

        assert_eq!(q.front(), 12);
    }
}
