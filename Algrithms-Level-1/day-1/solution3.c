int searchInsert(int *nums, int numsSize, int target)
{
    int mid = (numsSize - 1) / 2;
    int start = 0;
    int end = numsSize - 1;

    while (start < mid)
    {
        if (target == nums[mid])
            return mid;
        else if (target < nums[mid])
            end = mid;
        else
            start = mid;
        mid = start + (end - start) / 2;
    }
    if ((target == nums[mid]) || (target < nums[mid]))
        return mid;
    else if (target > nums[end])
        return end + 1;
    else
        return end;
}