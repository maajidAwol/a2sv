class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        count = defaultdict(int)
        for x in bills: 
            count[x] +=1
            if x ==10:
                if count[5]:
                    count[5] -=1
                else:
                    return False
            elif x==20:
                if count[5] and count[10]:
                    count[5] -=1
                    count[10] -=1
                elif count[5] >=3:
                    count[5] -=3
                else:
                    return False
        return True