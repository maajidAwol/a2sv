class Solution:
    def breakPalindrome(self, palindrome: str) -> str:
        
        n = len(palindrome)
        if n%2 ==0:
            n = (n//2)
        else:
            n = n//2
    
        palindrome = list(palindrome)
        for i in range(n):
            # print('cvbnm')
            if palindrome[i] != "a":
                palindrome[i] = "a"
                return "".join(palindrome)
        if len(palindrome) >1 and palindrome[-1]=="a":
            return "".join(palindrome[:-1]) + "b"
        return ""