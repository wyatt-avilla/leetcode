// https://leetcode.com/problems/design-bitset/

struct Bitset {
    bits: Vec<bool>,
    flipped: Vec<bool>,
    setcount: usize,
}

impl Bitset {
    fn new(size: i32) -> Self {
        Bitset {
            bits: vec![false; size as usize],
            flipped: vec![true; size as usize],
            setcount: 0,
        }
    }

    fn fix(&mut self, idx: i32) {
        if self.bits[idx as usize] == false {
            self.bits[idx as usize] = true;
            self.flipped[idx as usize] = false;
            self.setcount += 1;
        }
    }

    fn unfix(&mut self, idx: i32) {
        if self.bits[idx as usize] == true {
            self.bits[idx as usize] = false;
            self.flipped[idx as usize] = true;
            self.setcount -= 1;
        }
    }

    fn flip(&mut self) {
        std::mem::swap(&mut self.bits, &mut self.flipped);
        self.setcount = self.bits.len() - self.setcount;
    }

    fn all(&self) -> bool {
        self.setcount == self.bits.len()
    }

    fn one(&self) -> bool {
        self.setcount > 0
    }

    fn count(&self) -> i32 {
        self.setcount as i32
    }

    fn to_string(&self) -> String {
        self.bits
            .iter()
            .map(|b| i32::from(*b).to_string())
            .collect()
    }
}

fn main() {
    let mut bs = Bitset::new(5);
    bs.fix(3);
    bs.fix(1);
    bs.flip();
    assert!(!bs.all());
    bs.unfix(0);
    bs.flip();
    assert!(bs.one());
    bs.unfix(0);
    assert!(bs.count() == 2);
    assert!(bs.to_string() == "01010");
}
