from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        strs.sort()
        agrams = defaultdict(list)
        for string in strs:
            agrams[tuple(sorted(string))].append(string)
        return list(agrams.values())