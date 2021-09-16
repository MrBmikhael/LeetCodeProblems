class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        # https://www.youtube.com/watch?v=q6IEA26hvXc
        
        A = nums1
        B = nums2
        
        total = len(nums1) + len(nums2)
        half = total // 2
        
        if len(A) > len(B):
            A, B = B, A
        
        l = 0
        r = len(A) - 1
        
        while True:
            i = (l + r) // 2
            j = half - i - 2
            
            Aleft = A[i] if i >= 0 else float('-inf')
            Aright = A[i+1] if (i + 1) < len(A) else float('inf')
            Bleft = B[j] if j >= 0 else float('-inf')
            Bright = B[j+1] if (j + 1) < len(B) else float('inf')
            
            if Aleft <= Bright and Bleft <= Aright:
                if total % 2 == 1:
                    return min(Aright, Bright)
                return (max(Aleft,Bleft) + min(Aright, Bright)) / 2.0
            elif Aleft > Bright:
                r = i - 1
            else:
                l = i + 1
        