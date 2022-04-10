int search(int *nums, int numsSize, int target)
{
    for (int i = 0; i < numsSize; i++)
    {
        if (target == nums[i])
            return i;
        else if (target < nums[i])
            return -1;
    }
    return -1;
}

// int search(int *nums, int numsSize, int target)
// {
//     int mid = (numsSize - 1) / 2;
//     int start = 0;
//     int end = numsSize - 1;

//     do
//     {
//         if (target == nums[mid])
//             return mid;
//         else if (target < nums[mid])
//         {
//             end = mid;
//             mid = (mid + start) / 2;
//         }
//         else
//         {
//             start = mid;
//             mid = (mid + end) / 2;
//         }
//         if (target == nums[mid])
//             return mid;
//     } while (start != mid);

//     if (target == nums[end])
//         return end;

//     return -1;
// }