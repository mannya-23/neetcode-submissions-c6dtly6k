class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dic = {}

        for num in nums:
            if num not in dic:
                dic[num] = 1
            else: 
                dic[num] += 1
        
        arr = []

        for num, count in dic.items():
            arr.append([count, num])

        arr.sort(reverse = True)

        ls = list()
        for num in arr[:k]:
            ls.append(num[1])

        return ls 


