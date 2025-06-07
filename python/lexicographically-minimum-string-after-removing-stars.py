# https://leetcode.com/problems/lexicographically-minimum-string-after-removing-stars/

import heapq


class Solution:
    def clearStars(self, s: str) -> str:
        del_idxs: set[int] = set()
        heap: list[tuple[str, int]] = []
        for i, c in enumerate(s):
            if c != "*":
                heapq.heappush(heap, (c, -i))
            else:
                _, popped_i = heapq.heappop(heap)
                del_idxs.add(-popped_i)

        return "".join(c for i, c in enumerate(s) if i not in del_idxs and c != "*")


if __name__ == "__main__":
    assert Solution().clearStars("aaba*") == "aab"
    assert Solution().clearStars("abc") == "abc"
    assert Solution().clearStars("d*e*d") == "d"
    assert Solution().clearStars("aaa***") == ""
