
from typing import List
class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        
        kSum = sum(nums[:k])
        window_sum_avg = kSum / k

        max_avg = window_sum_avg

        numsLen = len(nums)

        for i in range(numsLen - k):
            kSum = kSum - nums[i] + nums[i+k]
            window_sum_avg = kSum/ k
            max_avg = max(max_avg, window_sum_avg)
        
        return max_avg