class Solution:
    def balancedString(self, s: str) -> int:
        count = Counter(s)
        n = len(s)
        remain = defaultdict(int)
        check = defaultdict(int)
        for key, value in count.items():
            if value > n // 4:
                remain[key] += (value - (n // 4))
        if remain["Q"] == remain["W"] == remain["E"] == remain["R"] == 0:
            return 0 
        l = 0
        min_ = float("inf")
        
        for i in range(n):
            check[s[i]] += 1
            while check["Q"] >= remain["Q"] and check["W"] >= remain["W"] and check["E"] >= remain["E"] and check["R"] >= remain["R"]:
                min_ = min(min_, i - l + 1)
                check[s[l]] -= 1
                l += 1
        return min_