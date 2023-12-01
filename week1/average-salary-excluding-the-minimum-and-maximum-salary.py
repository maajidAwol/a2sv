class Solution:
    def average(self, salary: List[int]) -> float:
        total = sum(salary)-(max(salary)+min(salary))
        rt = total/(len(salary)-2)
        return rt