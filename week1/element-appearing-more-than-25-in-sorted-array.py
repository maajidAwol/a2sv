class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        my_count = {}
        for num in arr:
            if num in my_count:
                my_count[num]+=1
            else:
                my_count[num] =1
            if my_count[num] > len(arr)/4:
                    return num