class Solution:
    def longestNiceSubstring(self, s: str) -> str:
        ans = ""
        for i in range(len(s)):
            l= 0
            while l<=i:
                set_up = set()
                set_low = set()
                temp = s[l:i+1]
                for ch in temp:
                    if ch.isupper():
                        set_up.add(ch)
                    else:
                        set_low.add(ch.upper())
                if set_up == set_low:
                    ans = temp if len(temp) >len(ans) else ans
                l+=1
        return ans
                