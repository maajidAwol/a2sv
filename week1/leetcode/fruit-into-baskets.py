class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        dict_ = defaultdict(int)
        ans = 0
        l =0
        for i in range(len(fruits)):
            dict_[fruits[i]] +=1
            while len(dict_) >2:
                dict_[fruits[l]] -=1
                if dict_[fruits[l]] ==0:
                    del dict_[fruits[l]]
                l+=1
            ans = max(ans,i-l+1)
        return ans
            