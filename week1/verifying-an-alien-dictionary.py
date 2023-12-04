class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        new_words =sorted(words,key = lambda x: [order.index(c) for c in x])
        for i in range(len(words)):
            if words[i] != new_words[i]:
                return False
        return True