int max(int a, int b){
    return (a>b) ? a : b;
}

int maxSubArray(int* nums, int numsSize){
    int max1=0, max2=INT_MIN;
    
    for (int i=0; i<numsSize; i++){
        max1 = max(nums[i], max1+nums[i]);
        max2 = max(max1, max2);
    }
    return max2;
}