class Solution:
    def firstUniqChar(self, s):
        #Creating a dictionary to store the frequency of each character
        char_count = {}
        
        #Counting occurrences of each character in the string
        for char in s:
            char_count[char] = char_count.get(char, 0) + 1
        
        #Finding the first character with a frequency of 1
        for index, char in enumerate(s):
            if char_count[char] == 1:
                return index
        
        # If no unique character is found, then return -1
        return -1
