from typing import List

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        """
        1. run a loop and shift element to the right on each step
        2. on every right shift keep the next element to the temp variable
        3. temp = nums[index]
        4. on last step check if index == numsLen - 1:
                nums[0] = nums[index]
            
        """