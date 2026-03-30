class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max=0
        for i in range(len(prices)-1,0,-1):
            for j in range(len(prices)):
                if j<i:
                    #print(prices[i],prices[j],"----",prices[i]-prices[j])
                    if prices[i]-prices[j] > max :
                        max = prices[i]-prices[j] 
        return max            


        