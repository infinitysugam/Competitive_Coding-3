# K-Diff Pairs
# Time Complexity : O(n2)
# Space Complexity : O(n)

class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        hashset= set()
        for i in range(0,len(nums)):
            for j in range(i+1,len(nums)):
                if abs(nums[i] - nums[j]) == k:
                    if nums[i]+nums[j]-k not in hashset:
                        hashset.add(nums[i]+nums[j]-k)
        return len(hashset)


