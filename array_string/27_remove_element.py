from typing import List

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        n = len(nums) - nums.count(val)
        m = nums.count(val)
        for i in range(m):
            nums.remove(val)
            nums.append(0)
        return n
    
nums = [0,1,2,2,3,0,4,2]
val = 2

s = Solution()
print(s.removeElement(nums, val), nums)