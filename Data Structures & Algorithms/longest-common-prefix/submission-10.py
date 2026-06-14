class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res = ''
    
        sort = sorted(strs)
        first = sort[0]
        last = sort[-1]
        for i in range(min(len(first), len(last))):
            if first[i] == last[i]:
                res += first[i]
            else:
                break
        return res 