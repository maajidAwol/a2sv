class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        ans =0
        count = Counter(answers)
        for x in count:
            if x==0:
                ans += count[x]
            else:
                sets = count[x]//(x+1)
                temp = (x+1)*(sets)
                if count[x] %(x+1):
                    temp+= (x+1)
                ans +=temp
        return ans
