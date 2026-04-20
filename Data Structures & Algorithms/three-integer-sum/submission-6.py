class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = set()
        for i in range(len(nums)):
            l,r = i +1, len(nums) -1
            
            while l < r:
                sum1 = nums[i] + nums[l] +nums[r]
                if sum1 == 0:
                    res.add(tuple([nums[l], nums[i] ,nums[r]]))
                    r-= 1
                    l += 1
                elif sum1>0:
                    r -= 1
                else: 
                    l += 1
        return list(res)