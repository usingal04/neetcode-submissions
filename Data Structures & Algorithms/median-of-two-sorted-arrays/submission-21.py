class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        
        def kthelement(index1, index2, k):
            if index1 >= length1:
                return nums2[index2+k-1]
            if index2 >= length2:
                return nums1[index1+k-1]
            if k == 1:
                return min(nums1[index1], nums2[index2])
            
            halfk = k // 2

            m1 = nums1[index1+halfk-1] if index1+halfk-1 < length1 else float('inf')
            m2 = nums2[index2+halfk-1] if index2+halfk-1 < length2 else float('inf')

            if m1 < m2:
                return kthelement(index1+halfk, index2, k-halfk)
            else:
                return kthelement(index1, index2+halfk, k-halfk)
            
        length1 = len(nums1)
        length2 = len(nums2)

        m1 = kthelement(0,0,(length1+length2+1) // 2)
        m2 = kthelement(0,0,(length1+length2+2) // 2)

        return (m1 + m2) / 2