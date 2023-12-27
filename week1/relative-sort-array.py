class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        count = [0] *( max(arr1) +1)
        for i in range(len(arr1)):
            count[arr1[i]] +=1
        new_arr = []
        for i in range(len(arr2)):
           new_arr.extend([arr2[i]] *( count[arr2[i]]))
           count[arr2[i]] =0
        for i in range(len(count)):
            if count[i]:
                new_arr.extend([i] *count[i])
        return new_arr