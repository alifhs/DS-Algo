from remove import Solution

solution = Solution()
nums = [1,1,1,1,1]
lens = solution.removeDuplicates(nums)
print(lens)
print(nums)
nums = [0,0,0,1,1,1,1,1,1,2,3,3,3,4]

lens = solution.removeDuplicates(nums)
print(lens)
print(nums)
# assert lens == 8
# assert nums == [0,0,1,1,2,3,3,3,3, 3]

nums = [1,1,1,1]

lens = solution.removeDuplicates(nums)
print(lens)
print(nums)