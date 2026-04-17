class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        max_len = 0
        for i in range(0,n):
            seen = []
            for j in range(i,n):
                if s[j] in seen:
                    break
                seen.append(s[j])
                length = j-i+1

                max_len = max(max_len,length)
        return max_len
        