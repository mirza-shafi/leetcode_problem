# perfact
from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        out = [1]*n
        prefix = 1
        for i in range(n):
            out[i] = prefix
            prefix = prefix*nums[i]
        print(out)
        suffix = 1
        for i in range(n-1, -1, -1):
            out[i] = out[i] * suffix
            suffix = suffix * nums[i]
        return out

nums = [1, 2, 4, 6]
sol = Solution()
print(sol.productExceptSelf(nums))  # [48, 24, 12, 8]