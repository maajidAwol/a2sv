class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort()
        i= len(nums)-1
        s1 =nums[i]
        s2=nums[i-1]
        s3=nums[i-2]
        while i-2 >=0:
            if s3+s2 <= s1:
                i-=1
                s1 =nums[i]
                s2=nums[i-1]
                s3=nums[i-2]
            else:
                return (s1+s2+s3)
        return 0