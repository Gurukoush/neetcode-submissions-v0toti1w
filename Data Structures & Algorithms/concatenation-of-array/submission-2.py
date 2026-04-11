class Solution:
    def getConcatenation(self, arr: List[int]) -> List[int]:
        ans = []
        for i in range(2):
            for i in arr:
                ans.append(i)
        return ans

        
        