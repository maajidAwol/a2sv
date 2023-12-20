class Solution:
    def flipgame(self, fronts: List[int], backs: List[int]) -> int:
        no_valid = set()

        for front, back in zip(fronts, backs):
            if front == back:
                no_valid.add(front)

        valid_values = set(fronts + backs) - no_valid
        return min(valid_values, default=0)
