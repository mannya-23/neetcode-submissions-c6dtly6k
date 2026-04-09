class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums1 = set(nums)
        print(nums1)
        max1 = 0

        for num in nums:
            count = 1
            if num - 1 not in nums1:
                length = 1
                while num + length in nums1:
                    length += 1
        
                max1 = max(max1, length)
        return max1
                

