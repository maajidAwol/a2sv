class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l =0
        max_string=0
        visited = defaultdict(int)
        for i in range(len(s)):
            visited[s[i]] +=1
            while visited[s[i]]  > 1:
                visited[s[l]] -=1
                l+=1
            max_string= max(max_string,(i-l+1))
        return max_string
                 