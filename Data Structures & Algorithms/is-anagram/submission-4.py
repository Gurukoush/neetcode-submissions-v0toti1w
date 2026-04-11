class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        m = sorted(s)
        k = sorted(t)
        if m!=k:
            return False
        return True

      