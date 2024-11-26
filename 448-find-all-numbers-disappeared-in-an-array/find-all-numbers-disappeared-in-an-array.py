class Solution:
    def findDisappearedNumbers(self, nums):
        # Mark each number's corresponding index as visited by making it negative
        for num in nums:
            index = abs(num) - 1  # Get the index (1-based to 0-based)
            nums[index] = -abs(nums[index])  # Mark as done
        
        # Find indices that were not marked (these correspond to missing numbers)
        result = []
        for i in range(len(nums)):
            if nums[i] > 0:  # If the number is still positive, it's missing
                result.append(i + 1)  # Convert index back 
        
        return result
