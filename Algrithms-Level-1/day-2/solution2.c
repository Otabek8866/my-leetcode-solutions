void rotate(int *nums, int numsSize, int k)
{
    int arr[numsSize];
    for (int i = 0; i < numsSize; i++)
        arr[i] = nums[i];
    int rot = numsSize - k % numsSize;
    int j = 0;
    for (int i = rot; i < numsSize; i++, j++)
        nums[j] = arr[i];
    for (int i = 0; i < rot; i++, j++)
        nums[j] = arr[i];
}