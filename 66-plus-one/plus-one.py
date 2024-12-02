class Solution:
    def plusOne(self, digits):
        n = len(digits)
        
        # Traverse the array in reverse order
        for i in range(n - 1, -1, -1):
            if digits[i] < 9:  
                digits[i] += 1
                return digits
            # If the current digit is 9, set it to 0
            digits[i] = 0
        
        # If all digits were 9, we need to add an additional 1 at the front
        return [1] + digits
