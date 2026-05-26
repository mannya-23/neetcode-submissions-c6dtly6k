from collections import Counter

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        counts = Counter(nums)
        for num in counts:
            if counts[num] > 1:
                return num