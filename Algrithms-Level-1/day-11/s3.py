class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        res = ['']
        for x in s:
            if x.isalpha():
                res = [i+j for i in res for j in [x.upper(), x.lower()]]
            else:
                res = [i + x for i in res]
        return res
