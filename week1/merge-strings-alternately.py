class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        n=len(word1)+len(word2)
        word3=[" "]*n
        index =0
        for i in range(n):
            if i < len(word1):
                word3[index] = word1[i]
                index += 1
            if i < len(word2):
                word3[index] = word2[i]
                index += 1  
        return "".join(word3)             
            