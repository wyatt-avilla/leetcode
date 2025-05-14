// https://leetcode.com/problems/longest-uploaded-prefix/
use std::collections::BTreeSet;

struct LUPrefix {
    n: i32,
    remaining: BTreeSet<i32>,
}

impl LUPrefix {
    fn new(n: i32) -> Self {
        LUPrefix {
            n,
            remaining: (1..=n).collect(),
        }
    }

    fn upload(&mut self, video: i32) {
        self.remaining.remove(&video);
    }

    fn longest(&self) -> i32 {
        match self.remaining.first() {
            Some(i) => i - 1,
            None => self.n,
        }
    }
}

#[cfg(test)]
mod tests {
    use super::LUPrefix;

    #[test]
    fn case_1() {
        let mut lup = LUPrefix::new(4);
        lup.upload(3);
        assert_eq!(lup.longest(), 0);
        lup.upload(1);
        assert_eq!(lup.longest(), 1);
        lup.upload(2);
        assert_eq!(lup.longest(), 3);
    }
}
