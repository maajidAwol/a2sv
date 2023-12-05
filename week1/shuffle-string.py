class Solution(object):
    def restoreString(self, s, indices):
        """
        :type s: str
        :type indices: List[int]
        :rtype: str
        """
        r=[' ']*len(s)
        
        for i in range(len(s)):
            r[indices[i]]= s[i]
        # for i in range(len(r)):
        #     st +=r[i]
        return "".join(r)