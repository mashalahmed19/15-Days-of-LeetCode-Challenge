class Solution:
    def pivotIndex(self, nums):
        #Calculating the total sum of the array
        total_sum = sum(nums)
        left_sum = 0
        
        for i, num in enumerate(nums):
            #Checking if left sum equals the right sum
            if left_sum == (total_sum - left_sum - num):
                return i
            #Updating the left sum
            left_sum += num
        
        return -1
