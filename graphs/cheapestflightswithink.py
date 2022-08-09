# https://leetcode.com/problems/cheapest-flights-within-k-stops/
# leetcode 787 medium
# Bellman-ford algorithm
# weights can be negative
class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        prices = [float('inf')] *n
        prices[src] = 0
        
        for i in range(k+1):
            tempprices = prices.copy()
            
            for s,d,p in flights:
                if prices[s] == float('inf'):
					# check if the sources is reachable
                    continue
                if prices[s] + p < tempprices[d]: # we could already updated tempprices in the previous loop
                    tempprices[d] = prices[s] + p
            prices = tempprices
        return -1 if prices[dst] == float('inf') else prices[dst]
        