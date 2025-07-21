# https://leetcode.com/problems/delete-characters-to-make-fancy-string/


class Solution:
    def makeFancyString(self, s: str) -> str:
        ans: list[str] = []
        contig_count = 0
        contig_char = ""
        for c in (c for c in s):
            if c == contig_char:
                contig_count += 1
                if contig_count >= 3:
                    continue
            else:
                contig_count = 1
                contig_char = c

            ans.append(c)

        return "".join(ans)


if __name__ == "__main__":
    assert Solution().makeFancyString("leeetcode") == "leetcode"
    assert Solution().makeFancyString("aaabaaaa") == "aabaa"
    assert Solution().makeFancyString("aab") == "aab"
