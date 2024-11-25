class Solution:
    def removeDuplicates(self, nums):
        #If the array is empty, return 0
        if not nums:
            return 0

        #Pointer to place the next unique element
        k = 0

        #Iterate through the array
        for i in range(1, len(nums)):
            if nums[i] != nums[k]:  #if a new unique element is found
                k += 1             #move to the next position
                nums[k] = nums[i]  #Update the array with the unique element

        # Return the count of unique elements
        return k + 1
