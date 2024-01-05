class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        chem =0
        l =0
        r = len(skill)-1
        skill.sort()
        sumed = skill[l] +skill[r]
        while l <r:
            if (skill[l] + skill[r]) == sumed:
                chem += (skill[r] *skill[l]) 
                l +=1
                r -=1
            else:
                return -1
        return chem