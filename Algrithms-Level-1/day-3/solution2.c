#include <stdio.h>

/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int *twoSum(int *numbers, int numbersSize, int target, int *returnSize)
{
    *returnSize = 2;
    int *arr = malloc(4 * 2);
    int k;
    int i = 0;
    int j = numbersSize - 1;
    while (i < j)
    {
        k = numbers[i] + numbers[j];
        if (k == target)
        {
            arr[0] = i + 1;
            arr[1] = j + 1;
            return arr;
        }
        if (k < target)
            i++;
        else
            j--;
    }
    return arr;
}