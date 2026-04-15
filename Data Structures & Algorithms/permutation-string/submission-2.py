
from collections import Counter
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_len = len(s1)
        s2_len = len(s2)
        
        if s1_len > s2_len:
            return False
        
        s1_count = Counter(s1)
        window_count = Counter(s2[0:s1_len])
        if s1_count == window_count:
            return True

        for i in range(s1_len,s2_len):
            window_count[s2[i]]+=1
            window_count[s2[i-s1_len]]-=1

            if window_count[s2[i-s1_len]]==0:
                del window_count[s2[i-s1_len]]

            if s1_count==window_count:
                return True
        return False 




        






