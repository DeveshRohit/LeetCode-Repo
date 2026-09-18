class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:

        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
        
        m = len(nums1)
        n = len(nums2)

        low = 0
        high = m

        half = (m+n+1) // 2
        while low <= high:
            i = (low+high) // 2
            j = half - i

            if i == 0:
                leftA = float('-inf')
            else:
                leftA = nums1[i-1]

            if i == m:
                rightA = float('inf')
            else:
                rightA = nums1[i]

            if j == 0:
                leftB = float('-inf')
            else:
                leftB = nums2[j-1]

            if j == n:
                rightB = float('inf')
            else:
                rightB = nums2[j]

            if leftA > rightB:
                high = i-1

            elif leftB > rightA:
                low = i+1

            else:
                if (m+n) % 2 == 0:
                    median = (max(leftA, leftB) + min(rightA, rightB)) / 2
                    return median
                else:
                    median = max(leftA, leftB)
                    return median
            