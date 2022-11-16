### Problem Statement ###

# Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.

# The overall run time complexity should be O(log (m+n)).

# Approach - 01 : High Runtime and Memory
# Runtime: 233 ms
# Memory Usage: 14.2 MB
from typing import List

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        mergedSortedList = sorted(nums1 + nums2)
        mergedSortedListLength = len(mergedSortedList)
        if mergedSortedListLength % 2 == 0 :
            return (mergedSortedList[int(mergedSortedListLength/2)] + mergedSortedList[int((mergedSortedListLength/2)-1)])/2
        else:
            return mergedSortedList[int(mergedSortedListLength/2)]


# s = Solution()
# print(Solution.findMedianSortedArrays(s, [1,2], [3,4]))