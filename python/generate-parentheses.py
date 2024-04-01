# https://leetcode.com/problems/generate-parentheses/

from __future__ import annotations


def build_tree(
    valid_moves: list[str],
    max_path_len: int,
    current_path: list[str],
    stack_val: int,
) -> None:
    if len(current_path) == max_path_len:
        valid_moves.append("".join(current_path))
        return

    if stack_val == 0:
        build_tree(valid_moves, max_path_len, current_path + ["("], stack_val + 1)
    elif stack_val == max_path_len - len(current_path):
        build_tree(valid_moves, max_path_len, current_path + [")"], stack_val - 1)
    else:
        build_tree(valid_moves, max_path_len, current_path + ["("], stack_val + 1)
        build_tree(valid_moves, max_path_len, current_path + [")"], stack_val - 1)


class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        valid_moves = []

        build_tree(valid_moves, n * 2, [], 0)
        return valid_moves


print(Solution().generateParenthesis(4))
