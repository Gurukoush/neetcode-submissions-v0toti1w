class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        k = sorted(s)
        m = sorted(t)
        if k!=m:
            return False

        return True

      