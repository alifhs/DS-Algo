class Solution:
    def merge(self, nums1, m: int, nums2, n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        
        newList = []
        
        nums1Index = 0
        nums2Index = 0
        iterationNum = 0
        # biggerList = m if m > n else n

        while nums1Index < m and nums2Index < n:
            if nums1[nums1Index] < nums2[nums2Index]:
                newList.append(nums1[nums1Index])
                nums1Index += 1
            else:
                newList.append(nums2[nums2Index])
                nums2Index += 1

        while nums1Index < m:
                newList.append(nums1[nums1Index])
                nums1Index += 1
        while nums2Index < n:
                newList.append(nums2[nums2Index])
                nums2Index += 1

        while iterationNum < m+n:
             nums1[iterationNum] = newList[iterationNum]
             iterationNum += 1

        return nums1
    


solution = Solution()
print(solution.merge([1,2,3,0,0,0], 3, [2,5,6], 3))

             
             

                
            
            
            

        

        