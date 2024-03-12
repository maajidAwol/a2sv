class Solution:
    def bestClosingTime(self, customers: str) -> int:
        n = len(customers)
        prefix = [0] * (n + 1)
        suffix = [0] * (n + 1)

        for i in range(n):
            prefix[i + 1] = prefix[i] + (customers[i] == 'N')

        for i in range(n - 1, -1, -1):
            suffix[i] = suffix[i + 1] + (customers[i] == 'Y')

        min_penalty = float('inf')
        best_hour = 0

        for i in range(n + 1):
            penalty = prefix[i] + suffix[i]
            if penalty < min_penalty:
                min_penalty = penalty
                best_hour = i

        return best_hour
