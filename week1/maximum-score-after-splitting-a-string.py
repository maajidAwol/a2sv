class Solution:
    def maxScore(self, s: str) -> int:
        ans = float("-inf")
        one =s.count("1")
        zero =0
        if s[0] =="1":
            one-=1
        else:
            zero+=1
        for i in range(1,len(s)):
            ans = max(ans,zero+one)
            if  s[i] == "1":
                one -=1
            else:
                zero +=1
            
        return ans
        