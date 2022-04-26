bool canJump(int *nums, int numsSize)
{
    int jump = 0;
    for (int i = 0; i < numsSize; i++)
    {
        if (jump < i)
            return false;
        jump = (jump > i + nums[i]) ? jump : i + nums[i];
    }
    return true;
}