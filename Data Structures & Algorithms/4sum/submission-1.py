class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
     
        result = []   # use set to avoid duplicates
        n = len(nums)

        for i in range(n):
            for j in range(i+1, n):
                for k in range(j+1, n):
                    for m in range(k+1, n):
                        total = nums[i] + nums[j] + nums[k] + nums[m]
                        if total == target:
                            forplet = [nums[i],nums[j],nums[k],nums[m]]
                           
                            if forplet not in result:
                                result.append(forplet)
        return result