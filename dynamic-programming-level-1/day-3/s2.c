int max(int a, int b)
{
    return (a > b) ? a : b;
}

int rob(int *nums, int numsSize)
{
    if (numsSize == 1)
        return nums[0];

    int now1 = 0, now2 = 0, prev = 0, tmp;
    for (int i = 0; i < numsSize - 1; i++)
    {
        tmp = prev;
        prev = now1;
        now1 = max(tmp + nums[i], now1);
    }

    prev = 0;
    for (int i = 1; i < numsSize; i++)
    {
        tmp = prev;
        prev = now2;
        now2 = max(tmp + nums[i], now2);
    }

    return max(now1, now2);
}
