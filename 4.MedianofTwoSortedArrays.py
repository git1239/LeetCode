import numpy as np
class Solution(object):
    def findMedianSortedArrays(self,nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        arr1 = np.array(nums1)
        arr2 = np.array(nums2)
        arr = np.concatenate((arr1, arr2))
        arr = np.sort(arr)
        return np.median(arr)
