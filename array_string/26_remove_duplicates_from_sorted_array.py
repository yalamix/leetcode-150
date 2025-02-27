from typing import List

## FIRST ACCEPTED SOLUTION

# class Solution:
#     def removeDuplicates(self, nums: List[int]) -> int:
#         last = None
#         n = len(nums)
#         k = 0
#         for i in range(n):
#             if nums[k] == last:
#                 nums.pop(k)
#                 nums.append(0)
#             else:
#                 last = nums[k]
#                 k += 1
#         return k

## SECOND ACCEPTED SOLUTION (FINAL)

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        last = nums[0]
        n = len(nums)
        k = 1
        for i in range(1, n):
            if nums[i] != last:
                last = nums[i]
                nums[k] = last
                k += 1
        return k     
    
nums = [0,0,1,1,1,2,2,3,3,4]

s = Solution()
s.removeDuplicates(nums)
print(nums)