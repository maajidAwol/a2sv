class Solution:
    def freqAlphabets(self, s: str) -> str:
        sr=""
        p = len(s) -1
        while p>=0:
            if s[p] =="#":
                sr+=chr(int(s[p-2:p])+96)
                p-=3
            else:
                sr +=chr(int(s[p])+96)
                p-=1
        
        return sr[::-1]