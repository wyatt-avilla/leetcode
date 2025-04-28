// https://leetcode.com/problems/encode-and-decode-tinyurl/

use std::hash::{DefaultHasher, Hash, Hasher};

struct Codec {
    hasher: DefaultHasher,
    arr: [Vec<String>; Self::BUCKETS],
}

impl Codec {
    const BUCKETS: usize = 512;

    fn new() -> Self {
        Codec {
            hasher: DefaultHasher::new(),
            arr: [const { Vec::new() }; Self::BUCKETS],
        }
    }

    fn encode(&mut self, long_url: String) -> String {
        long_url.hash(&mut self.hasher);
        let idx_1 = self.hasher.finish() as usize % Self::BUCKETS;
        let idx_2 = self.arr[idx_1].len();

        self.arr[idx_1].push(long_url);

        format!("{idx_1}-{idx_2}")
    }

    fn decode(&self, short_url: String) -> String {
        let mut split = short_url
            .split('-')
            .map(|s| s.parse::<usize>().expect("format"));
        let (idx_1, idx_2) = (split.next().expect("format"), split.next().expect("format"));

        self.arr[idx_1][idx_2].clone()
    }
}

#[cfg(test)]
mod tests {
    use super::Codec;

    #[test]
    fn case1() {
        let mut c = Codec::new();
        let url = String::from("test_url");
        let enc = c.encode(url.clone());
        let dec = c.decode(enc);

        assert_eq!(dec, url);
    }
}
