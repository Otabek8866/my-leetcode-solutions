int max(int a, int b)
{
    return (a > b) ? a : b;
}

int deleteAndEarn(int *nums, int numsSize)
{
    int points[10001], now = 0, prev = 0, tmp;
    for (int i = 0; i < 10001; i++)
        points[i] = 0;
    for (int i = 0; i < numsSize; i++)
        points[nums[i]] += nums[i];
    for (int i = 0; i < 10001; i++)
    {
        tmp = prev;
        prev = now;
        now = max(tmp + points[i], now);
    }
    return now;
}