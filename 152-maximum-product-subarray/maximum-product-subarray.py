class Solution:
    def maxProduct(self, nums):
        if not nums:
            return 0

        # Initializing the variables
        max_product = nums[0]
        min_product = nums[0]
        result = nums[0]

        # Traverse the array
        for i in range(1, len(nums)):
            num = nums[i]

            if num < 0:
                # Swapping max and min when the number is negative
                max_product, min_product = min_product, max_product

            # Calculating the max and min product including the current number
            max_product = max(num, max_product * num)
            min_product = min(num, min_product * num)

            # Updating the result
            result = max(result, max_product)

        return result
