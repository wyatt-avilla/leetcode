use std::collections::VecDeque;

#[derive(Debug)]
struct FrontMiddleBackQueue {
    front_half: VecDeque<i32>,
    back_half: VecDeque<i32>,
}

impl FrontMiddleBackQueue {
    fn new() -> Self {
        FrontMiddleBackQueue {
            front_half: VecDeque::new(),
            back_half: VecDeque::new(),
        }
    }

    fn balance(&mut self) {
        if self.front_half.len() == self.back_half.len()
            || self.front_half.len() == (self.back_half.len() + 1)
        {
            return;
        }

        match self.front_half.len().cmp(&self.back_half.len()) {
            std::cmp::Ordering::Less => {
                self.front_half
                    .push_back(self.back_half.pop_front().expect("problem constraints"));
            }
            std::cmp::Ordering::Greater => {
                self.back_half
                    .push_front(self.front_half.pop_back().expect("problem constraints"));
            }
            std::cmp::Ordering::Equal => {}
        }
    }

    fn push_front(&mut self, val: i32) {
        self.front_half.push_front(val);
        self.balance();
    }

    fn push_middle(&mut self, val: i32) {
        if self.front_half.len() > self.back_half.len() {
            self.back_half
                .push_front(self.front_half.pop_back().expect("problem constraints"));
        }
        self.front_half.push_back(val);
        self.balance();
    }

    fn push_back(&mut self, val: i32) {
        self.back_half.push_back(val);
        self.balance();
    }

    fn pop_front(&mut self) -> i32 {
        let popped = self.front_half.pop_front();
        self.balance();
        popped.unwrap_or(-1)
    }

    fn pop_middle(&mut self) -> i32 {
        let popped = self.front_half.pop_back();
        self.balance();
        popped.unwrap_or(-1)
    }

    fn pop_back(&mut self) -> i32 {
        let popped = self.back_half.pop_back();
        self.balance();
        if let Some(popped) = popped {
            popped
        } else {
            self.front_half.pop_back().unwrap_or(-1)
        }
    }
}

#[cfg(test)]
mod tests {
    use super::FrontMiddleBackQueue;

    #[test]
    fn case_1() {
        let mut q = FrontMiddleBackQueue::new();

        q.push_front(1);
        q.push_back(2);
        q.push_middle(3);
        q.push_middle(4);

        assert_eq!(q.pop_front(), 1);
        assert_eq!(q.pop_middle(), 3);
        assert_eq!(q.pop_middle(), 4);
        dbg!(&q);
        assert_eq!(q.pop_back(), 2);
        assert_eq!(q.pop_front(), -1);
    }
}
