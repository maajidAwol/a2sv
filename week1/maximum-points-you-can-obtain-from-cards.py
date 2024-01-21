class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        n = len(cardPoints)
        total_points = sum(cardPoints)
        window_size = n - k

        window_sum = sum(cardPoints[:window_size])
        min_window_sum = window_sum

        for i in range(window_size, n):
            window_sum += cardPoints[i] - cardPoints[i - window_size]
            min_window_sum = min(min_window_sum, window_sum)
        return total_points - min_window_sum