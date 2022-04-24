int climbStairs(int n){
    int nums[45] = {1,2};
    for (int i=2; i<n; i++)
        nums[i] = nums[i-1] + nums[i-2];
    return nums[n-1];
}