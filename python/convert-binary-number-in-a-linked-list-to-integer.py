# https://leetcode.com/problems/convert-binary-number-in-a-linked-list-to-integer/

from __future__ import annotations

from data_structures import ListNode


class Solution:
    def getDecimalValue(self, head: ListNode | None) -> int:
        ans = 0
        node = head
        while node:
            ans = (ans << 1) | node.val
            node = node.next
        return ans


if __name__ == "__main__":
    assert Solution().getDecimalValue(ListNode(1, ListNode(0, ListNode(1)))) == 5
    assert Solution().getDecimalValue(ListNode(0)) == 0
