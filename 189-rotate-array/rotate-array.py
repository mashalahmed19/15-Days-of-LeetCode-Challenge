class Solution:
    def rotate(self, nums, k):
        n = len(nums)
        k %= n  #Handle cases where k is greater than the length of nums

        #Helper function to reverse a portion of the array
        def reverse(start, end):
            while start < end:
                nums[start], nums[end] = nums[end], nums[start]
                start += 1
                end -= 1

        #1: Reverse the entire array
        reverse(0, n - 1)
        #2: Reverse the first k elements
        reverse(0, k - 1)
        #3: Reverse the rest of the array
        reverse(k, n - 1)
