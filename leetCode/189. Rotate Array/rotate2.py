from typing import List
import time

class Solution:

    def swap(nums: List[int]):
        pass

    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.

        1. loop through and swap with (i + k) % numsLen and replace initial with large int like 2^32
        2. if large int found replace and move to the next  by incrementing +1,
        3. increment count on each swap and check if count is surpassing the nums length.

        """
        largeNum = 2**32

        numsLen = len(nums)

        swapCount = 0
        temp = None
        index = 0
        while swapCount < numsLen:
            if temp == largeNum:
                pass
            shiftedIndex = (index + k) % numsLen
            temp = nums[shiftedIndex]
            nums[shiftedIndex] = nums[index]
            nums[index] = largeNum
            index = shiftedIndex
            swapCount += 1
        # clonedNums = list(nums)

        # numsLen = len(nums)

        # for i in range(0, numsLen):
        #     shiftedIndex = (i+k) % numsLen
        #     nums[shiftedIndex] = clonedNums[i]
        
