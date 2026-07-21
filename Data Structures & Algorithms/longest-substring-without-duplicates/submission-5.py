class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max1 = 0
        l = 0
        charSet = set()
        for r in range(len(s)):
            while s[r] in charSet:
                charSet.remove(s[l])
                l += 1
            charSet.add(s[r])
            max1 = max(max1, len(charSet))
        return max1