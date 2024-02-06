from typing import List


class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        if not nums: return 0
        n = len(nums)
        def dfs(index, current_sum, memo):
            if index == n:
                return 1 if current_sum == target else 0
            if (index, current_sum) in memo:
                return memo[(index, current_sum)]
            add = dfs(index + 1, current_sum + nums[index], memo)
            subtract = dfs(index + 1, current_sum - nums[index], memo)
            memo[(index, current_sum)] = add + subtract
            return memo[(index, current_sum)]
        return dfs(0, 0, {})