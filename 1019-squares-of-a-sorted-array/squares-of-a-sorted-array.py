class Solution:
    def sortedSquares(self, nums):
        n = len(nums)
        result = [0] * n  # Result array to store squares
        left, right = 0, n - 1
        pos = n - 1  # Position to insert the largest square in result

        while left <= right:
            left_square = nums[left] ** 2
            right_square = nums[right] ** 2

            if left_square > right_square:
                result[pos] = left_square
                left += 1
            else:
                result[pos] = right_square
                right -= 1

            pos -= 1  # Moving the position backward

        return result
