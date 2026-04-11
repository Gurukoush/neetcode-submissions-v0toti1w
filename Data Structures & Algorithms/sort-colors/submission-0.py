class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        nums_0 = []
        nums_1 = []
        nums_2 = []
        for i in range(len(nums)):
            if nums[i]==0:
                nums_0.append(0)
            elif nums[i]==1:
                nums_1.append(1)
            else:
                nums_2.append(2)
        nums[:]=nums_0+nums_1+nums_2
        