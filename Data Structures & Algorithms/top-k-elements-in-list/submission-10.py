from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
      
        res = []
        nums.sort()

        counts = Counter(nums)
        print(counts)

        arr = []
        for num, count in counts.items():
            arr.append([count, num])
        print(arr)
        arr.sort(reverse = True)
        print(arr)


        print(arr)
        for num in arr[:k]:
            res.append(num[1])

        return res