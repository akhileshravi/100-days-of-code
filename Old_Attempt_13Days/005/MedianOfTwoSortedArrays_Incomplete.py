class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        len1, len2 = len(nums1), len(nums2)
        if len1 == 1 and len2 == 1:
            return (nums1[0] + nums2[0]) / 2
        elif len1 == 1 and len2 == 2:
            if nums1[0] < nums2[0]:
                return nums2[0]
            elif nums1[0] > nums2[1]:
                return nums2[1]
            else:
                return nums1[0]
        elif len1 == 2 and len2 == 2:
            if nums2[0] < nums1[0]:
                return nums1[0]
            elif nums2[0] > nums1[1]:
                return nums1[1]
            else:
                return nums2[0]
        elif len1 == 2 and len2 == 2:
            mn = min(nums1 + nums2)
            mx = max(nums1 + nums2)
            m2 = sum(muns1 + nums2) - mn - mx
            return m2/2
        
        m, n = len(nums1), len(nums2)
        mid1, mid2 = nums1[m//2], nums2[n//2]
        if nums1[-1] < nums2[0]:
            return self.findMedianSortedArrays(nums1[m//2:], nums2[:n//2])
        elif nums2[-1] < nums1[0]:
            return self.findMedianSortedArrays(nums2[n//2:], nums1[:m//2])
        
            
        
        
        
            