class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        new_arr = sorted(arr)
        n = len(arr)
        ans = []
        for i in range(n-1,0,-1):
            idx = arr.index(new_arr[i])
            arr[:idx+1] = arr[:idx+1][::-1]
            ans.append(idx+1)
            arr[:i+1] = arr[:i+1][::-1]
            ans.append(i+1)
        return ans