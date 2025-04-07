// https://leetcode.com/problems/design-authentication-manager/

use std::collections::{BTreeMap, HashSet};

struct AuthenticationManager {
    time_to_live: i32,
    tokens: BTreeMap<i32, HashSet<String>>,
}

impl AuthenticationManager {
    fn new(time_to_live: i32) -> Self {
        AuthenticationManager {
            time_to_live,
            tokens: BTreeMap::new(),
        }
    }

    fn evict_up_to_and_including(&mut self, current_time: i32) {
        self.tokens = self.tokens.split_off(&(current_time + 1));
    }

    fn generate(&mut self, token_id: String, current_time: i32) {
        self.evict_up_to_and_including(current_time);

        self.tokens
            .entry(current_time + self.time_to_live)
            .or_default()
            .insert(token_id);
    }

    fn renew(&mut self, token_id: String, current_time: i32) {
        self.evict_up_to_and_including(current_time);

        if let Some((time, set_len)) = self.tokens.range(current_time..).find_map(|(t, s)| {
            if s.contains(&token_id) {
                Some((*t, s.len()))
            } else {
                None
            }
        }) {
            if set_len == 1 {
                self.tokens.remove(&time);
            } else {
                self.tokens.get_mut(&time).unwrap().remove(&token_id);
            }
            self.generate(token_id, current_time);
        }
    }

    fn count_unexpired_tokens(&mut self, current_time: i32) -> i32 {
        self.evict_up_to_and_including(current_time);
        self.tokens.len() as i32
    }
}

fn main() {}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn case1() {
        let mut am = AuthenticationManager::new(5);
        am.renew("aaa".into(), 1);
        am.generate("aaa".into(), 2);
        assert_eq!(am.count_unexpired_tokens(6), 1);
        am.generate("bbb".into(), 7);
        am.renew("aaa".into(), 8);
        am.renew("bbb".into(), 10);
        assert_eq!(am.count_unexpired_tokens(15), 0);
    }

    #[test]
    fn case62() {
        let mut am = AuthenticationManager::new(13);
        am.renew("ajvy".into(), 1);
        assert_eq!(am.count_unexpired_tokens(3), 0);
        assert_eq!(am.count_unexpired_tokens(4), 0);
        am.generate("fuzxq".into(), 5);
        am.generate("izmry".into(), 7);
        am.renew("puv".into(), 12);
        am.generate("ybiqb".into(), 13);
        am.generate("gm".into(), 14);
        assert_eq!(am.count_unexpired_tokens(15), 4);
        assert_eq!(am.count_unexpired_tokens(18), 3);
        assert_eq!(am.count_unexpired_tokens(19), 3);
        am.renew("ybiqb".into(), 21);
        dbg!(&am.tokens);
        assert_eq!(am.count_unexpired_tokens(23), 2);
        assert_eq!(am.count_unexpired_tokens(25), 2);
        assert_eq!(am.count_unexpired_tokens(26), 2);
        am.generate("aqdm".into(), 28);
        assert_eq!(am.count_unexpired_tokens(29), 2);
        am.renew("puv".into(), 30);
    }
}
