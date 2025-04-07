// https://leetcode.com/problems/time-based-key-value-store/

use std::collections::HashMap;
use std::vec::Vec;

struct TimeStapmedValue {
    timestamp: i32,
    value: String,
}

struct TimeMap {
    map: HashMap<String, Vec<TimeStapmedValue>>,
}

impl TimeMap {
    fn new() -> Self {
        TimeMap {
            map: HashMap::new(),
        }
    }

    fn set(&mut self, key: String, value: String, timestamp: i32) {
        self.map
            .entry(key)
            .or_default()
            .push(TimeStapmedValue { timestamp, value });
    }

    fn get(&self, key: String, timestamp: i32) -> String {
        let not_found = String::new();

        let Some(history) = self.map.get(&key) else {
            return not_found;
        };

        let closest_idx = history.binary_search_by_key(&timestamp, |x| x.timestamp);

        match closest_idx {
            Ok(x) => history[x].value.clone(),
            Err(0) => not_found,
            Err(e) => history[e - 1].value.clone(),
        }
    }
}

#[cfg(test)]
mod tests {
    use super::TimeMap;

    #[test]
    fn case_1() {
        let mut timemap: TimeMap = TimeMap::new();
        timemap.set("foo".into(), "bar".into(), 1);
        assert_eq!(timemap.get("foo".into(), 1), "bar");
        assert_eq!(timemap.get("foo".into(), 3), "bar");

        timemap.set("foo".into(), "bar2".into(), 4);
        assert_eq!(timemap.get("foo".into(), 4), "bar2");
        assert_eq!(timemap.get("foo".into(), 5), "bar2");
    }
}
