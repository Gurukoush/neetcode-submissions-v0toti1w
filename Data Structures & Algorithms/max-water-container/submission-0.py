class Solution:
    def maxArea(self, heights: List[int]) -> int:
        n = len(heights)
        res = 0
        for i in range(0,n):
            for j in range(i+1,n):
                area = min(heights[i],heights[j]) * (j-i)
                res = max(res,area)
        return res
        