from typing import List
import time

class Solution:

    # def swipe(nums: List[int])

    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        clonedNums = list(nums)

        numsLen = len(nums)

        for i in range(0, numsLen):
            shiftedIndex = (i+k) % numsLen
            nums[shiftedIndex] = clonedNums[i]
        
