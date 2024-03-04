class Solution:
    def minimumCardPickup(self, cards: List[int]) -> int:
        dict_ = defaultdict(list)
        for i in range(len(cards)):
            dict_[cards[i]].append(i)
        min_ = float("inf")
        for key,val in dict_.items():
            temp = float("inf")
            if len(val) >=2:
                for i in range(1,len(val)):
                    temp = min(temp,val[i]-val[i-1]+1)
                min_ = min(min_,temp)
        if min_ != float("inf"):
            return min_
        return -1
        # j=1
        # inside = defaultdict(int)
        # inside[cards[0]] =1
        # min_= float("inf")
        # ans = []
        # en = False

        # while j <len(cards):
        #     i =0
        #     inside[cards[j]] +=1
        #     temp = inside[cards[j]]
        #     while i < j  and temp >=2:
        #           if cards[j] == cards[i]:
        #             temp -=1
        #           i+=1
        #           en = True
        #     j+=1      
        #     if en:
        #         min_ = min(min_,j-i+1)
        # if en:
        #     return min_
        # else:
        #     return -1

