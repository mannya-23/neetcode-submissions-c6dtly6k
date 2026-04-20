class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        l, r = 0, len(nums) -1 

        while l < r:
            sum1 = nums[l] +nums[r]
            if sum1 == target:
                return [1+l, 1 + r]
            elif sum1> target:
                r -= 1
            else:
                l += 1