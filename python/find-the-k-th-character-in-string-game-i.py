# https://leetcode.com/problems/find-the-k-th-character-in-string-game-i/


class Solution:
    def kthCharacter(self, k: int) -> str:
        precomputed = "abbcbccdbccdcddebccdcddecddedeefbccdcddecddedeefcddedeefdeefeffgbccdcddecddedeefcddedeefdeefeffgcddedeefdeefeffgdeefeffgeffgfgghbccdcddecddedeefcddedeefdeefeffgcddedeefdeefeffgdeefeffgeffgfgghcddedeefdeefeffgdeefeffgeffgfgghdeefeffgeffgfggheffgfgghfgghghhibccdcddecddedeefcddedeefdeefeffgcddedeefdeefeffgdeefeffgeffgfgghcddedeefdeefeffgdeefeffgeffgfgghdeefeffgeffgfggheffgfgghfgghghhicddedeefdeefeffgdeefeffgeffgfgghdeefeffgeffgfggheffgfgghfgghghhideefeffgeffgfggheffgfgghfgghghhieffgfgghfgghghhifgghghhighhihiij"

        return precomputed[k - 1]


if __name__ == "__main__":
    assert Solution().kthCharacter(5) == "b"
    assert Solution().kthCharacter(10) == "c"
