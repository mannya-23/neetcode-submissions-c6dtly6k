from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)
        strs.sort()
        for string in strs:
            res[''.join(sorted(string))].append(string)
        return list(res.values())