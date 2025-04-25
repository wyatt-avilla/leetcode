use std::collections::HashMap;

struct FrequencyTracker {
    num_to_freq: HashMap<i32, i32>,
    freq_to_nums: HashMap<i32, i32>,
}

impl FrequencyTracker {
    fn new() -> Self {
        FrequencyTracker {
            num_to_freq: HashMap::new(),
            freq_to_nums: HashMap::new(),
        }
    }

    fn add(&mut self, number: i32) {
        if let Some(curr_freq) = self.num_to_freq.get_mut(&number) {
            *self
                .freq_to_nums
                .get_mut(curr_freq)
                .expect("problem constraints") -= 1;

            *curr_freq += 1;

            *self.freq_to_nums.entry(*curr_freq).or_default() += 1;
        } else {
            self.num_to_freq.insert(number, 1);
            *self.freq_to_nums.entry(1).or_default() += 1;
        }
    }

    fn delete_one(&mut self, number: i32) {
        if let Some(curr_freq) = self.num_to_freq.get_mut(&number) {
            if *curr_freq > 0 {
                *self
                    .freq_to_nums
                    .get_mut(curr_freq)
                    .expect("problem constraints") -= 1;

                *curr_freq -= 1;

                *self.freq_to_nums.entry(*curr_freq).or_default() += 1;
            }
        }
    }

    fn has_frequency(&self, frequency: i32) -> bool {
        self.freq_to_nums.get(&frequency).is_some_and(|n| *n > 0)
    }
}

#[cfg(test)]
mod tests {
    use super::FrequencyTracker;

    #[test]
    fn example_1() {
        let mut tracker = FrequencyTracker::new();
        tracker.add(3);
        tracker.add(3);
        assert_eq!(tracker.has_frequency(2), true);
    }

    #[test]
    fn example_2() {
        let mut tracker = FrequencyTracker::new();
        tracker.add(1);
        tracker.delete_one(1);
        assert_eq!(tracker.has_frequency(1), false);
    }

    #[test]
    fn example_3() {
        let mut tracker = FrequencyTracker::new();
        assert_eq!(tracker.has_frequency(2), false);
        tracker.add(3);
        assert_eq!(tracker.has_frequency(1), true);
    }

    #[test]
    fn example_4() {
        let mut tracker = FrequencyTracker::new();
        assert_eq!(tracker.has_frequency(2), false);
        tracker.add(3);
        tracker.add(3);
        tracker.delete_one(2);
        tracker.add(3);
        assert_eq!(tracker.has_frequency(1), false);
        assert_eq!(tracker.has_frequency(3), true);
        tracker.delete_one(3);
        assert_eq!(tracker.has_frequency(2), true);
    }
}
