from collections import Counter

class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        counts = Counter(nums)
        res = []

        for num in counts:
            if counts[num] > len(nums)//3:
                res.append(num)

        return res