class Solution:
    def maxCoins(self, piles: List[int]) -> int: 
        piles.sort()
        n = len(piles)
        n= n//3
        piles = piles[n:]  
        return sum([piles[i] for i in range(len(piles)) if i%2 ==0 ])
        
