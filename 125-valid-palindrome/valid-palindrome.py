class Solution:
    def isPalindrome(self, s):
        # Remove non-alphanumeric characters and convert to lowercase
        filtered_s = ""
        for char in s:
            if char.isalnum():
                filtered_s += char.lower()
        
        # Check if the filtered string is the same when reversed
        return filtered_s == filtered_s[::-1]