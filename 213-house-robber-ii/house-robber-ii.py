class Solution:
    def rob(self, nums):
        #Helper function which calculate the maximum amount in a linear arrangement
        def rob_linear(nums):
            prev = curr = 0
            for num in nums:
                temp = max(curr, prev + num)
                prev = curr
                curr = temp
            return curr
        
        n = len(nums)
        if n == 1:
            return nums[0]
        
        #Computing the maximum from the two cases
        return max(rob_linear(nums[:-1]), rob_linear(nums[1:]))
