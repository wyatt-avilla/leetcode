# https://leetcode.com/problems/largest-3-same-digit-number-in-string/


class Solution:
    def largestGoodInteger(self, num: str) -> str:
        prev_digit = num[0]
        contig_count = 1
        largest_digit: str | None = None

        for d in num[1:]:
            if d == prev_digit:
                contig_count += 1
                if contig_count == 3:
                    largest_digit = max(largest_digit, d) if largest_digit else d
            else:
                prev_digit = d
                contig_count = 1

        return largest_digit * 3 if largest_digit else ""


if __name__ == "__main__":
    assert Solution().largestGoodInteger("2213") == ""
    assert Solution().largestGoodInteger("6777133339") == "777"
    assert Solution().largestGoodInteger("2300019") == "000"
    assert Solution().largestGoodInteger("42352338") == ""
