# https://leetcode.com/problems/number-of-people-aware-of-a-secret/


class Solution:
    def peopleAwareOfSecret(self, n: int, delay: int, forget: int) -> int:
        delays = [0 for _ in range(delay)]
        forgets = [0 for _ in range(forget)]
        actively_telling = 0

        delays[delay - 1] = 1
        forgets[forget - 1] = 1

        for _ in range(n - 1):
            actively_telling += delays.pop(0)
            actively_telling -= forgets.pop(0)

            delays.append(actively_telling)
            forgets.append(actively_telling)

        return (sum(delays) + actively_telling) % (10**9 + 7)


if __name__ == "__main__":
    assert Solution().peopleAwareOfSecret(6, 2, 4) == 5
    assert Solution().peopleAwareOfSecret(4, 1, 3) == 6
