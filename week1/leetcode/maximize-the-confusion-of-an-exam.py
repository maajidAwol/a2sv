class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        count ={"T":0,"F":0}
        l =0
        max_ =0
        for i in range(len(answerKey)):   
            count[answerKey[i]] +=1
            while count["T"] >k and count["F"] >k:
                count[answerKey[l]] -=1
                l+=1
            max_ = max(max_,i-l+1)
        return max_