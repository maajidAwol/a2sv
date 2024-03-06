class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        l =-1
        r = len(nums)
        while l+1 <r:
            mid = (l+r)//2
            if target == nums[mid]:
                mid_r1 = mid
                mid_r2 = mid
                while l+1 <mid_r1:
                    mid1 = (mid_r1 +l)//2
                    if target == nums[mid1]:
                        mid_r1 = mid1
                    else:
                        l = mid1
                while mid_r2+1 <r:
                    mid2 = (mid_r2+r)//2
                    if target ==nums[mid2]:
                        mid_r2 = mid2
                    else:
                        r = mid2
                return [mid_r1,mid_r2]
            
            elif target >nums[mid]:
                l = mid
            elif target <nums[mid]:
                r = mid
            
        return [-1,-1]