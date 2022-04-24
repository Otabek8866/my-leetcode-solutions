int minCostClimbingStairs(int *cost, int costSize)
{
    int p[costSize];
    p[0] = cost[0];
    p[1] = cost[1];
    for (int i = 2; i < costSize; i++)
    {
        if (p[i - 2] < p[i - 1])
            p[i] = cost[i] + p[i - 2];
        else
            p[i] = cost[i] + p[i - 1];
    }
    return (p[costSize - 1] < p[costSize - 2]) ? p[costSize - 1] : p[costSize - 2];
}