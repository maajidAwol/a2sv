class Solution:
    def minimumSteps(self, s: str) -> int:
        s = list(s)
        s.reverse()
        count =0
        zeros = 0
        for i in range(len(s)):
            if s[i] =="0":
                zeros +=1
            else:
                count +=zeros
        return count
