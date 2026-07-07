from collections import Counter
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        j = 0
        count = Counter(nums)
        for num in range(3):
            for i in range(count[num]):
                nums[j] = num
                j += 1
        return nums