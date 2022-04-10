class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2) < len(s1):
            return False
        s1 = sorted(s1)
        l = len(s1)
        for i in range(0, len(s2)-l+1):
            if sorted(s2[i:i+l]) == s1:
                return True
        return False
