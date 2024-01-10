class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        cnt = Counter(p)
        ans =[]
        p_count = Counter(s[0:len(p)])
        l = 1
        if p_count == cnt:
            ans.append(0)
        for i in range(len(p),len(s)):   
            p_count[s[l-1]] -=1 
            p_count[s[i]] +=1
            if p_count[s[l-1]] ==0:
                del p_count[s[l-1]]
            if cnt == p_count:
                ans.append(l)
            l+=1
        return ans