#include <stdlib.h>
/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* sortedSquares(int* nums, int numsSize, int* returnSize){
    int i = 0, j = numsSize-1, k = numsSize-1;
    int *arr = malloc(numsSize * 4);
    *returnSize = numsSize;
    
    while (i != j){
        if (nums[i] >= 0) break;
        if (-1 * nums[i] == nums[j]){
            arr[k] = nums[i] * nums[i];
            k--;
            arr[k] = nums[j] * nums[j];
            i++;
            j--;
        } else if (-1 * nums[i] > nums[j]){
            arr[k] = nums[i] * nums[i];
            i++;
        } else {
            arr[k] = nums[j] * nums[j];
            j--;
        }
        k--;
    }
    while (j >= i){
        arr[k] = nums[j] * nums[j];
        k--;
        j--;
    }
    return arr;
}