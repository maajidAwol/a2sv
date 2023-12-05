class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        pattern1 = set("qwertyuiop")
        pattern2 = set("asdfghjkl")
        pattern3 =set("zxcvbnm")
        pattern=set()
        arr =[]
        for word in words:
            arr.append(word)
            word =word.lower()
            if word[0] in pattern1:
                pattern = pattern1
            elif word[0] in pattern2:
                pattern = pattern2
            elif word[0] in pattern3:
                pattern = pattern3
            
            
            for i in range(len(word)):
                if word[i] not in pattern: 
                    arr.pop()
                    break
                 
        return arr