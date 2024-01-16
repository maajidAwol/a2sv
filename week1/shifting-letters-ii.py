class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        
        a = list(map(ord,s))
        b = [0]*len(s)
        for i in range(len(shifts)):
            if shifts[i][2] ==1:
                if shifts[i][1] == len(b) -1:
                    b[shifts[i][0]] += 1
                else:
                    b[shifts[i][0]] += 1
                    b[shifts[i][1]+1] -=1
            else:
                if shifts[i][1] == len(b) -1:
                    b[shifts[i][0]] -= 1
                else:
                    b[shifts[i][0]] -= 1
                    b[shifts[i][1]+1] +=1
        for i in range(1,len(b)):
            b[i] +=b[i-1]
        for i in range(len(a)):
            a[i] +=b[i]
        string =""
        for i in range(len(a)):

            string += chr(((a[i]-97)% 26) +97)
        return string
                