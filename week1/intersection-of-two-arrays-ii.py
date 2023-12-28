class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        num1= Counter(nums1)
        num2 = Counter(nums2)
        set3 = set(nums1) and set(nums2)
        set3 = list(set3)
        rt = []
        for num in set3:
            rt= rt +( [num] *min(num1[num],num2[num]))
        return rt