class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        is_great = []
        for i in range(len(candies)):
            if candies[i] + extraCandies >= max(candies):
                is_great.append(True)
            else:
                is_great.append(False)
        return is_great