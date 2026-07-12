class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        res = ''
        j = 0
        for i in range(min(len(word1), len(word2))):
            res += word1[i]
            res += word2[i]
            j += 1
        if len(word1) > len(word2):
            res += word1[j:]
        else:
            res += word2[j:]
        return res