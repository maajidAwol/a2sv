class Solution:
    def numTimesAllBlue(self, flips: List[int]) -> int:
        binary = [0]*len(flips)
        count =0
        zero = 0
        for i in range(len(flips)):
            binary[flips[i]-1] =1
            zero = max(zero,flips[i]) 
            if i == zero-1:
                count +=1
        return count