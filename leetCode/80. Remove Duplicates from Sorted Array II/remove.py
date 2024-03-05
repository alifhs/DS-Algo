from typing import List
class Solution:

    def shiftListElements(self, nums: List[int], startIndex: int, endIndex: int)-> None:
        for i in range(startIndex, endIndex):
            nums[i] = nums[i+1]
    def removeDuplicates(self, nums: List[int]) -> int:
        currentElement = None
        appearanceCount = 0
        numsLen = len(nums)
        endIndex = numsLen
        index = 0
        duplicates = 0
        while index < numsLen:
            if currentElement == nums[index] and appearanceCount == 2:
                currentElement = nums[index]
                tempIndex = index 
                initialElement = currentElement
                while currentElement == initialElement:
                    # duplicates
                    self.shiftListElements(nums, index, endIndex-1)
                    
                    currentElement = nums[index]

                    if endIndex <= index:
                        break
                    tempIndex += 1
                    endIndex -= 1

                    
                appearanceCount = 1
                index += 1
                
                
            elif currentElement == nums[index]:
                appearanceCount += 1
                index += 1
            else:
                currentElement = nums[index]
                appearanceCount = 1
                index += 1
            
        return endIndex 