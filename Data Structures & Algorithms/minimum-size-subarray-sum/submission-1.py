class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        min1 = float('inf')
        res = 0
        l = 0
        for r in range(len(nums)):
            res += nums[r]
            while res >= target:
                min1 = min(min1, r - l + 1)
                res -= nums[l]
                l += 1
            
        return 0 if min1 == float('inf') else min1
            