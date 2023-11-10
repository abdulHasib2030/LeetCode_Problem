class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:

        lst = nums1+nums2
        lst.sort()

        if len(lst) % 2 != 0:
            prin = (lst[len(lst) // 2])
            return (prin/1)
        else:
            div = len(lst) // 2
            cnt = lst[div] + lst[div-1]
            return (cnt / 2)
                