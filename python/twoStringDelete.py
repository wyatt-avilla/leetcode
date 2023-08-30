class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        w1Len = len(word1)
        w2Len = len(word2)
        w1Startidx = 0
        w2Startidx = 0
        w1Similar = []
        w2Similar = []
        for i in range(max(w1Len, w2Len)):
            print(f"i is {i}")
            if i < w1Len and word1[i] in word2[w2Startidx:]:
                print(f"{word1[i]} in {word2[w2Startidx:]}")
                w1Similar.append(word1[i])
                w2Startidx += word2[w2Startidx:].index(word1[i]) + 1

            if i < w2Len and word2[i] in word1[w1Startidx:]:
                print(f"{word2[i]} in {word1[w1Startidx:]}")
                w2Similar.append(word2[i])
                w1Startidx += word1[w1Startidx:].index(word2[i]) + 1

        print(w1Similar, w2Similar)
        closestSimilar = max(len(w1Similar), len(w2Similar))
        return w1Len + w2Len - 2*closestSimilar



print(Solution().minDistance("abcdxabcde", "abcdeabcdx"))
