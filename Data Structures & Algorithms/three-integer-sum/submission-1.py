class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        result = []
        for i in range(0,n):
            for j in range(i+1,n):
                for k in range(j+1,n):
                    triplets = nums[i]+nums[j]+nums[k]
                    if triplets == 0:
                        triplets = [nums[i],nums[j],nums[k]]
                        triplets.sort()
                        
                        if triplets not in result:
                            result.append(triplets)
        return result
                    
                    




        