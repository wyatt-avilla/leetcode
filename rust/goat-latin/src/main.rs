// https://leetcode.com/problems/goat-latin/


pub struct Solution;

impl Solution {
    pub fn to_goat_latin_old(sentence: String) -> String {
        let mut sentence_words: Vec<String> = sentence.split_whitespace().map(|w| w.to_string()).collect();
        let vowels = ['a', 'e', 'i', 'o', 'u'];

        for (i, word) in sentence_words.iter_mut().enumerate() {
            match &word {
                word if vowels.iter().any(|&vowel| word.to_lowercase().starts_with(vowel)) => (),
                _ => { let c = word.remove(0); word.push(c) },
            };
            word.push_str("ma");
            word.push_str(&"a".repeat(i+1));
        }
        sentence_words.join(" ")
    }

    pub fn to_goat_latin(sentence: String) -> String {
        let vowels = ['a', 'e', 'i', 'o', 'u'];

        sentence.split_whitespace().map(|w| w.to_string()).enumerate()
            .map(|(i, mut word)| {
                 if !vowels.iter().any(|&vowel| word.to_lowercase().starts_with(vowel)) {
                     let c = word.remove(0);
                     word.push(c);
                 }
                 word.push_str("ma");
                 word.push_str(&"a".repeat(i+1));
                 word
            })
            .collect::<Vec<String>>()
            .join(" ")
    }
}

fn main() {
    println!("main executed")
}

// Import the necessary modules
#[cfg(test)]
mod tests {
    // Import the Solution struct (assuming it's in the same module or crate)
    use super::Solution;

    // Test case 1
    #[test]
    fn case1() {
        let sentence = String::from("I speak Goat Latin");
        assert_eq!(Solution::to_goat_latin(sentence), String::from("Imaa peaksmaaa oatGmaaaa atinLmaaaaa"));
    }

    // Test case 2
    #[test]
    fn case2() {
        let sentence = String::from("The quick brown fox jumped over the lazy dog");
        assert_eq!(Solution::to_goat_latin(sentence), String::from("heTmaa uickqmaaa rownbmaaaa oxfmaaaaa umpedjmaaaaaa overmaaaaaaa hetmaaaaaaaa azylmaaaaaaaaa ogdmaaaaaaaaaa"));
    }
}
