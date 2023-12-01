class Solution:
    def sumOfThree(self, num: int) -> List[int]:
        if num%3 ==0:
            av = num//3
            return [av-1,av,av+1]
        else:
            return []