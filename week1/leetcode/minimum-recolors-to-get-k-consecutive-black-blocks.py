class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        l =0
        min_= float("inf")
        for i in range(k,len(blocks)+1):
            count = Counter(blocks[l:i])
            min_ = min(min_,count["W"])
            l+=1

        return min_

        

            