import array



class Solution:
    def pivotIndex(self, nums) -> int:
        if len(nums) == 1:
            return 0
        nums_len = len(nums)
        running_sum = [None] * nums_len
        running_sum_rev = [None] * nums_len
        running_sum[0] =  nums[0]
        notFoundIndex = -1
        running_sum_rev[nums_len-1] = nums[nums_len-1]
        for i in range(1, nums_len):
            running_sum[i] = running_sum[i-1] + nums[i]
            running_sum_rev[nums_len-1 - i] = running_sum_rev[nums_len-1 - i + 1] + nums[nums_len-1 - i]
            
        for i in range(0, nums_len):
            if i == 0 or i == nums_len-1:
                if(  i == 0 and 0 == running_sum_rev[1]) or (i == nums_len-1 and 0 == running_sum[i-1]):
                    notFoundIndex = i
                    return notFoundIndex
            elif running_sum[i-1] == running_sum_rev[i+1]:
                notFoundIndex = i
                return notFoundIndex
        # return running_sum_rev
        return notFoundIndex
        
    
    
if __name__ == '__main__':
    file1 = open('724test.txt', 'r')
    Lines = file1.readline()
    arr =  [ int(n) for n in Lines.split() ]
    solution = Solution()
    # sum_array = solution.pivotIndex(arr)
    assert solution.pivotIndex([1,7,3,6,5,6]) == 3
    assert solution.pivotIndex([1,2,3]) == -1
    assert solution.pivotIndex([2,1,-1]) == 0
    assert solution.pivotIndex([1]) == 0
    
  