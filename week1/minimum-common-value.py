class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        # if set(nums1) & set(nums2):
        #     return min(set(nums1) & set(nums2))
        # else:
        #     return -1
        ptr1 = 0
        ptr2 = 0
        while not ptr2 == len(nums1) or not  ptr2 == len(nums2):
            if nums1[ptr1] == nums2[ptr2]:
                return nums1[ptr1]
            elif nums1[ptr1] < nums2[ptr2]:
                ptr1 += 1
            elif nums1[ptr1] > nums2[ptr2]:
                ptr2 += 1 
            if ptr1 == len(nums1) or ptr2== len(nums2):
                return -1
    