from collections import defaultdict 

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dic = defaultdict(list)
       
        for string in strs:
            key = ''.join(sorted(string))
            dic[key].append(string)
        return list(dic.values())
