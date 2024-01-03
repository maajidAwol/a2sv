class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        look = 0
        search = 1
        n = len(nums)
        while search < n:
            if nums[search] !=nums[look]:
                nums[search],nums[look +1] = nums[look +1],nums[search]
                look +=1
                search +=1
            else:
                search +=1
        return look+1