class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hash_map = {}
        for i in nums:
            if i in hash_map:
                hash_map[i]+=1
            else:
                hash_map[i]=1

        items = list(hash_map.items())

        items.sort(key=lambda x:x[1],reverse=True)

        result = []
        for k in range(k):
            result.append(items[k][0])
        return result        

        