class Solution:
    def countGoodNumbers(self, n: int) -> int:
        odd = 0
        even =0
        if n%2 ==1:
            even =(n//2) +1
            odd = n//2
        else:
            even = n//2
            odd = n//2
        
        return (pow(4,odd,((10**9)+7) ) * pow(5,even,((10**9)+7) )) %((10**9)+7)
        return ((4**odd) * (5**even))%((10**9)+7) 
