class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rotten = set()
        fresh = 0
        m, n = len(grid), len(grid[0])
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2:
                    grid[i][j] = 3
                    rotten.add((i, j))
                if grid[i][j] == 1:
                    fresh += 1
        if fresh == 0:
            return 0
        if len(rotten) == 0:
            return -1

        t = 0
        while fresh > 0:
            tmp = fresh
            new_round = []
            for i in range(m):
                for j in range(n):
                    if grid[i][j] == 3 and (i, j) in rotten:
                        print("found at", i, j, grid[i][j])
                        print(rotten)
                        grid[i][j] = 2
                        if i > 0 and grid[i-1][j] == 1:
                            grid[i-1][j] = 3
                            new_round.append((i-1, j))
                            fresh -= 1
                        if j > 0 and grid[i][j-1] == 1:
                            grid[i][j-1] = 3
                            new_round.append((i, j-1))
                            fresh -= 1
                        if i < m-1 and grid[i+1][j] == 1:
                            grid[i+1][j] = 3
                            new_round.append((i+1, j))
                            fresh -= 1
                        if j < n-1 and grid[i][j+1] == 1:
                            grid[i][j+1] = 3
                            new_round.append((i, j+1))
                            fresh -= 1
            t += 1
            rotten = set(new_round)
            if tmp == fresh:
                return -1

        return t
