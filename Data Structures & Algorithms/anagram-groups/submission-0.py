class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # better appraoch
        hash_map = {}
        for i in strs:
            key = "".join(sorted(i))
            if key not in hash_map:
                hash_map[key]= []
            hash_map[key].append(i)
        return list(hash_map.values())
        
        