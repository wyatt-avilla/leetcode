# https://leetcode.com/problems/find-the-minimum-amount-of-time-to-brew-potions/


class Solution:
    def minTime(self, skills: list[int], energy: list[int]) -> int:
        n, m = len(skills), len(energy)
        prefix_skills = [0] * n
        for i in range(1, n):
            prefix_skills[i] = prefix_skills[i - 1] + skills[i]

        total_time = skills[0] * energy[0]

        for j in range(1, m):
            max_time = skills[0] * energy[j]
            for i in range(1, n):
                diff_time = (
                    prefix_skills[i] * energy[j - 1] - prefix_skills[i - 1] * energy[j]
                )
                max_time = max(max_time, diff_time)
            total_time += max_time

        return total_time + prefix_skills[-1] * energy[-1]


if __name__ == "__main__":
    assert Solution().minTime([1, 3, 4], [2, 3, 3, 3]) == 53
    assert Solution().minTime([1, 5, 2, 4], [5, 1, 4, 2]) == 110
    assert Solution().minTime([1, 1, 1], [1, 1, 1]) == 5
    assert Solution().minTime([1, 2, 3, 4], [1, 2]) == 21
