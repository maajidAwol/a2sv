class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack = []
        dict_= {}
        for i in range(len(nums2)):
            while stack and nums2[i] >stack[-1]:
                dict_[stack.pop()] = nums2[i]
            stack.append(nums2[i])
        ans = [-1] *len(nums1)
        for i in range(len(nums1)):
            if nums1[i] in dict_:
                ans[i] =dict_[nums1[i]]
        return ans
        
