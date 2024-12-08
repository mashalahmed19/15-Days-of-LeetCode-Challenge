class Solution:
    def sortColors(self, nums):
        #Initializing pointers
        left, current, right = 0, 0, len(nums) - 1

        #Iterating through the array
        while current <= right:
            if nums[current] == 0:
                #Swapping the current element with the left pointer
                nums[left], nums[current] = nums[current], nums[left]
                left += 1
                current += 1
            elif nums[current] == 2:
                #Swapping the current element with the right pointer
                nums[current], nums[right] = nums[right], nums[current]
                right -= 1
            else:
                #Moving the current pointer forward
                current += 1
