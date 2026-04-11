class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        water = 0
        for i in range(n):
            left = max(height[:i+1])
            right = max(height[i:])
            water_level = min(left,right)
            if water_level > 0:
                water+= water_level-height[i]
        return water   