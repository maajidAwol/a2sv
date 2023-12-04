class Solution:
    def romanToInt(self, s: str) -> int:
        corr ={"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}
        res=0
        for i in range(len(s)):
                
            if i< len(s)-1 and corr[s[i]] < corr[s[i+1]]:
                res -= corr[s[i]]
            else:
                res += corr[s[i]]
        return res