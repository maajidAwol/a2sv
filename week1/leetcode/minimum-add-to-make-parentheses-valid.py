class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        paranth = {"(":0,")":0}
        for par in s:
            if par ==")":
                if paranth["("]:
                    paranth["("] -=1
                else:
                    paranth[")"] +=1
            else:
                paranth["("] +=1
        print(paranth)
        return paranth["("] + paranth[")"]
