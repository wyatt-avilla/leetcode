# https://leetcode.com/problems/vowel-spellchecker/


from itertools import product


class Solution:
    @staticmethod
    def check_word(
        word_set: set[str],
        case_map: dict[str, str],
        word_to_idx: dict[str, int],
        word: str,
    ) -> str:
        if word in word_set:
            return word

        lower_word = word.lower()

        if lower_word in case_map:
            return case_map[lower_word]

        vowels = {"a", "e", "i", "o", "u"}
        vowel_idxs = {i for i, c in enumerate(lower_word) if c in vowels}

        vowel_replacements = (
            "".join(
                next(combit) if i in vowel_idxs else c for i, c in enumerate(lower_word)
            )
            for combit in (
                iter(comb) for comb in product(vowels, repeat=len(vowel_idxs))
            )
        )

        vowel_replacement_matches = {
            case_map[vr] for vr in vowel_replacements if vr in case_map
        }

        return min(
            (word for word in vowel_replacement_matches),
            key=lambda w: word_to_idx[w],
            default="",
        )

    def spellchecker(self, wordlist: list[str], queries: list[str]) -> list[str]:
        word_set = set(wordlist)
        case_insensitive_map = {word.lower(): word for word in reversed(wordlist)}
        word_to_idx = {word: i for i, word in enumerate(dict.fromkeys(wordlist))}

        return [
            Solution.check_word(word_set, case_insensitive_map, word_to_idx, word)
            for word in queries
        ]


if __name__ == "__main__":
    assert Solution().spellchecker(
        ["KiTe", "kite", "hare", "Hare"],
        [
            "kite",
            "Kite",
            "KiTe",
            "Hare",
            "HARE",
            "Hear",
            "hear",
            "keti",
            "keet",
            "keto",
        ],
    ) == ["kite", "KiTe", "KiTe", "Hare", "hare", "", "", "KiTe", "", "KiTe"]

    assert Solution().spellchecker(["yellow"], ["YellOw"]) == ["yellow"]

    assert Solution().spellchecker(["ae", "aa"], ["UU"]) == ["ae"]
