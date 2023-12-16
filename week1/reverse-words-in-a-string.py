class Solution:
    def reverseWords(self, s: str) -> str:
        s = s.split()
        reversed_s = ""
        for i in range(len(s)):
            s[i] = s[i].strip()
            reversed_s = s[i] + " " + reversed_s
        return reversed_s.rstrip()
