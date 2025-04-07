// https://leetcode.com/problems/camelcase-matching/

pub struct Solution;

impl Solution {
    pub fn camel_match_old(queries: Vec<String>, pattern: String) -> Vec<bool> {
        // two pointers instead?
        let pattern_capital_indices: Vec<_> = pattern
            .chars()
            .enumerate()
            .filter(|(_, c)| c.is_uppercase())
            .map(|(i, _)| i)
            .collect();

        let mut prefixes: Vec<&str> = Vec::new();
        let mut remaining: &str = pattern.as_ref();
        for i in pattern_capital_indices.into_iter().rev() {
            let (l, r) = remaining.split_at(i);
            remaining = l;
            prefixes.push(r);
        }

        println!("p: {:?}", prefixes);

        let mut matches: Vec<bool> = Vec::new();
        for word in queries {
            if prefixes.iter().all(|&prefix| word.contains(prefix))
                && word.chars().filter(|&c| c.is_uppercase()).count() == prefixes.len()
            {
                matches.push(true);
                continue;
            }
            matches.push(false)
        }

        matches
    }

    pub fn capital_indices(word: &String) -> Vec<usize> {
        word.chars()
            .enumerate()
            .filter(|(_, c)| c.is_uppercase())
            .map(|(i, _)| i)
            .collect()
    }

    pub fn expandable_to(smaller: &str, bigger: &str) -> bool {
        let mut search_slice = &bigger[0..];
        for c in smaller.chars() {
            match search_slice.find(c) {
                Some(i) => search_slice = &search_slice[i + 1..],
                None => return false,
            }
        }
        true
    }
    pub fn camel_match(queries: Vec<String>, pattern: String) -> Vec<bool> {
        // find idxs of capital letters that correspond to the ones in pattern
        // check that the letters between the capitals in pattern are also between the capitals in word
        let mut matches: Vec<bool> = Vec::new();

        let pattern_capital_indices = Self::capital_indices(&pattern);
        println!("p: {} {:?}", &pattern, pattern_capital_indices);

        'outer: for word in queries {
            let word_capital_indices = Self::capital_indices(&word);
            println!("w: {} {:?}", &word, word_capital_indices);

            if word_capital_indices.len() != pattern_capital_indices.len() {
                matches.push(false);
                continue;
            }

            let mut l_word_bound = 0;
            let mut l_pat_bound = 0;
            for (&widx, &pidx) in word_capital_indices
                .iter()
                .zip(pattern_capital_indices.iter())
            {
                if widx == 0 || pidx == 0 {
                    continue;
                };
                let subword = &word[l_word_bound..widx];
                let subpat = &pattern[l_pat_bound..pidx];
                println!(
                    "{}[{}..{}] = {} and {}[{}..{}] = {}",
                    &word, l_word_bound, widx, subword, pattern, l_pat_bound, pidx, subpat
                );
                println!(
                    "{} can be expanded to {}, {}",
                    subpat,
                    subword,
                    Self::expandable_to(subpat, subword)
                );
                if !Self::expandable_to(subpat, subword) {
                    matches.push(false);
                    continue 'outer;
                }

                l_word_bound = widx;
                l_pat_bound = pidx;
            }
            println!(
                "final {} and {}",
                &pattern[l_pat_bound..],
                &word[l_word_bound..]
            );
            matches.push(Self::expandable_to(
                &pattern[l_pat_bound..],
                &word[l_word_bound..],
            ));
        }
        matches
    }
}

#[cfg(test)]
mod tests {
    use super::Solution;

    #[test]
    fn case_1() {
        let queries = vec![
            String::from("FooBar"),
            String::from("FooBarTest"),
            String::from("FootBall"),
            String::from("FrameBuffer"),
            String::from("ForceFeedBack"),
        ];
        let pattern = String::from("FB");
        let result = Solution::camel_match(queries, pattern);
        assert_eq!(result, vec![true, false, true, true, false]);
    }

    #[test]
    fn case_2() {
        let queries = vec![
            String::from("FooBar"),
            String::from("FooBarTest"),
            String::from("FootBall"),
            String::from("FrameBuffer"),
            String::from("ForceFeedBack"),
        ];
        let pattern = String::from("FoBa");
        let result = Solution::camel_match(queries, pattern);
        assert_eq!(result, vec![true, false, true, false, false]);
    }

    #[test]
    fn case_3() {
        let queries = vec![
            String::from("FooBar"),
            String::from("FooBarTest"),
            String::from("FootBall"),
            String::from("FrameBuffer"),
            String::from("ForceFeedBack"),
        ];
        let pattern = String::from("FoBaT");
        let result = Solution::camel_match(queries, pattern);
        assert_eq!(result, vec![false, true, false, false, false]);
    }

    #[test]
    fn case_4() {
        let queries = vec![
            String::from("CompetitiveProgramming"),
            String::from("CounterPick"),
            String::from("ControlPanel"),
        ];
        let pattern = String::from("CooP");
        let result = Solution::camel_match(queries, pattern);
        assert_eq!(result, vec![false, false, true]);
    }
}
