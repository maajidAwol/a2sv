class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        max_g = 0
        max_s =0
        count =0
        g.sort()
        s.sort()
        while max_g < len(g) and max_s < len(s):
            if g[max_g] > s[max_s]:
                max_s +=1
            elif g[max_g] <= s[max_s]:
                max_g +=1
                max_s+=1
                count +=1
        return count