int maxProfit(int* prices, int pricesSize){
    int profit = 0, left = 0, right = 1, diff;
    while (right < pricesSize){
        diff = prices[right] - prices[left];
        profit = (diff > profit) ? diff : profit;
        if (diff < 0)
            left = right;
        right++;
    }
    return profit;
}