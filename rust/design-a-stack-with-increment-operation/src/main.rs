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

fn main() {
    let mut s1 = CustomStack::new(3);
    s1.push(1);
    s1.push(2);
    assert!(s1.pop() == 2);
    s1.push(2);
    s1.push(3);
    s1.push(4);
    s1.increment(5, 100);
    s1.increment(2, 100);
    assert!(s1.pop() == 103);
    assert!(s1.pop() == 202);
    assert!(s1.pop() == 201);
    assert!(s1.pop() == -1);

    let mut s2 = CustomStack::new(30);
    assert!(s2.pop() == -1);
    s2.increment(3, 40);
    s2.push(30);
    s2.increment(4, 63);
    s2.increment(2, 79);
    s2.increment(5, 57);
    assert!(s2.pop() == 229);
    s2.increment(5, 32);
}
