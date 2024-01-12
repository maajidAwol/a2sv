class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowel = "aeiou"
        count =0

        for a in s[:k]:
            if a in vowel:
                count+=1
        max_count =count
        l =1
        r= k 
        for i in range(k,len(s)):
            if s[l-1] in vowel:
                count-=1
            if s[i] in vowel:
                count+=1
            l+=1
            max_count =max(max_count,count)

        return max_count
