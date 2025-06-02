# https://leetcode.com/problems/minesweeper/

from collections.abc import Iterator


class Solution:
    MINE = "M"
    EMPTY = "E"
    BLANK = "B"

    def updateBoard(
        self,
        board: list[list[str]],
        click: [list[int]],
    ) -> list[list[str]]:
        r, c = click
        total_rows = len(board)
        total_cols = len(board[0])
        if board[r][c] == self.MINE:
            board[r][c] = "X"
            return board

        self.recursive_reveal(r, c, total_rows, total_cols, board)

        return board

    def recursive_reveal(
        self,
        row: int,
        col: int,
        total_rows: int,
        total_cols: int,
        board: list[list[str]],
    ) -> None:
        adj_spots = tuple(self.adj_from(row, col, total_rows, total_cols))
        adj_mines = sum(board[r][c] == self.MINE for (r, c) in adj_spots)

        if adj_mines > 0:
            board[row][col] = str(adj_mines)
        else:
            board[row][col] = self.BLANK
            for r, c in ((r, c) for (r, c) in adj_spots if board[r][c] == self.EMPTY):
                self.recursive_reveal(r, c, total_rows, total_cols, board)

    def adj_from(
        self,
        row: int,
        col: int,
        total_rows: int,
        total_cols: int,
    ) -> Iterator[tuple[int, int]]:
        return (
            (r, c)
            for r in range(row - 1, row + 2)
            for c in range(col - 1, col + 2)
            if r in range(total_rows)
            and c in range(total_cols)
            and (r, c) != (row, col)
        )


if __name__ == "__main__":
    assert Solution().updateBoard(
        [
            ["E", "E", "E", "E", "E"],
            ["E", "E", "M", "E", "E"],
            ["E", "E", "E", "E", "E"],
            ["E", "E", "E", "E", "E"],
        ],
        [3, 0],
    ) == [
        ["B", "1", "E", "1", "B"],
        ["B", "1", "M", "1", "B"],
        ["B", "1", "1", "1", "B"],
        ["B", "B", "B", "B", "B"],
    ]

    assert Solution().updateBoard(
        [
            ["B", "1", "E", "1", "B"],
            ["B", "1", "M", "1", "B"],
            ["B", "1", "1", "1", "B"],
            ["B", "B", "B", "B", "B"],
        ],
        [1, 2],
    ) == [
        ["B", "1", "E", "1", "B"],
        ["B", "1", "X", "1", "B"],
        ["B", "1", "1", "1", "B"],
        ["B", "B", "B", "B", "B"],
    ]
