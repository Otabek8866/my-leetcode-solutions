class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        prev = new = [1]
        for i in range(1, rowIndex+1):
            prev = new
            new = [1]
            for j in range(1, i):
                new.append(prev[j-1]+prev[j])
            new.append(1)
        return new
