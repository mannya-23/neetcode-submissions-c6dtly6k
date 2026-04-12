from collections import Counter 

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = Counter(nums)
        res = []
        print(counts)
        for num in counts:
            res.append([counts[num], num])

        res.sort(reverse = True)

        output = []
        for count in res[:k]:
            output.append(count[1])
        return output

