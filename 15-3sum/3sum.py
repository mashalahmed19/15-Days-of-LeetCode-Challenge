class Solution:
    def threeSum(self, nums):
        # Sorting the array to simplify finding unique triplets
        nums.sort()
        result = []
        n = len(nums)
        
        for i in range(n - 2):
            # Skipping duplicate values for the first number
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            
            # Using two pointers to find the other two numbers
            left, right = i + 1, n - 1
            
            while left < right:
                current_sum = nums[i] + nums[left] + nums[right]
                
                if current_sum == 0:
                    result.append([nums[i], nums[left], nums[right]])
                    
                    # Moving the pointers and skip duplicates
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1
                    
                    left += 1
                    right -= 1
                
                elif current_sum < 0:
                    left += 1  # Moving left pointer to increase sum
                else:
                    right -= 1  # Moving right pointer to decrease sum
        
        return result
