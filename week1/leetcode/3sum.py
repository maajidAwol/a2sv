class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ans =[]
        n= len(nums)
        nums.sort()
        for i in range(n):
            l = i+1
            r = n-1
            while l <r:
                if( nums[l]+ nums[r] +nums[i])==0:
                    ans.append([nums[l],nums[r],nums[i]])
                    l+=1
                    r-=1
                elif ( nums[l]+ nums[r] +nums[i]) >0:
                    r -=1
                elif ( nums[l]+ nums[r] +nums[i]) <0:
                    l+=1
        temp = (tuple(el) for el in ans)
        temp = list(set(temp))
        ans = [list(el) for el in temp]
        return ans