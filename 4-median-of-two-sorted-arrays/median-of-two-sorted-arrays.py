class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        nums1=nums1+nums2
        nums1.sort()
        n=len(nums1)
        mid = n // 2
        if n % 2 == 0:
            return (nums1[mid - 1] + nums1[mid]) / 2.0
        else:
            return nums1[mid]
