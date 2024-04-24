from typing import List
class Solution:

    def swap(self, nums: List[int], currentIndex: int, numsLen: int) -> int:
        zeroIndex = None
        while currentIndex < numsLen - 1:
            
            nums[currentIndex], nums[currentIndex + 1] = nums[currentIndex + 1], nums[currentIndex]
            currentIndex += 1
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        numsLen = len(nums)

        i = 0 

        # find number zeros
        numsOfZeros = 0

        while i < numsLen:
            if nums[i] == 0:
                numsOfZeros += 1
            i += 1
        
        # variable replaceIndex = 0 ; will be used to replace the value with non zero number
        replaceIndex = 0
        i = 0
        while i < numsLen:
            if nums[i] != 0:
                nums[i] , nums[replaceIndex] =  nums[replaceIndex] , nums[i]
                replaceIndex += 1
            i += 1

        # now fill the array, numOfZeros  times with 0
        
        
        
        
        print(nums)
