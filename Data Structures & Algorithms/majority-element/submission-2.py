from collections import Counter

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        freq = Counter(nums)
        for i in nums:
            if freq[i]>=len(nums)//2:
                return i

        