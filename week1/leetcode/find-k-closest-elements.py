class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        left = -1
        right = len(arr)

        while left +1< right:
            mid = (left+right)//2
            if arr[mid] >= x:
                right =  mid
            else:
                left = mid
        idx = right-k
        ans = []
        l = right-1
        r = right
        while k:
            if l >=0 and r<len(arr):
                if abs(arr[r]-x) >= abs(x-arr[l]):
                    num = arr[l]
                    l-=1
                else:
                    num = arr[r]
                    r+=1
            elif l>=0:
                num = arr[l]
                l-=1
            else:
                num= arr[r]
                r+=1
            k-=1
            ans.append(num)
        return sorted(ans)