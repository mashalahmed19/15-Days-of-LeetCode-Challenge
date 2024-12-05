class Solution:
    def maxSubArray(self, nums):
        max_sum = nums[0]  #Initializing max sum as the first element
        current_sum = nums[0]  #Current subarray sum
        
        for i in range(1, len(nums)):
            #Updating current sum: either add the current element or start a new subarray
            current_sum = max(nums[i], current_sum + nums[i])
            #Updating max sum
            max_sum = max(max_sum, current_sum)
        
        return max_sum
