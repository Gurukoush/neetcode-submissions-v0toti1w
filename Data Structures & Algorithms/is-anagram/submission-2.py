class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        k = ''.join(sorted(s))
        m = ''.join(sorted(t))
        if len(k)!=len(m):
            return False
        if k==m:
            return True
        else:
            return False
       
            
        