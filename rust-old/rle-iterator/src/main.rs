// https://leetcode.com/problems/rle-iterator/

use std::iter;
use std::{
    iter::{FlatMap, Repeat, Take},
    vec::IntoIter,
};

struct RLEIterator {
    it: FlatMap<IntoIter<(i32, i32)>, Take<Repeat<i32>>, fn((i32, i32)) -> Take<Repeat<i32>>>,
}

impl RLEIterator {
    fn new(encoding: Vec<i32>) -> RLEIterator {
        RLEIterator {
            it: encoding
                .chunks(2)
                .map(|c| (c[0], c[1]))
                .collect::<Vec<(i32, i32)>>()
                .into_iter()
                .flat_map(
                    (|(n, c)| iter::repeat(c).take(n.try_into().unwrap()))
                        as fn((i32, i32)) -> Take<Repeat<i32>>,
                ),
        }
    }

    fn next(&mut self, n: i32) -> i32 {
        self.it
            .by_ref()
            .nth((n - 1).try_into().unwrap())
            .unwrap_or(-1)
    }
}

fn main() {
    let v = vec![
        923381016, 843, 898173122, 924, 540599925, 391, 705283400, 275, 811628709, 850, 895038968,
        590, 949764874, 580, 450563107, 660, 996257840, 917, 793325084, 82,
    ];

    let mut rleit = RLEIterator::new(v);

    rleit.next(612783106);
    rleit.next(486444202);
    rleit.next(630147341);
    rleit.next(845077576);
    rleit.next(243035623);
    rleit.next(731489221);
    rleit.next(117134294);
    rleit.next(220460537);
    rleit.next(794582972);
    rleit.next(332536150);
    rleit.next(815913097);
    rleit.next(100607521);
    rleit.next(146358489);
    rleit.next(697670641);
    rleit.next(45234068);
    rleit.next(573866037);
    rleit.next(519323635);
    rleit.next(27431940);
    rleit.next(16279485);
    rleit.next(203970);
}
