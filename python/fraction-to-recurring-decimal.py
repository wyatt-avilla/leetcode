# https://leetcode.com/problems/fraction-to-recurring-decimal/


class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        if numerator == 0:
            return "0"

        if (naive_frac := numerator / denominator).is_integer():
            return f"{naive_frac:.0f}"

        dividend = abs(numerator)
        divisor = abs(denominator)

        frac = [
            "-" if (numerator < 0) ^ (denominator < 0) else "",
            str(dividend // divisor),
            ".",
        ]

        remainder = dividend % divisor
        seen_pos: dict[int, int] = {}
        while remainder != 0:
            if remainder in seen_pos:
                frac.insert(seen_pos[remainder], "(")
                frac.append(")")
                break
            seen_pos[remainder] = len(frac)
            remainder *= 10
            frac.append(str(remainder // divisor))
            remainder %= divisor

        return "".join(frac)


if __name__ == "__main__":
    assert Solution().fractionToDecimal(0, -5) == "0"
    assert Solution().fractionToDecimal(2, 1) == "2"
    assert Solution().fractionToDecimal(-2, 2) == "-1"
    assert Solution().fractionToDecimal(1, 2) == "0.5"
    assert Solution().fractionToDecimal(4, 333) == "0.(012)"
    assert Solution().fractionToDecimal(-50, 8) == "-6.25"
