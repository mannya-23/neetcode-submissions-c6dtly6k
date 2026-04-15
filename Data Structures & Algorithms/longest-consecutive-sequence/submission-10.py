class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        res = 0
        numset = set(nums)

        nums.sort()

        for num in nums:
            if num -1 not in numset:
                length = 0
                while num + length in numset:
                    length += 1
                res = max(res, length)
        return res
    
