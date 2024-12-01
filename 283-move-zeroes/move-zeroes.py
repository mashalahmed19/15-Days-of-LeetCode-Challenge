class Solution:
    def moveZeroes(self, nums):
        #Pointer to track the position of the next non-zero element
        non_zero_index = 0

        #Iterating through the array
        for i in range(len(nums)):
            if nums[i] != 0:
                #Only swaping if i and non_zero_index are different
                if i != non_zero_index:
                    nums[i], nums[non_zero_index] = nums[non_zero_index], nums[i]
                non_zero_index += 1
