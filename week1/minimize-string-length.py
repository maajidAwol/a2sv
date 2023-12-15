class Solution:
    def minimizedStringLength(self, s: str) -> int:
        # counted = Counter(s)
        # return len(counted) 
        s =set(s)
        return len(s)