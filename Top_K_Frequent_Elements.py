from typing import List
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dic = {}
        l = []
        for v in nums:
            key = v
            if key not in dic:
                dic[key] = []
            dic[key].append(v)
        lst = list(dic.values())
        lst.sort(key = len)
        
        for i in range(k):
            a = (len(lst)-1) - i
            l.append(lst[a][0])
        return l
        
nums = [1,1,1,1,1,1,2,2,2,2,3,3,3,3,3]
k = 2
sol = Solution()
print(sol.topKFrequent(nums, k))