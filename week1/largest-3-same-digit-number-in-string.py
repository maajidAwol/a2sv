class Solution:
    def largestGoodInteger(self, num: str) -> str:
        for i in range(9,-1,-1):
            comp =str(i)*3
            if comp in num:
                return comp
        return ""