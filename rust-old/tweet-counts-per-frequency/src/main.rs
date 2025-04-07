// https://leetcode.com/problems/tweet-counts-per-frequency/

use std::cmp;
use std::collections::BTreeMap;

struct TweetCounts {
    tweets: BTreeMap<i32, BTreeMap<String, i32>>,
}

impl TweetCounts {
    fn new() -> Self {
        TweetCounts {
            tweets: BTreeMap::new(),
        }
    }

    fn record_tweet(&mut self, tweet_name: String, time: i32) {
        *self
            .tweets
            .entry(time)
            .or_default()
            .entry(tweet_name)
            .or_default() += 1;
    }

    fn get_tweet_counts_per_frequency(
        &self,
        freq: String,
        tweet_name: String,
        start_time: i32,
        end_time: i32,
    ) -> Vec<i32> {
        let chunk_size: i32 = match freq.as_str() {
            "minute" => 60,
            "hour" => 3600,
            "day" => 86400,
            _ => unreachable!("problem constraints"),
        };

        let bounds = (0..)
            .map(move |i| start_time + i * chunk_size)
            .take_while(move |&chunk_start| chunk_start <= end_time)
            .map(move |chunk_start| {
                (
                    chunk_start,
                    cmp::min(chunk_start + chunk_size - 1, end_time),
                )
            });

        bounds
            .map(|(beg, end)| {
                self.tweets
                    .range(beg..=end)
                    .map(|(_, m)| m.get(&tweet_name).unwrap_or(&0))
                    .sum()
            })
            .collect()
    }
}

fn main() {
    let mut tc = TweetCounts::new();
    tc.record_tweet("tweet3".to_string(), 0);
    tc.record_tweet("tweet3".to_string(), 60);
    tc.record_tweet("tweet3".to_string(), 10);
    assert!(
        tc.get_tweet_counts_per_frequency("minute".to_string(), "tweet3".to_string(), 0, 59)
            == vec![2]
    );
    assert!(
        tc.get_tweet_counts_per_frequency("minute".to_string(), "tweet3".to_string(), 0, 60)
            == vec![2, 1]
    );
    tc.record_tweet("tweet3".to_string(), 120);
    assert!(
        tc.get_tweet_counts_per_frequency("hour".to_string(), "tweet3".to_string(), 0, 210)
            == vec![4]
    );

    let mut tc2 = TweetCounts::new();
    tc2.record_tweet("tweet3".to_string(), 0);
    tc2.record_tweet("tweet3".to_string(), 60);
    tc2.record_tweet("tweet3".to_string(), 10);
    tc2.record_tweet("tweet3".to_string(), 10);
    assert!(
        tc2.get_tweet_counts_per_frequency("minute".to_string(), "tweet3".to_string(), 0, 59)
            == vec![3]
    );
    assert!(
        tc2.get_tweet_counts_per_frequency("minute".to_string(), "tweet3".to_string(), 0, 60)
            == vec![3, 1]
    );
    tc2.record_tweet("tweet3".to_string(), 120);
    assert!(
        tc2.get_tweet_counts_per_frequency("hour".to_string(), "tweet3".to_string(), 0, 210)
            == vec![5]
    );
}
