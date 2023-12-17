class Solution:
    def isHappy(self, n: int) -> bool:
        my_set =set()       
        while True:
            n =list(str(n))
            n = sum([int(num)**2 for num in n ])
            if n ==1:
                return True
            elif n in my_set:
                return False
            else:
                my_set.add(n)
        