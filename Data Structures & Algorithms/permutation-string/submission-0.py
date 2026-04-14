from collections import Counter
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1counts = Counter(s1)
        s2counts = Counter(s2[:len(s1)])

        if s1counts == s2counts:
            return True
       
       
        for r in range(len(s1), len(s2)):
            s2counts[s2[r]] += 1
            
            s2counts[s2[r - len(s1)]] -= 1

            if s2counts == s1counts:
                return True
        return False
