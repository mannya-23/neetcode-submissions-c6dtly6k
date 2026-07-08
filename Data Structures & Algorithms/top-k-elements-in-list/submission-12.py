from collections import Counter 

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        res = []
        for num in count:
            res.append([count[num], num])

        res.sort(reverse = True)
        print(res)
        final_res = []
        for count in res[:k]:
            final_res.append(count[1])
        return final_res


