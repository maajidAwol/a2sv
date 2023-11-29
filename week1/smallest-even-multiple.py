class Solution(object):
    def smallestEvenMultiple(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n %2 ==0 :
            return n
        nm=n*2
        for i in range(nm):
            if nm %2 == 0 and nm %n == 0:
                return nm