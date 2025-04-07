// https://leetcode.com/problems/design-memory-allocator/

use std::vec::Vec;

struct Allocator {
    vec: Vec<i32>,
}

impl Allocator {
    fn new(n: i32) -> Self {
        Allocator {
            vec: vec![0; n.try_into().unwrap()],
        }
    }

    fn allocate(&mut self, size: i32, m_id: i32) -> i32 {
        let want_size: usize = size.try_into().unwrap();
        let vsize = self.vec.len();

        for ref mut i in 0..vsize {
            if self.vec[*i] != 0 {
                continue;
            }

            let mut count = 0;
            for j in *i..vsize {
                if self.vec[j] == 0 {
                    count += 1;
                } else {
                    break;
                }
            }

            if count < want_size {
                *i += count;
                continue;
            }

            for j in *i..(*i + want_size) {
                self.vec[j] = m_id;
            }

            return (*i).try_into().unwrap();
        }

        -1
    }

    fn free_memory(&mut self, m_id: i32) -> i32 {
        self.vec
            .iter_mut()
            .filter(|x| **x == m_id)
            .map(|x| *x = 0)
            .count()
            .try_into()
            .unwrap()
    }
}

#[cfg(test)]
mod tests {
    use super::Allocator;

    #[test]
    fn case1() {
        let mut loc = Allocator::new(10);

        assert_eq!(loc.allocate(1, 1), 0);
        assert_eq!(loc.allocate(1, 2), 1);
        assert_eq!(loc.allocate(1, 3), 2);
        assert_eq!(loc.free_memory(2), 1);
        assert_eq!(loc.allocate(3, 4), 3);
        assert_eq!(loc.allocate(1, 1), 1);
        assert_eq!(loc.allocate(1, 1), 6);
        assert_eq!(loc.free_memory(1), 3);
        assert_eq!(loc.allocate(10, 2), -1);
        assert_eq!(loc.free_memory(7), 0);
    }
}
