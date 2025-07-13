# https://leetcode.com/problems/maximum-matching-of-players-with-trainers/


class Solution:
    def matchPlayersAndTrainers(
        self,
        players: list[int],
        trainers: list[int],
    ) -> int:
        p_len = len(players)
        t_len = len(trainers)

        players.sort()
        trainers.sort()

        i_p = 0
        i_t = 0

        ans = 0
        while i_p < p_len and i_t < t_len:
            if players[i_p] <= trainers[i_t]:
                ans += 1
                i_p += 1
                i_t += 1
            else:
                i_t += 1

        return ans


if __name__ == "__main__":
    assert Solution().matchPlayersAndTrainers([4, 7, 9], [8, 2, 5, 8]) == 2
    assert Solution().matchPlayersAndTrainers([1, 1, 1], [10]) == 1
