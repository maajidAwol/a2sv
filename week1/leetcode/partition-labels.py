class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        alph = {}
        ans =[]
        last = 0
        maxed = 0
        for i in range(len(s)):
            alph[s[i]] = i
        
        for i in range(len(s)):
            maxed = max(maxed,alph[s[i]])
            if maxed == i:  
                ans.append((i+1)-last)
                last = i+1
        return ans