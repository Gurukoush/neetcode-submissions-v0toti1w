class Solution:
    def sortArray(self, arr: List[int]) -> List[int]:
        n = len(arr)
        for i in range(n):
            for j in range(i+1,n):
                if arr[i]>arr[j]:
                    arr[i],arr[j]=arr[j],arr[i]
        return arr
        