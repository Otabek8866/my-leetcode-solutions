# Solution 1:
from itertools import combinations


class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        return list(combinations(range(1, n+1), k)

# Solution 2:
# adopted from @StefanPochmann
# class Solution:
#     def combine(self, n, k):
#         if k == 0:
#             return [[]]
#         return [pre + [i] for i in range(k, n+1) for pre in self.combine(i-1, k-1)]
