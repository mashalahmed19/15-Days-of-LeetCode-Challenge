class Solution:
    def isPalindrome(self, x):
        #Negative numbers and numbers ending in 0 (except 0 itself) cannot be palindromes
        if x < 0 or (x % 10 == 0 and x != 0):
            return False
        
        reversed_half = 0
        while x > reversed_half:
            reversed_half = reversed_half * 10 + x % 10
            x //= 10
        
        #Checking if the first half equals the reversed second half
        #or if ignoring the middle digit (for odd-length numbers) works
        return x == reversed_half or x == reversed_half // 10
