class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        prices = [float("inf")]*n
        prices[src]=0
        
        for i in range(k+1): #atmost 'k' times
            tempPrices=prices.copy()
            for source, destination ,price in flights:
                if prices[source] == float("inf"):
                    continue
                tempPrices[destination] = min(prices[source]+price, tempPrices[destination])
            prices=tempPrices

        if prices[dst] == float("inf"):
            return -1
        else:
            return prices[dst]                
                    
                       


        