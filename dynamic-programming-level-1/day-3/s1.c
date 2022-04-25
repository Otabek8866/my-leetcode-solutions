int max(int a, int b){
    return (a>b) ? a : b;
}

int rob(int* nums, int numsSize){
    int now=0, prev=0, tmp;
    for (int i=0; i<numsSize; i++){
        tmp = prev;
        prev = now;
        now = max(tmp+nums[i], now);
    }
    return now;
}