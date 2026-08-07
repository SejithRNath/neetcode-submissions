class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        a = len(nums1)
        b = len(nums2)

        mid1 = mid2 = 0
        i,j =0,0
        for count in range((a+b)//2+1):

            mid2 = mid1

            if i<a and j<b:
                if nums1[i]<nums2[j]:
                    mid1 = nums1[i]
                    i+=1
                else:
                    mid1 = nums2[j]
                    j+=1
            elif i < a:
                mid1 = nums1[i]
                i+=1
            else:
                mid1 = nums2[j]
                j+=1
        if (a+b)%2:
            return mid1
        return (mid1+mid2)/2.0
            

        