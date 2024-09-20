# https://leetcode.com/problems/longest-absolute-file-path/
from __future__ import annotations


class Solution:
    def lengthLongestPath(self, input: str) -> int:
        split = input.split("\n")
        return max(
            (
                self.__dfs_sum(partition, 1)
                for partition in (self.__partition(split, 0))
            ),
        )
        return self.__dfs_sum(input.split("\n"), 0)

    def __partition(self, tokens: list[str], t_count: int) -> list[list[str]]:
        indices = [i for i in range(len(tokens)) if tokens[i].count("\t") == t_count]
        return [
            tokens[indices[i] :]
            if i + 1 == len(indices)
            else tokens[indices[i] : indices[i + 1]]
            for i in range(len(indices))
        ]

    def __dfs_sum(self, tokens: list[str], depth: int) -> int:
        if len(tokens) == 1:
            return len(tokens[0]) if "." in tokens[0] else 0

        subroot = tokens.pop(0)

        curr_max = max(
            [
                rec_sum - depth + 1
                for partition in self.__partition(
                    tokens,
                    depth,
                )
                if (rec_sum := self.__dfs_sum(partition, depth + 1)) > 0
            ],
            default=0,
        )

        return len(subroot) + curr_max if curr_max > 0 else 0


solution = Solution()

case_1 = solution.lengthLongestPath(
    "dir\n\tsubdir1\n\t\tfile1.ext\n\t\tsubsubdir1\n\tsubdir2\n\t\tsubsubdir2\n\t\t\tfile2.ext",
)
print(case_1)
print("---")

case_2 = solution.lengthLongestPath("file1.txt\nfile2.txt\nlongfile.txt")
print(case_2)
print("---")

case_3 = solution.lengthLongestPath("a")
print(case_3)
print("---")

case_4 = solution.lengthLongestPath("a\n\tb.txt\na2\n\tb2.txt")
print(case_4)
