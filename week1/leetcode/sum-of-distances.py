class Solution:
    def distance(self, nums: List[int]) -> List[int]:
        n= len(nums)
        ans = [0]*n
        temp = dict()
        count = defaultdict(int)
        val = defaultdict(int)
        for i in range(n):
            if nums[i] in temp:
                val[nums[i]] += (count[nums[i]] *(i-temp[nums[i]]))
                ans[i] += val[nums[i]] 
            temp[nums[i]] = i
            count[nums[i]] +=1
        temp = dict()
        count = defaultdict(int)
        val = defaultdict(int)
        for i in range(n-1,-1,-1):
            if nums[i] in temp:
                val[nums[i]] += (count[nums[i]] *abs(i-temp[nums[i]]))
                ans[i] += val[nums[i]]
            temp[nums[i]] = i
            count[nums[i]] +=1
        return ans