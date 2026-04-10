class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # ensure only unique pairs are added
        res = set()
        nums.sort()

        for i, num in enumerate(nums):
            l, r = i + 1, len(nums) - 1
            while l < r:
                threesum = nums[l] + nums[r] + num
                if threesum == 0: 
                    res.add(tuple([num, nums[l], nums[r]]))
                    l += 1
                    r -= 1
                elif threesum > 0:
                    r -= 1
                else:
                    l += 1
        return list(res)
            

            
