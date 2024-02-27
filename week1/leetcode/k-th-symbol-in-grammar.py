class Solution: 
    def kthGrammar(self, n: int, k: int) -> int: 
 
        if n == 1: 
            return 0 
 
        if k > (2 ** n) / 4: 
 
            k -= (2 ** n) // 4 
         
            return 1 - self.kthGrammar(n - 1, k) 
        else: 
            return  self.kthGrammar(n - 1, k)
