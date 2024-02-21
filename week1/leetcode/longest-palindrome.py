class Solution:
    def longestPalindrome(self, s: str) -> int:
        count = Counter(s)
        maximum = 0
        odd = False
        for key,value in count.items():
            if value %2 ==0:
                maximum +=value
            else:
                odd = True
                maximum += ((value//2)*2)
        if odd:
            return maximum+1
        return maximum