class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        separated = {}
        answer =[[],[]]
        for match in matches:
            if match[0] in separated:
                separated[match[0]][0] +=1
            else:
               separated[match[0]]=[1,0]
            if match[1] in separated:
                separated[match[1]][1] -=1
            else:
                separated[match[1]]=[0,-1]
        for key,value in separated.items():
            if value[1] ==0:
                answer[0].append(key)
            elif value[1] == -1:
                answer[1].append(key)
        answer[0].sort()
        answer[1].sort()
        return answer
        