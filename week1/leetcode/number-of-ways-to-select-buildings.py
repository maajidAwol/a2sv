class Solution:
    def numberOfWays(self, s: str) -> int:
        n= len(s)
        count_0 = 0
        count_1 = 0
        count_01 = 0
        count_10 = 0
        ans =0
        for i in range(n):
            if s[i] =="1":
                count_1+=1
            else:
                count_0 +=1
            if count_0 > 0 and s[i] =="1":
                count_01 += count_0
            elif s[i] =="0" and count_1 >0:
                count_10 +=count_1
            if count_10 > 0 and s[i]=="1":
                ans += count_10
            elif count_01 >0 and s[i] =="0":
                ans += count_01
        return ans