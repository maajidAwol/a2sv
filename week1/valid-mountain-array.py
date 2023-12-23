class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        if len(arr) < 3 :
            return False
        for i in range(1, len(arr)-1):
            if arr[i] >arr[i -1] and arr[i] >arr[i +1]:
                
                if len(arr[:i+1]) >len(set(arr[:i+1])) or len(arr[i:]) >len(set(arr[i:])):
                    return False
                elif arr[:i+1] == sorted(arr[:i+1])  and arr[i:] == sorted(arr[i:], reverse =True):
                    return True
        return False