// https://leetcode.com/problems/design-a-stack-with-increment-operation/

use std::cmp;

struct CustomStack {
    max_size: usize,
    stack: Vec<i32>,
    offsets: Vec<i32>,
}

impl CustomStack {
    fn new(max_size: i32) -> Self {
        CustomStack {
            max_size: max_size as usize,
            stack: vec![],
            offsets: vec![0; max_size as usize + 1],
        }
    }

    fn push(&mut self, x: i32) {
        if self.stack.len() < self.max_size {
            self.stack.push(x);
        }
    }

    fn pop(&mut self) -> i32 {
        let idx = self.stack.len();

        match self.stack.pop() {
            Some(v) => {
                let to_return = v + self.offsets[idx];
                self.offsets[idx - 1] += self.offsets[idx];
                self.offsets[idx] = 0;

                to_return
            }
            None => -1,
        }
    }

    fn increment(&mut self, k: i32, val: i32) {
        let bound = cmp::min(self.stack.len(), k as usize);
        if bound > 0 {
            self.offsets[bound] += val;
        }
    }
}

#[cfg(test)]
mod tests {
    use super::CustomStack;

    #[test]
    fn case_1() {
        let mut s = CustomStack::new(3);
        s.push(1);
        s.push(2);
        assert_eq!(s.pop(), 2);
        s.push(2);
        s.push(3);
        s.push(4);
        s.increment(5, 100);
        s.increment(2, 100);
        assert_eq!(s.pop(), 103);
        assert_eq!(s.pop(), 202);
        assert_eq!(s.pop(), 201);
        assert_eq!(s.pop(), -1);
    }

    #[test]
    fn case_2() {
        let mut s = CustomStack::new(30);
        assert!(s.pop() == -1);
        s.increment(3, 40);
        s.push(30);
        s.increment(4, 63);
        s.increment(2, 79);
        s.increment(5, 57);
        assert!(s.pop() == 229);
        s.increment(5, 32);
    }
}
