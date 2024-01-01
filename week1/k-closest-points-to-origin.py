class Solution:
    def ab(self,item):
        return ((item[0]**2) +(item[1]**2))**0.5
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        points.sort(key=self.ab)
        return points[:k]