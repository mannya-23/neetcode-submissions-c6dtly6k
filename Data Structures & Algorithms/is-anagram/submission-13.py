class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dic = {}
        dic1 = {}
        for char in s:
            if char in dic:
                dic[char] += 1
            else:
                dic[char] = 1

        for char in t:
            if char in dic1:
                dic1[char] += 1
            else:
                dic1[char] = 1

        return dic1 == dic