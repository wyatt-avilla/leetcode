# https://leetcode.com/problems/design-spreadsheet/

from collections import defaultdict
from string import ascii_uppercase


class Spreadsheet:
    def __init__(self, _rows: int) -> None:
        self.letters = set(ascii_uppercase)
        self.cells: dict[int, dict[str, int]] = defaultdict(lambda: defaultdict(int))

    @staticmethod
    def __rc_from(cell: str) -> tuple[int, str]:
        return (int(cell[1:]), cell[0])

    def setCell(self, cell: str, value: int) -> None:
        row, col = Spreadsheet.__rc_from(cell)
        self.cells[row][col] = value

    def resetCell(self, cell: str) -> None:
        self.setCell(cell, 0)

    def getValue(self, formula: str) -> int:
        left, right = (formula[1:]).split("+")

        def numeric_from(s: str) -> int:
            return (
                int(s)
                if all(c not in self.letters for c in s)
                else self.cells[int(s[1:])][s[0]]
            )

        return numeric_from(left) + numeric_from(right)


if __name__ == "__main__":
    s1 = Spreadsheet(3)
    assert s1.getValue("=5+7") == 12
    s1.setCell("A1", 10)
    assert s1.getValue("=A1+6") == 16
    s1.setCell("B2", 15)
    assert s1.getValue("=A1+B2") == 25
    s1.resetCell("A1")
    assert s1.getValue("=A1+B2") == 15
