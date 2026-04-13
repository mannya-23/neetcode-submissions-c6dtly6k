class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res = 0
        chars = set()
        l = 0

        for r in range(len(s)):
            # remove duplicate letters from set until all chars in set are unique 
            while s[r] in chars:
                chars.remove(s[l])
                l += 1
            chars.add(s[r])
            res = max(res, len(chars))
        return res
            
        
            
