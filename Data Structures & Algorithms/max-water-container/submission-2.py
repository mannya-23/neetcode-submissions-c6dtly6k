class Solution:
    def maxArea(self, heights: List[int]) -> int:
        res = 0 

        for i in range(len(heights)):
            for j in range(i + 1, len(heights)):
                if i - j != 0:
                    area = min(heights[i], heights[j]) * (j - i)
                    res = max(res, area)
        return res 