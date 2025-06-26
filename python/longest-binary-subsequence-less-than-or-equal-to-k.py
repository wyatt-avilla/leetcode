# https://leetcode.com/problems/longest-binary-subsequence-less-than-or-equal-to-k/


class Solution:
    def longestSubsequence(self, s: str, k: int) -> int:
        sub_seq_val = 0
        sub_seq_len = 0
        for i, c in enumerate(reversed(s)):
            match c:
                case "0":
                    sub_seq_len += 1
                case "1":
                    new_bit = 1 << i
                    if sub_seq_val | new_bit <= k:
                        sub_seq_val |= new_bit
                        sub_seq_len += 1

        return sub_seq_len


if __name__ == "__main__":
    assert Solution().longestSubsequence("1001010", 5) == 5
    assert Solution().longestSubsequence("00101001", 1) == 6
