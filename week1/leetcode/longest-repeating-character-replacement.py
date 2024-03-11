class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = defaultdict(int)
        n = len(s)
        max_length = 0
        max_freq = 0
        l = 0
        
        for i in range(n):
            count[s[i]] += 1
            max_freq = max(max_freq, count[s[i]])
            
            if i - l + 1 - max_freq > k:
                count[s[l]] -= 1
                l += 1
            
            max_length = max(max_length, i - l + 1)
        
        return max_length
