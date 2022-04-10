class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        # length = len(s)
        # if length % 2 == 1:
        #     right = length // 2 + 1
        # else:
        #     right = length // 2
        # left = length // 2 - 1
        # while left >= 0:
        #     tmp = s[left]
        #     s[left] = s[right]
        #     s[right] = tmp
        #     left -= 1
        #     right += 1
        l = len(s)
        s.extend(s[::-1])
        s[:l] = []