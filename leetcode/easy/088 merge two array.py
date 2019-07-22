class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        if n == 0 or nums2 is None:
            return
        elif m == 0 or nums1 is None:
            nums1[:] = nums2[:]
            return

        i,j = 0,0
        while i < m+n:
            if nums1[i] > nums2[j]:
                nums1.insert(i,nums2[j])
                if nums1[-1] == 0:
                    nums1.pop()
                j = j + 1
                if j == n:
                    break
            i = i + 1
        if j < n:
            nums1[m+j:m+n] = nums2[j:n]
        
            
                   
                            