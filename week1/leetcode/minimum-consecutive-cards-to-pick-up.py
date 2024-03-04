class Solution:
    def minimumCardPickup(self, cards: List[int]) -> int:
        dict_ = defaultdict(list)
        for i in range(len(cards)):
            dict_[cards[i]].append(i)
        min_ = float("inf")
        for key,val in dict_.items():
            if len(val) >=2:
                for i in range(1,len(val)):
                    min_ = min(min_,val[i]-val[i-1]+1)
        if min_ != float("inf"):
            return min_
        return -1

