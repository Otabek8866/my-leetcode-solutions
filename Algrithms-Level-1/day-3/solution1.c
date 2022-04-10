void moveZeroes(int *nums, int numsSize)
{
    int left = 0;
    for (; left < numsSize; left++)
        if (nums[left] == 0)
            break;
    int right = left + 1;
    for (; right < numsSize; right++)
        if (nums[right] != 0)
        {
            nums[left] = nums[right];
            nums[right] = 0;
            left++;
        }
}