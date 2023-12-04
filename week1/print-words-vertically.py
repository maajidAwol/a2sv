class Solution:
    def printVertically(self, s: str) -> List[str]:
        s= s.split()
        n =len(max(s,key=len))
        rt =[""]*n
        for i in range(n):
            for word in s:
                if i >= len(word) :
                    rt[i]+=" "
                else:
                    rt[i] +=word[i]
        for i in range(n):
            rt[i] =rt[i].rstrip()
        return rt
