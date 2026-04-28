class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        res = set()
        for r in range(len(nums)):
            if r  > k:
                res.remove(nums[r - k - 1])
            if nums[r] in res:
                return True
            else:
                res.add(nums[r])
        

        return False