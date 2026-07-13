class Solution {
    public int maxProfit(int[] prices) {
        int minCost = prices[0];
        int profit = 0;
        int maxProfit = 0;

        for(int i=0; i < prices.length;i++){
            if(prices[i] < minCost){
                minCost = prices[i];
            }
            profit = prices[i] - minCost;
            if(profit > maxProfit){
                maxProfit = profit;
            }
        }
        return maxProfit;
    }
}