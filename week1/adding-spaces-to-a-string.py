class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
     start =0
     end= 0
    
     s_return =[]
     for i in range(len(spaces)):
        end = spaces[i]
        s_return.append(s[start:end])
        start =end
     s_return.append(s[start:])
     return " ".join(s_return)