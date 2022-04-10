class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        table = {'(': ')', '[': ']', '{': '}'}
        for ch in s:
            if ch in ('(', '[', '{'):
                stack.append(ch)
            elif len(stack) == 0 or ch != table[stack.pop(-1)]:
                return False
        return False if len(stack) else True
