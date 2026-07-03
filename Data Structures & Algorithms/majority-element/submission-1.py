from collections import Counter 

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = Counter(nums)
        print(count)
        for num in count:
            if count[num] > len(nums)//2:
                return num