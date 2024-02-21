class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        opened = closed = 0
        for par in s:
            if par ==")":
                if opened:
                    opened -=1
                else:
                    closed +=1
            else:
                opened +=1
        return opened + closed
