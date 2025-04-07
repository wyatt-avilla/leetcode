// https://leetcode.com/problems/destination-city/

use std::collections::HashMap;

pub struct Solution;

impl Solution {
    pub fn dest_city(paths: Vec<Vec<String>>) -> String {
        let outgoing_from: HashMap<&String, Vec<&String>> =
            paths.iter().fold(HashMap::new(), |mut map, path| {
                map.entry(&path[0]).or_insert_with(Vec::new).push(&path[1]);
                map
            });

        paths
            .iter()
            .flatten()
            .collect::<Vec<&String>>()
            .into_iter()
            .filter(|city| !outgoing_from.contains_key(city))
            .map(|city| city.to_string())
            .collect::<String>()
    }
}

#[cfg(test)]
mod tests {
    use super::Solution;

    #[test]
    fn case_1() {
        let paths = vec![
            vec!["London".to_string(), "New York".to_string()],
            vec!["New York".to_string(), "Lima".to_string()],
            vec!["Lima".to_string(), "Sao Paulo".to_string()],
        ];
        assert_eq!(Solution::dest_city(paths), String::from("Sao Paulo"));
    }

    #[test]
    fn case_2() {
        let paths = vec![
            vec!["B".to_string(), "C".to_string()],
            vec!["D".to_string(), "B".to_string()],
            vec!["C".to_string(), "A".to_string()],
        ];
        assert_eq!(Solution::dest_city(paths), String::from("A"));
    }

    #[test]
    fn case_3() {
        let paths = vec![vec!["A".to_string(), "Z".to_string()]];
        assert_eq!(Solution::dest_city(paths), String::from("Z"));
    }
}
