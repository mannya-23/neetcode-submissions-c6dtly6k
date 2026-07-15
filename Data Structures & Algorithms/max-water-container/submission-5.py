class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max1 = 0

        l, r = 0, len(heights) - 1

        while l < r:
            max1 = max(max1, (r - l) * min(heights[l],heights[r]))
            if heights[l] > heights[r]:
                r -= 1
            else:
                l += 1
        
        return max1 


