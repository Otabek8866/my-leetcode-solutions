class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0

        found = {}
        start = result = 0

        for i in range(len(s)):
            if s[i] in found and start <= found[s[i]]:
                start = found[s[i]] + 1
            else:
                result = max(result, i - start + 1)
            found[s[i]] = i

        return result
