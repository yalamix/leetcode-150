from typing import List

## FIRST ACCEPTED SOLUTION

# class Solution:
#     def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
#         """
#         Do not return anything, modify nums1 in-place instead.
#         """
#         if n > 0:
#             i = 0
#             j = 0
#             aux = [0 for i in range(m + n)]
#             for k in range(m + n):
#                 if j < n:
#                     if nums1[i] < nums2[j] and i < m:
#                         aux[k] = nums1[i]
#                         i += 1
#                     else:
#                         aux[k] = nums2[j]
#                         j += 1
#                 else:
#                     aux[k] = nums1[i]
#                     i += 1                    
#             for k in range(m + n):
#                 nums1[k] = aux[k]   

## SECOND ACCEPTED SOLUTION (FINAL)

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        i = m - 1
        j = n - 1
        if m == 0:
            for k in range(n):
                nums1[k] = nums2[k]
        elif n > 0:
            for k in range(m + n - 1, -1, -1):
                if nums1[i] > nums2[j] and i >= 0:
                    nums1[k] = nums1[i]
                    i -= 1
                elif j >= 0:
                    nums1[k] = nums2[j]
                    j -= 1

nums1 = [2,0]
nums2 = [1]

s = Solution()
s.merge(nums1, 1, nums2, 1)

print(nums1)
print(nums2)