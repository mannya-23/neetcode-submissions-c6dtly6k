class Solution:
    def validPalindrome(self, s: str) -> bool:
        if s == s[::-1]:
            return True
        
        l, r = 0, len(s) - 1

        while l < r:
            if s[l] == s[r]:
                l += 1
                r -= 1
            else:
                rleft = s[l + 1:r+1]
                right = s[l:r]
                return rleft == rleft[::-1] or right == right[::-1]
                
