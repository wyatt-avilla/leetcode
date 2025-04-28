// https://leetcode.com/problems/insert-delete-getrandom-o1/

use std::collections::HashSet;
use std::fs::File;
use std::io::Read;

struct RandomizedSet {
    set: HashSet<i32>,
}

impl RandomizedSet {
    const BUCKETS: usize = 256;

    fn new() -> Self {
        RandomizedSet {
            set: HashSet::new(),
        }
    }

    fn insert(&mut self, val: i32) -> bool {
        self.set.insert(val)
    }

    fn remove(&mut self, val: i32) -> bool {
        self.set.remove(&val)
    }

    fn get_random(&self) -> i32 {
        let mut rng = File::open("/dev/urandom").unwrap();

        let mut buffer = [0u8; 1];
        rng.read_exact(&mut buffer).unwrap();

        *self
            .set
            .iter()
            .nth(buffer[0] as usize % self.set.len())
            .unwrap()
    }
}

#[cfg(test)]
mod test {
    use super::RandomizedSet;

    #[test]
    fn case1() {
        let mut rs = RandomizedSet::new();
        assert!(rs.insert(1));
        assert!(!rs.remove(2));
        assert!(rs.insert(2));
        assert!(rs.remove(1));
        assert!(!rs.insert(2));
        assert_eq!(rs.get_random(), 2);
    }
}
