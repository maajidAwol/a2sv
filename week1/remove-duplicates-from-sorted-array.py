class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        look = 0
        place = 1
        search = 1
        n = len(nums)
        while search < n:
            if nums[search] !=nums[look]:
                nums[search],nums[place] = nums[place],nums[search]
                look +=1
                place +=1
                search +=1
            else:
                search +=1
        return place