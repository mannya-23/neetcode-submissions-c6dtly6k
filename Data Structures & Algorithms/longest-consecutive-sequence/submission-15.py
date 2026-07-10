class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        if not nums:
            return 0 
            
        numbers = sorted(set(nums))
        res = 1
        count = 1
        i = 0
        
        while i < len(numbers) - 1:
            if numbers[i + 1] == numbers[i] + 1:
                count += 1
            else:
                res = max(res, count)
                count = 1
            i += 1
            
        # This must be outside the while loop!
        return max(res, count)
